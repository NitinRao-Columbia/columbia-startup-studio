# **Recruitr — MVP Doc**

---

**Core Flow — User → Action → Value**

**COACH FLOW**

**Step 1 — Discovery & Signup** A college coach hears about Recruitr through a peer, ad, or cold outreach. They land on the marketing page, read the value prop, and click "Sign up as a coach." They enter their name, email, school, sport, and division (D1 / D2 / D3 / NAIA / JUCO). The account is held for manual verification before activation (DM disabled until verified).

**Step 2 — Verification** Recruitr (manually, for now) confirms the coach is real — checks school email domain or LinkedIn. Coach gets an email: "You're approved, here's your login."

**Step 3 — Profile Setup** Coach logs in and fills out their profile: school name, sport, division, roster needs, what they're looking for in recruits (grad year, position, region). This doubles as a signal to athletes about what programs are actively recruiting.

**Step 4 — Search & Filter** Coach goes to the search page. They filter by: sport, position, graduation year, state/region, GPA range. Results show a list of athlete cards — name, sport, position, grad year, school, and a thumbnail.

**Step 5 — Athlete Profile Review** Coach clicks into an athlete's profile. They see: bio, stats, academic info (GPA, intended major), highlight reel, and contact info. Coach can also see if the athlete has marked themselves as "actively seeking recruitment."

**Step 6 — Outreach** Coach clicks "Message" and sends a direct message to the athlete through the platform. For now this triggers an email to the athlete — the in-app inbox is the future state. Coach can also save the athlete to a shortlist.

**Step 7 — Ongoing Recruiting** Coach returns to the platform to manage their shortlist, follow up with athletes, and search for new recruits as their roster needs change.

**Value delivered:** Coach spent 20 minutes finding 5 real prospects instead of 3 hours cold-emailing club coaches and scrolling through Instagram.

---

**ATHLETE FLOW**

**Step 1 — Discovery & Signup** An athlete (or their parent) finds Recruitr through social media, a coach referral, or a club team. They land on the page and click "Create athlete profile." They enter name, email, graduation year, sport, and position.

**Step 2 — Profile Build** Athlete fills out their full profile:

* Personal info: name, high school, grad year, GPA, intended major  
* Sport info: position, stats, awards, club team  
* Highlight reel  
* Recruiting preferences: divisions interested in, regions open to, whether they want to be visible to coaches

**Step 3 — Go Live** Athlete toggles their profile to "Active — open to recruitment." They are now discoverable in coach search results.

**Step 4 — Getting Found** Coaches matching the athlete's sport/position/grad year find them in search. The athlete doesn't have to do anything — they just show up in results.

**Step 5 — Receiving Interest** Athlete gets an email notification: "A coach from \[School Name\] sent you a message." They log in and see the message in their inbox. They can read the coach's profile — school, sport, division — before deciding to reply.

**Step 6 — Reply & Conversation** Athlete replies through the platform. Back-and-forth messaging continues. The athlete can also share their profile link directly with coaches they're interested in, even outside the platform.

**Step 7 — Off-Platform** At some point the recruiting relationship moves off Recruitr — campus visit, phone call, official offer. Recruitr's job is to create that first connection.

**Value delivered:** A D3-caliber athlete who never would have been found by a small program in New Hampshire gets a message from their coach. That connection doesn't happen without the platform.

---

**WHERE THE FLOWS INTERSECT**

The match happens when a coach's search filters align with an athlete's profile. The tighter and more complete both profiles are, the better the match quality. Early on, we're manually improving match quality by helping athletes build out their profiles (concierge onboarding) and coaching coaches on how to search effectively.

---

## **Tech Stack**

### **Backend (built)**

| *Layer* | *Technology* |
| ----- | ----- |
| API Framework | FastAPI (Python 3.12) |
| ASGI Server | Uvicorn |
| ORM | SQLAlchemy 2.x |
| Migrations | Alembic |
| Database | PostgreSQL 16 |
| DB Driver | psycopg |
| Config/validation | Pydantic v2 \+ pydantic-settings |

### 

### **Infrastructure (configured / containerized)**

| *Service* | *Purpose* |
| ----- | ----- |
| PostgreSQL 16 | Primary relational database |
| Redis 7 | Catching, task queue, session store |
| MeiliSearch v1.6 | Athlete and school search and filtering |
| MinIO (S3-compatible) | Media storage (highlight reels, photos, etc) |
| Centrifugo v5 | Realtime messaging and notifications |

### **Data**

* NCES IPEDS HD directory used to seed all 2-year and 4-year colleges in the Northeast (\~500+ institutions)  
* School records include: name, address, website, public/private flag, institution level (2-year / 4-year), community college flag, logo URL (via Clearbit)

### **Planned additions**

* Passlib / bcrypt — password hashing  
* python-jose / PyJWT — JWT auth tokens  
* pytest \+ httpx — automated testing  
* Mobile app (TBD framework)

---

## **Team Roles**

| *Name* | Role | Focus Area |
| :---- | :---- | :---- |
| Cam | Full-Stack Engineering | Built majority of codebase, architecture, and technical decisions |
| Joao Pedro | Enginering & GTM | Deployment, code contributions, and co-leads GTM strategy |
| Benjamin | Enginering & GTM | Deployment, code contributions, and co-leads GTM strategy |
| Connor | Admin & Demand Gen | Operations, outreach, coordination. |

---

## **What's Faked (Wizard of Oz / Concierge)**

| *Feature* | *What users see* | *What’s happening* |
| ----- | ----- | ----- |
| Athlete search | Filtered search results | Manually curated athlete list, MiliSearch not fully indexed yet |
| Messaging | In-app message threads | Emails or manual follow-ups to be handled off platforms if needed |
| Highlight reels | Video on athlete profile |  |
| School database | Full schools list |  |
| Coach verification | Verified coach badge |  |
| Notifications | Realtime alerts | Email notifications as of now |

## ---

## **Demand Gen Status**

### **What's running**

- [ ] Direct outreach to HS coaches / club coaches (email or DM)  
- [ ] College coach cold outreach (target: D3 / NAIA / community colleges in Northeast)  
- [ ] Social content (TikTok / Instagram targeting HS athletes \+ sports parents)  
- [ ] Waitlist page 

### **Numbers**

| *Metric* | *Current* |
| ----- | ----- |
| Waitlist signups | 25 waitlist signups |
| Coach accounts | 5 coach accounts created |
| Athlete accounts | 25 player account created  |
| Outreach sent | Approximately 50 emails sent out to friends, family, and coaches that are in the sports space |
| Response rate | 15 replies |
| Activation | 5 accounts created out of the replies |

### 