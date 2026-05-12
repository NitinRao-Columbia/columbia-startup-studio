#!/usr/bin/env python3
"""
Synthetic user testing utilities.

Usage:
    python3 synthetic_eval.py extract <output_dir> <results_file>
    python3 synthetic_eval.py stats <results_file> [--previous <prev_results>]
    python3 synthetic_eval.py charts <version_label> <results_file> <output_html> [--history V1:file1.json V2:file2.json]
    python3 synthetic_eval.py skeleton <config_file> <output_file>

Examples:
    # Extract agent output into results JSON
    python3 synthetic_eval.py extract /tmp/v6_outputs/ results_v6.json

    # Print stats with deltas from previous version
    python3 synthetic_eval.py stats results_v6.json --previous results_v5.json

    # Generate charts with cross-version history
    python3 synthetic_eval.py charts V6 results_v6.json charts_v6.html --history V5:results_v5.json V4:results_v4.json

    # Generate audience skeleton from config
    python3 synthetic_eval.py skeleton skeleton_config.json audience_skeleton.json
"""

import argparse
import json
import os
import re
import random
import sys
from collections import Counter, defaultdict


# ── Constants ──

LIKERT_ORDER = ['strongly_disagree', 'disagree', 'neutral', 'agree', 'strongly_agree']
AGREE_PLUS = {'agree', 'strongly_agree'}
LIKERT_COLORS = {
    'strongly_disagree': '#d32f2f',
    'disagree': '#ff7043',
    'neutral': '#bdbdbd',
    'agree': '#66bb6a',
    'strongly_agree': '#2e7d32',
}
DIM_COLORS = {
    'resonance': '#7e57c2',
    'intent': '#1976d2',
    'conversion_confidence': '#2e7d32',
}


# ── Extract Results ──

def extract_results(output_dir):
    """Parse agent JSONL output files into a list of evaluation results.

    Scans all files in output_dir for JSONL lines containing agent messages
    with ```json [...] ``` blocks. Returns a flat list of result dicts sorted
    by person_id.
    """
    results = []

    for filename in sorted(os.listdir(output_dir)):
        filepath = os.path.join(output_dir, filename)
        if not os.path.isfile(filepath):
            continue

        with open(filepath, 'r') as f:
            content = f.read()

        for line in content.split('\n'):
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
                if isinstance(msg, dict) and 'message' in msg:
                    message = msg['message']
                    if isinstance(message, dict) and 'content' in message:
                        for block in message.get('content', []):
                            if isinstance(block, dict) and block.get('type') == 'text':
                                text = block['text']
                                json_match = re.search(r'```json\s*(\[[\s\S]*?\])\s*```', text)
                                if json_match:
                                    data = json.loads(json_match.group(1))
                                    results.extend(data)
            except json.JSONDecodeError:
                continue

    # Deduplicate by person_id (keep last occurrence)
    seen = {}
    for r in results:
        seen[r.get('person_id')] = r
    results = sorted(seen.values(), key=lambda x: x.get('person_id', 0))

    return results


# ── Compute Stats ──

def compute_stats(results, previous_results=None):
    """Compute aggregate statistics from evaluation results.

    Returns a dict with:
      - n: total count
      - overall: per-dimension distributions and agree_pct
      - by_bucket: same stats broken out by bucket
      - deltas: difference from previous_results (if provided)
    """
    n = len(results)
    stats = {'n': n, 'overall': {}, 'by_bucket': {}, 'deltas': None}

    # Overall Likert dimensions
    for dim in ['resonance', 'intent', 'conversion_confidence']:
        dist = Counter(r.get(dim, 'unknown') for r in results)
        agree_count = sum(dist.get(level, 0) for level in AGREE_PLUS)
        stats['overall'][dim] = {
            'distribution': {level: dist.get(level, 0) for level in LIKERT_ORDER},
            'agree_pct': round(agree_count / n * 100) if n > 0 else 0,
        }

    # Price perception
    stats['overall']['price_perception'] = dict(
        Counter(r.get('price_perception', 'unknown') for r in results)
    )

    # Clarity
    stats['overall']['clarity'] = dict(
        Counter(r.get('clarity_score', 'unscored') for r in results)
    )

    # Dealbreakers
    db_count = sum(1 for r in results if r.get('dealbreaker'))
    stats['overall']['dealbreaker_pct'] = round(db_count / n * 100) if n > 0 else 0
    stats['overall']['dealbreaker_count'] = db_count

    # Per bucket
    buckets = defaultdict(list)
    for r in results:
        buckets[r.get('bucket', 'unknown')].append(r)

    for bucket_name, bucket_results in sorted(buckets.items()):
        bn = len(bucket_results)
        bs = {'n': bn}

        for dim in ['resonance', 'intent', 'conversion_confidence']:
            dist = Counter(r.get(dim, 'unknown') for r in bucket_results)
            agree_count = sum(dist.get(level, 0) for level in AGREE_PLUS)
            bs[dim] = {
                'distribution': {level: dist.get(level, 0) for level in LIKERT_ORDER},
                'agree_pct': round(agree_count / bn * 100) if bn > 0 else 0,
            }

        db_count = sum(1 for r in bucket_results if r.get('dealbreaker'))
        bs['dealbreaker_pct'] = round(db_count / bn * 100) if bn > 0 else 0
        stats['by_bucket'][bucket_name] = bs

    # Deltas
    if previous_results:
        prev = compute_stats(previous_results)
        deltas = {'overall': {}, 'by_bucket': {}}

        for dim in ['resonance', 'intent', 'conversion_confidence']:
            deltas['overall'][dim] = (
                stats['overall'][dim]['agree_pct'] - prev['overall'][dim]['agree_pct']
            )
        deltas['overall']['dealbreaker'] = (
            stats['overall']['dealbreaker_pct'] - prev['overall']['dealbreaker_pct']
        )

        for bucket_name in stats['by_bucket']:
            if bucket_name in prev['by_bucket']:
                bd = {}
                for dim in ['resonance', 'intent', 'conversion_confidence']:
                    bd[dim] = (
                        stats['by_bucket'][bucket_name][dim]['agree_pct']
                        - prev['by_bucket'][bucket_name][dim]['agree_pct']
                    )
                bd['dealbreaker'] = (
                    stats['by_bucket'][bucket_name]['dealbreaker_pct']
                    - prev['by_bucket'][bucket_name]['dealbreaker_pct']
                )
                deltas['by_bucket'][bucket_name] = bd

        stats['deltas'] = deltas

    return stats


