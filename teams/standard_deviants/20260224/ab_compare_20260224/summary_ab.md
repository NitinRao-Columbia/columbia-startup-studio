# A/B Comparison (Same Audience, Same Protocol)

**Date:** 2026-02-24  
**Audience:** `trk2121_synthetic/audience.json` (n=60, 5 buckets x 12)  
**Schema:** `eval_schema_common.json` (shared)  
**Model/protocol:** Sonnet, one-persona-per-call, identical prompt template; only copy changed.

- **Variant A:** `synthetic-user-testing/trk2121_synthetic/copy_v3.md`
- **Variant B:** `sa4166/20260224.01_product-v1/copy_v2.md`

---

## Top-line Result

Variant **A** wins clearly on this audience.

| Metric | A | B | Delta (A-B) |
|---|---:|---:|---:|
| Resonance agree+ | 18% | 5% | **+13pp** |
| Intent agree+ | 18% | 5% | **+13pp** |
| Conversion confidence agree+ | 0% | 0% | 0pp |
| Dealbreakers | 78% | 97% | **-19pp** |
| Price too expensive | 0%* | 55% | **-55pp** |
| Price fair | 97% | 45% | **+52pp** |

\*A had 2 `unknown` price-perception responses.

---

## Segment-level Results (A -> B)

| Bucket | Resonance | Intent | Conversion | Dealbreakers |
|---|---|---|---|---|
| thesis_dreader | 33% -> 0% | 33% -> 0% | 0% -> 0% | 67% -> 100% |
| duct_tape_analyst | 8% -> 0% | 8% -> 0% | 0% -> 0% | 75% -> 100% |
| ai_loop_prisoner | 50% -> 25% | 50% -> 25% | 0% -> 0% | 50% -> 83% |
| budget_gatekeeper | 0% -> 0% | 0% -> 0% | 0% -> 0% | 100% -> 100% |
| skeptical_methodologist | 0% -> 0% | 0% -> 0% | 0% -> 0% | 100% -> 100% |

Takeaway: B underperformed A in every movable bucket for this audience.

---

## Why A beat B here

1. **Audience-copy fit:** This audience is thesis/mixed-methods heavy; A speaks directly to that workflow (interviews, survey analysis, method explanation).
2. **B is handoff/legacy-stack oriented:** B’s strongest lines resonated somewhat, but it still read as less relevant for thesis_dreader and duct_tape_analyst in this audience.
3. **Price framing:** A’s low-friction/free framing prevented price from becoming the top objection; B triggered materially more "too expensive" calls.

---

## What this does *not* mean

- It does **not** mean A is globally better than B in all markets.
- It means A is better for **this exact audience** under controlled protocol.
- Both copies still failed conversion confidence (0% agree+), so neither is launch-ready without further risk-reduction proof.

---

## Recommended next step

Run a **crossed audience test** to separate copy strength from segment fit:

1. Test A and B on the **sa4166 audience** (same protocol)  
2. Compare with this run (A/B on trk audience)  
3. Build a two-track strategy:
   - Track 1: thesis/mixed-methods buyer page (A lineage)
   - Track 2: legacy-workflow/handoff buyer page (B lineage)

---

## Generated artifacts

- `results_A.json`
- `results_B.json`
- `charts_A.html`
- `charts_B.html`
- `summary_ab.md`
