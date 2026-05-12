---
name: synthetic-user-testing
description: >-
  Use this skill to run synthetic user testing on copy, messaging, and
  positioning using AI-generated personas. Triggered by "let's do
  synthetic testing", "synthetic user test", "test this copy", "run a
  synthetic test", or "/synthetic-user-testing". Handles the full
  lifecycle: brief creation, audience generation, iterative evaluation
  rounds, per-round reports, PDF conversion, and Google Ads campaign
  recommendations.
---

# Synthetic User Testing

Guide the full lifecycle of synthetic user testing: simulating audience reactions to copy using AI-generated personas before spending money on real traffic.

This is not a replacement for real user testing. It's a rapid iteration tool for getting copy from "first draft" to "ready to put in front of real people."

## Prerequisites

- **Python 3** (stdlib only; no pip installs needed)
- **Web browser** to view HTML reports and charts
- **Google Chrome** (optional, only for PDF conversion via headless mode)
- **Model requirements:** Opus for orchestration, Sonnet for evaluation agents, Haiku for clarity scoring

If not running as Opus, flag it:
> "Note: I'm currently running as [model]. Synthetic testing orchestration works best on Opus. Want me to proceed anyway?"

## Bundled Resources

| Resource | Purpose | When to use |
|----------|---------|-------------|
| [references/prompt-templates.md](references/prompt-templates.md) | Canonical evaluation + clarity scoring prompts (verbatim) | When assembling prompts for an evaluation round |
| [references/evaluation-schemas.md](references/evaluation-schemas.md) | Full + simplified JSON schemas, narrative JSON schema, audience persona schema | When setting up a new test or switching schema versions |
| [references/best-practices.md](references/best-practices.md) | Patterns and best practices for synthetic testing at scale | When making decisions at any phase |
| [scripts/synthetic_eval.py](scripts/synthetic_eval.py) | Utilities: extract, stats, charts, report, skeleton. Also importable: `from synthetic_eval import extract_results, compute_stats, apply_clarity_scores` | During evaluation rounds and reporting |

If the project has a methodology doc at `docs/user_testing/synthetic_testing/methodology.md`, read it for additional context. The skill is self-contained without it.

---

## Phase 0: Gather Context

Before writing the brief, ask the user for context documents:

> Before we start, do you have any of these documents I should read?
> 1. **Product brief or PRD** — what the product does, who it's for
> 2. **Style guide** — brand voice, tone, visual identity
> 3. **Brand positioning doc** — competitive positioning, messaging pillars
> 4. **Existing copy** — current landing page, ad copy, emails to test
> 5. **Existing user research** — interviews, survey results, personas
>
> I can work without these, but having them makes the personas and evaluations much sharper.

Read any provided documents before proceeding. If the project has `docs/ongoing/` files (PRD.md, STYLE_GUIDE.md, BRAND_POSITION.md), check those too.

---

## Phase 1: Brief Creation

Create the test folder: `docs/user_testing/synthetic_testing/yyyymmdd.nn_[test_name]/`

Walk the user through the brief interactively. Don't dump a template; ask questions and build it together.

### Sections to walk through

**1. What we're testing** — What specific copy/messaging? Where does it live?

**2. Who's seeing this** — How do people arrive? (Ad click, organic search, referral, cold email?) This affects evaluation context.

**3. Persona buckets** — Design 4-6 archetypes. Ask:
> "Who are the different types of people who would see this? Think about their motivations, past experiences with your product category, and skepticism levels."

For each bucket, define: a descriptive name (e.g., `journal_graveyard`), 2-3 sentence behavioral description, a typical quote in their voice, and expected prevalence.

**4. Product description** — Canonical 1-2 sentences. Feeds into clarity scoring.

**5. Pricing** (if applicable) — Tiers and prices to test reactions to.

**6. Copy skeleton** — Structural sections of the copy (hero, problem, solution, social proof, pricing, CTA, etc.).

**7. Evaluation criteria** — Start with the standard schema from [references/evaluation-schemas.md](references/evaluation-schemas.md). Ask:
> "The standard evaluation covers resonance, clarity, intent, conversion confidence, price perception, and qualitative feedback. Do you want to add any test-specific questions?"

**8. Stopping criteria** — Defaults: minimum 5 rounds, stop at >50% conversion agree+, 10 iterations, or convergence. Adjust if needed.