def print_stats(stats):
    """Print stats to stdout in a readable format."""
    print(f"\n{'=' * 60}")
    print(f"EVALUATION RESULTS (n={stats['n']})")
    print(f"{'=' * 60}\n")

    print("OVERALL:")
    for dim in ['resonance', 'intent', 'conversion_confidence']:
        d = stats['overall'][dim]
        print(f"  {dim}: {d['agree_pct']}% agree+  |  {d['distribution']}")
    print(
        f"  dealbreakers: {stats['overall']['dealbreaker_pct']}% "
        f"({stats['overall']['dealbreaker_count']}/{stats['n']})"
    )
    print(f"  clarity: {stats['overall']['clarity']}")
    print(f"  price: {stats['overall']['price_perception']}")

    print(f"\nPER BUCKET:")
    for bucket, bs in stats['by_bucket'].items():
        print(f"\n  {bucket} (n={bs['n']}):")
        for dim in ['resonance', 'intent', 'conversion_confidence']:
            d = bs[dim]
            print(f"    {dim}: {d['agree_pct']}% agree+")
        print(f"    dealbreakers: {bs['dealbreaker_pct']}%")

    if stats['deltas']:
        print(f"\nDELTAS FROM PREVIOUS:")
        d = stats['deltas']['overall']
        for dim in ['resonance', 'intent', 'conversion_confidence', 'dealbreaker']:
            sign = '+' if d[dim] > 0 else ''
            print(f"  {dim}: {sign}{d[dim]}pp")

        if stats['deltas']['by_bucket']:
            print(f"\n  Per bucket:")
            for bucket, bd in stats['deltas']['by_bucket'].items():
                parts = []
                for dim in ['resonance', 'intent', 'conversion_confidence']:
                    sign = '+' if bd[dim] > 0 else ''
                    parts.append(f"{dim[:3]}:{sign}{bd[dim]}")
                print(f"    {bucket}: {', '.join(parts)}")


# ── Generate Charts ──

_chart_counter = 0


def _div_id():
    global _chart_counter
    _chart_counter += 1
    return f'chart_{_chart_counter}'


def generate_charts(version_label, results, output_html, history=None):
    """Generate Plotly HTML charts from results.

    Args:
        version_label: e.g. "V6"
        results: list of result dicts for current version
        output_html: path to write HTML file
        history: optional dict of {label: results_list} for cross-version comparison
    """
    global _chart_counter
    _chart_counter = 0

    stats = compute_stats(results)
    sections = []

    # Per-round charts
    sections.append('<h2>Score Distributions</h2>')
    sections.append(_chart_likert_stacked(f'{version_label} Resonance', 'resonance', stats))
    sections.append(_chart_likert_stacked(f'{version_label} Intent', 'intent', stats))
    sections.append(
        _chart_likert_stacked(f'{version_label} Conversion Confidence', 'conversion_confidence', stats)
    )
    sections.append(_chart_price_perception(version_label, stats))
    sections.append(_chart_clarity(version_label, stats))
    sections.append(_chart_dealbreaker_by_bucket(version_label, stats))

    # Cross-version comparison
    if history:
        sections.append('<h2>Cross-Version Comparison</h2>')
        all_stats = {}
        for label, res in history.items():
            all_stats[label] = compute_stats(res)
        all_stats[version_label] = stats

        sections.append(_chart_trend_lines(all_stats))
        sections.append(_chart_dealbreaker_trend(all_stats))
        sections.append(_chart_funnel(version_label, stats))
        sections.append(_chart_bucket_comparison(all_stats))

    html = (
        f'<!DOCTYPE html>\n<html><head>\n'
        f'<title>{version_label} Evaluation Charts</title>\n'
        f'<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n'
        f'</head><body>\n'
        f'<h1>{version_label} Evaluation Charts</h1>\n'
        + '\n'.join(sections)
        + '\n</body></html>\n'
    )

    with open(output_html, 'w') as f:
        f.write(html)

    print(f"Charts written to {output_html}")


def _chart_likert_stacked(title, dimension, stats):
    div_id = _div_id()
    categories = ['Overall'] + list(stats['by_bucket'].keys())

    traces = []
    for level in LIKERT_ORDER:
        values = [stats['overall'][dimension]['distribution'].get(level, 0)]
        for bucket in stats['by_bucket']:
            values.append(stats['by_bucket'][bucket][dimension]['distribution'].get(level, 0))
        traces.append({
            'name': level.replace('_', ' ').title(),
            'x': categories,
            'y': values,
            'type': 'bar',
            'marker': {'color': LIKERT_COLORS[level]},
        })

    return (
        f'<div id="{div_id}" style="width:100%;height:400px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", {json.dumps(traces)}, {{\n'
        f'  title: "{title}",\n'
        f'  barmode: "stack",\n'
        f'  yaxis: {{title: "Count"}},\n'
        f'  legend: {{orientation: "h", y: -0.2}},\n'
        f'  margin: {{b: 100}}\n'
        f'}});</script>\n'
    )


def _chart_price_perception(version_label, stats):
    div_id = _div_id()
    pp = stats['overall']['price_perception']
    cats = ['too_expensive', 'fair', 'good_deal']
    labels = ['Too Expensive', 'Fair', 'Good Deal']
    values = [pp.get(c, 0) for c in cats]
    colors = ['#d32f2f', '#f57c00', '#2e7d32']

    return (
        f'<div id="{div_id}" style="width:100%;height:350px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", [{{\n'
        f'  x: {json.dumps(labels)}, y: {json.dumps(values)},\n'
        f'  type: "bar", marker: {{color: {json.dumps(colors)}}}\n'
        f'}}], {{title: "{version_label} Price Perception", yaxis: {{title: "Count"}}}});</script>\n'
    )


def _chart_clarity(version_label, stats):
    div_id = _div_id()
    cl = stats['overall']['clarity']
    cats = ['wrong', 'partial', 'nailed_it']
    labels = ['Wrong', 'Partial', 'Nailed It']
    values = [cl.get(c, 0) for c in cats]
    colors = ['#d32f2f', '#f57c00', '#2e7d32']

    return (
        f'<div id="{div_id}" style="width:100%;height:350px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", [{{\n'
        f'  x: {json.dumps(labels)}, y: {json.dumps(values)},\n'
        f'  type: "bar", marker: {{color: {json.dumps(colors)}}}\n'
        f'}}], {{title: "{version_label} Clarity Accuracy", yaxis: {{title: "Count"}}}});</script>\n'
    )


