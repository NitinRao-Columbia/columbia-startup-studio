# Unified Combined Test Brief

**Test Name:** unified_combined
**Date:** 2026-02-25
**Folder:** `synthetic-user-testing/unified_combined/`

---

## What We're Testing

A unified landing page for Standard Deviants — synthesizing the strongest messaging and audience insights from three independent synthetic test runs (trk2121, sa4166, mhk2182).

Each team member tested a different product framing against their own audience:
- **trk2121:** Mixed-methods analysis platform (auto-selects stats, explains results). Best conversion: 17% at V3.
- **sa4166:** CleanSheet — workflow audit trail, dependency mapping, "Receipt" metaphor. Best resonance: 52% at V2, 0% conversion.
- **mhk2182:** Coquali — qualitative coding + collaboration workspace. V1 results only.

This test combines:
1. The strongest copy elements from all three (transparency/auditability framing, paste-cycle pain recognition, outcome-focused language)
2. A unified audience that merges overlapping segments and adds unique ones discovered by individual members
3. Messaging that drops "no code" language per brand position guidelines — leads with outcomes and transparency

**Goal:** Get from "three separate experiments" to "one coherent landing page ready for real user testing."

---

## Who's Seeing This

Mixed referral sources reflecting real acquisition channels:
- Google search (e.g., "analyze interview data without coding," "data analysis tool for researchers")
- Word of mouth / colleague referral
- Social media ad (Instagram, LinkedIn)
- Academic forum / Slack community link

Each persona gets a randomized referrer to avoid channel bias.

---

## Persona Buckets

**6 buckets x 12 personas = 72 total**

Dropped segments: `skeptical_methodologist` and `budget_gatekeeper` — both hit 0% conversion across all team members' tests. These are product-level blockers (need Bayesian/SEM support, SOC 2 Type II, FERPA compliance) that copy cannot solve.

### 1. thesis_dreader
Grad students (MA/PhD) who have collected data — interviews, surveys, observations — and are dreading the analysis chapter. Currently brute-forcing with Excel + ChatGPT. High urgency (deadline-driven), tight personal budgets, domain expertise is their work (sociology, education, public health), not statistics.

**Typical quote:** "If I could change anything, it would be have someone else do my data analysis."

**Source:** trk2121 (17% conversion at V3), sa4166 (social_science_thesis_dreader), mhk2182 (deadline-driven researchers)

### 2. duct_tape_analyst
Mid-career professionals (program evaluators, operations analysts, research coordinators) with a 4-6 tool workflow: Excel → Word → R or SPSS → ChatGPT → email → Google Drive. Chronic pain but inertia is the barrier — "I know how Excel is going to malfunction." Often the only person who understands the workflow.

**Typical quote:** "If I'm out for one week, nobody can run this workflow without breaking something."

**Source:** trk2121 (25% conversion at V3), sa4166

### 3. ai_loop_prisoner
People actively stuck in the paste-error-paste cycle with ChatGPT or Claude. They know what AI can do, they can see the potential, but actually executing means generating code they can't debug, waiting on outputs they can't verify, and trusting results they can't explain. The gap between "theoretically possible" and "practically controllable" is the pain.

**Typical quote:** "I do not have the capacity to figure it out myself, just to copy and paste it again to GPT."

**Source:** trk2121 (33% conversion at V3 — best performer), sa4166

### 4. ai_weary_old_school_analyst
Experienced analysts who write their own R, MATLAB, or Python. They value the manual process because it builds understanding. They've seen colleagues use AI-generated code that breaks silently, and they distrust automation for exploratory or novel analysis. They're not anti-tech — they're pro-comprehension.

**Typical quote:** "I wrote it all up by myself because I wanted to learn R... I'm not sure I'd trust AI for exploration."

**Source:** sa4166 (unique segment — untested against unified product concept)

### 5. power_qual_practitioner
UX researchers, insights leads, and research ops professionals who do collaborative qualitative work at scale. They manage multiple concurrent studies, care about codebook governance, inter-rater reliability, and traceability. Currently using Dovetail, Reframer, or spreadsheets. Want rigor without heavyweight tools like NVivo.

**Typical quote:** "Synthesis used to mean a week of copy-pasting into spreadsheets. Now I need to show patterns the same day the interviews finish."

**Source:** mhk2182 (unique segment — untested against unified product concept)

### 6. fast_moving_product_team
PMs, designers, and founders doing scrappy research. They run 5-10 user interviews per sprint, need to synthesize fast, and present findings to stakeholders who want clear, defensible themes — not a 40-page report. Speed and clarity matter more than methodological purity.

**Typical quote:** "I don't need another notes tool. I need something that gets me from calls to defensible themes fast."

**Source:** mhk2182 (unique segment — untested against unified product concept)

---

## Product Description (Canonical)

> Standard Deviants is a web-based analysis platform that takes you from raw data to understood results by clicking, not coding. Upload interviews, surveys, or spreadsheets — the platform selects the right analysis method, runs it, and explains what it means in plain language. Every result is auditable, exportable, and reproducible.

