# V2 Evaluation Summary

**Test:** Landing Page Copy V2
**Date:** 2026-02-20
**Personas:** 60 (5 buckets x 12)

---

## Top-Line Metrics

| Metric | V2 | V1 | Delta |
|--------|-----|-----|-------|
| Resonance (agree+) | **30%** | 38% | **-8pp** |
| Intent (agree+) | **27%** | 28% | **-1pp** |
| Conversion Confidence (agree+) | **2%** | 10% | **-8pp** |
| Dealbreakers | **30%** (18/60) | 32% (19/60) | **-2pp** |
| Clarity: Nailed It | **78%** | 3% | **+75pp** |
| Price: Too Expensive | **2%** (1/60) | 0% | +2pp |

**Verdict:** V2 moved in the wrong direction on the core funnel metrics. The copy got dramatically clearer (+75pp nailed_it) but that clarity came with specificity that exposed capability gaps and diluted emotional resonance. The changes intended for professional segments didn't move them, while the tonal shift hurt the two early-adopter segments that were actually converting.

---

## Score Distributions

### Overall (n=60)

| Dimension | SD | D | N | A | SA | Agree+% | V1 |
|-----------|-----|-----|-----|-----|-----|---------|-----|
| Resonance | 4 | 18 | 20 | 17 | 1 | 30% | 38% |
| Intent | 7 | 12 | 25 | 16 | 0 | 27% | 28% |
| Conversion | 16 | 26 | 17 | 1 | 0 | 2% | 10% |

### Per Bucket

| Bucket | V2 Res | V1 Res | V2 Int | V1 Int | V2 Conv | V1 Conv | V2 DB% | V1 DB% |
|--------|--------|--------|--------|--------|---------|---------|--------|--------|
| thesis_dreader | 67% | 67% | 58% | 58% | **0%** | **33%** | 8% | 0% |
| ai_loop_prisoner | **50%** | **83%** | 50% | 50% | 8% | 17% | 0% | 0% |
| duct_tape_analyst | 25% | 25% | 17% | 25% | 0% | 0% | 25% | 33% |
| budget_gatekeeper | 8% | 17% | 8% | 8% | 0% | 0% | **58%** | **50%** |
| skeptical_methodologist | 0% | 0% | 0% | 0% | 0% | 0% | **58%** | **75%** |

**The two biggest movements are regressions:**
1. **thesis_dreader conversion collapsed: 33% → 0%.** V2's added specificity (regression, thematic coding) actually exposed capability gaps. Multiple thesis_dreaders realized the tool doesn't cover their specific committee requirements (HLM, SEM, multilevel modeling). V1 was vague enough to leave room for hope; V2 was specific enough to show the ceiling.
2. **ai_loop_prisoner resonance dropped: 83% → 50%.** The V2 problem section added a second paragraph for experienced analysts, which diluted the "I'm stuck in a ChatGPT loop" emotional hook that was the primary resonance driver for this segment.

---

## Clarity Accuracy

| Score | V2 Count | V2 % | V1 Count | V1 % |
|-------|----------|------|----------|------|
| Wrong | 0 | 0% | 5 | 8% |
| Partial | 13 | 22% | 53 | 88% |
| Nailed It | 47 | **78%** | 2 | **3%** |

**Analysis:** This is V2's clear win. The V2 copy is dramatically better at communicating what the product actually does. The addition of specific methods (regression, thematic coding, override language) gave personas concrete things to anchor on. Even skeptical_methodologists who rejected the product could accurately describe it.

Per-bucket clarity:
- ai_loop_prisoner: 12/12 nailed_it (100%)
- duct_tape_analyst: 10/12 nailed_it (83%)
- budget_gatekeeper: 9/12 nailed_it (75%)
- skeptical_methodologist: 9/12 nailed_it (75%)
- thesis_dreader: 7/12 nailed_it (58%)

**Implication:** V2 proves that specificity drives clarity. The challenge is that specificity also drives rejection when the specific methods listed don't match the user's specific needs. This is the "specificity trap" — the more concrete you get, the more people you help understand the product AND the more people you help realize it's not for them.

---

## Top Strongest Lines (by frequency)

