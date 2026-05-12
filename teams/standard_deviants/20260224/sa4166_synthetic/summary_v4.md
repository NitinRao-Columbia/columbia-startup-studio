# V4 Evaluation Summary

## Top-Line Metrics (n=60)

| Dimension | V4 | V3 | Delta |
|-----------|-----|-----|-------|
| Resonance (agree+) | 58% | 37% | **+21pp** |
| Intent (agree+) | 58% | 33% | **+25pp** |
| Conversion (agree+) | 8% | 0% | **+8pp** |
| Dealbreakers | 17% | 55% | **-38pp** |
| Clarity (nailed_it) | 55% | — | — |
| Price (fair) | 85% | — | — |

V4 is the strongest round so far. Resonance and intent both recovered past V2 levels while dealbreakers dropped dramatically. Conversion remains low but moved off zero for the first time since V1.

---

## Score Distributions by Bucket

| Bucket | Resonance | Intent | Conversion | Dealbreakers | V3→V4 Δ Res |
|--------|-----------|--------|------------|-------------|-------------|
| duct_tape_analyst | 100% | 100% | 0% (all neutral) | 10% | +0pp |
| ai_loop_prisoner | 100% | 100% | 0% (all neutral) | 0% | +0pp |
| ai_weary_old_school_analyst | 60% | 60% | 30% | 0% | +40pp |
| budget_gatekeeper | 60% | 60% | 20% | 20% | +60pp |
| social_science_thesis_dreader | 30% | 30% | 0% | 20% | +30pp |
| skeptical_quant_methodologist | 0% | 0% | 0% | 50% | +0pp |

**Big movers:** budget_gatekeeper (+60pp resonance, +60pp intent) and ai_weary_old_school_analyst (+40pp resonance, +30pp conversion) had dramatic recoveries from V3's waitlist-model collapse.

**Stuck at neutral:** duct_tape_analyst and ai_loop_prisoner both hit 100% resonance/intent but 0% conversion — every single persona in both buckets scored "neutral" on conversion confidence. They like the pitch but aren't ready to commit.

**Intractable:** skeptical_quant_methodologist remains at 0% across all metrics with 50% dealbreakers. This bucket wants methodological auditing (parameter capture, assumption logging, statistical decision provenance) that the product doesn't claim to do.

---

## Clarity Accuracy

| Score | Count | % |
|-------|-------|---|
| nailed_it | 33 | 55% |
| partial | 27 | 45% |
| wrong | 0 | 0% |

**By bucket:**
- duct_tape_analyst: 100% nailed_it
- ai_weary_old_school_analyst: 90% nailed_it
- ai_loop_prisoner: 80% nailed_it
- budget_gatekeeper: 60% nailed_it
- skeptical_quant_methodologist: 100% partial
- social_science_thesis_dreader: 100% partial

Zero "wrong" is excellent — nobody misunderstands the product. The partial scores cluster in two buckets that describe the tool functionally (change tracking + dependency mapping) but miss the "unified workspace" and "defensible results" framing. They understand WHAT it does but not WHY it matters.

---

## Strongest Lines (by frequency)

| Line | Count | Buckets |
|------|-------|---------|
| "When the person who built the workflow leaves, the workflow dies." | 11 | duct_tape (9), budget (2) |
| "I kept getting AI-generated code from my team that I couldn't verify..." | 10 | ai_loop (10) |
| "If the original project was built by three people in Python, R, and Excel over four years..." | 4 | cross-bucket |
| "Every edit, every formula change, every decision gets recorded with a timestamp and a reason." | 4 | skeptical (2), thesis (1), weary (1) |
| "Our grant committee wanted to see how we got from raw survey data..." | 4 | thesis (2), budget (1), weary (1) |
| "Flagged for you to review, not auto-fixed." | 3 | skeptical (2), weary (1) |

The hero opener and the AI code testimonial are dominant resonance anchors for their respective buckets. "Flagged for you to review, not auto-fixed" is the only line that lands with the skeptical/weary segments.

---

## Qualitative Themes

### 1. Testimonials feel fake (near-universal)
Every bucket flagged the testimonials as too polished, too convenient, or too perfectly calibrated to the pitch. "Operations Analyst, Regional Healthcare System" is vague enough to mean nothing. The three testimonials each hit exactly one use case, which reads as constructed.

### 2. Hero headline "Receipt" metaphor is trying too hard (ai_loop, skeptical, weary)
Across 20+ responses: the metaphor doesn't map naturally to the product. "Receipt" implies a transaction; the product creates provenance records. Several personas noted it "reads like accounting software."

### 3. CTA "Stop managing files. Start defending your results" is generic (universal)
Called out as meaningless startup copy, too punchy, or making a logical leap the product doesn't support. "Defending against whom?" asked one budget gatekeeper.

### 4. Data security is the unaddressed elephant (duct_tape, budget, weary)
"Where do my files go?" appeared in 8/10 duct_tape responses and multiple budget/weary responses. One dealbreaker (P3) was explicitly about no on-prem option. The Security & Governance section exists but doesn't answer the core question: where is data stored?

### 5. AI code understanding vs. logging (ai_loop)
All 10 ai_loop personas distinguished between "logging that code changed" and "understanding what AI-generated code does." They want the latter; the copy promises the former dressed up as the latter.