def _chart_dealbreaker_by_bucket(version_label, stats):
    div_id = _div_id()
    buckets = list(stats['by_bucket'].keys())
    bucket_labels = [_fmt_bucket(b) for b in buckets]
    values = [stats['by_bucket'][b]['dealbreaker_pct'] for b in buckets]

    return (
        f'<div id="{div_id}" style="width:100%;height:350px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", [{{\n'
        f'  x: {json.dumps(bucket_labels)}, y: {json.dumps(values)},\n'
        f'  type: "bar", marker: {{color: "#d32f2f"}}\n'
        f'}}], {{\n'
        f'  title: "{version_label} Dealbreaker Rate by Segment",\n'
        f'  yaxis: {{title: "%", range: [0, 100]}},\n'
        f'  margin: {{b: 120, l: 60}}\n'
        f'}});</script>\n'
    )


def _chart_trend_lines(all_stats):
    div_id = _div_id()
    versions = list(all_stats.keys())

    traces = []
    for dim, name in [('resonance', 'Resonance'), ('intent', 'Intent'), ('conversion_confidence', 'Conversion')]:
        values = [all_stats[v]['overall'][dim]['agree_pct'] for v in versions]
        traces.append({
            'name': name,
            'x': versions,
            'y': values,
            'type': 'scatter',
            'mode': 'lines+markers',
            'line': {'color': DIM_COLORS[dim], 'width': 3},
            'marker': {'size': 10},
        })

    return (
        f'<div id="{div_id}" style="width:100%;height:450px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", {json.dumps(traces)}, {{\n'
        f'  title: "Agree+ % Across Versions",\n'
        f'  yaxis: {{title: "Agree + Strongly Agree %", range: [0, 100]}},\n'
        f'  xaxis: {{title: "Version"}},\n'
        f'  legend: {{orientation: "h", y: -0.15}}\n'
        f'}});</script>\n'
    )


def _chart_dealbreaker_trend(all_stats):
    div_id = _div_id()
    versions = list(all_stats.keys())
    values = [all_stats[v]['overall']['dealbreaker_pct'] for v in versions]

    return (
        f'<div id="{div_id}" style="width:100%;height:400px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", [{{\n'
        f'  x: {json.dumps(versions)}, y: {json.dumps(values)},\n'
        f'  type: "scatter", mode: "lines+markers",\n'
        f'  line: {{color: "#d32f2f", width: 3}}, marker: {{size: 10}},\n'
        f'  fill: "tozeroy", fillcolor: "rgba(211,47,47,0.1)"\n'
        f'}}], {{\n'
        f'  title: "Dealbreaker % Across Versions",\n'
        f'  yaxis: {{title: "%", range: [0, 60]}},\n'
        f'  xaxis: {{title: "Version"}}\n'
        f'}});</script>\n'
    )


def _chart_funnel(version_label, stats):
    div_id = _div_id()
    res = stats['overall']['resonance']['agree_pct']
    intent = stats['overall']['intent']['agree_pct']
    conv = stats['overall']['conversion_confidence']['agree_pct']

    return (
        f'<div id="{div_id}" style="width:100%;height:400px;margin-bottom:30px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", [{{\n'
        f'  type: "funnel",\n'
        f'  y: ["Resonance", "Intent", "Conversion"],\n'
        f'  x: [{res}, {intent}, {conv}],\n'
        f'  textinfo: "value+percent initial",\n'
        f'  textposition: "inside",\n'
        f'  marker: {{color: ["#7e57c2", "#1976d2", "#2e7d32"]}}\n'
        f'}}], {{\n'
        f'  title: "{version_label} Conversion Funnel (Agree+ %)",\n'
        f'  margin: {{l: 130, r: 40, t: 60, b: 40}}\n'
        f'}});</script>\n'
    )


def _chart_bucket_comparison(all_stats):
    """Grouped bar comparing buckets across the two most recent versions."""
    versions = list(all_stats.keys())
    if len(versions) < 2:
        return ''

    prev_label = versions[-2]
    curr_label = versions[-1]
    prev = all_stats[prev_label]
    curr = all_stats[curr_label]
    all_buckets = sorted(set(list(prev['by_bucket'].keys()) + list(curr['by_bucket'].keys())))

    charts = ''
    dim_meta = [
        ('resonance', 'rgba(126,87,194,0.5)', '#7e57c2', 'Resonance'),
        ('intent', 'rgba(25,118,210,0.5)', '#1976d2', 'Intent'),
        ('conversion_confidence', 'rgba(46,125,50,0.5)', '#2e7d32', 'Conversion'),
    ]

    for dim, color_prev, color_curr, title_dim in dim_meta:
        div_id = _div_id()
        prev_vals = [
            prev['by_bucket'].get(b, {}).get(dim, {}).get('agree_pct', 0) for b in all_buckets
        ]
        curr_vals = [
            curr['by_bucket'].get(b, {}).get(dim, {}).get('agree_pct', 0) for b in all_buckets
        ]

        charts += (
            f'<div id="{div_id}" style="width:100%;height:400px;margin-bottom:30px;"></div>\n'
            f'<script>Plotly.newPlot("{div_id}", [\n'
            f'  {{name:"{prev_label}", x:{json.dumps(all_buckets)}, y:{json.dumps(prev_vals)}, type:"bar", marker:{{color:"{color_prev}"}}}},\n'
            f'  {{name:"{curr_label}", x:{json.dumps(all_buckets)}, y:{json.dumps(curr_vals)}, type:"bar", marker:{{color:"{color_curr}"}}}}\n'
            f'], {{\n'
            f'  title: "{title_dim} Agree+ % by Bucket ({prev_label} vs {curr_label})",\n'
            f'  barmode: "group",\n'
            f'  yaxis: {{title: "%", range: [0, 100]}},\n'
            f'  legend: {{orientation: "h", y: -0.2}},\n'
            f'  margin: {{b: 100}}\n'
            f'}});</script>\n'
        )

    return charts


# ── Generate Skeleton ──

