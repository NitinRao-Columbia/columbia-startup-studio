# misfitAI – MVP Doc (Real-Data Barebones MVP)

**Product direction:** We’re building a **mobile app** (not web-only). MVP client is a mobile app (e.g. React Native/Expo); backend is shared.

## Core flow — user → action → value

**User:** Busy student/young professional who wants low‑friction outfit planning for the week.

**Core flow (MVP demo):**

1. User opens the mobile app (auto‑assigned demo `user_id`).
2. User goes to **Wardrobe** and:
   - Sees garments loaded from the backend wardrobe store for that `user_id`.
   - Adds 1–3 new garments via a simple form (name, category, color, formality), which creates real `GarmentItem`s in the backend in‑memory store.
3. User goes to **Week Events** and:
   - Sets a 7‑day plan (one event per day with an `event_type` like `work_meeting`, `date_night`, `gym`, `casual`).
   - Clicks “Generate my outfits.”
4. Frontend:
   - Saves events via `PUT /users/{user_id}/week-events`.
   - Calls `POST /recommendations/week` with `user_id` and the 7 events.
5. Backend:
   - Loads the real wardrobe from `_wardrobes[user_id]`.
   - Uses a simple rule‑based selector (no ML) to choose outfits per day based on `event_type` and garment attributes (category, formality).
   - Returns 7 `DayRecommendation` objects with day, event_type, garment ids/names, and a short explanation.
6. Frontend shows a **Weekly Plan**:
   - 7 day cards (Mon–Sun) with outfit and explanation for each day.
   - User sees “one click → full week of outfits” generated from their own wardrobe and events, with no mock data in this main flow.

---

## Tech stack — what we’re building with

- **Client (mobile app):**
  - React Native + TypeScript (Expo) in `frontend` (or equivalent mobile stack the team chooses).
  - API client module wrapping `fetch` with typed responses.
  - State managed via existing `AppStateContext` plus new wardrobe/events/recommendation hooks.

- **Backend (services):**
  - FastAPI app in `backend`.
  - In‑memory storage only for MVP:
    - `_wardrobes: dict[user_id, list[GarmentItem]]`
    - `_jobs: dict[job_id, MediaIngestionJob]` (existing)
    - `_week_events: dict[user_id, list[WeekEvent]]` (new)
  - Endpoints:
    - Existing:
      - `GET /wardrobe/{user_id}` (returns wardrobe).
      - `POST /media-ingestion`, `GET /media-ingestion/{job_id}` (kept for future pipeline).
    - New for MVP:
      - `POST /wardrobe/{user_id}/items` – create a garment from form fields.
      - `PUT /users/{user_id}/week-events` – save 7‑day events.
      - `GET /users/{user_id}/week-events` – fetch saved events.
      - `POST /recommendations/week` – compute weekly outfit plan from wardrobe + events.

- **Optional “real photo” flow (not required for MVP to pass):**
  - `POST /upload`:
    - Accepts multipart/form‑data (`file`, `user_id`).
    - Saves file, optionally calls OpenAI Vision once to infer category/color/formality for **one** garment, creates a GarmentItem, marks job as COMPLETED.
    - Frontend can refetch wardrobe after success.
  - This stays off the critical path so the MVP can function purely with manual garment add.

- **Dev workflow:**
  - Local dev: FastAPI on `http://localhost:8000`; mobile app via Expo dev server (or Simulator/emulator).
  - CORS open to the app origin (Expo / localhost as needed).
  - Git with feature branches + CLAUDE.md per class instructions.

---

## Team roles — who’s building what, who’s on demand gen

Using your team split:

- **Frontend (mobile app) – Shrey & Meona**
  - Implement API client with:
    - `getWardrobe(userId)`, `addGarment(userId, payload)`.
    - `saveWeekEvents(userId, events)`, `getWeekEvents(userId)`.
    - `getRecommendations(userId, events)`.
  - Wire API into `AppStateContext`:
    - Replace mock wardrobe/events with real API data.
    - Use a fixed demo `userId` or one random UUID stored in `localStorage`.
  - Views:
    - **Wardrobe view:** list garments, show empty/loading/error states, add‑garment form.
    - **Events view:** 7‑day cards, connect‑calendar UX, “Generate my outfits” button that hits backend.
    - **Weekly plan view:** 7 recommendations, explanations; simple “Regenerate week” button that recalls `getRecommendations`.

- **Inventory building (backend wardrobe + upload) – Shivangi**
  - Implement `POST /wardrobe/{user_id}/items`:
    - Accept `{ name, category, color, formality, primary_image_url? }`.
    - Create GarmentItem, append to `_wardrobes[user_id]`, return it.
  - Ensure `GET /wardrobe/{user_id}` returns the updated list.
  - Optional:
    - Implement `POST /upload` for single‑item photo ingestion (either real Vision call or stubbed attributes), then update `_jobs` and `_wardrobes`.

