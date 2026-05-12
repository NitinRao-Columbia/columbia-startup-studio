# HAUNT – MVP Doc

**Product direction:** We're building a **social event discovery and group coordination** app for NYC. Users browse real events from 20+ sources, see what their friends have attended and rated, mark themselves as "looking to go out," and coordinate plans with group swipe-voting. The client is a **mobile app** (Expo/React Native); the backend is **Supabase** (Postgres, Auth, Realtime, Storage). Event data is populated by a **Python scraper pipeline** that pulls from Ticketmaster, Eventbrite, Dice, SeatGeek, Meetup, and ~15 NYC-specific sources.

---

## Core flow — user → action → value

**User:** Someone in NYC who wants to go out but doesn't want to browse 10 sites, text 5 group chats, or end up at something nobody actually enjoys.

**Core flow (MVP):**

1. **Discover events**
   User opens the app and browses a masonry grid of real NYC events (Explore tab) or views them on a map (Map tab). Events are filterable by category (music, comedy, art, nightlife, food, sports, community, other), date range, and price range. Each event shows a popularity score badge and category color.

2. **See social signal**
   On any event detail screen, the user sees which friends are going or considering, plus friend event logs — ratings, photos, notes, and who they went with. This replaces anonymous star ratings with trusted opinions from real people.

3. **Mark yourself as "out"**
   User toggles their going-out status (available / maybe / offline) with an optional time and note. Friends see this on the "Who's Out" screen and in the feed. This is the low-friction nudge that turns "I might go out" into "let's go."

4. **Coordinate with friends**
   User shares an event to a DM or group chat. For groups, they can create an **event proposal** (poll with multiple event options) or trigger the **group suggestion system**: the app finds events matching the group's combined interests and overlapping free times, each member swipes through them Tinder-style, and the top-voted events auto-send as a proposal.

5. **Log and rate**
   After attending, the user logs the event with a 1–5 star rating, notes, up to 5 photos, and companion tags (which friends they went with). Logs are visible on their profile and populate friends' feeds.

---

## Tech stack

- **Mobile app (`/app`):**
  Expo SDK 55, React Native 0.83, React 19, TypeScript 5.9. Navigation: React Navigation (native-stack + bottom-tabs) with a custom PagerView-based tab bar for swipeable tabs. Animations: Reanimated 4 + Gesture Handler. Maps: react-native-maps (native) / Leaflet (web). Fonts: Bebas Neue (display) + DM Mono (body). Dark-mode-first theme with light mode toggle (persisted in SecureStore).

- **Backend (Supabase):**
  Postgres with RLS. Supabase Auth (email/password). Supabase Realtime (message streaming, feed updates). Supabase Storage (avatars, event log photos). Heavy use of RPC functions (`get_my_conversations`, `get_my_feed`, `send_chat_message`, `send_event_proposal`, `update_going_out_status`, etc.) for complex queries.

- **Event data (`/app/scraper`):**
  Python scraper pipeline with 20+ source-specific scrapers (Ticketmaster, Eventbrite, Dice, SeatGeek, Meetup, Nonsense NYC, Oh My Rockness, Brooklyn Vegan, The Skint, etc.). `run_all.py` orchestrates. Includes dedup/cleanup, image auditing, and an auto-tagger. Writes directly to Supabase.

- **Landing page (`/landing_page`):**
  Static HTML/CSS/JS. Needs rebrand to HAUNT.

---

## Team roles

- **App development (frontend + backend):** Saanvi
- **Scraper pipeline:** Thomas
- **Design:** Mike
- **Demand gen:** Marium

---

## What's faked / simplified (WoZ-style)

- **Event recommendation / personalization:**
  Events show a `popularity_score` badge, but there is no personalized recommendation algorithm ranking events for individual users. The Explore grid is filtered by category and date, not by taste. The "algo scores each event based on your taste" described in the README is not yet implemented — users browse and filter manually.

- **Group suggestion algorithm:**
  The suggestion system is real but simple: it unions group members' interests (weighted by overlap), finds events in matching categories during members' free windows, scores by interest match count, and deduplicates. No ML, no collaborative filtering — it's a rule-based matcher in `src/lib/suggestions.ts`. Effective enough for MVP.

- **Event data coverage:**
  Scrapers pull real events from 20+ sources, but coverage depends on scraper maintenance and API availability. Some sources may go stale. Image quality varies — there's an `audit_images.py` and `fallback_images.py` to patch gaps. No editorial curation layer.

- **Notifications:**
  Push notification infrastructure is not wired up. The app tracks unread counts in-app (chat badges, feed) but does not send native push notifications for new messages, friend requests, or event updates.

- **Calendar integration:**
  Users can mark busy blocks in a calendar screen (used by the suggestion algorithm to find group free times), but there is no external calendar sync (Google Calendar, Apple Calendar). Busy blocks are manually entered.

- **Event creation:**
  The `CreateEventScreen` exists and lets users create events (title, description, venue, date, category, image, visibility), but the primary event supply comes from scrapers. User-created events supplement rather than drive the experience.

- **Auth:**
  Real email/password auth via Supabase (with input sanitization and password requirements). No social login (Google, Apple). No phone/SMS auth.

- **Web / cross-platform:**
  The app targets iOS, Android, and web via Expo, but the primary experience is mobile. Web may have gaps (e.g., Leaflet for maps instead of native MapView).

---

## Demand gen status

- **Landing page:** Needs to be rebuilt or rebranded for HAUNT.
- **Channels:** Not yet active for HAUNT. Prior work focused on the data analysis product.
- **Near-term:** Landing page rebrand, initial outreach to NYC friend groups for beta testing, social presence TBD.
