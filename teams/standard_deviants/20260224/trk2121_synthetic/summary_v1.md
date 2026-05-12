# V1 Evaluation Summary

**Test:** Landing Page Copy V1
**Date:** 2026-02-20
**Personas:** 60 (5 buckets x 12)

---

## Top-Line Metrics

| Metric | Value | Target |
|--------|-------|--------|
| Resonance (agree+) | **38%** | — |
| Intent (agree+) | **28%** | — |
| Conversion Confidence (agree+) | **10%** | >50% |
| Dealbreakers | **32%** (19/60) | — |
| Price: Too Expensive | **0%** | — |

**Verdict:** V1 is well below the 50% conversion target. The copy resonates with early adopters (thesis_dreader, ai_loop_prisoner) but fails to convert the professional segments that represent the majority of the addressable market.

---

## Score Distributions

### Overall (n=60)

| Dimension | SD | D | N | A | SA | Agree+% |
|-----------|-----|-----|-----|-----|-----|---------|
| Resonance | 3 | 16 | 18 | 18 | 5 | 38% |
| Intent | 4 | 15 | 24 | 14 | 3 | 28% |
| Conversion | 10 | 23 | 21 | 6 | 0 | 10% |

### Per Bucket

| Bucket | Res | Int | Conv | DB% |
|--------|-----|-----|------|-----|
| thesis_dreader | 67% | 58% | 33% | 0% |
| ai_loop_prisoner | 83% | 50% | 17% | 0% |
| duct_tape_analyst | 25% | 25% | 0% | 33% |
| budget_gatekeeper | 17% | 8% | 0% | 50% |
| skeptical_methodologist | 0% | 0% | 0% | 75% |

The funnel narrows sharply: 38% resonance drops to 28% intent drops to 10% conversion. The biggest gap is intent-to-conversion — people relate to the problem and might try it, but very few are confident they'd actually sign up.

---

## Clarity Accuracy

| Score | Count | % |
|-------|-------|---|
| Wrong | 5 | 8% |
| Partial | 53 | 88% |
| Nailed It | 2 | 3% |

**Analysis:** Almost no one articulated the core claim (auto-selects the right statistical method + explains results in plain language). Most personas understood the general "upload data, get answers" pitch but missed the auto-selection differentiator. The 5 "wrong" scores came from personas who described their emotional reaction rather than the product (e.g., "reads like it was written about my last three months").

**Implication:** The copy's unique value prop — that the platform *chooses the right test for you* — isn't landing clearly enough. It's mentioned in the Solution section but gets lost in the broader pitch.

---

## Top Strongest Lines (by frequency)

1. **"Every result shows the method used, the parameters, and what it means in plain language. Auditable. Exportable."** — 34 citations across all 5 buckets. This is the copy's strongest moment by a wide margin.
2. **"You get an error. You paste the error back in..."** — 4 citations (ai_loop_prisoner, thesis_dreader). The ChatGPT loop description resonates deeply with the two early-adopter segments.
3. **"Upload your interviews, surveys, or spreadsheets..."** — 3 citations (budget_gatekeeper, duct_tape_analyst, thesis_dreader).
4. **"If you're spending $10-20/month on ChatGPT to debug R code, this replaces that."** — 3 citations (ai_loop_prisoner, duct_tape_analyst).

**Takeaway:** Transparency and auditability are what people want to hear about. The "auditable/exportable" line works because it addresses the trust gap directly. Double down on this.

---

## Most Common Objections

### 1. "What can it actually do?" (capability ceiling)
Across thesis_dreader and ai_loop_prisoner, the most common concern is whether the tool supports advanced methods: regression, HLM, SEM, IRT, mixed-methods, repeated measures. The copy showcases chi-square, t-test, and ANOVA — intro-level tests — which signals a low ceiling.

### 2. "Where's the security/compliance info?" (enterprise blockers)
Budget_gatekeeper personas universally flagged the absence of: data security documentation, SOC 2, FERPA, HIPAA, data residency, BAA availability. This isn't a copy tone issue — the information simply doesn't exist on the page.

