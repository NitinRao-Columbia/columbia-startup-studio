# MVP Doc — Sift
**Team:** J Combinator
**Due:** Thursday, March 5, 2026
**Product:** Sift — NYC Event Discovery App
**Landing Page:** http://siftapp.site

---

## Core Flow

**User → Action → Value**

1. **User opens Sift** and is greeted with a single prompt: *"What do you want to do this weekend?"*
2. **User answers 3 quick questions:**
   - What kind of thing are you in the mood for? *(category: arts, music, comedy, food, outdoors, etc.)*
   - When are you free? *(today, this weekend, specific day)*
   - How far are you willing to go? *(neighborhood, borough, anywhere in NYC)*
3. **Sift returns 3–5 recommendations** — events and activities matched to their answers, pulled from curated NYC sources
4. **User picks one** and gets the key details: what it is, where, when, and how to get tickets or show up
5. **Value delivered:** They went from "I don't know what to do" to a concrete plan in under 60 seconds — without opening six other apps

---

## Tech Stack

### Option A — Mobile App (iOS + Android)
| Layer | Tool | Why |
|-------|------|-----|
| Frontend | React Native + Expo | Write once, deploy to both iOS and Android; fast iteration |
| Language | TypeScript | Type safety across the whole codebase |
| Backend / DB | Supabase | Auth, database, storage — generous free tier |
| Hosting | Expo EAS | Managed builds and OTA updates |
| Events data | Hardcoded JSON → Supabase table (MVP) | Start manual, migrate to scraped data later |

### Option B — Web App
| Layer | Tool | Why |
|-------|------|-----|
| Frontend | Next.js (App Router) | Fast, SEO-friendly, easy to deploy |
| Language | TypeScript | Consistent with mobile option if you expand later |
| Backend / DB | Supabase | Same backend works for both web and mobile |
| Hosting | Vercel | One-click deploys, free tier, pairs natively with Next.js |
| Events data | Hardcoded JSON → Supabase table (MVP) | Start manual, migrate to scraped data later |

> **Recommendation:** Start with the web app (Option B) to move fastest, then use the same Supabase backend when you expand to mobile. The Lovable landing page is already in this ecosystem.

---

## Team Roles

| Person | Primary Focus | Notes |
|--------|--------------|-------|
| Jerry | Build (frontend + product) | Leading app development |
| Yijie | Build (frontend + product) | Leading app development |
| Irene | Demand gen (community, social) | Leading growth and distribution |
| Jary | Demand gen (email, referrals) | Leading growth and distribution |

> All four team members are working across both build and demand gen — roles above reflect primary ownership, not strict boundaries.

---

## What's Faked (WoZ / Concierge)

**Data is hardcoded — not live scraped.**

For the MVP, event and activity recommendations are manually curated and stored as static data rather than pulled in real time from external sources. This lets us validate the core user flow (quiz → recommendations → decision) without building a data pipeline first.

**What this means in practice:**
- A small set of hand-picked NYC events across 4–6 categories (arts, comedy, music, food, outdoors, nightlife) are loaded into the app
- Recommendations are filtered from this static dataset based on the user's quiz answers
- The experience *feels* personalized and dynamic — the filtering logic is real, only the data source is manual
- Events are updated by hand on a rolling basis until we hit validation milestones

**When we'll un-fake it:**
Once the core flow is validated and we have signal on which categories users care about most, we'll replace the hardcoded data with a live scraper or API integrations (Eventbrite API, NYC Open Data, manual partnerships with venues).

---

## Demand Gen Status

**Status: 25 sign ups**

**Channels active as of March 3, 2026:**
- Landing page live at https://sift-landing-page.lovable.app/
- Demand gen strategy drafted and ready to execute (see `demand_gen_strategy.md`)

**Channels launching this week (Week 1: Mar 3–10):**
- Organic social: blast on founder social media pages
- Community: joining r/AskNYC and r/nyc, making genuine contributions before any product mention
- Email: setting up nurture sequence (Loops / ConvertKit), welcome email drafted
- Referrals: unique referral link to go live on thank-you page after signup

**Target for Week 3:** 50-75 waitlist signups

**Tracking:** Vercel Analytics or Plausible on the landing page; UTM parameters per channel; email analytics via ESP dashboard

> Numbers will be updated here as channels go live and data comes in.
