# Assignment — c18w10: Get Users

**Assigned:** Tuesday, March 31, 2026
**Class:** Startup Studio: AI-Accelerated Building & Validation

---

## Two tracks. Both are required.

---

## Track A: Qualitative

### 3–5 User Testing Sessions
**Due: Tuesday, April 7**

Run usability testing sessions on your onboarding flow. Strangers give better signal than people who know you.

**Requirements:**
- Use the consent form for anyone recruited via Reddit, Craigslist, or cold DM
- Use `interview-script-template.md` (in Discord as Google Doc) as your starting point — customize Task 3 for your product
- Record with Loom or QuickTime if you have the participant's consent

**Deliverable:** A short synthesis + product recommendation:

> **What we observed:** [pattern that appeared across sessions]
> **What we're changing:** [specific product change]
> **Why:** [what the sessions showed that led to this decision]

The goal is to do user research so you know what to fix. The recommendation should be specific enough that your team could start building it the same day.

Submit as a Google Doc link in the class Discord channel.

---

## Track B: Quantitative + Growth

### Due Thursday, April 2

**1. Analytics installed + funnel tracking live**
GA4 and Amplitude both running, with all funnel events firing for your onboarding flow. Screenshot or screen recording showing events in each dashboard.

**2. Expose a user count API endpoint**
Add a public endpoint: `GET /api/user-count` → returns total user count as JSON (e.g. `{ "user_count": 42 }`). We'll use this to update the leaderboard automatically each week.

**3. Growth Strategy Doc — Part 1 (the plan)**
Which 2–3 channels are you targeting? What's your approach for each? What does success look like? Use AI to help plan: *"I'm building [product] for [audience]. What acquisition channels should I try first and how should I approach each?"*

---

### Due Thursday, April 9

**4. Drive 20+ users to your product**
Get at least 20 people to touch your product. Any channel: Reddit, cold DMs, friends, LinkedIn, paid. The goal is real funnel data, not just installs.

**5. Growth Strategy Doc — Part 2 (results + next steps)**
Fill in what happened: results per channel, what worked, what didn't, what you're changing next. Use AI to help analyze: *"Here are my results by channel. What worked, what didn't, and what should I focus on next?"*

---

## Recruiting participants for Track A

| Channel | What to post |
|---------|-------------|
| Reddit (r/beermoney, r/[your niche]) | "20-min product test, $10 Venmo" |
| Craigslist gigs | "Paid usability test, 20 min" |
| Discord / Slack communities | Post in communities where your target users hang out |
| Cold DMs | LinkedIn, Instagram, Twitter |
| Columbia network | Students and staff you don't know personally |

**Offer $10/session** — compensation dramatically increases response rates from strangers.

---

## Setting up analytics

**Install GA4**
Add the tracking snippet to your app. Reference: [skillshop.google.com](https://skillshop.google.com) — complete the certification alongside installation.

**Install Amplitude**
Add the SDK and define custom events for each step in your sign-up and activation flows. Free tier is enough. Reference: [amplitude.com](https://amplitude.com)

*Mobile apps: use Amplitude's iOS/Android SDK and Firebase Analytics in place of GA4.*

---


