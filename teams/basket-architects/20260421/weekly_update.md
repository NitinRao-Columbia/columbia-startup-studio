# Vouch — Weekly Update · April 21, 2026

*Week of April 15–21*

---

## What shipped

This was the heaviest week of the term — a major upstream merge plus the
final feature push before the April 23 freeze.

### Friends + Tastemakers (Sprints 1 & 2)
- **Friends tab** end-to-end: Find-Friends search, Follow/Unfollow,
  Followers/Following lists, suggested users, taste-match score with
  any other user.
- **Tastemaker system** — six curated profiles seeded across food,
  nightlife, arts, fitness, live music, and hidden gems. Each has 8
  domain-specific ratings live in production so a brand-new account
  with zero friends still sees a useful feed on day one.
- Admin endpoint `/users/admin/promote-tastemaker` for ongoing
  curation, gated by `ADMIN_SECRET`.

### Tushar's polish merge (upstream → main)
- **Feed redesign** with category chips, location-aware ranking, and
  multi-image carousel cards.
- **Map** rebuilt around `LocationContext` + the new `LocationPicker`
  modal; CartoDB Positron tiles; cleaner pin popups.
- **Search**, **Profile**, and **Landing** polish.
- **Lists feature:** create/rename/delete, add/remove places,
  per-experience-detail "Save to list" picker modal.

### Production data
- **Cover-photo column widened** from VARCHAR(500) to TEXT — Google
  Places (New) photo tokens routinely exceed 500 chars and were
  failing the seeder.
- **NYC-region seed** (5 cities) — Brooklyn, Queens, Jersey City,
  Hoboken, plus the broader NYC area. ~1,500 places with full photos.
- **Top-15 US cities seed** — LA, Chicago, Miami, SF, Austin,
  Nashville, Seattle, Boston, DC, Philadelphia, Atlanta, Denver,
  San Diego, Dallas, Houston. **+5,288 places** added in a single
  background run. Map and Feed now have substance everywhere a tester
  is likely to be.
- **Database state at end of week: 6,779 experiences total** across
  6 categories, 99.3% with Google photos, 100% with map coordinates.

### Infra
- Idempotent Alembic migration for `lists` / `list_items` (some prod
  tables had been created out-of-band; the migration now skips if
  they already exist).
- `VITE_GOOGLE_CLIENT_ID` slot added to `render.yaml` for the static
  site build, fixing the silent Google-login failure on the public
  site.

## Metrics

- **Total experiences in prod:** 6,779 (up from ~1,500 pre-week)
- **Place categories:** Food & Drink 2,012 · Wellness/Fitness 1,216 ·
  Sports 991 · Arts/Culture 967 · Live Events 873 · Social Scenes 720
- **Geographic coverage:** 16 US cities (NYC metro + top-15)
- **Photo coverage:** 99.3%

## Blockers / Issues

- Two API keys got pasted in chat during the seed (Google Places +
  internal DB URL). Flagged for rotation in GCP / Render dashboard
  rotation post-freeze.
- Render's static-site env vars are baked at build time — confirmed
  that frontend changes require a manual redeploy after env-var
  edits, not just a code push.

## Next week (final week → Demo Day)

1. Finalize pitch deck + leave-behind.
2. Capture final measurement data (GA4 funnel + Amplitude cohort).
3. Live demo dry-runs — make sure cold start doesn't bite during
   the actual presentation.
4. Cert PDFs (Google Analytics, Meta Blueprint) to confirm with
   instructor where they should land.

---

**Team:** Cynthia Jin · Tushar Mittal · Gaurav Agarwal · Mandy Cheng
**Live app:** https://vouchnyc.onrender.com
**Live metrics:** https://vouch-api-5pa4.onrender.com/api/metrics
