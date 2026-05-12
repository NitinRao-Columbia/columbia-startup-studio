# Vouch — Weekly Update · April 28, 2026

*Week of April 22–28*

---

## What shipped

This is the post-Feature-Freeze week — focus shifted from product to
delivery: deck, leave-behind, measurement infrastructure, and the
final pre-Demo-Day repo audit.

### Demo Day artifacts
- **Pitch Deck** — `20260512/Vouch_Pitch_Deck.pptx`. Problem →
  solution → validation → iteration history → traction → future
  vision. Ready for the May 12 demo.
- **Leave-Behind** — `20260512/Vouch_Leave_Behind.pptx`. Standalone
  handout for judges, alums, and anyone we ran out of time pitching to.

### Live measurement endpoints
- `GET /api/metrics` (composite: signups, active users, page views,
  ratings) is live in production and was wired into the deck's
  traction slide.
- `GET /api/user-count` (legacy single-field) preserved for any
  existing embeds.
- `20260512/metrics_snapshot.py` — stdlib-only script that hits both
  endpoints and prints a Markdown table ready to paste into a slide.
  Run the morning of Demo Day for the freshest numbers.

### Repo hygiene
- `20260305/` folder rename and `mvp_doc.md` filename fix to match
  the official repo checklist.
- `CHECKLIST_INDEX.md` added at the team-folder root, mapping every
  checklist line item to the artifact that satisfies it (since some
  deliverables — Experiments 3/4, AARRR analytics, pricing test,
  onboarding findings — live as sections inside the Growth Strategy
  PDF and User Testing Report rather than as separately-named files).
- **Product repo got `CLAUDE.md` and `README.md`** at the root — the
  AI-engineering primer (stack, conventions, gotchas) and the
  human-facing project page respectively.

### Two PRs open
- `kenxle/columbia-startup-studio` ← `Acinonyx44:fix/repo-checklist-paths`
- `Acinonyx44/vouch_startup_studio` ← `docs/add-claude-and-readme`

## Live metrics (snapshot)

Pulled from `/api/metrics` on the morning of April 28:

| Metric | Value |
|---|--:|
| Total signups | 68 |
| Active users | 19 |
| Activation rate | 27.9% |
| Total ratings logged | 55 |
| Ratings per active user | 2.89 |
| Total page views | 102 |

Ratings/active-user is sitting in the middle of the Week 2 target band
(3.0) we set in the Growth Strategy doc, even with a non-aggressive
outreach push so far.

## Blockers / Issues

- Individual certifications (Google Analytics for Beginners, Meta
  Blueprint Fundamentals) — need to confirm with instructor where
  these PDFs should be submitted (course repo `certifications/`
  folder vs. Canvas).
- Two yellow-flag items in the final audit: explicit Experiment 3 /
  Experiment 4 docs (currently indexed via the Growth Strategy PDF,
  not titled as such), and a captured GA4/Amplitude funnel export
  to sit alongside the live metrics endpoint.

## Next two weeks → Demo Day (May 12)

1. **April 30:** capture final measurement data (GA4 funnel
   screenshot + Amplitude weekly cohort) into `20260430/`.
2. **May 1–7:** dry-run the deck twice with a peer team. Time the
   live-demo segment cold (~60s buffer for Render free-tier wake-up).
3. **May 8–11:** push for one more dense seed cohort — 10+ mutually
   following testers in a single friend group — so the social feed
   visibly does its job during the live demo.
4. **May 12:** Demo Day.

---

**Team:** Cynthia Jin · Tushar Mittal · Gaurav Agarwal · Mandy Cheng
**Live app:** https://vouchnyc.onrender.com
**Live metrics:** https://vouch-api-5pa4.onrender.com/api/metrics
