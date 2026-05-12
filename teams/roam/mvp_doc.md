# Roam – MVP Doc (Real-Data Barebones MVP)

**Product direction:** We’re building a **social planning** product. Users describe a plan in plain English → AI enriches it → they schedule with friends → invitees **RSVP from a web link with no app**. The main client is a **mobile app** (Expo/React Native); the **web app** in `apps/web` does two things: (1) **public invite/RSVP page** (`/join/:slug`) and (2) a **full SPA** that mirrors mobile flows (create plan, invite, schedule, ingest, etc.) for development and demo. Backend is shared.

---

## Core flow — user → action → value

**User:** Someone who wants to plan with friends with minimal friction: describe the plan once, get a shareable link, and have friends RSVP from the browser.

**Core flow (MVP demo):**

1. **Create plan (mobile or web app)**  
   User goes to “New plan” and types natural language (e.g. “Ramen with @sam and @alex this Saturday, I’ll book, Sam brings drinks”).  
   - Frontend calls `POST /ideas` with `{ ra Groq parse → Groq classify → Google Places for location → idea saved in Postgres with a unique `slug`.  
   - Response is full idea (title, slug, suggested_times, invitees, ai_data).  
   - No mock data: real DB, real AI when enabled.

2. **Invite friends**  
   User opens the plan → Share → adds invitees by `@username` or email.  
   - Frontend: `POST /ideas/:id/invites` with `{ identifier, role?, task? }`.  
   - Backend: creates/updates `IdeaShare`, sends push (if token) and email with join link: `https://join.getroam.app/join/{slug}` (or `?token=...` for identified invitee).  
   - Invitee does not need the app.

3. **Invitee RSVPs on web (critical path)**  
   Invitee opens the link in a browser.  
   - **Web app** (`apps/web`): route `/join/:slug` → `JoinPage` loads.  
   - Frontend: `GET /join/:slug` (optional `?token=...`) → backend returns `JoinPageOut`: title, organizer, plan_datetime, location, attendees, invitees, `task_for_viewer`, `suggested_times`, tags, etc.  
   - UI: `Inviteoptional `TaskCard` (“You have a task”), suggested times with “+ Cal” links, who’s coming, name/email if no token, then **“I’m in!”** / **“Can’t make it”**.  
   - On RSVP: `POST /join/:slug/rsvp` with `{ response: 'yes'|'no', name?, email?, invite_token? }`.  
   - Backend: finds share by token or name/email, updates `rsvp_status`, notifies organizer (push), returns `add_to_cal_link` (Google Calendar template or null if already added).  
   - Success screen: message + “Add to calendar” CTA when applicable.  
   - End-to-end: real plan, real invite, real RSVP, real notification; no mock in this path.

4. **Schedule (organizer)**  
   Organizer can get suggested slots (`POST /schedule` with `idea_id`, preference, duration) and book a time (`POST /schedule/book`). Google Calendar event creation for organizer when linked; invitee gets an add-to-cal link from the RSVP response.

5. **Reel ingest (optional)**  
   User can paste a TikTok/Instagram URL; backend runs yt-dlp → Groq visio and mobile both have an “ingest” surface that polls `GET /ingest/jobs/:id`.

---

## Tech stack — what we’re building with

- **Mobile app (`apps/mobile`):**  
  React Native (Expo SDK 51), Expo Router, TypeScript. State: Zustand (`authStore`). API client with Bearer Firebase ID token; 401 → refresh and retry. Hooks: useAuth, useIdeas, useIngest, useNotifications. Screens: Home, Plans, Inbox, Profile, Ideas (new, [id], schedule, share), Ingest, Map.

- **Web app (`apps/web`):**  
  React 18, TypeScript, Vite 5, React Router, Tailwind. Two entry points:
  - **Public:** `/join/:slug` only — `fetchJoinPage(slug, token)` and `submitRSVP(slug, body)` in `api/join.ts`; no auth.  
  - **Authenticated SPA:** Same API as mobile via `live/apiClient.ts` (Bearer token in `localStorage`) and `live/adapter.ts` (ideas, invites, buckets, notifications, schedule, ingest, join). Routes: login, onboard, home, plans, inbox, profile, ideas/new, ideas/:id, ideas/:id/schedule, ideas/:id/share, ingest, map.  
  State:text` (LiveAdapter). Themed AppShell, TabBar, theme toggle.  
  Deploy: Cloudflare Pages (`wrangler.toml` → `dist`, `VITE_API_BASE_URL` for production).

