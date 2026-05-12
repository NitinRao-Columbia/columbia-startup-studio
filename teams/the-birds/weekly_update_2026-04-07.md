# Weekly update — Circles — 2026-04-07

## What we built last week (and why)

**Home, feed, and navigation**

- **Home redesign (spec + implementation):** Stories-style **live bubbles**, photo-forward **feed cards**, adaptive empty states, and **Trending / All Circles** sections—so discovery feels social, not admin-dashboard.
- **App shell:** **BottomNav** (mobile), **IconRail** (desktop), and **DesktopSidebar** with circles list, friends, and campus pulse; **MainLayout** moved to a **CSS Grid** (sidebars + feed) with a **max-width 1080px** centered column on large screens.
- **Feed stack:** **LiveBubbles**, **FeedCard** (including horizontal layout with thumbnail, LIVE badge, metadata), **FeedSuggestion**, **EmptyFeed**; **data hooks** for campus pulse, friends active, and notifications; **NotificationPanel**.
- **My Circles:** Dedicated way to see circles the user has joined—bridging feed discovery and ongoing participation.

**Circle creation and circle detail**

- **Guided create flow:** Category → location → duration → size → auto-create, with the **custom form kept for power users**—fewer steps for the common path.
- **Create UI refresh:** Stronger visual treatment (typography, motion, category cards, progress)—to match the quality bar of the rest of the app.
- **Live status on circle details:** Segmented **On My Way / I’m Here**, pulsing avatar badges, and a live summary—so members see who is actually heading to the hangout.
- **Circle scheduling:** Scheduling support with **smart time bucketing**—clearer times without noisy precision.
- **Circle detail roadmap:** **Design spec** and **implementation plan** for a collapsing-orbit hero, live activity feed, and chat drawer; **audit hardening** on the current page (accessibility, touch targets, animations, mobile orbit scaling, inline delete confirm, design tokens)—safer baseline before the full revamp.

**Account, media, and trust**

- **Auth:** **Google-only** campus sign-in with **Supabase email enforcement**—campus-appropriate identity and fewer fake accounts.
- **Profile v2:** Social layer, **avatar uploads**, and a **profile completeness nudge**—profiles that look real and encourage finishing setup.
- **Images:** **High-performance pipeline** with **HEIC** support, **compression**, and **upload progress**—faster, more reliable photos at circle scale.
- **Docs / data:** **v2 features** documentation and audit; **Columbia events parser** (Python) plus docs for future event-based content.

**Polish and quality bar**

- **Global UI pass:** Removed dead actions (e.g. non-functional search / notifications shortcuts where applicable), **Web Share** on share, **skip-to-content**, fixed landmark nesting, **44px** touch targets, **lazy-loaded** images, tokens for color/radius/shadows, Lucide icons where emojis were decorative—fewer sharp edges and better accessibility.
- **Home iteration:** Stronger borders, larger live rings, sidebar **Create** affordances, **FeedCard** / **FeedSuggestion** layout tweaks—readability and hierarchy on real devices.

**Why (summary):** We focused on **discovery, navigation, trust (auth + profile + images), and circle lifecycle (create → schedule → status)** so the product is credible for campus use before we lean on growth loops alone.
