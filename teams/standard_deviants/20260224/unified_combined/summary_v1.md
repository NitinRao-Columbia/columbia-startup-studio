# Unified Combined V1 — Evaluation Summary

**Date:** 2026-02-25
**Copy version:** V1
**Personas:** 72 (6 buckets x 12)
**Model:** Sonnet (eval), Haiku (clarity)

---

## Top-Line Metrics

| Metric | Overall | Best Bucket | Worst Bucket |
|--------|---------|-------------|--------------|
| **Resonance** (agree+) | **76%** | ai_loop_prisoner (100%) | ai_weary_old_school (0%) |
| **Intent** (agree+) | **71%** | ai_loop_prisoner (100%) / thesis_dreader (100%) | ai_weary_old_school (0%) |
| **Conversion** (agree+) | **11%** | ai_loop_prisoner (33%) | ai_weary_old_school / duct_tape / power_qual (0%) |
| **Dealbreakers** | **18%** (13/72) | 4 buckets at 0% | ai_weary_old_school (92%) |
| **Clarity** (nailed_it) | **93%** | Multiple at 100% | ai_weary_old_school (58%) |
| **Price** (good_deal) | **85%** | 4 buckets at 100% | ai_weary_old_school (25%) |

---

## Per-Bucket Breakdown

### 1. ai_loop_prisoner (n=12) — STRONGEST PERFORMER
- **Resonance:** 100% agree+ (1 strongly_agree)
- **Intent:** 100% agree+
- **Conversion:** 33% agree+ (4/12)
- **Dealbreakers:** 0%
- **Price:** 100% good_deal
- **Signal:** This segment sees themselves in the copy and the Receipt solves their specific credibility problem. The AI loop description ("paste, get output, paste somewhere else, can't reproduce it") is hitting emotional bullseyes.

### 2. thesis_dreader (n=12) — STRONG RESONANCE
- **Resonance:** 100% agree+
- **Intent:** 100% agree+
- **Conversion:** 17% agree+ (2/12)
- **Dealbreakers:** 0%
- **Price:** 100% good_deal
- **Signal:** The "400-row dataset and a methods chapter that's still a placeholder" line is their most-cited moment. Gap between intent (100%) and conversion (17%) = they believe the product could help but don't trust it yet.

### 3. fast_moving_product_team (n=12) — HIGH INTENT
- **Resonance:** 92% agree+
- **Intent:** 92% agree+
- **Conversion:** 17% agree+ (2/12)
- **Dealbreakers:** 0%
- **Price:** 100% good_deal
- **Signal:** The "decision to make by Thursday" framing lands. But the copy leans academic and they feel like an afterthought. They need to see messy-data handling, not statistical rigor.

### 4. duct_tape_analyst (n=12) — INTERESTED BUT INERT
- **Resonance:** 83% agree+
- **Intent:** 58% agree+
- **Conversion:** 0% agree+
- **Dealbreakers:** 8% (1/12 — Jason Garcia, public sector data portability)
- **Price:** 83% good_deal
- **Signal:** The 15-years-and-overhead line resonates. But their problem is often upstream of upload (data trapped in legacy systems, ODBC connections, VBA macros). The copy assumes portable data.

### 5. power_qual_practitioner (n=12) — RIGHT PAIN, MISSING DEPTH
- **Resonance:** 83% agree+
- **Intent:** 75% agree+
- **Conversion:** 0% agree+
- **Dealbreakers:** 8% (1/12 — Patrick Thornton, needs team governance not individual tools)
- **Price:** 100% good_deal
- **Signal:** IRR buried in pricing table is a repeated frustration. They need to know: Cohen's kappa or percentage agreement? Can they import codebooks? Is this actually team-grade or individual-with-sharing?

### 6. ai_weary_old_school_analyst (n=12) — NEAR-TOTAL REJECTION
- **Resonance:** 0% agree+ (all neutral or disagree)
- **Intent:** 0% agree+
- **Conversion:** 0% agree+
- **Dealbreakers:** 92% (11/12)
- **Price:** 25% good_deal, 75% fair
- **Signal:** This is a product-level blocker, not a copy problem. "Assumptions checked" without specifying WHICH assumptions is a red flag to this segment. They need: method-selection logic visibility, assumption test details, override capability. The copy's value prop ("platform selects the method") is precisely what they distrust.

---

## Strongest Lines by Citation Count