- **Backend (`apps/api`):**  
  FastAPI, Python 3.12, Pydantic v2, SQLAlchemy 2 (async), Alembic. Postgres (Supabase).  
  **Auth:** Firebase ID token in `Authorization: Bearer`; middleware verifies and sets `request.state.user`. `GET /join/:slug` and `POST /join/:slug/rsvp` are **public** (no auth).  
  **Endpoints (relevant to MVP):**
  - Ideas: `GET /ideas`, `GET /ideas/:id`, `POST /ideas`, `PATCH /ideas/:id`, `POST /ideas/:id/command`, delete.  
  - Invites: `GET /ideas/:id/invites`, `POST /ideas/:id/invites`, patch, delete.  
  - Join (public): `GET /join/:slug`, `POST /join/:slug/rsvp`.  
  - Schedule: `POST /schedule`, `POST /schedule/book`.  
  - Ingest: `POST /ingest/reel`, `GET /ingest/jobs/:id`.  
  - Users, buckets, notifications, auth (e.g. OTP).  
  **AI:** Groq (parse, classify, command, vision for reel). Google Places, Google Calendar (FrBusy + create event). Resend (email), Expo Push.

- **Shared:**  
  `packages/types` (TS), `packages/utils` (slug, dates, tag normaliser). Monorepo: Yarn workspaces, Turborepo.

- **Dev workflow:**  
  API: `yarn dev:api` → uvicorn port 8080. Web: `yarn dev:web` → Vite (e.g. 5173). Mobile: `yarn dev:mobile` → Expo. CORS allows app origins (e.g. join.getroam.app, roam-web.pages.dev). Auth: `AUTH_ENABLED=false` (API) and `VITE_AUTH_ENABLED=false` (web) for local dev stub user; API blocks start if `AUTH_ENABLED=false` in production.

---

## Web app in `apps/web` — detail

- **Join page (public):**  
  `src/pages/join/[slug].tsx` → `JoinPage`. Fetches via `api/join.ts` (`VITE_API_BASE_URL`). States: loading, error, ready, rsvped. Renders `InviteCard`, optional `TaskCard`, suggested times (with calendar links), “Who’s coming”, name/email when no `?token=`, and RSVP buttons. On success, shows message and optional “Add to calendar”. No auth; link is the credential.

- **  
  `App.tsx`: `BrowserRouter`, `ThemeProvider`, `RoamApiProvider`. Routes: `/join/:slug` → `JoinPage`; `/` → `AppShell` with nested routes (login, onboard, home, plans, inbox, profile, ideas/new, ideas/:id, ideas/:id/schedule, ideas/:id/sh ingest, map).  
  **API usage:** All non-join calls go through `live/apiClient.ts` (fetch + Bearer) and `live/adapter.ts` (users, ideas, invites, buckets, notifications, schedule, ingest, join). Same surface as mobile for ideas CRUD, invite create/list, schedule slots/book, ingest submit/poll.

- **Components:**  
  AppShell (header, theme toggle, inbox badge, TabBar), InviteCard (title, organizer, date, location, who’s in), TaskCard (task text), RSVPButtons (used on join page), ErrorBoundary, TabBar.

- **E2E:**  
  Playwright in `apps/web`; tests cover log → home → create plan → join page → RSVP (see `docs/E2E_TESTING.md`).

---

## Data model (relevant to MVP)

