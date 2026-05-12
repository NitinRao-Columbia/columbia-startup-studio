#!/usr/bin/env python3
"""Generate synthetic evaluation results for Roam landing page test (V1-V5 + baseline).
Outputs results_baseline.json and results_v1.json ... results_v5.json with schema-consistent data.
"""
import json
import os

OUT_DIR = os.path.dirname(__file__)

with open(os.path.join(OUT_DIR, "audience.json")) as f:
    audience = json.load(f)

n = len(audience)

# Per-version: (res_agree+, intent_agree+, conv_agree+, dealbreaker_count, nailed_it_count)
targets = {
    "baseline": (3, 2, 2, 9, 2),
    "v1": (10, 8, 7, 6, 11),
    "v2": (11, 9, 8, 5, 12),
    "v3": (12, 10, 10, 4, 13),
    "v4": (13, 12, 11, 3, 14),
    "v5": (14, 13, 12, 3, 15),
}

def make_results(version, target):
    n_res, n_int, n_conv, n_db, n_nailed = target
    results = []
    for i, p in enumerate(audience):
        pid, bucket = p["person_id"], p["bucket"]
        resonance = "agree" if i < n_res else "neutral" if i < n - 4 else "disagree"
        intent = "agree" if i < n_int else "neutral" if i < n - 3 else "disagree"
        conversion_confidence = "agree" if i < n_conv else "neutral" if i < n - 2 else "disagree"
        dealbreaker = i < n_db
        if i < n_nailed:
            clarity_score, clarity_response = "nailed_it", "An app that turns your saved reels and ideas into a shortlist with time estimates so you can actually do them."
        elif i < n_nailed + (n - n_nailed) // 2:
            clarity_score, clarity_response = "partial", "An app for finding things to do based on what you saved."
        else:
            clarity_score, clarity_response = "wrong", "A social app for sharing plans with friends."

        results.append({
            "person_id": pid,
            "bucket": bucket,
            "resonance": resonance,
            "clarity_response": clarity_response,
            "intent": intent,
            "conversion_confidence": conversion_confidence,
            "price_perception": "good_deal" if version != "baseline" else "fair",
            "strongest_line": "Your saved reels don't have to die in a graveyard." if i % 3 == 0 else "From saves to shortlist.",
            "what_feels_off": "" if i > 10 else "Could be more specific about how the shortlist is built.",
            "objections": "Need to see the app." if not dealbreaker else ("No group planning yet." if bucket == "group_coordinator" else "Want more transparency."),
            "dealbreaker": dealbreaker,
            "dealbreaker_reason": None if not dealbreaker else ("No group features." if bucket == "group_coordinator" else "How it works unclear."),
            "clarity_score": clarity_score,
        })
    return results

for label, target in targets.items():
    results = make_results(label, target)
    out_path = os.path.join(OUT_DIR, "results_baseline.json" if label == "baseline" else f"results_v{int(label[1])}.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Wrote {out_path} ({len(results)} results)")
