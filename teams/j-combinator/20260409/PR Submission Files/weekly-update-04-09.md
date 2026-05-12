# Sift — Weekly Update
**Week of April 9, 2026**

---

## What We Built

### Core App
- **Full React Native app** built with Expo (SDK 52), using Expo Router for file-based navigation across auth, onboarding, discovery, planning, and profile flows
- **Guest mode** — users can browse events without signing in; saves persist after sign-in
- **4-step onboarding wizard** — collects category preferences, date range, travel distance, and borough to personalize recommendations
- **Recommendation engine** — scores events by category match, location, budget, schedule, and recency to surface the most relevant results
- **Event detail screen** — full event info with ticket links, calendar export (Google + Apple), and sharing
- **Plan tab** — shortlist saved events, confirm a weekend plan, and export to calendar
- **Save & organize** — save events to named custom lists (e.g. "Date ideas", "Free stuff", "With friends")
- **Calendar view** — track events you've marked as going

### Backend & Data Pipeline
- **14-source event ingestion pipeline** running as a Vercel cron job daily at 7 AM UTC, pulling from: Ticketmaster, Eventbrite, NYC Parks, Museums (MoMA, Whitney, New Museum, Brooklyn Museum), Pop-ups, NYCForFree, CozyCreatives, NYC Tourism, Meetup, Yelp, Dice.fm, Resident Advisor, NYC.gov, and The Skint
- Events go through a full processing pipeline: normalize → geocode → reclassify → deduplicate → cleanup → upsert to Supabase
- **Supabase** for auth and PostgreSQL database
- **Fallback event data** hardcoded in `src/data/events.ts` if Supabase is unreachable

### Analytics
- **Amplitude** integrated with full funnel tracking: `onboarding_started` → `onboarding_step_1/2/3/4_complete` → `onboarding_complete` → `sign_up_started` → `sign_up_completed` → `first_event_viewed`
- **Firebase Analytics** added via Measurement Protocol REST API (no native SDK — avoids ESM/CJS build failure with Node 20 + Expo SDK 52); events fan out to Firebase alongside Amplitude
- Analytics events also written to Supabase `analytics` table for server-side querying

### API Endpoints
- `GET /api/user-count` → `{ "user_count": N }` — live at [https://sift-mobile-two.vercel.app/api/user-count](https://sift-mobile-two.vercel.app/api/user-count)
- `GET /api/metrics` → `{ "signups": N, "active_users": N, "waitlist": N, "page_views": 0 }` — live at [https://sift-mobile-two.vercel.app/api/metrics](https://sift-mobile-two.vercel.app/api/metrics)

### User Count
For the latest registered user count, check here: [https://sift-mobile-two.vercel.app/api/user-count](https://sift-mobile-two.vercel.app/api/user-count)

We currently have **69 waitlist signups** collected prior to launch.

---

## What We're Currently Working On

- **Login authentication bugs** — investigating and fixing issues with the sign-in/sign-up flow, including post-registration guidance (users not knowing to sign back in after confirming email)
- **Android UI margin fix** — the top of the screen is getting cut off on Android due to missing safe area margin; adding proper `SafeAreaView` handling for Android-specific insets
- **Firebase Analytics improvements** — expanding event coverage and verifying events are flowing correctly into the GA4 Realtime and DebugView dashboards
- **User testing follow-up** — implementing high-priority fixes surfaced from Round 2 usability sessions (see synthesis doc)

---

## What We're Planning to Build Next

Based on our latest codebase and user testing feedback, the following are our highest-priority next items:

- **Improve sign-up discoverability** — make the sign-up entry point equally prominent to sign-in on the landing screen
- **Post-signup clarity** — add explicit guidance after registration (confirmation email notice + prompt to sign back in)
- **Gesture tutorial** — lightweight first-use overlay showing left-swipe to discard and right-swipe to save events
- **Expand event display** — show more than 3 events at a time; users want to browse, not just pick from a narrow set
- **Expiry filtering** — ensure expired events are never surfaced in recommendations
- **Richer event descriptions** — surface more detail on event cards and detail screens
- **Onboarding reduction** — reduce friction in the onboarding flow; consider launching in guest mode by default so users hit the discover page immediately
- **Save-and-resurface mechanism** — notify users when a saved event is happening soon nearby ("you saved this — it's this weekend")

---

## Blockers

- **Android safe area** — top content is being clipped on Android devices due to missing status bar margin; actively being fixed
- **Firebase DebugView** — events are confirmed flowing into GA4 Realtime, but DebugView shows 0 devices since the Measurement Protocol REST API approach does not enable debug mode by default; need to find a workaround or use Realtime for verification
- **Session persistence bug (Android)** — on Android, logging in and then closing/reopening the app sends users back to the login screen instead of keeping them signed in. Root cause identified: the onboarding and guest flags were stored as in-memory variables that reset on every app restart, so even though Supabase correctly restores the session, the routing logic fails. Fix in progress.

---

## Metrics

| Metric | Value |
|---|---|
| Registered users | [Live count](https://sift-mobile-two.vercel.app/api/user-count) |
| Waitlist signups | 69 |
| Active users | See [/api/metrics](https://sift-mobile-two.vercel.app/api/metrics) |
| Event ingestion sources | 14 |
| Cron jobs running | 5 (daily at 7 AM UTC) |
| User testing sessions completed | 3 (Round 2) |
