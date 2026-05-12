# EVIDENCE OF LIFE

## MVP Document

**August Fan Club · March 2026**

*Life deserves evidence, not just plans.*
*Proof that you lived.*

---

## 01 Core Flow: User → Action → Value

### Who Is the User?

Students and young professionals who use Apple Calendar or Reminders. They plan their days, know plans change, take photos of moments that matter, and feel like weeks disappear without any clear record of what actually happened.

### The Core Problem

| Plans | Memories | Reality |
|-------|----------|---------|
| Apple Calendar | Photos App | Evidence of Life ✓ |

### The Flow

| User | Action | Value |
|------|--------|-------|
| User arrives via waitlist / word of mouth | Connects Apple Calendar (and optionally Photos) | Sees a unified timeline: what was planned vs. what actually happened |
| Feels like time disappears without a record | Their past events auto-import as the Plan layer | Timeline updates daily — no new habits required |
| Wants proof of their days without journaling | Can log or confirm actual activity in seconds | Can scroll a week and instantly understand it |

### Core Value Proposition

> For students and young professionals who feel like weeks disappear, **Evidence of Life** is the automatic private timeline that finally shows what actually happened — not just what was planned.

---

## 02 Tech Stack

### Overview

The app is built on **Lovable** — an AI-powered full-stack generator that produces production-grade React + Supabase applications from natural language prompts. The team shipped a working app in weeks without a dedicated engineering team.

### Stack Breakdown

| Layer | Detail |
|-------|--------|
| Frontend | React + Vite + Tailwind CSS (Lovable-generated) |
| Backend / DB | Supabase — PostgreSQL database, Auth, Storage, Edge Functions |
| Auth | Supabase Auth (email/password; OAuth expandable) |
| Hosting | Lovable Cloud (lovable.app subdomain, CDN-backed) |
| Calendar Integration | Apple Calendar & Google Calendar (planned via CalDAV / API) |
| Photos Integration | Apple Photos (planned) |
| Code Ownership | Full React + Supabase codebase exportable via GitHub at any time |

### Two Live Deployments

| Property | URL / Purpose |
|----------|---------------|
| Landing Page | lived-timeline-maker.lovable.app — waitlist capture + brand positioning |
| App (Auth) | evidenceoflife.lovable.app — authenticated user shell, core UI |

### Scalability Note

Lovable generates standard React + Supabase code fully owned by the team. When scale demands it, the codebase can be exported to GitHub and extended or migrated by any React/Node developer without platform lock-in.

---

## 03 Team Roles

### Team Overview

Five-person founding team. Nearly all product development has been handled by one person. The remaining four members own brand, research, and demand generation.

### Role Assignments

| Person | Role | Primary Owns | On Demand |
|--------|------|-------------|-----------|
| Willow Wu | Product / Engineering | Full-stack build (Lovable), app architecture, integrations, deployments | Tech debt triage, new feature scoping |
| Shan Ye | Strategy / Ops | MVP doc, investor narrative, research synthesis, go-to-market logic | Demand gen analysis, sprint planning |
| Judy Shi | Brand / Design | Visual identity, landing page copy, tone guidelines, creative direction | Social content, waitlist email copy |
| Hanzhi Bian | User Research / Design | Interview recruitment, persona validation, V1/V2 test synthesis, Front-end Designing | Ongoing ICP refinement, feedback loops, optimizing idea |
| Eric Xue | Growth / Demand Gen | Outreach campaigns, community posts, waitlist growth, channel testing | Analytics, conversion tracking |

### Known Gap

The team is currently single-threaded on engineering. The primary developer is the critical path for all product milestones. Priority for next 30 days: reduce that dependency by documenting build process and exploring Lovable's collaborative editing features.

---

## 04 What's Faked: Woz / Concierge Strategies

### Philosophy

Evidence of Life is in **Woz mode** — the product vision is fully defined, but several core experiences are being delivered manually or approximated rather than built. This is intentional. We are testing demand before engineering automation.

### The Reality Layer, Today