### 3. "Auto-selecting tests is the problem, not the solution" (methodological trust)
Skeptical_methodologists see "you don't need to know which test" as a red flag. They want to see the decision logic, not have it hidden. The copy frames opacity as convenience; they experience it as a threat to rigor.

### 4. "This adds a sixth tool, not replaces five" (integration gap)
Duct_tape_analysts need to know about integrations, export formats, and whether this replaces or supplements their existing stack. The copy says "one place" but doesn't prove it.

---

## Dealbreaker Analysis

**19 dealbreakers (32%)** — distributed as:

| Bucket | DB Count | DB Rate | Primary Reason |
|--------|----------|---------|----------------|
| skeptical_methodologist | 9 | 75% | Auto-selection is epistemologically unacceptable |
| budget_gatekeeper | 6 | 50% | No compliance/security documentation |
| duct_tape_analyst | 4 | 33% | No integration/migration story |
| thesis_dreader | 0 | 0% | — |
| ai_loop_prisoner | 0 | 0% | — |

The early-adopter segments (thesis_dreader, ai_loop_prisoner) have zero dealbreakers. The professional segments have hard blockers that copy alone may not resolve — some require product features (compliance docs, security architecture) that don't exist yet.

---

## Price Perception

| Rating | Count | % |
|--------|-------|---|
| Good Deal | 41 | 68% |
| Fair | 19 | 32% |
| Too Expensive | 0 | 0% |

**Price is not a barrier.** Not a single persona found the pricing too expensive. Even budget_gatekeeper personas (9/12 good_deal) think the price is reasonable — their objections are about capability and compliance, not cost. The $10/month ChatGPT anchor works.

---

## Key Qualitative Themes

### What's working
1. **Problem section is exceptional.** The ChatGPT error loop and tool fragmentation descriptions are viscerally accurate for the target audience. Multiple personas called it "uncomfortably accurate."
2. **Transparency promise resonates universally.** "Auditable. Exportable." is the most cited line by a factor of 10x.
3. **Price is right.** The free tier removes all friction for individual users. The ChatGPT spend anchor is clever and effective.
4. **The "Who It's For" list helps** thesis_dreaders and ai_loop_prisoners see themselves.

### What's not working
1. **Copy pitches to the wrong persona for 3/5 segments.** The framing ("You're not a data person") alienates duct_tape_analysts who ARE data people, budget_gatekeepers who don't need emotional validation, and skeptical_methodologists who find the framing condescending.
2. **Solution section showcases intro-level stats.** Chi-square, t-test, ANOVA signal a low capability ceiling. People with real problems (regression, HLM, SEM) assume the tool can't handle them.
3. **Zero compliance/security content.** This is a hard blocker for institutional buyers.
4. **The auto-selection pitch backfires with experts.** "You don't need to know which" is comfort for novices and alarm for experienced users.
5. **No qualitative analysis specifics.** Many personas have interview data and the copy mentions transcripts but never explains what the platform does with them.

---

## Recommendations for V2

1. **Reframe the hero away from "you're not a data person."** Try: "You have the data. You need the answers." — same energy, doesn't alienate professionals.
2. **Add a capability section that shows advanced methods.** Mention regression, mixed-methods, qualitative coding — even briefly. Signal that the ceiling is higher than intro stats.
3. **Add a trust/security section.** Even placeholder language about data handling, encryption, and audit trails addresses the budget_gatekeeper hard blocker.
4. **Reframe auto-selection as "transparent automation."** Instead of "you don't need to know which," try "the platform selects the method and shows you exactly why." This flips the value prop from hiding complexity to explaining it.
5. **Add qualitative analysis specifics.** What does the platform do with interview transcripts? Thematic coding? Sentiment analysis? This is a major gap.
6. **Consider a "Who It's For" rewrite** that acknowledges experienced analysts, not just people who are "lost."

---

*Charts: [charts_v1.html](charts_v1.html)*
