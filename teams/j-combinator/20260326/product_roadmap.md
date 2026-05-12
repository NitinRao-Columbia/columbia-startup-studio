# Product Roadmap — J Combinator

**Product:** Sift
**Date:** March 26, 2026
**Demo Day:** May 12, 2026

---

## Where We Are Now

**What's working:**
- Core discovery flow lands: 3 questions → 3–5 recommendations. Users get the concept immediately (98% clarity in synthetic testing).
- Landing page converts well — 70% resonance, 57% conversion on waitlist CTA across 60 synthetic personas.
- Onboarding flow, "Going" button, bookmarks/lists, share button, and profile screen are functional in the MVP.
- The match reasoning on cards ("Matched because…") is consistently cited as the strongest UX moment.

**What's not working / biggest gap:**
- Event data is entirely hardcoded. No real API integrations — the app can't show what's actually happening in NYC this week.
- Recommendation logic is cosmetic. There's no real ranking, scoring, or personalization — every user sees the same cards regardless of preferences.
- No "decision funnel" after browsing. Users save events but there's no flow for narrowing saved events down to a final plan.
- The profile calendar is a shell — events don't have real dates tied to them.
- Multi-day events save to the calendar as the first available date only. Users have no way to pick which date they're attending, and recurring events don't show their full schedule.

**What we learned from peer review:**
- The "why it matched" reasoning on cards is the strongest trust signal — people want more of it, not less.
- Several reviewers wanted ticket/booking links — seeing a great event but having no way to act on it is frustrating.
- Questions about data sourcing came up repeatedly. Need to address this concretely, not just with "public APIs."
- Sharing should be more seamless. We deliberately excluded social features (friend feeds, group planning) based on interview data — users don't want another social app. But sharing a specific event should be frictionless: if you send a Sift link to a friend who also uses Sift, the event should auto-save to their app. The share flow should feel like forwarding a text, not "inviting someone to a platform."
- Some reviewers asked about search/browse outside the 3-card flow. Currently the only path to events is through the recommendation engine. Worth exploring whether a secondary browse mode adds value or undercuts the core "fewer, better" promise.

**One improvement we shipped this week:**
- Added auth gate with guest/sign-in flow, full onboarding sequence (interests, neighborhood, budget, availability), and profile screen with calendar + saved lists. Live at https://sift-app-mvp.vercel.app/

---

## What We Need to Learn About Our Product

1. **Does the app feel useful with real data?** Hardcoded events feel like a concept demo. The moment real, time-sensitive events appear, does the product click differently? Does it feel worth opening again next week?

2. **What makes someone come back?** Is it a weekly habit (open Thursday, plan weekend)? Is it notification-driven (alert when something matching your taste is ending soon)? Or is it purely transactional (open when bored, close when plan is made)? We need to find the retention hook.

3. **Is 3–5 the right number?** Our whole positioning is "fewer, better." But after we add real data and real filtering, does 3 feel too few and 7 feel like a feed? Where's the sweet spot between "curated" and "enough to choose from"?

4. **Does sharing need to be a product loop?** Our interviews told us people don't want another social app — they just DM friends. But if someone shares a Sift event link and the recipient also has Sift, should it auto-save to their saved events? Does that lightweight "shared → saved" loop drive adoption without becoming a social feature people resent? Need to test whether this feels helpful or invasive.

5. **Should there be a way to search/browse outside the recommendation flow?** The entire product is built around "3 questions → shortlist." But what if a user hears about a specific event and wants to check if it's on Sift? Or wants to browse everything in a category without the filter funnel? A search bar could add utility — but it could also undermine the "we do the filtering for you" positioning. Need to figure out whether search is a complement or a contradiction.

---

## What We Need to Build

