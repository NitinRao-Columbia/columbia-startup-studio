# Submission: Growth Strategy + Analytics

**Spans:** Weeks 10–11
**Submit via:** GitHub (public repo)

---

## Overview

This is a two-track assignment that runs across two classes. Both tracks are required. They inform each other: user testing tells you why people get stuck; analytics tells you how many people get stuck. Fix the onboarding. Drive the users. Report what happened.

Deck references:
- [slides_c18w10_tue_onboarding-and-growth.pdf](../classes/20260331_c18w10_tue_onboarding-and-growth/slides_c18w10_tue_onboarding-and-growth.pdf)
- [slides_c19w10_thu_ai-and-growth.pdf](../classes/20260402_c19w10_thu_ai-and-growth/slides_c19w10_thu_ai-and-growth.pdf)

---

## What to Submit

Create a folder `20260402/` inside your team folder in the public repo:

```
teams/your-team-name/20260402/
```

Submit all deliverables inside that folder. See format for each below.

---

## Track A: Qualitative — User Testing

**Due: Tuesday, April 7**

Run 3–5 user testing sessions on your onboarding flow.

**Who to recruit:** Strangers give better signal than people who know you. Friends will be polite and fill in your gaps with imagination. A stranger who has never heard of your product will click the wrong things, get confused, and give up — and that confusion is the data you need.

Where to find strangers: Reddit (r/beermoney, relevant communities), Craigslist gigs, Discord/Slack communities your target users are in, cold DMs on Instagram or LinkedIn, Columbia students and staff you don't know personally.

**Compensation:** Offering $10/session (Venmo/PayPal) dramatically increases response rates from strangers.

**Consent form:** Use the consent form template for anyone recruited via Reddit, Craigslist, or cold DM. Verbal consent is fine for people you know well.

**How to run the session:**

1. Brief them: "I'm going to have you try to use our product. Please think out loud — say what you're looking at and what you're thinking. I won't help you. There are no wrong answers."
2. Hand over the URL. Let them explore, or give them specific tasks.
3. Don't help. If they get stuck, that's the data. The only lifeline: "What are you looking for?" — then stop.
4. After the session: "What was the first moment you understood what this is for?" / "What was most confusing?" / "Would you use this again?"

**Deliverable:** A short synthesis + product recommendation. Submit as `user_testing.md`:

```
What we observed: [pattern that appeared across sessions]
What we're changing: [specific product change]
Why: [what the sessions showed that led to this decision]
```

---

## Track B: Quantitative + Growth

This track has two sets of due dates.

### Due Thursday, April 2

**Analytics installed + funnel tracking live**

GA4 and Amplitude both running. All funnel events firing — not just "sign-up completed" but every step in your acquisition, sign-up, and activation flows. Granularity is the point: if you only track "sign-up completed," you'll never know where in the flow people are dropping.

- GA4: outside the product — traffic sources, pageviews, sessions
- Amplitude: inside the product — custom events, funnel drop-off, user paths

**User Count API Endpoint**

Build a public endpoint:

```
GET /api/user-count
```

Returns JSON with your current user count. Powers the automatic leaderboard. Must be public (no auth), always live, and pulling from your actual database — not hardcoded.

**Growth Strategy Doc — Part 1**

Submit as `growth_strategy.md`. Answer three questions:

- Which channels are you targeting? (Be specific: not "social media" but "Instagram DMs to NYC food bloggers with 5k–50k followers")
- What's your approach for each? (Draft the actual message. Volume commitment: "10 DMs per day for 5 days.")
- What does success look like? How will you know if a channel is working?

---

### Due Thursday, April 9

**Drive 20+ real users to your product**

Any channel. The goal is real funnel data, not just installs. 20 is the floor.

**Growth Strategy Doc — Part 2**

Add to your existing `growth_strategy.md`:

- Results per channel (use your funnel data: views, clicks, sign-ups, activations)
- What worked and what didn't (a conclusion from data, not a guess)
- What you're changing next ("We're doubling down on X because Y")

**API Metrics Endpoint**

Build a public endpoint:

```
GET /api/metrics
```

Returns JSON:

```json
{
  "signups": 42,
  "active_users": 15,
  "waitlist": 147,
  "page_views": 820
}
```

Definitions:
- `signups`: registered accounts in your database
- `active_users`: users who did something meaningful (you define what)
- `waitlist`: email signups before the product is live
- `page_views`: from GA4 or your analytics tool

Return 0 for any metric you don't have yet.

**Register your endpoint URL**

Add a file called `20260402_api-metrics.md` to your repo root. Contents: just the URL to your `/api/metrics` endpoint. One file, one URL. Commit and push.

---

## Folder Structure

```
teams/your-team-name/20260402/
├── user_testing.md       (Track A — due Apr 7)
└── growth_strategy.md    (Track B — due Apr 2 for Part 1, Apr 9 for Part 2)

[repo root]/
└── 20260402_api-metrics.md    (your /api/metrics URL — due Apr 9)
```