- **Personalised data fetching (weather, location, etc.) – Rushin**
  - For **barebones MVP**:
    - No real weather API in the critical path.
    - However, structure the code so we can plug real weather later:
      - Define event model to include location and datetime if needed.
      - Add placeholder functions and types for weather/location, but keep recommendation logic independent for now.
  - Owns future‑ready data layer:
    - Decide how events would carry location/time.
    - Sketch API surface for a future `/weather` service or upstream fetch.
  - For this assignment/doc, this role is more about **making data structures extension‑ready** than shipping weather itself.

- **Recommendation system (backend rules engine) – Gautam**
  - Implement `POST /recommendations/week`:
    - Input: `{ user_id, events: [ { day, event_type }... ] }`.
    - Load wardrobe for user.
    - For each event:
      - Apply simple rules:
        - `work_meeting` → prefer formal tops/bottoms.
        - `date_night` → smart‑casual mix.
        - `gym` → casual/activewear.
        - `casual` → relaxed pieces.
      - Select garments by category/formality; if no perfect match, fall back gracefully.
      - Generate explanation template (“For your Monday work meeting, we picked a formal shirt and pants from your wardrobe to keep it polished but simple.”).
    - Output: `{ recommendations: [ { day, event_type, top_id, bottom_id, top_name, bottom_name, explanation }... ] }`.
  - MVP assumes tops + bottoms only; dresses/one-pieces are out of scope.
  - Keep payload small; return ids/names, not full nested objects.

- **Demand gen – Meona (primary) with support from others**
  - Owns the landing page and tracking:
    - Makes sure there is a simple signup or interest capture (e.g., email + “Describe your wardrobe planning pain”).
  - Coordinates outreach across channels below.

---

## What’s faked — WoZ / concierge strategies

To match the “barebones but real” requirement:

- **Calendar integration is faked.**
  - “Connect calendar” is just a UX flag (e.g., once user sets events and clicks a button, we show “Calendar connected”).
  - No real Google/Outlook OAuth or syncing; events are directly entered into our Week Events screen and persisted to backend.

- **Weather and deep personalization are deferred.**
  - MVP recommendations do **not** use a real weather API; they are purely rule‑based off `event_type` and garment attributes.
  - Copy can hint at comfort (“keeps you comfortable for a long day”), but we are not actually calling weather or location APIs yet.
  - User‑specific style embeddings, “don’t repeat outfits too often,” color‑matching, etc. are out of scope.

- **Vision pipeline is massively simplified.**
  - Heavy YOLO / EfficientSAM / multi‑item detection is not in the main flow.
  - We may optionally offer a “beta” button: upload one photo → we fake or lightly automate a single GarmentItem creation.
  - For the core MVP, users create garments via a manual form, which is simpler and more reliable in 10 days.

- **Regenerate granularity.**
  - If needed, “Regenerate this day” can be faked by re‑using the existing weekly recommendation and just re‑selecting from it on the client, or we drop it and only support “Regenerate week” to keep backend simple.

---

## Demand gen status — what’s running, what are the numbers

We don’t have numbers yet, but we have a plan and initial actions.

- **Current status (as of Mar 5, 2026):**
  - Landing page is under active iteration; core pitch and email capture are being refined.
  - No reliable traffic or conversion numbers to report yet; we expect first data by Tuesday after soft launch.

- **Channels we’re using / will use immediately:**
  - **LinkedIn:**
    - Personal posts from team members explaining the “outfit calendar” idea.
    - DMs to past interview participants and relevant connections asking if they want early access.
  - **Instagram:**
    - Story posts and short reels showing the weekly outfit planner concept.
    - Link‑in‑bio to the landing page.
  - **Social circles:**
    - Classmates at Columbia/NYC universities, friends/housemates.
    - Targeted group chats (WhatsApp/Discord/Slack) where wardrobe / outfit talk comes up.
  - **1:1 follow‑ups from interviews:**
    - Reach back out to users who expressed interest in “easy digital wardrobe” and “weekly outfit suggestions” and invite them to try the MVP.

- **Near‑term demand gen goals (next 5 days):**
  - Get the landing page to a “good enough” state (clear problem, one concrete benefit, email capture).
  - Run at least:
    - 1 LinkedIn post per founder.
    - 1 Instagram story/reel showing early mock or screenshots.
  - Start measuring:
    - Visits to landing page (from Vercel/Netlify/GA).
    - Number of email signups / people who explicitly say “I want to try this.”
  - Line up 3–5 people willing to use the MVP and give feedback by next Thursday’s class.