def generate_skeleton(config, output_file):
    """Generate audience skeleton from a config dict.

    Config format:
    {
        "buckets": ["journal_graveyard", "had_it_lost_it", ...],
        "per_bucket": 12,
        "females_per_bucket": 9,
        "males_per_bucket": 3,
        "age_bands": [[24,30], [31,37], [38,44], [45,51], [52,58]],
        "female_allocations": [
            {"bucket": "journal_graveyard", "age_band": [24,30], "count": 2},
            ...
        ],
        "male_ages": {
            "journal_graveyard": [28, 37, 44],
            ...
        }
    }
    """
    profiles = []
    pid = 1

    # Female profiles from allocations
    for alloc in config['female_allocations']:
        bucket = alloc['bucket']
        low, high = alloc['age_band']
        count = alloc['count']
        ages = sorted(random.sample(range(low, high + 1), count))
        for age in ages:
            profiles.append({
                'person_id': pid,
                'gender': 'female',
                'bucket': bucket,
                'age': age,
            })
            pid += 1

    # Male profiles from fixed ages
    for bucket, ages in config['male_ages'].items():
        for age in sorted(ages):
            profiles.append({
                'person_id': pid,
                'gender': 'male',
                'bucket': bucket,
                'age': age,
            })
            pid += 1

    # Sort by bucket order then age
    bucket_order = {b: i for i, b in enumerate(config['buckets'])}
    profiles.sort(key=lambda p: (bucket_order.get(p['bucket'], 99), p['age']))

    # Reassign person_ids after sorting
    for i, p in enumerate(profiles):
        p['person_id'] = i + 1

    with open(output_file, 'w') as f:
        json.dump(profiles, f, indent=2)

    # Verify and print
    bucket_counts = Counter(p['bucket'] for p in profiles)
    gender_counts = Counter(p['gender'] for p in profiles)
    print(f"Skeleton written to {output_file} ({len(profiles)} profiles)")
    print(f"  Buckets: {dict(bucket_counts)}")
    print(f"  Gender: {dict(gender_counts)}")

    # Verify female age bands
    female_ages = [p['age'] for p in profiles if p['gender'] == 'female']
    for low, high in config.get('age_bands', []):
        count = sum(1 for a in female_ages if low <= a <= high)
        expected = config.get('females_per_age_band', '?')
        print(f"  Women {low}-{high}: {count}")


# ── Generate Report ──

REPORT_CSS = """
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
       max-width: 1100px; margin: 0 auto; padding: 20px 40px; color: #333; line-height: 1.6; }
h1 { border-bottom: 3px solid #1976d2; padding-bottom: 10px; }
h2 { color: #1976d2; margin-top: 40px; border-bottom: 1px solid #e0e0e0; padding-bottom: 5px; }
h3 { color: #555; margin-top: 25px; }
table { border-collapse: collapse; width: 100%; margin: 15px 0; }
th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
th { background: #f5f5f5; font-weight: 600; }
tr:nth-child(even) { background: #fafafa; }
.metric-cards { display: flex; gap: 15px; margin: 20px 0; flex-wrap: wrap; }
.metric-card { flex: 1; min-width: 140px; padding: 15px; border-radius: 8px; text-align: center; }
.metric-card .value { font-size: 2em; font-weight: 700; }
.metric-card .label { font-size: 0.85em; color: #666; margin-top: 4px; }
.metric-card .sublabel { font-size: 0.75em; color: #999; margin-top: 2px; }
.card-purple { background: #ede7f6; color: #4527a0; }
.card-blue { background: #e3f2fd; color: #1565c0; }
.card-green { background: #e8f5e9; color: #2e7d32; }
.card-red { background: #ffebee; color: #c62828; }
.narrative { margin: 15px 0; }
.narrative ul { margin: 5px 0; }
.narrative li { margin: 4px 0; }
.chart-explainer { color: #555; font-size: 0.95em; margin: 5px 0 15px 0; padding: 8px 12px;
                   background: #f8f9fa; border-left: 3px solid #1976d2; }
.methodology { background: #f8f9fa; padding: 15px 20px; border-radius: 8px; margin: 15px 0;
               font-size: 0.95em; line-height: 1.7; }
.methodology strong { color: #1976d2; }
.bucket-name { font-style: italic; }
.segment-header { display: flex; align-items: baseline; gap: 15px; margin-top: 30px; margin-bottom: 5px; }
.segment-header h3 { margin: 0; }
.segment-stats { font-size: 0.9em; color: #666; }
.segment-stats .good { color: #2e7d32; font-weight: 600; }
.segment-stats .mid { color: #1976d2; font-weight: 600; }
.segment-stats .bad { color: #c62828; font-weight: 600; }
.segment-dive { padding: 10px 0 15px 0; border-bottom: 1px solid #eee; }
.segment-dive:last-child { border-bottom: none; }
.segment-context { display: flex; gap: 20px; margin: 12px 0 15px 0; }
.segment-context .context-box { flex: 1; background: #f8f9fa; border-radius: 8px; padding: 15px 18px; font-size: 0.92em; line-height: 1.6; }
.segment-context .context-box h4 { margin: 0 0 8px 0; font-size: 0.85em; text-transform: uppercase; letter-spacing: 0.5px; color: #888; }
.segment-context .context-box .persona-detail { color: #555; margin: 3px 0; }
.segment-context .context-box .persona-voice { font-style: italic; color: #666; margin-top: 8px; border-top: 1px solid #e0e0e0; padding-top: 8px; }
blockquote { border-left: 3px solid #ddd; margin: 10px 0; padding: 5px 15px; color: #555; font-style: italic; }
"""

BUCKET_DISPLAY_NAMES = {
    'journal_graveyard': 'Journal Graveyard',
    'had_it_lost_it': 'Had It, Lost It',
    'guilt_spiral': 'Guilt Spiral',
    'overwhelmed_parent': 'Overwhelmed Parent',
    'curious_skeptic': 'Curious Skeptic',
    'midlife_seeker': 'Midlife Seeker',
    'repeat_buyer': 'Repeat Buyer',
    'digital_dabbler': 'Digital Dabbler',
    'loved_it_but_life': 'Loved It But Life',
    'guilt_quitter': 'Guilt Quitter',
    'ai_wary_journaler': 'AI-Wary Journaler',
}