1. **"Every result shows the method used, the parameters, the assumptions checked, and what it means in plain language. Auditable. Exportable. Reproducible."** — 21 citations across all 5 buckets. Still the copy's strongest line (was 34 in V1 — V2's expanded version with "assumptions checked" and "Reproducible" added resonated slightly less broadly but still dominant).
2. **"Results are deterministic — same data, same output, every time."** — 4 citations (ai_loop_prisoner, budget_gatekeeper, thesis_dreader). New in V2's objection handling; this is the strongest new line.
3. **"Click 'Correlate' — it selects Spearman or Pearson based on your data, shows you why it chose that method"** — 3 citations (ai_loop_prisoner, skeptical_methodologist). The transparency reframe landed.
4. **"Click 'Regress' — build linear or logistic regression models"** — 2 citations (ai_loop_prisoner, thesis_dreader). Adding advanced methods signaled higher ceiling.
5. **"We're pursuing SOC 2 Type II certification"** — 2 citations (budget_gatekeeper). Cited as strongest AND as dealbreaker — the acknowledgment matters but "pursuing" isn't enough.
6. **"Import from CSV, Excel, SPSS, Qualtrics, and Google Forms"** — 2 citations (budget_gatekeeper). Integration specifics resonate with institutional buyers.

**Takeaway:** The auditable/exportable/reproducible line remains dominant but is cited less (21 vs 34). The "deterministic" claim is a strong new entry. Transparency-reframed lines ("shows you why") are landing with the segments that needed them.

---

## Most Common Objections & Themes

### 1. The specificity trap: "You mentioned X but not MY X"
V2 added regression, thematic coding, and mixed-methods — which helped clarity but triggered a new class of objection: "Where's multilevel modeling / SEM / IRT / psychometrics / factor analysis / survival analysis?" Multiple thesis_dreaders who were neutral-to-positive in V1 now see the listed methods as a ceiling, not a floor. The copy is specific enough to be helpful AND specific enough to be limiting.

### 2. "Pursuing SOC 2" is the new dealbreaker anchor
Budget_gatekeepers unanimously flagged "pursuing SOC 2 Type II" as a yellow or red flag. The acknowledgment was better than silence (V1), but "pursuing" signals "not yet compliant" — which is a hard institutional blocker. 7/12 budget_gatekeepers have dealbreakers, up from 6/12 in V1.

### 3. "'Full transparency' is marketing language until proven otherwise"
Across ai_loop_prisoner, duct_tape_analyst, and skeptical_methodologist, the phrase "full transparency" triggers eye-rolls. Multiple personas explicitly called it out as a genre of SaaS copy. The specific instances (Spearman vs Pearson, assumption checking) land; the abstract claims don't.

