# User Testing Synthesis

**Sessions run:** 3
**Format:** Think-aloud, unguided exploration of onboarding + core flows, followed by debrief questions.

---

## Headline

Testers treated the app like Eventbrite. They browsed events, looked for tickets, and only stumbled into the social layer by accident — which is a problem, because the social layer is the entire reason this app exists. On top of that, the first minute was full of broken or unintuitive interactions (dead taps, broken back navigation, bad category recommendations), which shifted every session from "evaluating the concept" to "working around the bugs."

---

## Finding 1: The social layer is buried

**What we observed:** In two of three sessions, testers defaulted to Explore and never voluntarily visited the Feed or Friends areas. Friends is nested inside Profile. One tester said directly that for a social app, hiding the social component is "a little weird," and that if the social aspect is the differentiator, it should be the default. The third tester didn't articulate this but exhibited the same browsing pattern.

**What we're changing:** Promote Feed to the default landing screen on launch. Add Friends as a top-level nav tab. Move Profile to a top-right icon. We're flagging internally that we're not 100% sure Feed-as-default is right (it could feel empty for new users with no friends yet), so we'll instrument the change carefully and watch D1 retention and session-to-feed-visit rate before committing.

**Why:** Explore looks indistinguishable from any other event app. The differentiation — who's going, what friends are logging, the social signal on each event — only shows up if you go looking for it. New users don't go looking. They take what's in front of them, decide the app is "another Eventbrite," and leave.

---

## Finding 2: No way to actually attend an event

**What we observed:** All three testers, at some point, tried to buy or reserve tickets in-app and hit a dead end. They could save events, send to friends, and start group chats — but the actual action of committing to going wasn't supported. One tester put it bluntly: they could send an invite but couldn't book the thing they were inviting people to.

**What we're changing:** Add a "Get Tickets" CTA on every event detail page that deep-links to the source platform (Ticketmaster, Dice, Eventbrite, etc.). For free events or events without ticketing, show "No tickets needed" explicitly so the absence is intentional, not a missing feature.

**Why:** The whole funnel of the app — discover → coordinate with friends → go — has a missing final step. Driving a user to commit emotionally to an event they can't book is the worst possible dead end, because it happens at the moment of highest intent.

---

## Finding 3: The first minute is broken

**What we observed:** Across sessions: scroll didn't initialize on first load, the ellipsis menu on event detail did nothing, back navigation broke on the map detail page, and tapping an address didn't open Maps. Filter changes didn't apply without a manual refresh. Some flows required multiple back taps to escape. None of these are edge cases — they're on the critical path for a brand-new user.

**What we're changing:** Fix scroll initialization on first load. Make ellipsis functional (or remove it entirely until it does something). Restore back navigation across the map detail flow. Wire address taps to the native maps app. Make filter changes apply immediately without refresh.

**Why:** When standard mobile gestures fail in the first minute, the session stops being about the product idea and becomes about the bugs. Trust collapses before the differentiated value ever surfaces. These fixes are unglamorous, but they're the precondition for any other testing being meaningful.

---

## Finding 4: Recommendations don't reflect stated interests

**What we observed:** One tester selected Food, Film, and Networking during onboarding. The app served them mostly Arts and Music events, with a Rangers game categorized as "Other." They flagged it as "problematic" within minutes. The internal team has also noted vague top-level tags (nightlife, community) that don't help users narrow down.

**What we're changing:** Audit the category mapping logic. Add a fallback categorization pass that uses event title and description keywords before defaulting to "Other." Surface the user's active filters visibly on Explore so they can see what's being applied. Begin work on subtags so users can filter below the top-level category.

**Why:** A miscategorized first session breaks trust in the recommendation engine. The user doesn't think "the algorithm needs more data" — they think "this app doesn't know what I want," which is much harder to recover from than a bug.

---

## Finding 5: Too many ambiguous action states on events

**What we observed:** One tester couldn't predict the difference between Save, Maybe, I'm In, Send to a Friend, Go With Friends, and Propose. Several required mid-session explanation. Once they couldn't predict what a button would do, they stopped tapping.

**What we're changing:** Collapse to three actions: **Save** (private), **I'm In** (visible to friends), and **Share**. Remove or merge the ambiguous middle states. Make the broken-heart / not-interested action more obvious as a counterpart to the sign-up action.

**Why:** Choice paralysis kills engagement faster than missing features. Three clear actions used confidently beat six nuanced actions used hesitantly. The merged states can come back later if data shows users want them.

---

## Finding 6: Group swipe lacks event context

**What we observed:** When using the group swipe feature, one tester saw only an enlarged photo with an X or checkmark — no event name, date, or venue.

**What we're changing:** Add event name, date, and venue beneath the photo on the group swipe card.

**Why:** A swipe decision on a photo alone is a coin flip. The whole point of the feature is collective decision-making, which requires the actual decision criteria be on the card.

---

## What testers liked (keep doing)

The map integration got positive mentions across all three sessions. The ability to create your own event / hang-out also landed well. These are anchors — when we restructure nav to surface social, we should not deprioritize the map; if anything, the bullet-list feedback ("a more mappy map," cafes/restaurants surfaced, zoom into buildings) suggests we should invest more there.

---

## Other issues logged for the backlog

These came up in internal review and bullet-list notes alongside the formal sessions, but didn't all surface in the three structured interviews. Triaging separately:

- Search doesn't return users by name reliably — needs fuzzy matching on usernames and names.
- Lag in friend list updating after accepting requests; friend count is showing 1 for everyone (likely off-by-one or self-counted).
- Link sharing is broken.
- New event creation appears broken (created events not findable).
- "Save login info / keep me logged in" is missing — likely meaningful for retention since there's no native app.
- Public-vs-friends feed visibility should be an explicit toggle, not an implicit default.
- One-event-at-a-time scrolling (IG-explore-style) preferred over the current pattern when drilling into an event.
- "My events" surface under the account section.
- In-app popup notifications for events.
- Popular searches surface (lower priority).

---

## Priority order for next sprint

1. Fix the broken-first-minute interactions (Finding 3) — precondition for everything else.
2. Ship "Get Tickets" deep links (Finding 2) — closes the funnel.
3. Fix category mapping and surface active filters (Finding 4) — restores trust in recs.
4. Restructure nav to make Feed default and Friends top-level (Finding 1) — instrument carefully.
5. Collapse event action states (Finding 5).
6. Add context to group swipe cards (Finding 6).
