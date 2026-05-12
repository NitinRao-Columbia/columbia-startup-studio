# Vouch — MVP Doc

**Your social life, ranked.**
NYC Pilot · March 2026

---

## Core Flow

**User → Action → Value**

A new user signs up via Google or Instagram OAuth → completes a 90-second onboarding survey (categories, neighborhoods, discovery style) → the feed immediately populates with trending NYC experiences and algorithmic picks seeded from their survey answers.

The core loop then kicks in:

1. **Rate** — User visits a restaurant, concert, fitness class, or any NYC experience. They open Vouch, search for the venue/event, and log a rating across three dimensions: Vibe, Value, and Experience (each 1–10). They can add up to 3 photos, a 280-char review, curated tags ("Worth the hype," "Great for dates"), and tag up to 5 friends they went with.

2. **Discover** — That rating surfaces in the feeds of everyone who follows them. Friends see the score (large, in brand yellow), the breakdown, photos, and tags. The friend now has a trusted signal — not an anonymous Yelp review, but a vouch from someone they know.

3. **Act** — The friend taps through to the listing, saves it to their wishlist, or goes and rates it themselves. When they do, the cycle repeats outward through the network.

**Cold start path:** Before a user's social graph is built, the feed is filled by a blend of trending-in-NYC data (high-velocity ratings across the network), Vouch Picks (algorithmic recs from survey prefs), and editorially curated Neighbourhood Guides. The Discover Bar — a voice-first AI search pinned at the top of the feed — lets users say things like "romantic dinner under $80 in the West Village" and get 3–5 personalized recommendations immediately.

**Value delivered:** Users stop guessing and start trusting. Every experience they log strengthens the network for their friends, and every friend's rating makes their own discovery better. The more you rate, the more useful Vouch becomes — for you and everyone around you.

---

## Tech Stack

| Layer | Choice | Rationale |
|---|---|---|
| **Platform** | Mobile-first web app (PWA-ready) | Ship fast, no App Store review. Must work on mobile Safari (iOS) and Chrome (Android). Desktop is nice-to-have. |
| **Auth** | OAuth 2.0 — Google + Instagram Basic Display API | Zero-friction sign-up. JWT session management. No password storage. |
| **Database** | PostgreSQL | Users, ratings, follows, wishlists, lists, streaks, Side Quests. Search-optimized indexes on experience lookup. |
| **Search** | Algolia or Elasticsearch | Full-text search across experience names and categories. Powers the universal search bar on the Search tab. |
| **Feed algorithm** | Server-side ranked feed | Blends friend activity recency, trending score, and category affinity. Recalculated on page load — no real-time push for MVP. |
| **Map** | Mapbox or Google Maps JS API | Clustered pin rendering for performance. Layer toggling (My Ratings / Friends / Wishlist) handled client-side. |
| **Voice input** | Web Speech API (browser-native) | Free, no external dependency. Fallback to text input. Whisper API is the post-launch upgrade path for accuracy. |
| **AI / LLM** | OpenAI or Anthropic Claude API | Powers the Discover Bar — intent parsing and recommendation generation. Prompt templates maintained by eng; editorial guardrails set by content team. Responses cached by intent hash. |
| **Image storage** | S3-compatible object storage, CDN-served | User-uploaded photos. Max 3 per rating, 5MB each. |
| **Share cards** | Satori (React → SVG → PNG) or Puppeteer | Server-side image generation. Open Graph tags on all public URLs. Cards cached 24hrs per object. |
| **Email** | SendGrid or Postmark | Transactional + batch. Friend activity digest, weekly trending, streak nudges, Side Quest reminders, Wrapped announcements. |
| **Analytics** | Mixpanel or Amplitude | Key events: sign_up, survey_complete, rating_submitted, wishlist_save, feed_item_click, discover_bar_query, share_tapped, email_open, email_click. |
| **External data — Venues** | Google Places API (primary), Yelp Fusion (supplementary), Foursquare (tertiary) | Venue name, address, category, hours, photos, coordinates. |
| **External data — Events** | Eventbrite, Ticketmaster Discovery, Resident Advisor, NYC Open Data, SeatGeek | Events, concerts, sports, DJ sets, free city programming, ticket pricing. |

---

## Team Roles

> *Fill in names — template below maps to what needs to get built.*

