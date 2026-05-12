# Vouch — Weekly Update · April 14, 2026

*Week of April 8–14*

---

## What shipped

- **User Testing Report finalized** (`20260409/Vouch_User_Testing_Report.pdf`).
  Captured findings from the small-cohort onboarding testing pass —
  what new users hit on first run, where the rating loop felt heavy,
  what the taste profile actually communicated.
- **Onboarding flow tightened** based on the testing-round feedback.
  Reduced field count on the survey, added category multi-select
  defaults so the feed isn't empty after step 1.
- **Map UI iteration round 1.** Pin density was overwhelming with the
  full place set; introduced category-based color coding and a
  zoom-aware pin density to prep for the larger seed.
- **First NYC venue seed.** ~1,500 places imported via Google Places
  for the core five-borough area, with photo URLs + categories. This
  is what the Map and Feed render against by default.
- **Search tab fully functional** — backend `/experiences/search` plus
  client-side instant filtering, category dropdown, and external
  Places fallback when a query has no DB hits.

## Metrics

- 23 places-per-search median across testing-round queries.
- Onboarding survey completion: ~85% on testers (up from ~60% pre-tightening).
- Frontend bundle size still under 350 KB gzipped after the new map
  components — no perf regression.

## Blockers / Issues

- Cold-start problem for new users with empty graphs — the For You
  feed feels random until friends + tastemakers are in place. Plan
  going into next week: ship the tastemaker seed + Friends tab.
- Render free tier still cold-starting the API on first load —
  user-facing 30–60s lag on first request after idle. Tabled the
  upgrade to a paid tier until closer to Demo Day.

## Next week

1. **Sprint 1 — Friends:** Tushar's branch with Find-Friends,
   Followers/Following lists, and the relationship graph.
2. **Sprint 2 — Tastemakers:** seeded curator profiles, follow
   bootstrapping, taste-match scoring.
3. Continue map polish (pin clustering at city zoom level).
4. Begin draft of Growth Strategy Part 1.

---

**Team:** Cynthia Jin · Tushar Mittal · Gaurav Agarwal · Mandy Cheng
**Live app:** https://vouchnyc.onrender.com
