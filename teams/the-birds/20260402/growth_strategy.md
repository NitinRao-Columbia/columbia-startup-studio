# Growth Strategy Doc — TheBirds

## Part 1: The Plan

### Channels We're Targeting

We are focusing on high-density campus networks where students already communicate about studying and socializing.

1. **Reddit (r/columbia)**
   - **Why**: High engagement, anonymous platform. Good for early unfiltered feedback and initial traction from Columbia students.
2. **WhatsApp Groups (Columbia / I-House / CS / Clubs)**
   - **Why**: Dense existing networks with trusted distribution. Fast virality since students often check these groups for impromptu studying or coordination.
3. **In-Person Flyers at Butler Library**
   - **Why**: Direct access to our target audience precisely at the moment of pain (studying alone / coordinating at the library). High visibility for campus-centric tools.

---

### Approach for Each

#### 1. Reddit (r/columbia)
- **What we will say (Post Style)**: Authentic, non-promotional.
  - *Example*: "I built this because coordinating study sessions at Butler is painful — would you use this to find people studying or grabbing coffee in real-time?"
- **The Offer**: Early access to shape the product and permanently solve a real campus coordination problem.
- **Target Volume**: 2–3 posts this week, plus active commenting on relevant threads.

#### 2. WhatsApp Groups
- **What we will say (Message Style)**: Casual and direct outreach to group admins and friends to drop a link with a short pitch.
  - *Example*: "Trying this app to find people studying / grabbing coffee around campus in real-time — lmk if you wanna try it out and create the first Circles."
- **The Offer**: Be the first early adopters and create the initial "Circles" on the platform.
- **Target Volume**: 10–15 groups seeded through our team's network.

#### 3. In-Person Flyers at Butler Library
- **What we will say**: "Tired of studying alone? Scan to see who wants to grab coffee right now."
- **The Offer**: Immediate utility (find a study buddy or coffee break companion instantly).
- **Target Volume**: 20–30 table tents/flyers placed on desks in Butler Library; 5–10 direct conversations with students on breaks.

---

### What Success Looks Like

How will we know if a channel is working?

- **Reddit (r/columbia)**
  - 20+ upvotes, comments, or discussions.
  - 50–100 signups generated from the Reddit source link.
- **WhatsApp Groups**
  - 50–100 users join via shared links.
  - The first 20–30 active study/coffee "Circles" are created by these users.
- **In-Person Flyers**
  - 30+ QR code scans resulting in at least 15 signups.
- **Overall Objectives**
  - Provide enough traffic to push **20+ users** fully through our onboarding funnel (tracked via GA4/Amplitude as per assignment requirements).
  - The feed is not empty; at least 1–2 Circles active at any time.

---

## Cold Start Strategy

**1. What is your cold start type?**

We are dealing with a dual cold start problem: **Network** and **Content/Supply**. As a social app, we inherently have a Network cold start problem because the value of the platform increases with the number of users. However, since the primary use case is joining "Circles" (events or study sessions), we also face a Content cold start problem—users won't stick around if they open the app and see an empty feed.

**2. Who is your hard side?**

Our hard side is the **10-15 highly active event organizers and social connectors within our specific CS classes and I-House friend groups**. These are the people who already take the initiative to organize study sessions, book Butler Library rooms, and coordinate coffee breaks in their respective WhatsApp group chats. If we can get them to post their events on Circles, the attendees will naturally follow. 

**3. What are your two strategies?**

- **Primary Strategy (Scrape/Automate Supply):** To solve the Content cold start, we will automatically populate the platform with high-quality, relevant events. We will use our custom `events-parser` script (`circles_main/scripts/events-parser`) to scrape official Columbia events and populate our database. This ensures that even the very first user sees an active feed of things happening around campus.
- **Secondary Strategy (Hand-to-Hand Combat / Direct Promotion):** To solve the Network cold start, we will manually recruit our initial user base through direct, unscalable promotion. This involves leveraging our immediate networks through word-of-mouth, sharing in specific WhatsApp group chats, placing physical posters/table tents in Butler library, and targeted posting on the r/columbia subreddit.

**4. What can you do THIS WEEK?**

- **Action for Primary Strategy (Scraping):** Run the `events-parser` script (`parser.py` and `import-events.cjs`) to scrape and successfully import at least 50 upcoming Columbia campus events into our production database to ensure the feed is lively.
- **Action for Secondary Strategy (Direct Promotion):** Post our authentic, non-promotional pitch on `r/columbia` and drop the app link into 3 specific high-activity WhatsApp groups (e.g., our CS study group and I-House floor group) to manually onboard our first 20 active users.