BUCKET_DESCRIPTIONS = {
    'journal_graveyard': 'People who have tried gratitude journals, apps, and guided prompts multiple times but always abandon them within days or weeks. They believe in gratitude but have never made a practice stick.',
    'had_it_lost_it': 'People who once had a consistent gratitude practice that genuinely worked for them, but lost it to a major life change: new baby, job change, divorce, illness, or caregiving. They want back in but can\'t rebuild the habit.',
    'guilt_spiral': 'People whose relationship with self-improvement is dominated by guilt and perfectionism. Every missed day becomes evidence of personal failure. They want to practice gratitude but fear creating another thing to feel bad about.',
    'overwhelmed_parent': 'Parents and caregivers who are in survival mode with zero bandwidth for anything that requires initiation. They live on their phones and have no time or energy for practices that require willpower.',
    'curious_skeptic': 'Analytically-minded people who are open to gratitude in principle but demand evidence, transparency, and rigor. They distrust emotional marketing and won\'t commit without research citations, privacy details, and proof of efficacy.',
    'therapy_adjacent': 'People whose therapist, counselor, or doctor recommended they start a gratitude practice, but they haven\'t followed through yet. They have emotional openness and external validation from a professional, but need a low-friction entry point. They\'re already in mental health support so they\'re not skeptics; they just haven\'t found the right format.',
    'midlife_seeker': 'People in midlife seeking depth, meaning, and intentional reflection. They want difficulty and richness in their practice, not convenience. They see the blank page as where the real work happens.',
}


def _fmt_bucket(name):
    """Convert bucket_name to human-readable display name."""
    return BUCKET_DISPLAY_NAMES.get(name, name.replace('_', ' ').title())


def _fmt_buckets_list(stats):
    """Return list of bucket names in display order."""
    return list(stats['by_bucket'].keys())


def _auto_explainer_likert(dimension, stats):
    """Generate an auto-explainer for a Likert dimension chart."""
    dim_label = dimension.replace('_', ' ').title()
    overall_pct = stats['overall'][dimension]['agree_pct']

    bucket_pcts = [(b, stats['by_bucket'][b][dimension]['agree_pct']) for b in stats['by_bucket']]
    best = max(bucket_pcts, key=lambda x: x[1])
    worst = min(bucket_pcts, key=lambda x: x[1])

    parts = [f'Overall {dim_label.lower()} agree rate: {overall_pct}%.']
    if best[1] > 0:
        parts.append(f'Strongest: <em>{_fmt_bucket(best[0])}</em> at {best[1]}%.')
    if worst[1] < best[1]:
        parts.append(f'Weakest: <em>{_fmt_bucket(worst[0])}</em> at {worst[1]}%.')

    return ' '.join(parts)


def _auto_explainer_funnel(stats):
    """Generate explainer text for the conversion funnel chart."""
    res = stats['overall']['resonance']['agree_pct']
    intent = stats['overall']['intent']['agree_pct']
    conv = stats['overall']['conversion_confidence']['agree_pct']
    if res == 0:
        return 'No personas reached agree+ on resonance, so the funnel is empty.'
    drop_r_to_i = res - intent
    drop_i_to_c = intent - conv
    parts = [f'{res}% resonated with the copy (agree+).']
    if intent > 0:
        parts.append(f'Of those, {intent}% expressed intent to try it, and {conv}% felt confident they\'d convert.')
    else:
        parts.append(f'But 0% expressed intent to try, so conversion is also 0%.')
    if drop_r_to_i > drop_i_to_c and drop_r_to_i > 10:
        parts.append('The biggest drop-off is from resonance to intent: people relate to the problem but aren\'t sold on the solution.')
    return ' '.join(parts)


def _auto_explainer_bucket_lines(stats):
    """Generate explainer text for the per-bucket line chart."""
    bucket_pcts = [(b, stats['by_bucket'][b]) for b in stats['by_bucket']]
    best_conv = max(bucket_pcts, key=lambda x: x[1]['conversion_confidence']['agree_pct'])
    worst_res = min(bucket_pcts, key=lambda x: x[1]['resonance']['agree_pct'])
    parts = []
    if best_conv[1]['conversion_confidence']['agree_pct'] > 0:
        parts.append(
            f'<em>{_fmt_bucket(best_conv[0])}</em> leads conversion at '
            f'{best_conv[1]["conversion_confidence"]["agree_pct"]}%.'
        )
    parts.append(
        f'<em>{_fmt_bucket(worst_res[0])}</em> has the lowest resonance at '
        f'{worst_res[1]["resonance"]["agree_pct"]}%.'
    )
    zero_conv = [b for b, bs in bucket_pcts if bs['conversion_confidence']['agree_pct'] == 0]
    if zero_conv:
        names = ', '.join(f'<em>{_fmt_bucket(b)}</em>' for b in zero_conv)
        parts.append(f'{names} showed 0% conversion.')
    return ' '.join(parts)


def _auto_explainer_dealbreaker(stats):
    """Generate explainer text for the dealbreaker chart."""
    db_pct = stats['overall']['dealbreaker_pct']
    bucket_pcts = [(b, stats['by_bucket'][b]['dealbreaker_pct']) for b in stats['by_bucket']]
    worst = max(bucket_pcts, key=lambda x: x[1])
    parts = [
        f'A dealbreaker means the persona identified a reason they would <strong>not</strong> sign up '
        f'regardless of other factors. Overall rate: {db_pct}%.'
    ]
    if worst[1] > 0:
        parts.append(f'Highest: <em>{_fmt_bucket(worst[0])}</em> at {worst[1]}%.')
    return ' '.join(parts)


def _chart_bucket_lines(version_label, stats):
    """Line chart: x=buckets, y=agree+ %, one line per dimension."""
    div_id = _div_id()
    buckets = list(stats['by_bucket'].keys())
    bucket_labels = [_fmt_bucket(b) for b in buckets]

    traces = []
    for dim, name, color in [
        ('resonance', 'Resonance', '#7e57c2'),
        ('intent', 'Intent', '#1976d2'),
        ('conversion_confidence', 'Conversion', '#2e7d32'),
    ]:
        values = [stats['by_bucket'][b][dim]['agree_pct'] for b in buckets]
        traces.append({
            'name': name,
            'x': bucket_labels,
            'y': values,
            'type': 'scatter',
            'mode': 'lines+markers',
            'line': {'color': color, 'width': 3},
            'marker': {'size': 10},
        })

    return (
        f'<div id="{div_id}" style="width:100%;height:420px;margin-bottom:10px;"></div>\n'
        f'<script>Plotly.newPlot("{div_id}", {json.dumps(traces)}, {{\n'
        f'  title: "{version_label} Agree+ % by Audience Segment",\n'
        f'  yaxis: {{title: "Agree + Strongly Agree %", range: [0, 100]}},\n'
        f'  legend: {{orientation: "h", y: -0.15}},\n'
        f'  margin: {{b: 120, l: 60}}\n'
        f'}});</script>\n'
    )


def _stat_color(pct):
    """Return CSS class for a percentage value."""
    if pct >= 40:
        return 'good'
    if pct >= 15:
        return 'mid'
    return 'bad'