| Feature | Status / Reality |
|---------|-----------------|
| Timeline Reconstruction | **FAKED** — Users manually confirm or log what actually happened. The "automatic" reconstruction shown in copy is the V2 build goal, not current state. |
| Apple Calendar Integration | **FAKED** — Calendar events are not yet auto-imported. Users currently add their plan data manually inside the app. |
| Photos Integration | **FAKED** — No live connection to Apple Photos or device camera roll. Memory layer is not yet functional. |
| Weekly Recap Feature | **FAKED** — Referenced heavily in V2 testing (highest-resonance feature for students). Not yet built. |
| "Automatic by Default" Claim | **PARTIAL** — Auth and UI shell are live. Core automation is the north star, not the current implementation. |
| Google Calendar Integration | **PLANNED** — Listed on landing page. Not yet wired. |

### What IS Real

- Landing page is live and collecting waitlist signups
- Auth shell exists at evidenceoflife.lovable.app — users can create accounts
- Core UI and timeline view are built and navigable
- Brand, positioning, and copy are fully developed
- 10-person synthetic V2 demand test completed with structured scoring
- Privacy and trust messaging fully in place

### Concierge Path (Next 30 Days)

For early access users: manually onboard 5–10 users. Walk them through connecting their calendar and reconstructing a week by hand with the team. Use these sessions as live UXR before building automation.

---

## 05 Demand Gen Strategy

### Target Audience

**Primary:** Students and young professionals who want to record what they did in a given day, week, or month — and look back on it. Key insight from interviews: many are already using Instagram Stories as a makeshift daily log. This is our clearest behavioral signal of latent demand.

| Segment | Detail |
|---------|--------|
| Primary ICP | Overwhelmed students, Apple Calendar/Reminders users, grad students |
| Secondary ICP | Young professionals who feel weeks disappear without a record |
| Where they live online | Instagram (primary), TikTok, Twitter/X, Reddit (r/productivity, r/PKMS) |
| Existing behavior signal | Using Instagram Stories as a day-log — same job, wrong tool |
| Core pain | Days pass without evidence. No single place shows what actually happened. |

### Channel Overview

| Channel | Budget | Status | Primary Goal |
|---------|--------|--------|-------------|
| Paid Ads (Meta/Instagram) | $100 | Planned | Waitlist signups <$5 CPA |
| Organic Social (Instagram, TikTok, Twitter/X) | $0 | Planned | Brand awareness + waitlist clicks |
| Community (Reddit, Discord) | $0 | Planned | Credibility + organic signups |
| Email Nurture | $0 | Planned | Waitlist → early access conversion |
| Word of Mouth | $0 | Active | Columbia network + team outreach |

### Paid Ads — Meta / Instagram

| Field | Detail |
|-------|--------|
| Platform | Meta (Instagram feed + Stories) |
| Budget | $100 total test budget |
| Launch date | TBD — pending analytics setup |
| Target audience | 18–28, US, interests: journaling, Apple ecosystem, productivity, memory/nostalgia, VSCO, BeReal |
| Success metric | Cost per waitlist signup under $5; landing page CVR above 15% |

**Ad Angles:**

- **Angle 1 — Problem:** "You planned your week. You took some photos. But there's no single place that shows what actually happened."
- **Angle 2 — Behavioral mirror:** "You're already using Instagram Stories as a day log. Evidence of Life does it automatically — and keeps it private."
- **Angle 3 — Emotional:** "Most days disappear. Not because they didn't matter. Because nothing kept them."

### Organic Social

| Field | Detail |
|-------|--------|
| Platforms | Instagram (primary), TikTok, Twitter/X |
| Posting frequency | 3x per week across platforms — assumed; adjust based on capacity |
| Content lead | Judy Shi (brand) + Shan Ye (strategy narrative) |

**Content Themes:**

- **Theme 1 — Problem stories:** "I interviewed students about how they remember their weeks. Here's what they said."
- **Theme 2 — Behavioral insight:** "People are using Instagram Stories as a journal. That's not an accident."
- **Theme 3 — Build-in-public:** Behind the scenes of building Evidence of Life — design decisions, user tests, pivots.