Save as `01_brief_[test_name].md`.

**STOP** — Wait for user review and approval before proceeding.

---

## Phase 2: Audience Generation

### Generate the audience

**Default:** 60 personas, 5 equal buckets of 12. Ask the user:
> "Default is 60 personas (12 per bucket x 5 buckets). Want to change the total count or bucket sizes?"

**Generation method (deterministic skeleton):**
1. Create a skeleton config JSON with bucket sizes, gender ratios, age ranges
2. Run: `python3 <skill_dir>/scripts/synthetic_eval.py skeleton config.json skeleton.json`
3. Use a Sonnet agent to fill in qualitative fields (name, occupation, backstory, emotional baseline, voice quote)
4. Save as `audience.json`

Generate names via Faker library (Python or Ruby), not LLM-invented.

### Baseline round (recommended)

Run the audience against a deliberately mediocre or generic copy version. This calibrates the floor for what "neutral" looks like. Save as `copy_baseline.md` and `results_baseline.json`.

### Write or receive copy v1

Save as `copy_v1.md`.

---

## Phase 3: Iterative Evaluation

This is the core loop. **Do not stop after one round.**

### For each round

**1. Confirm before launching:**
> "Ready to run V[N] evaluation? This will launch [Y] individual evaluation calls against copy_v[N].md. Confirm?"

**2. Run evaluation calls.** Read [references/prompt-templates.md](references/prompt-templates.md) for the canonical prompt. Key rules:
- **One persona per call.** Each persona gets its own isolated Sonnet call. This prevents cross-contamination between personas and maximizes persona fidelity (research shows LLMs flatten within-group diversity and lose character consistency when roleplaying multiple personas simultaneously).
- For 60 personas: 60 calls. Use `run_in_background: true` and batch into groups of 10 parallel agents, each handling one persona.
- Only `{PERSONA}` changes between calls. Prompt is frozen for the round.

**3. Extract and compile results:**
```bash
python3 <skill_dir>/scripts/synthetic_eval.py extract /tmp/vN_outputs/ results_vN.json
```

Post-extraction cleanup:
- **Enrich with names:** Eval agents don't always include names. Load the audience file, build a `person_id → name` map, and patch each result.
- **Check for stray files:** Agents sometimes write results to `evaluation_persons_*.json` in the working directory instead of outputting inline. Merge these by `person_id` and clean up afterward.

**4. Run clarity scoring.** Single Haiku agent using the clarity prompt from [references/prompt-templates.md](references/prompt-templates.md). Use `apply_clarity_scores()` to patch results. **Never skip this step.**

**5. Generate report:**

Rounds 1-5:
```bash
python3 <skill_dir>/scripts/synthetic_eval.py stats results_vN.json --previous results_vN-1.json
python3 <skill_dir>/scripts/synthetic_eval.py charts VN results_vN.json charts_vN.html \
    --history BL:results_baseline.json V1:results_v1.json ...
```

Rounds 6+:
```bash
python3 <skill_dir>/scripts/synthetic_eval.py report VN results_vN.json report_vN.html \
    --narrative narrative_vN.json \
    --audience audience.json \
    --copy copy_vN.md \
    --history BL:results_baseline.json V1:results_v1.json ...
```

Write a narrative JSON for each report round (see [references/evaluation-schemas.md](references/evaluation-schemas.md) for schema).

**6. Present results.** For rounds 1-5 (separate summary + charts), write `summary_vN.md` covering:
- Score distributions per dimension (overall + per bucket)
- Clarity accuracy breakdown (wrong / partial / nailed it)
- Top qualitative themes (what keeps coming up)
- Strongest lines by frequency and which buckets they came from
- Most common objections + dealbreaker count
- Price perception summary
- **Deltas from previous version** (V2+): how each dimension moved, which buckets shifted most

For all rounds, present to the user: top-line metrics, biggest changes from previous round, key qualitative themes, and specific recommendations.

**7. Revise copy** based on feedback. Save new copy as `copy_v{N+1}.md`. Document what changed in `copy_vN_changes.md` (separate from copy; evaluators must never see it). Write the changes doc **before** running the next eval. Use this template:

```markdown
## Changes from V{N-1}

- **Section:** [which section changed]
  **Change:** [what was replaced with what]
  **Why:** [specific feedback that motivated the change, with data]
```

This creates a decision log for post-mortem analysis.

### Encourage iteration

After presenting results:
> "We're at V[N] with [X]% conversion. The qualitative feedback suggests [specific opportunities]. Want to iterate further, or is this good enough to move to the final report?"

### Mid-study pivots

Offer these when the data supports them:
- **Swap dead segments** — 0% conversion across 3+ versions with high dealbreakers. Create new audience file (`audience_vN.json`), keep returning personas unchanged.
- **Change audience size** — Increase for more statistical reliability, decrease to reduce cost.
- **A/B variants** — Test two approaches against the same audience in parallel (e.g., different framings).

### Stopping criteria

After minimum 5 rounds, stop when ANY of:
- Conversion confidence: majority (>50%) "Agree" or "Strongly agree"
- 10 iterations run
- Two consecutive rounds with no meaningful change
- Qualitative feedback converges
- User says they're satisfied

Consult [references/best-practices.md](references/best-practices.md) for analytical guidance throughout.

---

## Phase 4: Final Report

### Deliverables

The final output of a synthetic test is:

- The winning copy version (highest scores)
- A summary of what messaging resonated and what didn't
- Key objections the copy couldn't fully resolve (useful for FAQ, follow-up content)
- Dealbreaker analysis (hard blockers and their prevalence)
- Price perception data
- The full decision log from `copy_vN_changes.md` files across versions

### Generate the report

Generate the unified HTML report for the final version with full cross-version history:

```bash
python3 <skill_dir>/scripts/synthetic_eval.py report VN results_vN.json report_vN.html \
    --narrative narrative_vN.json \
    --audience audience_vN.json \
    --copy copy_vN.md \
    --history BL:results_baseline.json V1:results_v1.json ... VN:results_vN.json
```

The report includes: executive summary, findings, recommendations, qualitative themes, cross-version trend charts, per-bucket breakdowns with deep dives, individual persona cards, the full copy, and audience profiles.

### PDF conversion (optional)

After generating the final report, offer:
> "Want me to convert the final report to PDF?"

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
    --headless --disable-gpu --no-margins \
    --print-to-pdf="report_vN.pdf" \
    "file://$(pwd)/report_vN.html"
```

Requires Google Chrome installed.

---

## Phase 5: Ad Campaign Recommendation (Optional)

After the final report, offer:
> "Based on the test results, I can draft a Google Ads campaign that targets the highest-converting segments first and scales up as ROI is proven. Want me to put that together?"

If yes, generate `google_ads_campaign.md` with:
- Strategy: start with highest-converting segment, expand as ROI proves out
- Expansion ladder with budget thresholds and advancement triggers
- Segment performance summary from the study
- Campaign setup (type, bidding, budget, networks, locations)
- Conversion tracking (set up before spending)
- Ad extensions derived from the copy
- Per-segment ad groups with keywords and responsive search ads
- Negative keywords
- Post-launch optimization playbook
- Landing page notes based on persona feedback

Prioritize segments by conversion rate and dealbreaker rate. Never include segments with 0% conversion across all versions (suggest alternative paths for them instead).

---

## File Structure

Each test produces files in its dated folder:

```
docs/user_testing/synthetic_testing/
  yyyymmdd.nn_[test_name]/
    01_brief_[test_name].md
    02_plan_[test_name].md            (evaluation prompts, audience config, execution plan)
    audience.json                    (may evolve: audience_v2.json, etc.)
    audience_vN_skeleton.json        (if using skeleton approach)
    copy_baseline.md
    copy_v1.md
    copy_vN_changes.md              (v2+, separate from copy)
    results_vN.json
    narrative_vN.json               (v6+, feeds into report)
    report_vN.html                  (v6+, unified report)
    summary_vN.md                   (v1-v5, human-readable)
    charts_vN.html                  (v1-v5, standalone charts)
    google_ads_campaign.md          (optional, post-study)
```

---

## When NOT to Use This Skill

- Quick copy edits that don't need audience validation
- Testing design or visual elements (this tests copy only)
- When real user feedback already exists and synthetic validation adds nothing
- Single-question A/B tests (use simpler methods)
- When the user explicitly says they don't want the full workflow