def _auto_bucket_summary(bucket_results):
    """Auto-generate a basic qualitative summary for a bucket from individual persona results."""
    lines = []

    # Strongest lines with frequency
    sl = Counter(r.get('strongest_line', '') for r in bucket_results if r.get('strongest_line'))
    if sl:
        top_line, top_count = sl.most_common(1)[0]
        if top_count > 1:
            lines.append(f'<strong>Most-cited strongest line ({top_count}x):</strong> &ldquo;{top_line}&rdquo;')
        else:
            samples = [r.get('strongest_line', '') for r in bucket_results[:2] if r.get('strongest_line')]
            if samples:
                lines.append('<strong>Strongest lines (varied):</strong> ' +
                             '; '.join(f'&ldquo;{s}&rdquo;' for s in samples))

    # Top objections (sample 3)
    objections = [r.get('objections', '') for r in bucket_results if r.get('objections')]
    if objections:
        samples = objections[:3]
        formatted = []
        for o in samples:
            text = o[:120] + '...' if len(o) > 120 else o
            formatted.append(f'&ldquo;{text}&rdquo;')
        lines.append('<strong>Sample objections:</strong> ' + ' | '.join(formatted))

    # Dealbreaker details
    dbs = [r for r in bucket_results if r.get('dealbreaker')]
    if dbs:
        reasons = []
        for r in dbs:
            reason = r.get('objections', r.get('what_feels_off', 'unspecified'))
            text = reason[:100] + '...' if len(reason) > 100 else reason
            reasons.append(f'&ldquo;{text}&rdquo;')
        lines.append(
            f'<strong>Dealbreakers ({len(dbs)}/{len(bucket_results)}):</strong> ' +
            '; '.join(reasons)
        )

    # What feels off (sample top themes)
    off = [r.get('what_feels_off', '') for r in bucket_results if r.get('what_feels_off')]
    if off:
        samples = off[:2]
        formatted = [f'&ldquo;{o[:100]}...&rdquo;' if len(o) > 100 else f'&ldquo;{o}&rdquo;' for o in samples]
        lines.append('<strong>What feels off:</strong> ' + ' | '.join(formatted))

    if not lines:
        return '<p><em>No qualitative data available.</em></p>'

    return '<div class="narrative"><ul>' + ''.join(f'<li>{l}</li>' for l in lines) + '</ul></div>'


