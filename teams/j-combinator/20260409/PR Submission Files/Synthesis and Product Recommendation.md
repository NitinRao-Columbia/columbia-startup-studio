# Synthesis & Product Recommendation
**Round 2 · 3 User Testing Sessions**

---

## What We Observed

A consistent pattern emerged across all three sessions: users were getting blocked before they could experience the product's core value. Confusion concentrated at the very top of the funnel — account creation, onboarding, and first-time event discovery — before users ever reached the features that make Sift useful.

Specific patterns that appeared across multiple sessions:

- Sign-up was not discoverable — both usability testers had trouble finding or completing account creation.
- The left-swipe gesture for disliking events was invisible to both usability testers — no one discovered it without being told.
- The onboarding preference survey felt redundant alongside the mood filter on the discover page, adding friction without clear value.
- Event display felt limited and untrustworthy — users saw too few options, and some events had already expired.
- Post-signup flow was unclear — one user completed sign-up but did not know to sign back in afterward.
- The expert reviewer reinforced that the discover page is the highest-leverage intervention point — if most users drop off there, downstream features do not matter.

---

## What We're Changing

We will improve the first-time user flow across three areas, in priority order:

**1. Account entry and post-signup clarity**

- Make the sign-up option equally prominent to sign-in on the landing page.
- Add a clear prompt after registration informing users to check their email for a confirmation link.
- Guide users explicitly to sign in after confirming their email — the handoff between steps must be explicit.

**2. Onboarding and gesture discoverability**

- Add a lightweight gesture tutorial on first use — show left-swipe to discard and right-swipe to save.
- Reduce or eliminate the onboarding preference survey; introduce filters organically on the discover page instead.
- Guard against accidental back-swipe navigation resetting progress — save onboarding state so users do not lose their place.
- Consider launching in guest mode by default so users reach the discover page immediately without being forced to log in.

**3. Event discovery and recommendation quality**

- Expand the number of events shown — users want to browse, not choose from a narrow curated set of three.
- Add expiry filtering — never surface events that have already passed.
- Add richer event descriptions so users have enough context to make a decision.
- Support casual browsing without requiring a specific time or date filter.

---

## Why

The sessions made clear that users are dropping off before they ever reach Sift's value. When sign-up is hard to find, gestures are invisible, and the recommendation set feels thin or stale, users lose trust in the product before they can form a habit around it.

The expert reviewer reinforced this with a structural point: the discover page is the top of the funnel, and if the majority of users drop off there, even strong conversion downstream produces almost no retained users. Fixing discoverability and first-impression quality is not a polish exercise — it is the highest-leverage product intervention available right now.

These changes are scoped to flow and content quality, not feature additions. The team can begin implementing them the same day without new infrastructure.