**Core claim (for clarity scoring):** A point-and-click data analysis platform that selects the right statistical or qualitative method for your data and explains the results in plain language.

---

## Pricing

- **Free** — 3 projects, core analysis features, unlimited exports
- **Pro — $10/month** — unlimited projects, advanced visualizations, collaboration, priority support
- **Team — $25/month** — everything in Pro plus shared workspaces, inter-rater reliability, and role-based permissions

(Kept from trk2121's testing — price perception was overwhelmingly "fair" at these tiers.)

---

## Copy Skeleton

The unified V1 copy should be structured as:

1. **Hero** — Headline + subhead + CTA. Lead with outcome, not feature.
2. **Problem** — The paste-cycle / tool fragmentation pain. Grounded, specific, not abstract.
3. **Solution** — What the platform does. Transparency framing: "shows what method, why, what it means." Use "starting points, not the full list" to avoid the specificity trap (V2 regression lesson).
4. **Who It's For** — Segments reflected back. Each audience should see themselves.
5. **How It Works** — Upload → Clean → Analyze → Visualize → Export
6. **Social Proof** — Composite testimonials from personas that match target segments
7. **Objection Handling** — Trust, inertia, price, existing tools
8. **Security & Data** — Encryption, data isolation, never trains models, DPA/BAA available
9. **Pricing** — Tiers with free tier prominent
10. **Final CTA** — Reinforces the outcome promise

---

## Evaluation Criteria

Using the **full schema** (V1-V5):

```json
{
  "person_id": "<number from profile>",
  "bucket": "<bucket from profile>",
  "resonance": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "clarity_response": "<describe in one sentence what this product does>",
  "intent": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "conversion_confidence": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "price_perception": "<too_expensive|fair|good_deal>",
  "strongest_line": "<single line from the copy that resonated most>",
  "what_feels_off": "<anything generic, try-hard, or dishonest-feeling>",
  "objections": "<what's stopping you from signing up>",
  "dealbreaker": "<true|false>",
  "dealbreaker_reason": "<why, or null if dealbreaker is false>",
  "gut_reaction": "<1-2 sentences, first impression>",
  "unanswered_questions": "<what the page didn't answer>",
  "price_reaction": "<specific thoughts on pricing tiers>"
}
```

No test-specific additions for V1.

---

## Stopping Criteria

- **Minimum:** 5 rounds
- **Target:** >50% conversion confidence agree+
- **Hard stop:** 10 iterations
- **Convergence:** Two consecutive rounds with <3pp change on all dimensions
- **User discretion:** Stop whenever user is satisfied with copy quality

---

## Template Inputs (for prompt assembly)

| Variable | Value |
|----------|-------|
| `{PRODUCT_DESCRIPTION}` | "Standard Deviants is a web-based analysis platform that takes you from raw data to understood results by clicking, not coding. Upload interviews, surveys, or spreadsheets — the platform selects the right analysis method, runs it, and explains what it means in plain language. Every result is auditable, exportable, and reproducible." |
| `{PRODUCT_CORE_CLAIM}` | "a point-and-click data analysis platform that selects the right statistical or qualitative method for your data and explains the results in plain language" |
| `{SCHEMA}` | Full schema (above) |
| Audience file | `audience.json` |
| Copy file | `copy_v1.md` (to be written after audience generation) |

---

## Cross-Team Insights Feeding V1 Copy

These are the proven signals from all three tests that V1 must incorporate:

### Must include (proven resonance drivers):
- **Transparency/auditability framing** — "Every result shows the method used, the parameters, the assumptions checked, and what it means in plain language" (trk's most-cited line, ~25x in V3). Sa's "Receipt" metaphor (15x citations). Universal demand for traceability (mhk).
- **Paste-cycle pain recognition** — The specific frustration of AI-generated code that can't be verified. Appears across all three audience designs.
- **"Starting points, not the full list"** — Avoids the specificity trap that caused trk's V2 regression (listing specific methods created a perceived capability ceiling, conversion dropped 10%→2%).
- **Qualitative + quantitative in one place** — Interview coding AND statistical analysis. This is what differentiates from NVivo (qual only) and SPSS (quant only).

### Must avoid (proven failure modes):
- **"No code" / "low code" language** — Brand position explicitly prohibits. Table stakes, not differentiator.
- **Jargon** — "Polyglot Logic Engine" and "Transparency Tax" were catastrophic in sa's V1 (98% dealbreakers). No invented terminology.
- **"AI-powered" / "intelligent" / "smart"** — Triggers skepticism per brand position.
- **Exhaustive method lists** — Creates perceived ceiling (trk V2 regression). Show breadth, don't enumerate.
- **"All-in-one platform"** — Explicitly warned against by advisor. Sets undeliverable expectations.
- **Hiding pricing** — Sa's V3 removed visible pricing; budget_gatekeeper resonance dropped to 0% and dealbreakers hit 100%. "Waitlist + free trial sounds like beta, not readiness."
