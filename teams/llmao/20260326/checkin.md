# Check-in — 20260326

## Look back: peer review

**What worked when people used your product?**
Strong resonance with the core pain point. People who have moved to a new city or are navigating social life solo immediately saw themselves using the app. The problem felt real and personal to a lot of people in the room, which validated the direction.

**What confused them or broke?**
The biggest source of confusion was the app's identity. Reviewers could not clearly tell if this is a dating app or a friend-making app. This ambiguity will hurt conversion and needs to be resolved before we go wider with the product.

**What's the biggest gap?**
Onboarding at scale. Users want to see other people already on the platform before they commit, which creates a cold-start problem. The main suggestions were a hybrid room model (user-created rooms + algorithmically seeded rooms from third-party sources), online/digital event support for easier onboarding, breakout group chats from larger rooms, DMs, user bios, and room descriptions. On the business side, a freemium model was suggested with room creation and event swipe limits as the paid tier levers.

**Ship one improvement based on what you heard**
DMs and breakout rooms. These were the most concrete and actionable feature requests from the session.

---

## Look forward: your roadmap

**What do we still need to learn about our product?**
- Are we a dating app or a friend-making app? We need to pick a lane and make it clear from the first screen.
- Who is the primary user, someone new to a city, a single person looking to socialize, or both?
- What is the aha moment and are we designing toward it intentionally?
- Which third-party events API is the right fit for us (Eventbrite, Meetup, Ticketmaster) and what are the commercial terms if we build a paid product on top of it?

**What do we need to build between now and Demo Day?**
- DMs and breakout rooms (shipping this week)
- Online/digital event support as the primary launch context. Lower friction than IRL events, no geographic constraint, easier to onboard users and iterate quickly. This is the move that takes the load off users and could bring in more people without relying heavily on in-person events.
- Replace hardcoded events with real data from a third-party API (Eventbrite or Meetup are the top candidates). Meetup is especially well aligned given our use case. Need to validate API terms before building a paid model on top of it.
- Hybrid room model: user-created and algorithmically seeded from third-party event sources
- User bios and room descriptions
- Freemium model: room creation and daily event swipe limits as the paid boundary
- Email waitlist or landing page to capture interest now

**What's our team's biggest open question?**
How do we solve the cold-start problem fast enough that early users don't churn before the community reaches critical mass? And separately, what are the commercial constraints of building a paid product on top of a third-party events API?

**What does success look like on May 12?**
A live product where users can join rooms, chat, and break out into smaller groups or DMs, with enough real users or seeded activity that it does not feel empty. Events are pulled from a real data source, not hardcoded. The dating vs. friends question is answered clearly in the UI, onboarding takes under 2 minutes, and the freemium model is live with at least one paid conversion.
