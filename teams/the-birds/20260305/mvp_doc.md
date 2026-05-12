# MVP Scope Document — The Birds

**Product:** Circles — A high-intent social app designed for the density of Columbia & Barnard.

**Team:** The Birds

**Date:** March 2026

---

## 01 Core Flow: User → Action → Value

**The Problem:** Columbia students want to meet new people and go out more, but coordinating plans feels awkward and exhausting ("I don't want to text a bunch of people"). 

**The Solution:** A real-world social coordination app centered around live activity circles instead of messaging threads.

### The Flow

| Step | User Action | System / Value Delivered |
|------|-------------|--------------------------|
| **1. Auth & Verification** | User signs in with `.columbia.edu` or `.barnard.edu` email. | Strict SSO validation ensures an exclusively verified student community, establishing trust. |
| **2. Discovery** | User opens the Circles app and views the feed. | App displays the "Pulse" — a real-time heatmap feed of current campus happenings (e.g., "Alex J. is at Butler 301"). |
| **3. Intent & Creation** | User decides they want to do an activity (Productivity, Social, or Off-Campus). | Taps "I'm Going" and selects a location/activity, which opens a visible circle to the campus. |
| **4. Join** | Other students see the open circle on the Pulse feed and tap to join. | Delivers frictionless coordination without back-and-forth group chats, awkward DMs, or performative posts. |
| **5. Arrival** | User arrives at the location and taps the "I'm Here" button. | Notifies the circle creator instantly, effectively eliminating "Where are you?" text fatigue. |

**Value Delivered:** A student goes from sitting alone scrolling on their phone to joining a group for coffee or studying with exactly zero text messages sent.

---

## 02 Tech Stack

We are building a **Mobile-First, Responsive Web Application** to bypass App Store approval bottlenecks while delivering a native-feeling experience to users on iOS, Android, and Desktop.

| Layer | Technology | Why We Chose It |
|-------|------------|-----------------|
| **Frontend Framework** | React + Vite | Fast, lightweight development environment ideal for a highly interactive SPA without the need for heavy SSR. |
| **Language** | TypeScript | Strict data typing is essential for safely parsing real-time database feeds and preventing runtime crashes. |
| **Styling** | Custom CSS / Tailwind CSS | Allows for a rigorous mobile-first design system with native-feeling responsive grids and 44x44px touch targets. |
| **Backend / DB** | Supabase | Essential for mandatory real-time data subscriptions so the "Pulse" feed instantly updates when users join circles. |
| **Authentication** | Supabase Auth | Enables secure, verified-only routing for university email addresses integrated cleanly with the database. |

---

## 03 Team Roles

| Name | Primary Role | Core Responsibilities |
|------|--------------|-----------------------|
| **Arjun Vaidya** | Front-end & UI/UX | Building React components, implementing the mobile-first design system with Tailwind, ensuring application responsiveness. |
| **Geonsik Moon** | Back-end & Database | Setting up Supabase schemas, real-time data subscriptions, API routes, and secure SSO authentication. |
| **Alessandro Sayad** | Testing & Marketing | QA testing the core flows across device sizes, coordinating demand gen strategies, targeting micro-influencers. |
| **In Keun Kim** | Workflow & Debugging | Managing general project workflow, resolving merge conflicts, debugging cross-stack issues, maintaining code quality. |

---

## 04 What's Faked (Wizard of Oz / Concierge) & Cut

To keep coordination lightweight and low-friction, several complex "social app" features are actively excluded or handled manually in the MVP:

| Feature | MVP Reality | Future State |
|---------|-------------|--------------|
| **"The Pulse" Activity Feed** | **FAKED (Shadow Circles):** To combat the "Empty Table" problem, the team manually seeds activities daily (e.g., "Coffee Runs", "Low Steps Hangouts") for the first 500 users. | Organic user-generated circles sustain the platform's density. |
| **Messaging / Chat** | **CUT:** No DMs or messaging threads exist in the app. Coordination is handled purely via "I'm Going" and "I'm Here" buttons. | May add limited proximity or event-specific chat if user demand requires it. |
| **Location Tracking** | **CUT:** No passive "Find My Friends" style tracking. Visibility is "Active State" only with room-level granularity (e.g., "Butler 301"). | Retain privacy-first approach to avoid the location-sharing creep factor. |
| **Social Feeds** | **CUT:** No generalized posting, photo sharing, or performative social feeds. | Remains focused entirely on real-life coordination and high-intent actions. |

---

## 05 Demand Gen & Growth Strategy

Our path to 1,000 users focuses entirely on extreme density within Morningside Heights rather than broad geographic expansion.

**Core Growth Tactics:**
1. **Micro-Influencer Seeding:** Target "Circle Leaders" (e.g., TAs seeking to host unofficial office hours, club leadership transitioning post-meeting debriefs onto the platform).
2. **Strategic Interventions:** Focus heavily on high-value, high-stress periods (like midterm weeks) by initiating timely academic review sessions precisely when students need them most to drive retention.
3. **Social Accountability:** Implement the "Ghosting Penalty"—users who join a Circle but fail to attend three times suffer a drop in their reliability score, enforcing trust in a tight-knit campus community.