| Count | Line |
|-------|------|
| **42x** | "Every result shows the method used, the parameters, the assumptions checked, and what it means in plain language." |
| 4x | "You didn't plan to become a research operation..." |
| 3x | "Maybe you've been doing this for fifteen years..." |
| 2x | "Maybe you're a grad student with a 400-row dataset..." |
| 2x | "I've tried using AI to analyze interview data and it works until it doesn't..." |
| 2x | "Sometimes you do it alone. Sometimes with a team..." |
| 2x | Receipt description paragraph |

The transparency line dominates at 58% of all citations — universal appeal across segments.

---

## What Feels Off (Top Themes)

| Count | Theme |
|-------|-------|
| **36x** | Testimonials feel staged/constructed — "nobody talks like that" |
| **31x** | "Receipt" branding feels try-hard or over-clever |
| **11x** | "The gap has been there long enough" CTA header is try-hard |
| 6x | "Assumptions checked" is vague/unearned |

**Testimonial problem is universal.** Every single bucket flagged the testimonials as constructed. The doctoral candidate quote is the worst offender ("that conversation went differently" reads as copywriter voice, not student voice). This needs to be either rewritten to sound messier/more human, or replaced with actual user quotes when available.

---

## Key Unanswered Questions (by frequency)

| Count | Question |
|-------|----------|
| **37x** | What specific methods does the platform actually support? |
| 17x | What does "assumptions checked" mean operationally? |
| 17x | Can I import existing codebooks/data/workflows? |
| 17x | Does it handle messy/unclean real-world data? |
| 15x | What does the Receipt actually look like? |
| 14x | Will my committee/advisor/IRB accept this? |
| 12x | What does inter-rater reliability actually calculate? |
| 10x | Can I override the method the platform selects? |

---

## Dealbreaker Analysis

**13 dealbreakers total (18%)**

| Bucket | Count | Root Cause |
|--------|-------|------------|
| ai_weary_old_school_analyst | 11/12 | Unverifiable method-selection claims, no assumption-test specifics, epistemological objection to outsourcing method choice |
| duct_tape_analyst | 1/12 | Data portability — legacy systems can't export to upload |
| power_qual_practitioner | 1/12 | Team governance features missing — product is individual-oriented |

**ai_weary_old_school_analyst dealbreakers are NOT solvable by copy.** These are product requirements: expose method-selection logic, specify assumption tests, allow method override. This mirrors the skeptical_methodologist pattern from trk2121.

---

## Price Perception

**Zero "too_expensive" across all 72 personas.** Price is not a barrier.

- 85% good_deal, 15% fair
- Multiple personas noted pricing feels suspiciously low ("either early and untested, or depth isn't there")
- Free tier structure (3 projects, not 14-day timer) universally praised
- Several noted the low price actually reduces credibility for serious/enterprise work

---

## Recommendations for V2

### Copy changes:
1. **Rewrite testimonials** — Make them sound human. Add specific institutional context, messier language, less perfectly-aligned-to-pain-point phrasing.
2. **Show the Receipt** — A screenshot or concrete example. "What does it actually look like" was asked 15x.
3. **Flesh out IRR feature** — Move from pricing table checkbox to Solution section description. Specify: Cohen's kappa? Krippendorff's alpha? How does collaborative coding work?
4. **Add method override language** — "You stay in control of what happens next" is too vague. Make it concrete: "You can override any method choice and the platform documents why."
5. **Replace "the gap has been there long enough"** — Multiple personas flagged this as try-hard.
6. **Lead with messy data** — "Upload what you actually have" should be more prominent and specific. Mention Zoom transcripts, Otter.ai exports, messy Excel files.

### Segment strategy:
- **Drop ai_weary_old_school_analyst** — 92% dealbreakers, product-level blockers. Same pattern as skeptical_methodologist in trk2121. Cannot be fixed with copy.
- **Focus V2 on ai_loop_prisoner, thesis_dreader, fast_moving_product_team** — Highest intent, zero dealbreakers, best conversion potential.
- **Power_qual needs feature specificity** — The segment is interested but conversion requires explaining IRR, codebook management, and team workflows in detail.

### Key insight:
The intent-to-conversion gap (71% → 11%) is the story of V1. People believe the product could help them but don't trust the copy enough to commit. The fix isn't more persuasion — it's more specificity. Show the Receipt, show the method explanation, show the output. Replace assertions ("assumptions checked") with demonstrations.

---

*Next step: User decides whether to iterate (V2) or stop here.*
