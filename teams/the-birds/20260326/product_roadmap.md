# Product Roadmap — The Birds

**Product:** Circles
**Date:** March 26, 2026
**Demo Day:** May 12, 2026

---

## Where We Are Now

**What's working:**
- The core UI concept for the "Pulse" feed and the "I'm Going" / "I'm Here" button flow.
- Foundation of the React + Vite frontend and Supabase authentication with `.columbia.edu` / `.barnard.edu` SSO.
- Concept validation that students want a low-friction way to meet up without relying on group chats.

**What's not working / biggest gap:**
- The "Empty Table" problem (cold start). If a user logs in and the Pulse feed is empty, they will immediately churn. 
- Lack of organic event density to sustain the platform without manual "Shadow Circles".

**What we learned from peer review:**
- **Addressing the cold start problem:** We can prepopulate the feed by scraping Columbia events from official websites or school emails. This ensures there are always enough baseline events for new users to discover and join.
- **User transparency & engagement:** We need to provide more visibility into other users' activities to promote engagement. Showing what kind of circles people are joining, have joined before, or will likely join helps build trust and shared interests among users.

**One improvement we shipped this week:**
- Finalized our MVP Scope Document and CLAUDE.md to strictly define our engineering workflow, and locked in our core features vs. what we will fake/cut for launch.

---

## What We Need to Learn About Our Product

1. **Will students actually join a scraped event if no one else has tapped "I'm Going" yet?** (Does the scraped event act as a sufficient social catalyst, or does it feel like a sterile directory?)
2. **What level of user transparency is the "sweet spot"?** (How do we show past/future circle history to build trust and connection without violating privacy or feeling like passive tracking?)
3. **What is the critical mass of daily active users required inside Morningside Heights to make the "Pulse" feel organically alive?**

---

## What We Need to Build

| Week | Dates | Build Focus | Who |
|------|-------|-------------|-----|
| **9** | Mar 24-28 | Frontend core views (Pulse feed, Circle details). Supabase schema setup and SSO auth route. | Arjun (FE), Geonsik (BE) |
| **10** | Mar 31 - Apr 4 | Event Scraper (Columbia websites/emails) to solve cold start. User History / Transparency UI. | Geonsik (BE), Arjun (UI) |
| **11** | Apr 7-11 | "I'm Here" notification flow. "Ghosting Penalty" / Reliability Score logic integration. | In Keun (Workflow), Geonsik |
| **12** | Apr 14-18 | QA, Bug bashing. Micro-influencer onboarding and manual Seed testing. | Alessandro (QA), All |
| **13 (freeze Apr 23)** | Apr 21-25 | Final polish, performance optimization, and marketing push prep. | All |

_After Week 13: product is frozen. No new features. Only bug fixes and data collection._

---

## Demo Day Vision

**What does success look like on May 12?**
- A live, buzzing instance of Circles restricted to Morningside Heights, with real Columbia students using it to log their locations and find study groups or coffee runs. 
- A demonstrated solution to the cold start problem via our event scraping pipeline and a highly engaged early user base.

**What's the story we want to tell?**
- Columbia students are starved for connection but paralyzed by the friction of scheduling. Circles replaces the anxiety of the group chat with the simplicity of a live heatmap, proving that "intent + proximity" is the future of campus social life.

**What data/metrics do we need to support that story?**
- Number of active Circles created organically vs. joined from scraped events.
- "Join" conversion rate (how many users who open the app tap "I'm Going").
- Retention / repeated usage during midterm weeks (our highest stress/intent period).

---

## Biggest Open Question

_The one thing your team is most unsure about right now:_

> Will the transition from "Scraped Official Events" to "Organic User-Generated Circles" happen naturally, or will users treat the app as just another campus event directory rather than a spontaneous lifestyle/social tool?
