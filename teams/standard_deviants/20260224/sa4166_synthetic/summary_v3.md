# CleanSheet V3 Synthetic Eval — Summary
**Round:** 20260224.01 | **Version:** V3 (waitlist + free-trial test) | **n=60** | **Date:** 2026-02-24

---

## Executive read

The waitlist/free-trial pivot **reduced explicit price resistance** but **did not improve conversion confidence** and introduced a new blocker for budget-led buyers: **no visible pricing**.

- Win: price perception moved to **100% fair**
- Loss: top-funnel trust dropped versus V2 in key segments
- Net: V3 underperformed V2 on resonance and intent

---

## Top-line metrics (V2 → V3)

- **Resonance agree+**: **52% → 37%** (**-15pp**)
- **Intent agree+**: **42% → 33%** (**-9pp**)
- **Conversion confidence agree+**: **0% → 0%** (no change)
- **Dealbreakers**: **50% → 55%** (**+5pp**)
- **Price too expensive**: **42% → 0%**
- **Price fair**: **58% → 100%**

Clarity stayed acceptable but slipped slightly:
- V2: 9 nailed_it / 51 partial
- V3: 7 nailed_it / 53 partial

---

## Segment-level movement

### Improved / strong
- **duct_tape_analyst**: still strong (resonance 100%, intent 90%, dealbreakers 10%)
- **ai_loop_prisoner**: strongest segment (resonance 100%, intent 90%, dealbreakers 0%)

### Regressed vs V2
- **ai_weary_old_school_analyst**: resonance **60% → 20%**, intent **60% → 20%**
- **budget_gatekeeper**: resonance **50% → 0%**, intent **50% → 0%**, dealbreakers **100%**

### Persistently dead
- **skeptical_quant_methodologist**: 0% resonance/intent, 100% dealbreakers
- **social_science_thesis_dreader**: 0% resonance/intent, 100% dealbreakers

---

## Why V3 lost ground

### 1) Waitlist introduced procurement uncertainty
Budget-led personas repeatedly said the same thing:
- "I can't budget what I can't price."
- "Waitlist + free trial sounds like beta, not readiness."

This explains the budget_gatekeeper collapse despite better surface-level price perception.

### 2) Proof requirement got sharper, not weaker
V3 improved proof language, but technical buyers still asked for concrete evidence:
- How dependency mapping works across Python/R/MATLAB/SQL
- Accuracy rates, edge cases, and parsing behavior
- Real interface artifacts (not just claims)

### 3) Conversion bottleneck remains risk, not interest
Resonance/intent are decent in two core segments, but confidence never crosses neutral because users still perceive implementation and methodological risk.

---

## Strongest lines in V3

Most-selected lines:
1. **[16x]** "Automated suggestions never auto-apply. You approve every material change before it lands."
2. **[10x]** "I stopped losing days validating AI-generated code..."
3. **[6x]** "If I am out for one week, nobody can run this workflow..."

Interpretation: trust-control language continues to outperform feature jargon and broad value statements.

---

## Decision

V3 waitlist variant is **not the winner**. Keep the proof architecture from V3, but restore transparent pricing structure (or at least a pricing range + pilot offer) from V2.

Current best candidate remains **V2** for next iteration baseline.

---

## V4 recommendation (targeted)

1. **Hybrid CTA model**
   - Keep free trial CTA
   - Add transparent pricing ranges and pilot terms on-page

2. **Budget gatekeeper recovery block**
   - Seat assumptions, implementation timeline, support scope, compliance posture

3. **Technical proof addendum**
   - One concrete dependency-map example + parser limits/known edge cases

4. **Segment split strategy**
   - Run separate V4A (ops/AI loop) and V4B (budget/quant) variants
   - Do not force one page to serve all 6 buckets equally

---

## Artifact status

Generated in this round:
- `v3_prompts.jsonl`
- `v3_outputs/`
- `results_v3.json`
- `charts_v3.html`
- `summary_v3.md`
