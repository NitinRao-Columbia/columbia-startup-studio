# 20260224 — Landing Page + Synthetic Testing

## Live URL

**[https://sift-landing-page.lovable.app/](https://sift-landing-page.lovable.app/)**

---

## What's in here

| File | Description |
|------|-------------|
| `brand_position.md` | Final brand position document, updated with synthetic testing feedback |
| `landing_page_copy.md` | Written landing page copy organized by section, with notes on what changed and why |
| `synthetic_testing/` | Two rounds of synthetic user testing (V1 → V2) with copy, results, and changelogs |

---

## Sift — What it is

Sift is an event discovery app for NYC that filters thousands of activities down to 3–5 personalized recommendations based on your interests, schedule, location, and budget. It replaces the six-app scroll with a single shortlist.

---

## Synthetic Testing Summary

We ran synthetic user testing with 60 AI-generated personas across 5 behavioral archetypes derived from 10 real user interviews.

**Audience buckets:**

| Bucket | Who they are |
|--------|-------------|
| Overwhelmed Planner | Decision fatigue, uses 3-6 platforms, "planning friend" |
| Routine Breaker | Goes out often but same places, wants novelty |
| Quiet Explorer | Intentional, skeptical of hype, quality-over-quantity |
| Culture Seeker | Wants ephemeral cultural events, frustrated by info asymmetry |
| Budget-Conscious Socializer | Cost-aware, wants quality free/cheap activities |

**Results across rounds:**

| Metric | Baseline | V1 | V2 |
|--------|----------|-----|-----|
| Resonance (agree+) | 15% | 70% | 80% |
| Intent (agree+) | 15% | 57% | 62% |
| Conversion (agree+) | 7% | 57% | 57% |
| Dealbreaker rate | 43% | 23% | 13% |
| Clarity: nailed it | 0% | 65% | 98% |

**Key changes between rounds:**

- **V1 → V2:** Added two example recommendation cards (foraging walk + comedy lottery) to prove catalog depth. Replaced black-box "gets sharper" claim with visible match reasoning and transparent personalization language. Result: culture seeker conversion +17pp, quiet explorer dealbreakers -25pp, clarity +33pp.

- **V2 → Deployed version:** Added "Is Sift free?" and privacy FAQ entries to address remaining dealbreakers. Made budget filter language more prominent. Added "Spring 2026" launch timeline to CTA.

---

## Folder Structure

```
20260224/
├── README.md                    ← this file
├── brand_position.md
├── landing_page_copy.md
└── synthetic_testing/
    ├── v1_copy.md
    ├── v1_results.md
    ├── v2_copy.md
    └── v2_results.md
```