### 4. "This copy was written for scared beginners, not for me"
Duct_tape_analysts (#16, #21, #22, #24) and skeptical_methodologists (#51, #53, #55) explicitly noted that the copy's persona is someone who's afraid of data. Even with V2's broadened "Who It's For" section, the overall tone still reads as novice-facing.

### 5. "The qualitative analysis section is too thin"
Multiple duct_tape_analysts and thesis_dreaders said the "Click 'Code'" section was the most interesting part but had the least detail. "Emergent codes or bring your own codebook" isn't enough to evaluate the capability.

---

## Dealbreaker Analysis

**18 dealbreakers (30%)** — distributed as:

| Bucket | V2 DB | V1 DB | Delta | Primary Reason |
|--------|-------|-------|-------|----------------|
| skeptical_methodologist | 7 (58%) | 9 (75%) | **-17pp** | Epistemological + no evidence of methodological rigor |
| budget_gatekeeper | 7 (58%) | 6 (50%) | **+8pp** | "Pursuing" SOC 2 read as disqualifying |
| duct_tape_analyst | 3 (25%) | 4 (33%) | **-8pp** | Integration/migration + output format gaps |
| thesis_dreader | 1 (8%) | 0 (0%) | **+8pp** | Missing specific method (HLM) |
| ai_loop_prisoner | 0 (0%) | 0 (0%) | 0pp | — |

**Key shift:** Skeptical_methodologist dealbreakers dropped from 75% to 58% — the transparency reframe helped at the margins. But budget_gatekeeper dealbreakers increased from 50% to 58% — the security section actually crystallized the "pursuing" gap into a concrete objection rather than leaving it as vague absence.

---

## Price Perception

| Rating | V2 Count | V2 % | V1 Count | V1 % |
|--------|----------|------|----------|------|
| Good Deal | 39 | 65% | 41 | 68% |
| Fair | 20 | 33% | 19 | 32% |
| Too Expensive | 1 | 2% | 0 | 0% |

**Price remains a non-issue.** One duct_tape_analyst rated "too expensive" — but their qualitative feedback suggests the objection was about value/fit, not actual price sensitivity. Budget_gatekeepers remain 12/12 "good deal."

---

## Key Qualitative Themes

### What V2 improved
1. **Clarity is dramatically better.** 78% nailed_it vs 3%. This is the single biggest improvement across both rounds.
2. **"Deterministic" and "reproducible" are powerful words.** The new language in the objection handling section created a strong signal for people worried about ChatGPT reliability.
3. **The transparency reframe partially worked.** Skeptical_methodologist dealbreakers dropped 17pp. The "shows you why / lets you override" language is better than "you don't need to know which."
4. **Duct_tape_analyst dealbreakers dropped 8pp.** The integration language (CSV, Excel, SPSS, Qualtrics, Google Forms) helped, and the "My team uses multiple tools" objection was noticed.

### What V2 broke
1. **The specificity trap.** Adding regression and thematic coding helped clarity but triggered "where's MY specific method?" from thesis_dreaders, collapsing their conversion from 33% to 0%.
2. **Emotional resonance was diluted.** The V2 problem section added a second paragraph for experienced analysts. This split the emotional focus and weakened the "I felt seen" effect that drove the early-adopter segments. Ai_loop_prisoner resonance dropped 33pp.
3. **The security section backfired for budget_gatekeepers.** Saying "pursuing SOC 2" is worse than saying nothing for some personas — it's a concrete thing to reject rather than a vague absence.

### What V2 didn't fix
1. **Skeptical_methodologists remain at 0%/0%/0%.** The transparency reframe reduced dealbreakers but didn't generate positive engagement. These personas object to the product category, not the copy.
2. **Budget_gatekeepers can't convert without actual compliance.** Copy changes can't substitute for SOC 2 certification, BAA templates, and FERPA documentation.
3. **The copy's overall tone still reads as beginner-facing.** Multiple experienced personas said the "click a button, get an answer" framing is condescending.

---

## Diagnosis: What Happened

V2 attempted to broaden appeal to professional segments while preserving early-adopter resonance. The result was the opposite: professional segments barely moved (their blockers are product/business, not copy), while the tonal shift and added specificity hurt the segments that were actually converting.

**The core tension:** The V1 copy worked for early adopters *because* it was emotionally resonant and vague. The V2 copy tried to be specific and professional, which helped clarity but hurt resonance and conversion.

This is a classic pitfall: **trying to address all segments in one page.** The V1 problem section was a visceral emotional hook; V2 diluted it by also trying to speak to experienced analysts who have a completely different relationship to the problem.

---

## Recommendations for V3

### 1. Restore the emotional problem section — cut the second paragraph
The V1 problem section was the copy's strongest emotional moment. The V2 addition ("Or maybe you know exactly what analysis you need...") tried to address duct_tape_analysts but weakened the hook for thesis_dreaders and ai_loop_prisoners. **Cut the second paragraph and return to the V1 emotional core.** Duct_tape_analysts need a different page, not a modified paragraph.

### 2. Keep V2's clarity improvements — but handle the specificity trap
The method-specific language (regression, thematic coding, override) improved clarity by 75pp. Keep it. But add a framing signal that the listed methods are examples, not the full list. Something like: "including correlation, regression, group comparisons, thematic coding — with more methods in development."

### 3. Consider swapping skeptical_methodologist for a new segment
Skeptical_methodologists have been 0% conversion across both versions with 58-75% dealbreakers. Their objections are philosophical (the product category is epistemologically wrong) and will not resolve through copy. Recommend replacing with a segment that has addressable objections — e.g., a "junior analyst" or "program evaluator" bucket.

### 4. Remove or dramatically strengthen the security section
For budget_gatekeepers, "pursuing SOC 2" is worse than silence. Two options:
- **Remove it** and accept that institutional buyers can't convert until the certification exists
- **Strengthen it** with specific language: what encryption standard, where data is hosted, explicit "no LLM training" policy, timeline for SOC 2

### 5. Expand the qualitative analysis section
"Click 'Code'" is the most interesting section to the most personas and gets the least explanation. Add specifics: how many transcripts can it handle? What does the output look like? Can you iterate on codes? This addresses the #1 unanswered question across thesis_dreader and duct_tape_analyst.

### 6. Consider segment-specific pages
The fundamental tension — emotional resonance vs professional credibility — may not be resolvable on a single page. The early-adopter segments (thesis_dreader, ai_loop_prisoner) want to feel understood. The professional segments (duct_tape_analyst, budget_gatekeeper) want to see capabilities and compliance. A single page that does both may be structurally impossible.

---

*Charts: [charts_v2.html](charts_v2.html)*