def generate_report(version_label, results, output_html, narrative=None, history=None, audience=None, copy_file=None):
    """Generate a single HTML report with inline charts and narrative.

    Args:
        version_label: e.g. "V6"
        results: list of result dicts
        output_html: output file path
        narrative: optional dict with keys: exec_summary, findings, recommendations,
                   qualitative_themes, clarity_notes, appendix_notes,
                   bucket_deep_dives (dict of bucket_name: HTML) (all HTML strings)
        history: optional dict of {label: results_list} for cross-version charts
    """
    global _chart_counter
    _chart_counter = 0

    stats = compute_stats(results)
    nar = narrative or {}
    sections = []

    # ── Header ──
    sections.append(f'<h1>{version_label} Synthetic User Testing Report</h1>')

    # ── Synthetic Testing Notice ──
    sections.append(
        '<div class="methodology" style="font-size:0.72em;line-height:1.4;padding:8px 15px;color:#777;">'
        '<strong>&#9888; Synthetic testing notice:</strong> This report uses synthetic personas '
        'generated and evaluated by AI (Claude, Sonnet 4.5) to simulate user reactions '
        'to landing page copy. These are not real users. Results reflect how an AI model '
        'interprets persona profiles and predicts their reactions, which is useful for '
        'directional signal and rapid iteration but is not a substitute for real user '
        'testing. Treat findings as hypotheses to validate, not conclusions.<br>'
        '<strong>Models:</strong> Claude Sonnet 4.5 (claude-sonnet-4-5-20250929) for persona '
        'evaluations. Claude Haiku 4.5 for clarity scoring and data compilation.'
        '</div>'
    )

    # ── Methodology ──
    # Build audience descriptions from audience data or fallback to BUCKET_DESCRIPTIONS
    bucket_descs = {}
    if audience and isinstance(audience, dict) and 'bucket_descriptions' in audience:
        bucket_descs = audience['bucket_descriptions']
    else:
        bucket_descs = BUCKET_DESCRIPTIONS

    bucket_items = []
    for b in stats['by_bucket']:
        desc = bucket_descs.get(b, '')
        short_desc = f' &mdash; {desc}' if desc else ''
        bucket_items.append(
            f'<li><span class="bucket-name">{_fmt_bucket(b)}</span> '
            f'({stats["by_bucket"][b]["n"]}){short_desc}</li>'
        )
    bucket_list_html = '<ul style="margin:5px 0 0 0;padding-left:20px;">' + ''.join(bucket_items) + '</ul>'

    sections.append(
        '<div class="methodology">'
        '<h3 style="margin:0 0 5px 0;font-size:1em;color:#1976d2;">Governing Question</h3>'
        '<p style="margin:0 0 15px 0;">Would this person start a free trial '
        'after reading this landing page?</p>'
        '<h3 style="margin:0 0 5px 0;font-size:1em;color:#1976d2;">Method</h3>'
        f'<p style="margin:0 0 15px 0;">{stats["n"]} synthetic personas evaluated the landing '
        'page copy. Each persona rated resonance, intent, and conversion confidence on a '
        '5-point Likert scale (strongly disagree &rarr; strongly agree), plus qualitative '
        'feedback on what worked and what didn\'t. Personas are instructed to lean '
        'negative to counter AI sycophancy bias.</p>'
        '<h3 style="margin:0 0 5px 0;font-size:1em;color:#1976d2;">Audience Segments</h3>'
        f'{bucket_list_html}'
        '</div>'
    )

    # ── Metric Cards ──
    res_pct = stats['overall']['resonance']['agree_pct']
    int_pct = stats['overall']['intent']['agree_pct']
    conv_pct = stats['overall']['conversion_confidence']['agree_pct']
    db_pct = stats['overall']['dealbreaker_pct']
    db_count = stats['overall']['dealbreaker_count']
    sections.append(
        '<div class="metric-cards">'
        f'<div class="metric-card card-purple">'
        f'<div class="value">{res_pct}%</div>'
        f'<div class="label">Resonance (Agree+)</div></div>'
        f'<div class="metric-card card-blue">'
        f'<div class="value">{int_pct}%</div>'
        f'<div class="label">Intent (Agree+)</div></div>'
        f'<div class="metric-card card-green">'
        f'<div class="value">{conv_pct}%</div>'
        f'<div class="label">Conversion (Agree+)</div></div>'
        f'<div class="metric-card card-red">'
        f'<div class="value">{db_pct}%</div>'
        f'<div class="label">Dealbreakers ({db_count}/{stats["n"]})</div>'
        f'<div class="sublabel">Would not sign up regardless of other factors</div>'
        f'</div>'
        '</div>'
    )

    # ── Executive Summary ──
    if nar.get('exec_summary'):
        sections.append(
            f'<h2>Executive Summary</h2>\n'
            f'<div class="narrative">{nar["exec_summary"]}</div>'
        )

    # ── Conversion Funnel ──
    sections.append('<h2>Conversion Funnel</h2>')
    sections.append(f'<div class="chart-explainer">{_auto_explainer_funnel(stats)}</div>')
    sections.append(_chart_funnel(version_label, stats))

    # ── Researcher's Stance ──
    if nar.get('researchers_stance'):
        sections.append(
            f'<h2>Researcher\'s Stance</h2>\n'
            f'<div class="narrative">{nar["researchers_stance"]}'
            f'<p style="color:#888;margin-top:10px;">'
            f'&mdash; &#129302; Claude</p></div>'
        )

    # ── Key Findings ──
    if nar.get('findings'):
        sections.append(
            f'<h2>Key Findings</h2>\n'
            f'<div class="narrative">{nar["findings"]}</div>'
        )

    # ── Performance by Segment (line chart) ──
    sections.append('<h2>Performance by Audience Segment</h2>')
    sections.append(f'<div class="chart-explainer">{_auto_explainer_bucket_lines(stats)}</div>')
    sections.append(_chart_bucket_lines(version_label, stats))

    # Dealbreakers by segment
    sections.append(f'<div class="chart-explainer">{_auto_explainer_dealbreaker(stats)}</div>')
    sections.append(_chart_dealbreaker_by_bucket(version_label, stats))

    # ── Recommendations ──
    if nar.get('recommendations'):
        sections.append(
            f'<h2>Recommendations</h2>\n'
            f'<div class="narrative">{nar["recommendations"]}</div>'
        )

    # ── Qualitative Themes ──
    if nar.get('qualitative_themes'):
        sections.append(
            f'<h2>Qualitative Themes</h2>\n'
            f'<div class="narrative">{nar["qualitative_themes"]}</div>'
        )

    # ── Price & Clarity ──
    sections.append('<h2>Price Perception &amp; Clarity</h2>')
    sections.append(_chart_price_perception(version_label, stats))
    sections.append(_chart_clarity(version_label, stats))
    if nar.get('clarity_notes'):
        sections.append(f'<div class="narrative">{nar["clarity_notes"]}</div>')

    # ── Cross-version comparison ──
    if history:
        sections.append('<h2>Cross-Version Comparison</h2>')
        all_stats = {}
        for label, res in history.items():
            all_stats[label] = compute_stats(res)
        all_stats[version_label] = stats

        sections.append(_chart_trend_lines(all_stats))
        sections.append(_chart_dealbreaker_trend(all_stats))

    # ── Invalidated Segments ──
    if nar.get('invalidated_segments'):
        sections.append('<h2>Invalidated Segments</h2>')
        sections.append(
            '<p>These segments were tested in earlier rounds and removed from the audience '
            'due to poor fit. Useful for ad targeting: consider negative targeting or '
            'targeting around these profiles.</p>'
        )
        sections.append(f'<div class="narrative">{nar["invalidated_segments"]}</div>')

    # ── Segment Deep Dives ──
    sections.append('<h2>Segment Deep Dives</h2>')
    sections.append(
        '<p>Each segment is discussed below with its description, an example persona, '
        'key metrics, and qualitative feedback.</p>'
    )

    # Build audience lookup by person_id
    audience_by_bucket = defaultdict(list)
    if audience:
        # Handle both flat array and structured {bucket_descriptions, personas} format
        persona_list = audience.get('personas', audience) if isinstance(audience, dict) else audience
        for p in persona_list:
            audience_by_bucket[p.get('bucket', 'unknown')].append(p)

    # Group results by bucket for auto-summaries
    results_by_bucket = defaultdict(list)
    for r in results:
        results_by_bucket[r.get('bucket', 'unknown')].append(r)

    for b in stats['by_bucket']:
        bs = stats['by_bucket'][b]
        res_c = _stat_color(bs['resonance']['agree_pct'])
        int_c = _stat_color(bs['intent']['agree_pct'])
        conv_c = _stat_color(bs['conversion_confidence']['agree_pct'])

        sections.append(
            f'<div class="segment-dive">'
            f'<div class="segment-header">'
            f'<h3><span class="bucket-name">{_fmt_bucket(b)}</span></h3>'
            f'<span class="segment-stats">'
            f'Res: <span class="{res_c}">{bs["resonance"]["agree_pct"]}%</span> · '
            f'Int: <span class="{int_c}">{bs["intent"]["agree_pct"]}%</span> · '
            f'Conv: <span class="{conv_c}">{bs["conversion_confidence"]["agree_pct"]}%</span> · '
            f'DB: {bs["dealbreaker_pct"]}%'
            f'</span></div>'
        )

        # Side-by-side: bucket description + example persona
        desc = BUCKET_DESCRIPTIONS.get(b, '')
        example_persona = audience_by_bucket.get(b, [None])[0]

        context_html = '<div class="segment-context">'
        context_html += (
            f'<div class="context-box">'
            f'<h4>Who They Are</h4>'
            f'<p>{desc}</p>'
            f'</div>'
        )
        if example_persona:
            p = example_persona
            context_html += (
                f'<div class="context-box">'
                f'<h4>Example Persona</h4>'
                f'<p class="persona-detail"><strong>{p["name"]}</strong>, {p["age"]}, '
                f'{p["location"]}</p>'
                f'<p class="persona-detail">{p["occupation"]} · {p["life_stage"]}</p>'
                f'<p class="persona-detail">{p["relevant_history"]}</p>'
                f'<p class="persona-voice">"{p["in_their_voice"]}"</p>'
                f'</div>'
            )
        context_html += '</div>'
        sections.append(context_html)

        # Use narrative deep dive if available, otherwise auto-generate
        if nar.get('bucket_deep_dives', {}).get(b):
            sections.append(f'<div class="narrative">{nar["bucket_deep_dives"][b]}</div>')
        else:
            sections.append(_auto_bucket_summary(results_by_bucket.get(b, [])))

        sections.append('</div>')

    # ── Appendix ──
    sections.append('<h2>Appendix: Full Distributions</h2>')
    if nar.get('appendix_notes'):
        sections.append(f'<div class="narrative">{nar["appendix_notes"]}</div>')

    # Overall distribution table
    sections.append('<h3>Overall Score Distribution</h3>')
    dist_table = (
        '<table><tr><th>Metric</th><th>SD</th><th>D</th><th>N</th>'
        '<th>A</th><th>SA</th><th>Agree+%</th></tr>'
    )
    for dim, label in [
        ('resonance', 'Resonance'),
        ('intent', 'Intent'),
        ('conversion_confidence', 'Conversion'),
    ]:
        d = stats['overall'][dim]['distribution']
        dist_table += (
            f'<tr><td>{label}</td>'
            f'<td>{d["strongly_disagree"]}</td><td>{d["disagree"]}</td>'
            f'<td>{d["neutral"]}</td><td>{d["agree"]}</td><td>{d["strongly_agree"]}</td>'
            f'<td>{stats["overall"][dim]["agree_pct"]}%</td></tr>'
        )
    dist_table += '</table>'
    sections.append(dist_table)

    # Copy text evaluated
    if copy_file:
        try:
            with open(copy_file) as f:
                import html as html_mod
                copy_text = html_mod.escape(f.read())
            sections.append(
                f'<h3>Copy Evaluated ({version_label})</h3>'
                f'<pre style="white-space:pre-wrap;background:#f8f9fa;padding:15px;'
                f'border-radius:8px;font-size:0.85em;line-height:1.6;">{copy_text}</pre>'
            )
        except FileNotFoundError:
            pass

    html = (
        f'<!DOCTYPE html>\n<html><head>\n'
        f'<meta charset="utf-8">\n'
        f'<title>{version_label} Synthetic User Testing Report</title>\n'
        f'<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n'
        f'<style>{REPORT_CSS}</style>\n'
        f'</head><body>\n'
        + '\n'.join(sections)
        + '\n</body></html>\n'
    )

    with open(output_html, 'w') as f:
        f.write(html)

    print(f"Report written to {output_html}")