| Person | Role | Owns |
|---|---|---|
| ____Gaurav/Tushar____ | **Tech Lead / Full-Stack** | Auth, database schema, feed algorithm, API layer, deployment |
| ___Gaurav_____ | **Frontend** | All four tabs (Feed, Search, Map, Profile), rating modal, onboarding flow, responsive mobile web |
| ____Tushar____ | **Backend / Integrations** | Google Places / Eventbrite / Ticketmaster data pipelines, search index, experience data model |
| _____Tushar___ | **AI / Discover Bar** | LLM integration, intent parsing, recommendation ranking, prompt templates, caching layer |
| ______Cynthia__ | **Design** | UI/UX across all screens, share card templates, Wrapped card designs, brand system enforcement |
| ___Cynthia/Mandy_____ | **Demand Gen Lead** | Growth strategy, social content, campus/community outreach, referral loops, email campaigns |
| __All______ | **Content / Editorial** | Neighbourhood Guides, Side Quest creation, Vouch Staff Picks, Discover Bar guardrails |

---

## What's Faked (WoZ / Concierge Strategies)

Not everything needs to be fully automated at launch. The following features will be human-powered or semi-manual behind the scenes:

**1. Neighbourhood Guides — Manually curated**
At launch, there isn't enough user-generated data to populate guides algorithmically. The editorial team writes and maintains guides for ~10 key NYC neighborhoods, pulling from Google Places data and their own picks. These look algorithmic to the user but are hand-built. Transition to community data once a neighborhood crosses ~20+ ratings.

**2. Discover Bar recommendations — LLM + human QA**
The AI generates recommendations, but before any new recommendation *type* or *category* goes live, the editorial team reviews and approves it. In early weeks, the team spot-checks individual outputs daily. If the AI can't confidently parse intent or returns fewer than 3 results, it falls back to a hand-curated "Top picks for tonight in NYC" editorial set.

**3. Side Quests — Fully manual**
Side Quests ("The West Village Weekend — visit and rate 5 spots from this list by Sunday") are created, scheduled, and managed entirely by the editorial team. There is no automated generation. This is a concierge content operation disguised as a product feature.

**4. Trending in NYC — Seeded early**
Before there's enough rating velocity to generate genuine trending data, the team seeds the "Trending" feed section with editorially selected experiences that *should* be trending based on external signals (new openings, buzz on social, seasonal relevance). Once organic rating velocity is sufficient, this transitions to the real algorithm.

**5. Feed content for new users — Concierge cold start**
Users who skip the onboarding survey get a generic "trending in NYC" feed. But even users who complete the survey will have sparse friend-powered feeds early on. The feed is padded with Vouch Picks (algorithmic + editorial) and Trending cards to ensure no user ever sees an empty screen.

**6. Weekly Trending Digest email — Hand-assembled**
The Thursday digest email ("What NYC is vouching for this week") is assembled or at minimum reviewed by the editorial team each week. Automated candidate selection with manual final curation and one hand-picked Staff Pick per email.

---

## Demand Gen Status

> *Fill in actuals — framework below. Update numbers weekly.*

**Strategy:** Vouch grows through two loops — organic sharing (every rating and list shared externally is an acquisition touchpoint) and direct community outreach in NYC.

| Channel | Status | Notes / Numbers |
|---|---|---|
| **Instagram organic** | 🟡 In progress | Posting cadence: ___/week. Followers: ___. Content: NYC experience content, "rate this" polls, share card previews. |
| **TikTok organic** | 🟡 In progress | Posting cadence: ___/week. Views: ___. Content: "I rated every ___ in [neighborhood]" format. |
| **Landing page (vouchxp.netlify.app)** | 🟢 Live | Waitlist sign-ups to date: ___. Conversion rate: ___%. |
| **Waitlist email nurture** | 🔴 Not started / 🟡 In progress | Drip sequence: ___ emails. Open rate: ___%. |
| **Campus / community outreach** | 🔴 Not started / 🟡 In progress | Target: NYC colleges, young professional communities, fitness communities. Events attended: ___. |
| **Referral mechanic** | 🔴 Not started | In-app referral flow is post-MVP, but manual "invite your friends" CTA can ship at launch. |
| **Share-driven sign-ups** | 🟡 Tracking setup | Every shared Vouch link includes UTM params. Non-user landing page shows content + sign-up CTA. Target: >15% of total sign-ups from shares within 60 days of launch. |
| **Partnerships / cross-promo** | 🔴 Not started / 🟡 In progress | Target partners: NYC food bloggers, fitness influencers, event curators. Confirmed: ___. |

**Key targets (first 60 days post-launch):**

- Weekly Active Raters (north star): ___
- Activation rate (sign-up → first rating within 7 days): >60%
- Ratings per user per week: >2
- Follow graph density at 30 days: >8 avg follows per user
- Share rate on listings/lists: >5%
- Email open rate — friend activity: >40%, weekly digest: >30%