### 6. Solo researcher blind spot (thesis_dreader)
The copy is framed entirely around teams, handoffs, and institutional knowledge. 7/10 thesis personas noted they work alone. "I do not have a team. The entire value proposition is about institutional memory and handoffs, which does not apply to me."

### 7. No screenshots or demo (weary, budget)
Multiple personas across these buckets noted they can't evaluate the product without seeing what the dependency map, change log, or audit trail actually looks like.

---

## Objections Summary

| Theme | Buckets | Frequency |
|-------|---------|-----------|
| Data storage/security unclear | duct_tape, budget, weary | ~20 mentions |
| "Reads the files" too vague | duct_tape, ai_loop, weary | ~15 mentions |
| No visual proof (screenshots/demo) | weary, budget, thesis | ~10 mentions |
| Doesn't capture methodology/reasoning | skeptical, weary | ~10 mentions |
| Solo researcher not addressed | thesis | 7 mentions |
| Onboarding time concern | budget, thesis | ~6 mentions |
| Cross-language parsing skepticism | ai_loop, skeptical, weary | ~5 mentions |

---

## Dealbreaker Analysis (10/60 = 17%)

| Bucket | Count | Core Reason |
|--------|-------|-------------|
| skeptical_quant_methodologist | 5 | Product doesn't capture statistical decisions, parameters, or assumptions — it's a change log, not audit tooling |
| social_science_thesis_dreader | 2 | Time pressure (can't onboard new tool) + product designed for teams, not solo |
| budget_gatekeeper | 2 | No quantified ROI; no evidence it works for resource-constrained teams |
| duct_tape_analyst | 1 | No data residency or encryption detail |

Skeptical methodologist dealbreakers are product-level blockers, not copy-level. The product would need to actually capture statistical methodology to win this segment.

---

## Price Perception

| Rating | Count | % |
|--------|-------|---|
| Fair | 51 | 85% |
| Too expensive | 8 | 13% |
| Good deal | 1 | 2% |

**By bucket:** All buckets rated pricing "fair" except social_science_thesis_dreader (80% "too expensive"). This segment is price-sensitive graduate students — $29/month is real money on a student budget. No other bucket had pricing concerns.

---

## Test-Specific Metrics

### Transparency Trust (1-5 scale)
| Bucket | Average |
|--------|---------|
| duct_tape_analyst | 3.2 |
| ai_loop_prisoner | 3.0 |
| ai_weary_old_school_analyst | 3.0 |
| budget_gatekeeper | 3.0 |
| social_science_thesis_dreader | 2.8 |
| skeptical_quant_methodologist | 2.5 |

Midpoint across the board. Nobody trusts the transparency claims yet — they want to see it, not read about it.

### Manual Friction Relief
| Bucket | Yes | Partial | No |
|--------|-----|---------|-----|
| ai_weary_old_school_analyst | 50% | 50% | 0% |
| budget_gatekeeper | 50% | 50% | 0% |
| duct_tape_analyst | 0% | 100% | 0% |
| ai_loop_prisoner | 0% | 100% | 0% |
| social_science_thesis_dreader | 0% | 80% | 20% |
| skeptical_quant_methodologist | 0% | 70% | 30% |

---

## Recommendations for V5

1. **Fix the testimonials.** Add real names (or realistic-sounding ones with company names). Add rough edges — a caveat, a limitation acknowledged, a "it didn't do X but Y was enough." The current ones are the #1 trust-killer across all buckets.

2. **Answer "where do my files go?"** The Security & Governance section needs a direct answer: cloud-hosted with encryption at rest/in transit, SOC 2 in progress (or whatever the truth is), data residency options. This is a dealbreaker-level gap for duct_tape.

3. **Add a screenshot or interactive demo.** Multiple buckets can't evaluate the product without seeing the dependency map, change log, or audit trail. Even a static screenshot would help.

4. **Rewrite the hero headline.** The "Receipt" metaphor is universally criticized. The sub-headline ("Your data workflows lose knowledge every time someone leaves...") is stronger — consider leading with the problem statement directly.

5. **Rewrite the CTA.** "Stop managing files. Start defending your results" landed with nobody. Something concrete tied to the free trial: "See your dependency map in 5 minutes — free for 14 days."

6. **Add a solo researcher use case.** Even one sentence in the hero or a fourth testimonial from a PhD student would unlock the thesis_dreader segment. "I used it to document my methodology for my committee" or similar.

7. **Separate ai_loop from the general pitch.** The AI code verification testimonial is the only thing that resonates with this bucket, but the rest of the page doesn't follow through. Consider a dedicated section on AI code transparency.

8. **Accept that skeptical_quant_methodologist is a product gap, not a copy gap.** 50% dealbreakers with objections about parameter capture and assumption logging cannot be solved with better copy. Either build the feature or remove this segment from the target audience.

---

## V4 vs Previous Rounds

| Metric | Baseline | V1 | V2 | V3 | V4 |
|--------|----------|-----|-----|-----|-----|
| Resonance | — | — | 52% | 37% | **58%** |
| Intent | — | — | 42% | 33% | **58%** |
| Conversion | — | — | 10% | 0% | **8%** |
| Dealbreakers | — | — | 18% | 55% | **17%** |

V4 is the best round across resonance, intent, and dealbreakers. Conversion is still below V2's 10% but has moved off zero. The copy improvements (removing AI-sounding language, restoring transparent pricing, adding Security & Governance) all contributed to recovery.