# ── Apply Clarity Scores ──

def apply_clarity_scores(results_file, scores):
    """Patch clarity_score into results JSON from a list of {person_id, clarity_score} dicts."""
    with open(results_file) as f:
        results = json.load(f)

    score_map = {s['person_id']: s['clarity_score'] for s in scores}
    applied = 0
    for r in results:
        if r['person_id'] in score_map:
            r['clarity_score'] = score_map[r['person_id']]
            applied += 1

    with open(results_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Applied {applied} clarity scores to {results_file}")


# ── CLI ──

def main():
    parser = argparse.ArgumentParser(
        description='Synthetic user testing utilities',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    sub = parser.add_subparsers(dest='command', required=True)

    # extract
    p_extract = sub.add_parser('extract', help='Extract results from agent output files')
    p_extract.add_argument('output_dir', help='Directory containing agent JSONL output files')
    p_extract.add_argument('results_file', help='Output results JSON file')

    # stats
    p_stats = sub.add_parser('stats', help='Compute and print statistics')
    p_stats.add_argument('results_file', help='Results JSON file')
    p_stats.add_argument('--previous', help='Previous version results for deltas')

    # charts
    p_charts = sub.add_parser('charts', help='Generate Plotly HTML charts')
    p_charts.add_argument('version_label', help='Version label (e.g. V6)')
    p_charts.add_argument('results_file', help='Results JSON file')
    p_charts.add_argument('output_html', help='Output HTML file')
    p_charts.add_argument(
        '--history', nargs='+', metavar='LABEL:FILE',
        help='Previous versions as label:file pairs (e.g. V5:results_v5.json)',
    )

    # report
    p_report = sub.add_parser('report', help='Generate HTML report with inline charts')
    p_report.add_argument('version_label', help='Version label (e.g. V6)')
    p_report.add_argument('results_file', help='Results JSON file')
    p_report.add_argument('output_html', help='Output HTML report file')
    p_report.add_argument('--narrative', help='JSON file with narrative sections (exec_summary, findings, etc.)')
    p_report.add_argument('--audience', help='JSON file with audience personas for segment deep dives')
    p_report.add_argument('--copy', help='Markdown copy file to include in appendix')
    p_report.add_argument(
        '--history', nargs='+', metavar='LABEL:FILE',
        help='Previous versions as label:file pairs (e.g. V5:results_v5.json)',
    )

    # skeleton
    p_skeleton = sub.add_parser('skeleton', help='Generate audience skeleton from config')
    p_skeleton.add_argument('config_file', help='JSON config file')
    p_skeleton.add_argument('output_file', help='Output skeleton JSON file')

    args = parser.parse_args()

    if args.command == 'extract':
        results = extract_results(args.output_dir)
        with open(args.results_file, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Extracted {len(results)} results to {args.results_file}")

    elif args.command == 'stats':
        with open(args.results_file) as f:
            results = json.load(f)
        previous = None
        if args.previous:
            with open(args.previous) as f:
                previous = json.load(f)
        stats = compute_stats(results, previous)
        print_stats(stats)

    elif args.command == 'charts':
        with open(args.results_file) as f:
            results = json.load(f)
        history = None
        if args.history:
            history = {}
            for item in args.history:
                if ':' not in item:
                    print(f"Error: history items must be LABEL:FILE, got '{item}'", file=sys.stderr)
                    sys.exit(1)
                label, filepath = item.split(':', 1)
                with open(filepath) as f:
                    history[label] = json.load(f)
        generate_charts(args.version_label, results, args.output_html, history)

    elif args.command == 'report':
        with open(args.results_file) as f:
            results = json.load(f)
        narrative = None
        if args.narrative:
            with open(args.narrative) as f:
                narrative = json.load(f)
        history = None
        if args.history:
            history = {}
            for item in args.history:
                if ':' not in item:
                    print(f"Error: history items must be LABEL:FILE, got '{item}'", file=sys.stderr)
                    sys.exit(1)
                label, filepath = item.split(':', 1)
                with open(filepath) as f:
                    history[label] = json.load(f)
        audience = None
        if args.audience:
            with open(args.audience) as f:
                audience = json.load(f)
        generate_report(args.version_label, results, args.output_html, narrative, history, audience, args.copy)

    elif args.command == 'skeleton':
        with open(args.config_file) as f:
            config = json.load(f)
        generate_skeleton(config, args.output_file)


if __name__ == '__main__':
    main()
