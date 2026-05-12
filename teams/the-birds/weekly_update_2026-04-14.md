# Weekly update — Circles — 2026-04-14

## What we built last week (and why)

**Product**

- **Circle detail revamp:** New **orbit hero**, **sticky bar**, **member grid**, **activity feed**, **quick messages**, and a **chat drawer**, backed by **`useCircleLiveness`** / expanded **`useCircleDetail`** and a **`circle_events`** migration—so the detail page matches the spec (liveness, social context, and chat in one place) instead of the older layout.
- **Circle notifications + persistent navigation:** **`AppNavbar`** (persistent top bar), **`NotificationPanel`** wired to real notification data, **`useNotifications`** and DB migration for notifications, plus **`MainLayout` / Home** adjustments—so users see circle activity without hunting for a buried panel.
- **User metrics API:** **`api/metrics`** exposed (with Vercel routing and internal notes in `20260402_api-metrics.md`)—so we can report usage consistently for class analytics and iteration.
- **Build fix:** **`IconRail`** build error fixed (PR #3)—unblocked shipping the shell work above.

**Research**

- **User testing (three sessions):** Synthesis is in [`20260402/user_testing.md`](20260402/user_testing.md). Everyone reached the “aha” of creating a circle (e.g. study session), but **location input** (no map confirmation), **ambiguous copy** (“hang out” / landing framing), **chat buried** on the event page, **HEIC / time-picker** friction, and **no in-app friend sharing** broke trust and completion. **Why we ran it:** validate activation before scaling; we got a clear priority order for polish vs. positioning.

---

## What we’re building this week (and why)

Aligned with that synthesis:

1. **Google Maps for locations** — auto-complete and visible confirmation so users trust that the plan is “real” and can finalize events (replaces manual text that failed in testing).
2. **Copy and terminology** — landing headline, login line, and category labels (e.g. away from “hang out”) so the product reads as **student connection**, not something else.
3. **Layout** — raise **chat** on the circle/event page, add a clear **Home** path from profile, improve **time-picker** UX.
4. **Technical follow-ups** — **HEIC** support in the pipeline where still missing, and **in-app sharing** toward inviting specific friends (main pull from sessions).

**Why:** Testing showed the core idea engages users; removing onboarding and creation friction restores trust and gets them to **invite friends**, which participants said is the main reason they’d adopt.
