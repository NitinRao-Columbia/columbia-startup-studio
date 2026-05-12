# Growth Strategy — Part 1

Goal for the next week:** drive 20+ real users through the funnel with enough granularity to learn which channel actually converts, not just which channel makes noise.

---

## TL;DR

We're a social events app for NYC. The differentiator is the social layer (who's going, friends logging events), not the event catalog. That tells us where to fish: places where NYC-anchored people who already make plans together hang out. For Part 1, we're running two channels in parallel — our personal social graph (free, warm) and paid Reddit Ads targeted at NYC-focused subreddits (cold, $75 spend) — because the failure modes are different enough that we'll learn from running them simultaneously rather than sequentially.

---

## Channel 1: Personal social graph (ours + our friends')

### Who, specifically

- Direct first-degree contacts in NYC: classmates at Columbia, friends and friends-of-friends in the 20–30 age range living in Manhattan or Brooklyn, anyone we've gone to an event with in the last six months.
- Second-degree: we ask each first-degree contact who signs up to share with one specific friend group (their roommates, their grad cohort, their workout group, etc.). The ask is targeted — "share with the three people you'd actually go to a concert with" — not a generic "tell your friends."

### Volume commitment

- **30 personal DMs over 5 days** (6/day average), split across the founding team. Sent on iMessage, Instagram DM, and WhatsApp depending on where the relationship lives.
- **10 follow-ups** on day 4 to people who opened but didn't sign up.
- For every contact who signs up, **1 nudge** to bring in one friend group.

### Draft message