- **users** — id, firebase_uid, username, email, display_name, photo_uush_token, is_onboarded, city, etc.  
- **ideas** — id, owner_id, title, notes, location_name, lat, lng, place_id, tags, plan_type, estimated_minutes, suggested_times (jsonb), confirmedatetime, calendar_event_id, calendar_link, slug (unique), ai_enriched, status, reel_url, etc.  
- **idea_shares** — idea_id, user_id (nullable), role, rsvp_status, task, invite_token, guest_display_name, guest_email, submitted_slots, c.  
- **ml_extractions** — idea_id, activity_type, effort_level, suggested_tags, etc.  
- **reel_ingest_jobs**, **notifications**, **buckets**, **otp_tokens**.

Join response is built from `Idea` + owner + `IdeaShare` list; `task_for_viewer` and `suggested_times`/`calendar_link` come from idea and first ggested time.

---

## What’s faked / simplified (WoZ-style)- **Calendar for invitees:**  
  “Add to calendar” is either a Google Calendar **template link** (pre-filled date/time/location) or, for Roam users with linked Google Calendar, the backend creates the event and may omit the link. No two-way calendar sync; no OAuth for invitee’s calendar on the join page.

- **Auth in dev:**  
  With `AUTH_ENABLED=false`, API uses a stu; web “Skip Auth (dev)” hits `GET /users/me` and then goes to home or onboard. No real Firebase on that path.

- **Reel ingest:**  
  Real pipeline (yt-dlp, Groq vision, classify, DB), but optional for the “create plan → invite → RSVP on web” MVP. Heavy multi-item detection / clipping is not in P.

- **Schedule slots:**  
  If no availability is submitted, backend uses a default slot-finding path (e.g. next 7 days, scoring); when organizer/invitees submit slots, it uses `find_slots_from_availability`. Google FreeBusy is used where configured.

---


- **Frontend (mobile + web):**  
  Implement and wire API client (ideas, invites, schedule, ingest, join).  
  **Web:** Join page (InviteCard, TaskCard, RSVP, loading/error/success); authenticated SPA (login, home, new plan, idea detail, share, schedule, ingest) using the same adapter.  
  **Mobile:** Same flows in Expo (Home, Plans, Ideas, Share, Schedule, Ingest). Use a fixed or stored demo user when using auth bypass.

- **Backend (ideas, join, invites, schedule):**  
  Maintain `GET /join/:slug` and `POST /join/:slug/rsvp` (public), idea CRUD, invite CRUD, schedule slots and book. Ensure join response includes `suggested_times`, `calendar_link`, and `task_for_viewer`. Email (Resend) and push (Expo) for invites and RSVPs.

- **AI pipeline:**  
  Groq parse/classify for `POST /ideas`; command for `POST /ideas/:id/command`; vision for reel ingest. Graceful degradation (e.g. save idea with `ai_enriched=false` on failure).

- **Infra / DevOps:**  
  Postgres (Supabase), migrations (Alembic), CORS, env (API base URL, auth flags). Deploy API (e.g. Cloud Run), web (Cloudflare Pages), mobile (EAS).

- **Demand gen (optional section):**  
  Landing page, signup or interest capture, tracking. Channels (e.g. LinkedIn, Instagram, 1:1 from interviews) and near-term goals (visits, signups, 3–5 people to try MVP) can be added when you run campaigns.

---

## Demand gen status (placeholder)

- **Current status:**  
  No demand gen section in the repo. You can add: landing page URL, ce pitch, email capture, and whether any traffic or conversion is being measured.

- **Channels (example):**  
  LinkedIn, Instagram, link-in-bio to join/landing, 1:1 follow-ups from user interviews, classmates/friends, WhatsApp/Discord/Slack.

- **Near-term goals (example):**  
  Landing page live with one clear benefit and email capture; first posts/stories; measure visits and signups; line up 3–5 people to try the MVP and give feedbk.

---

## Summary

- **Product:** Social planning; describe plan → AI enriches → share link → friends RSVP on web, no app.  
- **Core demo:** Create plan (mobile or web) → inviteee opens `/join/:slug` on web → RSVP → organizer notified, invitee gets add-to-cal.  
- **Web:** Public join page + full SPA; both use real API and real data.  
- **Stack:** Expo ile), React/Vite/Tailwind (web), FastAPI/Postgres (backend), Groq + Google services.  
- **Faked/simplified:** Calendar is link or one-way create; auth bypass in dev; reel optional.
