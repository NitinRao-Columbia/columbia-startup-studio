# MVP Doc — QuestCity

**Team:** Team Millionaires (DG-ST-AB)
**Date:** March 5, 2026
**Product:** QuestCity — Gamified outdoor exploration app
**Landing Page:** https://questcity-millionaires.netlify.app

---

## Core Flow: User → Action → Value

**Who is the user?**

Couples and solo explorers (25–35) living in NYC who feel stuck doing the same things every weekend. They want to go out and discover new places but are paralyzed by decision fatigue and lack a compelling reason to break their routine.

**The core problem:**

It's not that there aren't places to go — it's that exploration lacks structure, motivation, and novelty. Without a clear goal, "going somewhere new" feels effortful and uncertain. The juice isn't worth the squeeze.

**The flow:**

| Step | User Action | Value Delivered |
|------|------------|-----------------|
| 1 | Opens QuestCity, sets their city (NYC) | Sees a curated quest board for their neighborhood |
| 2 | Picks a quest ("Coffee Connoisseur: Visit 5 indie coffee shops in your neighborhood") | Has a clear goal, a reason to go out |
| 3 | Goes to the first location, takes a photo to check in | Earns points, quest progress updates |
| 4 | Completes the quest across multiple outings | Gets a badge, unlocks the next quest tier |
| 5 | Shares their completion badge | Social proof moment — friends see it and want in |

**Core value delivered:**

> A first-time user goes from "I don't know what to do this weekend" to standing outside a coffee shop they've never been to before, quest card in hand. That's the aha moment.

---

## Tech Stack

We're building with a Wizard of Oz approach for MVP — real user experience, manually operated backend. This lets us validate the core loop without building the full system.

| Layer | Tool | Notes |
|-------|------|-------|
| Frontend | Lovable (React + Supabase) | AI-generated, production-grade, ships fast |
| Database | Supabase (PostgreSQL) | User accounts, quest progress, check-ins |
| Auth | Supabase Auth | Email sign-up |
| Hosting | Netlify | questcity-millionaires.netlify.app |
| Quest data | Hardcoded JSON (MVP) | 10 hand-curated NYC quests to start |
| Check-in | Photo upload → manual verification (MVP) | We verify photos; automate later |
| Points/badges | Supabase table, updated manually | Automate once loop is validated |

**Why Lovable:** No dedicated engineer on the team. Lovable lets us ship a working, real app in days rather than weeks. We export the codebase to GitHub and own it fully.

---

## Team Roles

| Person | Primary Focus |
|--------|--------------|
| DG | Product + build (leads Lovable development) |
| ST | Design + onboarding flow |
| AB | Growth + demand gen + quest content curation |

All three are working across build and demand — roles reflect primary ownership.

---

## MVP Scope (What We're Building)

**In scope for March 12 demo:**

- [ ] User sign-up and city selection (NYC only)
- [ ] Quest board: 10 curated NYC quests across 3 categories (Food, Art, Outdoor)
- [ ] Quest detail view: name, description, locations, time estimate
- [ ] Photo check-in at each location
- [ ] Points counter and quest progress tracker
- [ ] Quest completion badge (static image, no animation yet)
- [ ] Basic user profile (name, quests completed, points)

**Explicitly out of scope (for now):**

- Couple/group mode (top request — building post-MVP)
- Leaderboard (needs multiple users first)
- AI quest recommendations
- Map view
- Push notifications
- Any city outside NYC

---

## What We're Using to Fake the Hard Parts

We're using Wizard of Oz to ship fast and validate before over-building:

| Hard problem | How we're faking it |
|-------------|---------------------|
| Quest verification (did they actually go?) | Manual photo review by team within 24h |
| Quest curation at scale | 10 hand-built quests by the team |
| Couple mode (shared progress) | Single account shared on one device |
| Leaderboard | Not built — replaced with personal progress bar |

---

## Experiment 2: Demand Validation

Running in parallel with the build sprint:

**Test:** Can we get strangers (not just classmates) to sign up for the waitlist?

**Channel:** Instagram posts + Stories. We're posting 3x this week:
1. "What if your neighborhood was a game?" — concept hook
2. A mock quest card ("Coffee Connoisseur") — tangible example
3. A screenshot of the landing page with swipe-up to sign up

**Goal:** 50 waitlist sign-ups by March 12 from people we don't personally know.

**Metric:** Sign-up conversion rate from Instagram traffic (tracking via Netlify analytics + UTM params).

---

## Definition of MVP Success (March 12)

A working demo where:
1. A stranger can sign up, pick a quest, and see their first location — without us explaining anything
2. At least 3 team members have personally completed a quest end-to-end (dogfooding)
3. We can demo a photo check-in live in the presentation
4. We have at least 1 real user (not a teammate) who has started a quest

If we hit all four, the core loop works. Everything else is optimization.