**First 3 Posts (Planned):**

| Post | Date | Hook + Angle |
|------|------|-------------|
| Post 1 | Week of Mar 9 | "We interviewed 10 people about how they remember their weeks. 0 of them had a good answer." — Problem framing, waitlist CTA |
| Post 2 | Week of Mar 16 | "People are using Instagram Stories as a day log. We built something better." — Behavioral insight, product tease |
| Post 3 | Week of Mar 23 | "Here's what plans vs. reality actually looks like for a grad student." — Relatable use case, UI preview |

### Community (Reddit, Discord)

| Field | Detail |
|-------|--------|
| Target communities | r/productivity, r/PKMS, r/Notion, r/selfimprovement, r/college |
| Approach | 2-week participation before any product mention. Answer questions, share insights from user research. |
| Product mention timing | Week 3+, framed as: "I built this after interviewing students about how they remember their weeks" |
| Discord targets | Productivity-focused servers, student study servers, indie maker communities |

### Email Nurture Sequence

| Field | Detail |
|-------|--------|
| Tool | TBD — Loops, ConvertKit, or Mailchimp recommended |
| Trigger | Immediately on waitlist signup |

| Email | Subject Line | Content |
|-------|-------------|---------|
| Email 1 — Immediate | "You're on the list." | Welcome + set expectations. Ask: "What's the one thing you wish you could remember about this week?" |
| Email 2 — Day 3 | "Why we're building this." | Founder story. The gap between plans and reality. Why no existing tool closes it. |
| Email 3 — Day 7 | "Here's what we've learned." | Share a V2 research finding. Show that real people feel this pain. Build anticipation. |
| Email 4 — Launch | "It's ready. You're first." | Early access invite for waitlist. Concierge onboarding offer for first 10 users. |

### Current Numbers (as of March 2026)

| Metric | Value | Note |
|--------|-------|------|
| Waitlist Signups | 147 | Since landing page launch |
| Landing Page Visitors (30d) | ~820 | Organic + direct traffic |
| Waitlist Conversion Rate | ~18% | Visitors → signups |
| Demand Test Participants | 10 | Synthetic V2 persona tests |
| Resonance Score ≥4 (1–5) | 5 / 10 | Strong-fit segment: overwhelmed students |
| Intent to Try ≥4 | 5 / 10 | Apple ecosystem users |
| Top Dealbreaker | Subscription pricing | Price sensitivity among students |
| Strongest ICP | Overwhelmed students, Apple ecosystem | Graduate student / Apple Calendar users |

### Success Metrics

| Channel | Target Metric |
|---------|--------------|
| Primary goal | 200 waitlist signups by end of March 2026 |
| Paid ads | CPA under $5, landing page CVR above 15% |
| Organic social | 500+ impressions per post, 5%+ engagement rate |
| Email | 40%+ open rate on Email 1, 10%+ click rate on launch email |
| Community | 3+ meaningful threads participated in before product mention |

### Tracking Setup (Week 1 Priority)

- Install Plausible or PostHog on landing page — track visitors, scroll depth, CTA clicks
- Set up Meta Ads Manager before any paid spend launches
- Configure email tool and connect to waitlist form
- Create a simple weekly tracker: signups by channel, CVR, top referral sources

### Week 1 Launch Checklist

- Analytics installed and verified on landing page
- Email tool configured — Email 1 (welcome) live and triggering
- First organic social post published (Post 1 — problem framing)
- Joined r/productivity and r/PKMS — made first 3 genuine comments
- Meta Ads Manager account set up, creative drafted, not yet launched

### V2 Test Key Findings

- Automation messaging and explicit privacy section were the two biggest conversion lifters vs. V1
- Weekly recap framing significantly increased intent among overwhelmed students
- Strongest personas: overwhelmed students (Apple Calendar), privacy-sensitive journalers
- Weakest personas: low-pain professionals, anti-productivity skeptics
- Top remaining blocker: no visual product demo — requested by 3 of 10 testers; unlock before paid ads launch

---

**Evidence of Life · August Fan Club · March 2026**

*The private timeline of your lived reality.*