Cold-ish (someone we haven't talked to in a few months):

> hey — quick one. been building a social events app for nyc with my team for class — it's basically eventbrite + the social layer (you can see what your friends are going to, plan things together, log stuff after). looking for ~20 people to actually try it this week and tell us what's broken. would take you 5 min and you'd genuinely be helping. cool if i send the link?

Warm (a close friend):

> ok need a favor. we're testing the app this week and i need real users on it. can you sign up + try to find one event you'd actually go to? if it sucks tell me exactly where, that's the whole point. [link]

Follow-up at day 4 if they opened but didn't sign up:

> no pressure if you're slammed — but if you've got 5 min today, the funnel data on whether you bounce or not is genuinely useful to me. [link]

The "share with one friend group" ask, after they sign up:

> ok one more — could you send it to the [roommates / lab / whoever] group chat? that's the test we actually need, whether it's useful when a few friends are all on it.

### Why this channel

The product's value is unlocked when you have friends on it. A friend group joining together is worth more to us than ten isolated signups, both for our metrics (active usage, not just signups) and for the user experience (an empty feed makes the whole thing feel dead). Personal DMs are the only realistic way to get a clustered signup pattern in week one.

---

## Channel 2: Paid Reddit Ads targeting NYC subreddits

### Which subreddits, specifically

- r/nyc 
- r/AskNYC
- r/WhatsHappeningNYC
- r/nycevents
- r/Columbia
- r/FoodNYC
- r/NYStateofMind

### Approach: paid Reddit Ads, community-targeted

Rather than posting organically (which risks mod removal and patterns as spam at our size), we're running paid promoted posts via Reddit Ads Manager with **community targeting** — Reddit's most distinctive feature, which serves ads directly to users actively browsing the subreddits we care about. We layer NYC geo-targeting on top so we're not spending impressions on the half of r/nyc that doesn't actually live in NYC.

### Budget and volume commitment

- **Total budget: $75 over 5 days ($15/day).** Naming the tradeoff up front: this is well below the ~$50/day that Reddit Ads guides recommend for the optimization algorithm to do its job. At $15/day with typical Reddit CPCs of $0.75–$2.00, we're looking at roughly 7–20 clicks per day and 35–100 clicks total over the run. That's a small enough sample that a single high-performing or low-performing day can swing our conclusions, and Reddit's "Maximize Conversions" bidding will probably underperform because it won't see enough conversion events to learn from. We're going in with eyes open: this is a budget-constrained test, not a definitive read on the channel. We'll treat the directional signal seriously but won't kill or scale the channel based on $75 of data alone.
- **One ad group**, targeting all five subreddits as a cluster (r/nyc, r/AskNYC, r/FreeEventsNYC, r/Columbia, r/newyorkcity), with NYC geo-targeting layered on. At this budget, splitting per-subreddit is impossible — we'd starve every cell. Single ad group is the only viable structure.
- **Two ad creatives** running simultaneously so we get _some_ A/B signal, even if the per-creative data is noisy. Refresh if either tanks below 0.3% CTR after 48 hours.
- **Bid strategy:** **manual CPC capped at $1.25.** Skipping automated bidding here — at $15/day the algorithm won't accumulate enough conversions to optimize, and manual gives us tighter cost control on a small budget.
- **Tracking:** Reddit Pixel installed on the landing page before launch, firing on page view + signup. Even if the volume is too low for the algorithm to optimize on, the pixel data still gives us clean attribution for our own analysis.

### Draft ad creative #1 (problem-led, native Reddit voice)

> **Headline:** Finding things to do in NYC is somehow still annoying in 2026
> 
> **Body:** Image of 3 screens on branded background (think standard image based ad)
> 
> **CTA button:** Sign up

### Draft ad creative #2 (social-layer-led, more direct)

> **Headline:** An events app for NYC where the point is who you go with
> 
> **Body:** Eventbrite tells you what's happening. We tell you who's going. Discover events, see what friends are interested in, coordinate plans without 14 group chats. Free, in early access.
> 
> **CTA button:** Get early access

### Why this channel

Reddit's community-targeting puts us in front of people _while they're actively reading NYC subs_ — i.e., already in the mindset of "what's going on in this city." That's the exact decision moment our product is for. Compared to organic posting, paid ads sidestep the mod-removal risk and give us guaranteed delivery and clean attribution data through the Reddit Pixel. The honest tradeoff: at $75 of total spend, we won't get enough volume to make a definitive call on the channel — we'll get a directional read at best. But it's still the cleanest available source of cold-traffic signup data for the week, and combined with our personal-graph results, it's enough to inform Part 2's bigger decision about whether to invest more in paid acquisition.

---

## What does success look like

We're tracking per channel, not in aggregate, because the whole point of running two channels is to learn which one to double down on next week.

### Per-channel targets for the 5-day window

|Metric|Personal graph|Reddit Ads|
|---|---|---|
|Spend|$0|$75|
|Reach (DMs sent / impressions)|30 DMs sent|6,000–10,000 impressions|
|CTR / response rate|60%+ open-and-click|0.5%+ CTR (35–60 clicks)|
|Cost per click|n/a|under $2.00|
|Signups|50%+ of clicks (~10)|10%+ of clicks (~5)|
|Cost per signup|n/a|under $20|
|Active users (did one meaningful action)|70%+ of signups (~7)|40%+ of signups (~2)|
|Friend-cluster signups (≥2 people from same group)|2 clusters|0 expected|

The numbers are different on purpose. Personal DMs should convert at much higher rates because the trust is pre-existing — if we're sending 30 DMs and only getting 3 signups, the message is wrong, not the channel. Reddit ad traffic is much colder, so a 10% click-to-signup rate is the healthy benchmark. The Reddit signup target (~5) is small because the budget is small; that's a real limitation of this test, not a design choice. If Reddit drives more raw signups but personal DMs drive more _active_ users and friend clusters, that's a real signal about which channel matters for retention vs. vanity metrics.

### Total floor

20+ signups across both channels combined, with at least 8 active users (per our `/api/metrics` definition of active) and at least 2 friend clusters of 2+ people each. If we hit the signup number but not the activity number, that's a product problem, not a channel problem, and the user testing findings should already be addressing it.

### How we'll know a channel is working

- **Personal graph is working if:** we see friend clusters forming (multiple people from the same DM thread signing up within a day of each other), and post-signup activity rate is above 70%. If we get signups but no clusters, the "share with one friend group" ask is failing and we need to rework it.
- **Reddit Ads is working if:** CTR clears 0.5%, cost-per-signup stays under $20, and we can see _any_ meaningful difference between the two creatives (gives us a creative direction for Part 2). At $75 of total spend we won't get statistical certainty on any of these, but a directional read is the realistic goal. We let the campaign run the full 5 days regardless — pulling it early would shrink an already-small dataset for a savings of ~$30. The decision about whether to keep investing in Reddit Ads in Part 2 will weigh this directional read alongside the personal-graph results.

### What we'll change in Part 2 based on results

If personal-graph converts dramatically better, we lean further into clustered referral mechanics (group invite links, "see who else from your school is on") for next sprint. If Reddit Ads outperforms, we split the ad group by individual subreddit to find the highest-converting community, refresh creative based on which of the two test ads won, and increase the daily budget to ~$100/day. If both underperform, the user testing findings (broken first minute, no ticketing) are likely the bottleneck — not acquisition — and we re-prioritize bug fixes over channel expansion.