| Week | Dates | Build Focus | Who |
|------|-------|-------------|-----|
| **9** | Mar 24–28 | **Real event data pipeline (Phase 1).** Set up Eventbrite API integration (OAuth, event search by NYC location + category + date). Note: Eventbrite deprecated the public `/events/search/` endpoint in 2020 — use `/organizations/:id/events/` and `/venues/:id/events/` to pull from known NYC organizers/venues. Also set up Ticketmaster Discovery API (concerts, shows — no auth issues, straightforward). Store events in Supabase with a unified schema: title, category, `start_date`, `end_date`, `available_dates[]` (for multi-day events or recurring schedules), location, price, source, URL, lat/lng. Multi-day and recurring events must store all valid dates, not just the first. | [backend dev] |
| **10** | Mar 31 – Apr 4 | **Real event data pipeline (Phase 2).** Add lightweight scrapers for sources without APIs: NYC Parks events page, gallery/museum calendars (MoMA, Whitney, New Museum), and 2–3 pop-up/sample sale aggregators. Use Playwright for JS-rendered pages. Add a nightly cron job to refresh event data. Goal: 200+ real events in the database by end of week. Also add a "ticket link" field to the event schema — if the source has a buy/RSVP link, surface it on the card as a "Get tickets →" button. | [backend dev] |
| **11** | Apr 7–11 | **Recommendation engine v1.** Replace hardcoded card display with real filtering: match events to user profile (interests, neighborhood + travel range, budget, available days/times). Add a basic scoring layer: events that match more dimensions rank higher. Add "ending soon" boost for events within 7 days of closing. Surface match reasoning dynamically ("Matched because: you picked comedy + you're free Saturday + it's under $20 + 15 min from you"). | [full stack] |
| **12** | Apr 14–18 | **Decision funnel + sharing + UX polish.** Build "Plan your weekend" flow: user reviews saved/going events → app shows them on a mini timeline (Saturday afternoon: foraging walk, Saturday night: comedy show) → user confirms or swaps. **Fix multi-day event calendar save:** Currently, saving a multi-day event defaults to the first available date. Instead: (1) event cards for multi-day/recurring events should show "Available: Mar 14–28" or "Every Sat through Apr 12" so the user sees the full date range; (2) when a user taps "Going" or saves to a list, show a date picker bottom sheet with only the event's available dates selectable — user picks which date(s) they plan to attend; (3) the saved entry in `goingEvents`/`savedEvents` stores the user-selected date, not just the event's start date; (4) the profile calendar renders the event on the user's chosen date(s), not the event's first date. **Share deep-links:** Each event gets a shareable URL (`sift.app/event/:id`). When a non-Sift user opens the link, they see the event card + "Get Sift" CTA. When an existing Sift user opens the link, the event auto-saves to a "Shared with you" list and shows a toast: "Sam shared this with you — saved." This keeps sharing lightweight (just a link, no invites, no friend requests) while creating a natural adoption loop. **Explore mode (if time allows):** Add a secondary "Explore" tab alongside "Discover" that shows a scrollable, filterable list of all events in the catalog — searchable by keyword, filterable by category/date/price. This is the "I heard about a specific thing" path. Keep it visually distinct from the recommendation cards so it doesn't undermine the curated shortlist as the primary experience. Add ticket drop alerts: if an event has a future on-sale date, show "Tickets drop [date] — remind me" and wire up a basic email or push reminder. UX pass: loading states, empty states, error handling, transitions, mobile polish at 375px. | [frontend + design] |
| **13 (freeze Apr 23)** | Apr 21–25 | **Data quality + demo prep.** Manually QA the event catalog — remove stale/duplicate events, verify links work, spot-check match reasoning. Seed 20–30 high-quality "editor's pick" events to ensure demo always has strong results. Freeze features. Write demo script. Record backup video of the full flow in case of live demo issues. Collect any waitlist signup metrics from landing page for the story. | [all] |

*After Week 13: product is frozen. No new features. Only bug fixes and data collection.*

---

## Demo Day Vision

**What does success look like on May 12?**
- A live demo where we open Sift, answer 3 real questions, and see 3–5 events actually happening in NYC that week — with real dates, real venues, real ticket links. The audience should feel like they could use this right now.

**What's the story we want to tell?**
- "New York has endless things to do and no good way to find them. People bounce between six apps and give up. Sift pulls from everywhere — Eventbrite, Ticketmaster, gallery sites, park calendars — and gives you 3–5 things matched to what you actually care about. We built it because every person we interviewed described the same problem. Here's what it looks like with real events happening this week."

**What data/metrics do we need to support that story?**
- Number of real events in the database (target: 500+)
- Number of data sources integrated (target: 6–8)
- Waitlist signups from the landing page (whatever we have)
- Synthetic testing metrics: 80% resonance, 62% intent, 13% dealbreaker rate, 98% clarity
- If possible: 5–10 real user sessions (friends, classmates) with qualitative feedback on whether the real-data version feels useful

---

## Biggest Open Question

> **Can we build a catalog that's deep enough to feel real in 5 weeks?** Our entire product promise depends on having events that surprise people — the pop-up they didn't know about, the free workshop in their neighborhood, the exhibition closing this Sunday. If the catalog is shallow or stale, the product fails regardless of how good the filtering is. The pipeline in weeks 9–10 is the make-or-break work.
