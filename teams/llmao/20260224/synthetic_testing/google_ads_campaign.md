# Google Ads Campaign Plan (Based on Synthetic Copy Test Results)

_Date:_ 2026-02-23  
_Version referenced:_ V6 (final copy)

## Strategy
Start with the **highest-converting segments** first and scale spend only after **CPA + conversion rate** hold steady. Keep campaigns segmented so budgets follow performance.

- **Primary goal:** maximize *tracked* conversions (waitlist / “Try your first hang free” signup).
- **Secondary goals:** learn which *search intents* and *messages* drive the highest conversion confidence, lowest dealbreakers.

## Segment Performance Summary (V6)
Prioritized by **conversion rate (desc)** then **dealbreaker rate (asc)**.

| Segment (bucket)        | Conversion | Dealbreakers | High-confidence conv | $ feels like a deal | $ feels fair | $ too expensive |
| ----------------------- | ---------- | ------------ | -------------------- | ------------------- | ------------ | --------------- |
| high_urgency_reset      | 100.0%     | 0.0%         | 91.7%                | 41.7%               | 50.0%        | 8.3%            |
| new_city_rebuilder      | 91.7%      | 0.0%         | 83.3%                | 25.0%               | 66.7%        | 8.3%            |
| institutional_connector | 83.3%      | 0.0%         | 41.7%                | 50.0%               | 50.0%        | 0.0%            |
| post_breakup_rebound    | 83.3%      | 8.3%         | 75.0%                | 58.3%               | 41.7%        | 0.0%            |
| event_burned_out        | 58.3%      | 16.7%        | 16.7%                | 41.7%               | 58.3%        | 0.0%            |

**Notes from V6 qualitative feedback (what to answer on LP + ads):**
- Most common “objection” across segments is basically: **“When does this launch / can I try this now?”**
- Common unanswered questions: **cancellation policy**, **host training/vetting**, **how often hangs happen**, **can I bring a friend**, **when it’s in my area**.

## Expansion Ladder (Budgets + Advancement Triggers)

### Phase 0 — Tracking & QA (before spending)
**Budget:** $0  
**Exit criteria:** tracking verified end-to-end (see Conversion Tracking section).

### Phase 1 — Prove ROI on the top 2 segments
**Segments:** `high_urgency_reset`, `new_city_rebuilder`  
**Budget:** $30–$75/day total (start low; split 60/40 across the two segments)  
**Bidding:** Maximize Conversions (no tCPA for first 7–14 days)  
**Advance when (any 2):**
- ≥ **15 primary conversions** in the last 14 days
- CPA ≤ target (set initial target after first 10–15 conversions; aim **$8–$20** for waitlist / signup depending on funnel)
- Conversion rate stable (no week-over-week collapse >25%)

### Phase 2 — Add 2 more segments, maintain CPA
**Segments:** add `post_breakup_rebound`, `institutional_connector`  
**Budget:** $100–$200/day total  
**Bidding:** Maximize Conversions → introduce **tCPA** once you have ≥30 conversions/campaign (or ≥50 overall with stable mix)  
**Advance when:**
- CPA within target for 2 consecutive weeks
- Search term report shows consistent “high intent” queries (low irrelevant spend)

### Phase 3 — Scale & test broader intents
**Segments:** add `event_burned_out` + broader “make friends” / “meet people” terms  
**Budget:** $250+/day  
**Bidding:** tCPA or Max Conversions with portfolio strategy  
**Advance when:**
- You can scale budget +20–30%/week without CPA spiking >20%

## Campaign Setup (Recommended)

### Locations
Based on your tested audience locations:
- **NYC:** Manhattan, Brooklyn, Queens, Bronx
- **Nearby:** Hoboken + Jersey City  
Set targeting to **Presence** (people in or regularly in your locations).

### Network
- **Search Network only** (start)
- Turn **Display Network OFF** (avoid low-intent spend early)

### Structure
Create **separate Search campaigns** per top segment so you can:
- assign budget by segment performance
- tailor keyword intent + RSA language
- keep negatives tight

Recommended campaigns:
1. **Search — High Urgency Reset (Core)**
2. **Search — New City Rebuilder (Core)**
3. **Search — Post Breakup Rebound (Expansion)**
4. **Search — Institutional Connector (Expansion)**
5. **Search — Event Burned Out (Later)**

### Bidding + Budget Defaults
- Start each campaign at **$15–$40/day** (Phase 1), then reallocate weekly.
- Bidding: **Maximize Conversions** (initial learning) → **tCPA** once stable.
- Ad rotation: **Optimize**.

## Conversion Tracking (Set up BEFORE spending)
Primary conversions (choose 1–2 as “Primary” in Google Ads):
1. **Signup complete** (or waitlist submit) after clicking “Try your first hang free”
2. **Payment complete** (if applicable) OR **account created**

Secondary (set as “Secondary”):
- Click “See what a hang looks like”
- View Pricing / FAQ (engaged session)
- Start signup (but don’t complete)

Implementation checklist:
- Use **GA4 + GTM**.
- Fire events on confirmation page / backend success (avoid double counting).
- Import GA4 conversions into Google Ads (or use Google Ads tag).
- Test in Tag Assistant + real device + incognito.

## Ad Extensions (Derived from Winning Copy)
**Sitelinks**
- Try Your First Hang Free
- See What a Hang Looks Like
- How Matching Works
- Pricing ($10/hang or $25/mo)
- Safety & Hosts
- FAQ (Cancellation, timing, etc.)

**Callouts**
- First Hang Free
- Small Groups (6–8)
- Hosted (No standing alone)
- Transparent Vibes
- Group Chat After
- Not a random meetup

**Structured Snippets**
- **Activities:** Coffee, Museum Walk, Cooking, Board Games, Hiking, Pickup Basketball, Open Mic
- **Features:** Matching, Host, Small Group, Follow-up Hangs, Feedback Loop

## Per-Segment Ad Groups (Keywords + RSA Drafts)

> **Rule:** keep early keywords *high intent*. Start with Exact + Phrase. Add Broad only after negatives + conversions stabilize.

### 1) High Urgency Reset (Top performer)
**Intent:** “I need a fresh start / new people now.”  
**Keyword themes (Exact / Phrase)**
- "make new friends nyc"
- "meet new people nyc"
- "how to make friends in nyc"
- "social groups nyc"
- "friend group nyc"
- "meet people after life change"
- "new friends after breakup" (if crossover)

**RSA Headlines (mix & match)**
- Your Next Friend Group Starts Here
- 6–8 People. One Activity.
- Don’t Walk In Blind
- Try Your First Hang Free
- Hosted Small-Group Hangs
- Meet People Without Awkwardness
- Not a Random Meetup

**RSA Descriptions**
- Small groups matched by interest + vibe. A host keeps things flowing. Group chat after. First hang free.
- See the activity, vibe, group size, and host before you commit. Rebuild your social life one hang at a time.

### 2) New City Rebuilder
**Intent:** “Just moved — I need friends in my new city.”  
**Keywords**
- "new to nyc make friends"
- "just moved to nyc friends"
- "how to make friends after moving"
- "meet people nyc after moving"
- "social events for newcomers nyc"
- "new in manhattan make friends"
- "new in brooklyn make friends"

**RSA Headlines**
- New to NYC? Start Here
- Meet People In Small Groups
- First Hang Free
- Host Included (No Awkwardness)
- One Activity, Real Connections

**RSA Descriptions**
- New city, new crew. Small-group hangs with a host so nobody stands alone. Transparent vibe + group chat after.
- Skip the giant meetups. Get matched into 6–8-person hangs and actually get to know people.

### 3) Institutional Connector (Expansion)
**Intent:** “I want community + consistency (school/work/community connectors).”  
**Keywords**
- "community events nyc"
- "social groups for professionals nyc"
- "meet people after college nyc"
- "make friends as adult nyc"
- "group activities nyc"
- "meet people through activities nyc"

**RSA Headlines**
- Make Friends As An Adult (NYC)
- Small Groups That Actually Click
- Hosted Activity Hangs
- Try Your First Hang Free
- Build Community, Not Contacts

**RSA Descriptions**
- Matched small-group hangs with structured activities + follow-up. It’s not networking — it’s a friend group.
- A host runs the hang, the activity breaks the ice, and the group chat keeps it going.

### 4) Post Breakup Rebound (Expansion)
**Intent:** “Rebuild after a breakup — emotionally safe + low pressure.”  
**Keywords**
- "make friends after breakup"
- "how to rebuild social life after breakup"
- "meet new people after breakup"
- "lonely after breakup nyc"
- "supportive social groups nyc"

**RSA Headlines**
- Rebuild After A Breakup
- Don’t Do It Alone
- Small Groups, Low Pressure
- First Hang Free
- Your Next Friend Group Starts

**RSA Descriptions**
- Everyone comes alone. The activity carries the first 15 minutes. A host makes it easy. Group chat after.
- You don’t need a “new dating app.” You need a real friend group. Start with one hang.

### 5) Event Burned Out (Later)
**Intent:** “I’m tired of giant events + awkward networking.”  
**Keywords**
- "meetup alternative nyc"
- "small group events nyc"
- "curated social events nyc"
- "not awkward social events nyc"
- "make friends without meetup"

**RSA Headlines**
- A Better Meetup Alternative
- Small Groups (6–8)
- Transparent Vibe + Host
- First Hang Free
- No Wandering In Alone

**RSA Descriptions**
- Big events feel random. This is matched small groups + a host + an activity, with follow-up if it clicks.
- See the vibe and details upfront. Show up knowing what you’re walking into.

## Negative Keywords (Starter Set)
Goal: block dating/hookup intent, job seekers, and unrelated event searches.

- dating, hookup, tinder, hinge, bumble, match, okcupid, “speed dating”
- “one night”, “hook up”, “casual dating”
- job, hiring, internship, “event coordinator”, “host job”
- “free tickets”, “concert tickets”, “club promoters”
- “basketball league”, “soccer league” (unless you actually offer leagues)
- “meetup login”, “meetup app” (optional — keep if you’re targeting “meetup alternative”)

## Post-Launch Optimization Playbook

### Week 1 (Learning)
- Check search terms daily → add negatives aggressively.
- Split brand vs nonbrand (if brand searches appear).
- Watch device + location performance (Manhattan vs Brooklyn etc).

### Week 2–3 (Stabilize)
- Pause keywords/ad groups with spend >2× target CPA and 0 conversions.
- Expand exact-match winners into phrase match variants.
- Test 1–2 new RSAs per segment (message angle tests):
  - “First hang free” vs “6–8 people” vs “Host included” vs “Don’t walk in blind”.

### Week 4+ (Scale)
- Add broad match **only** in best segment campaigns + with strong negatives + conversion volume.
- Introduce tCPA and scale budgets 20–30% per week.
- Build remarketing (RLSA) for:
  - visited “What a hang looks like”
  - visited pricing/FAQ
  - started signup but didn’t finish

## Landing Page Notes (Based on Persona Feedback)
Add/clarify these above-the-fold or in FAQ to reduce friction for Search traffic:

1. **Launch timing + availability**
   - “Hangs running weekly in NYC. New neighborhoods added every X weeks.”
2. **Cancellation policy**
   - clear, simple, and visible (this was a repeated unanswered Q)
3. **Host selection + training**
   - 3–5 bullet “What hosts do” + screening / code of conduct
4. **Can I bring a friend?**
   - explicit yes/no + how it works
5. **Frequency**
   - “How many hangs per week?” + “How often will I get matched?”
6. **Trust**
   - real testimonials (or clearly-labeled pilot reviews) + post-hang feedback loop

## Message Guardrails (Pulled from what resonated)
Keep these lines consistent across ads + LP:
- 6–8 people. One activity. Zero guessing.
- Don’t walk in blind.
- Your first hang is free.
- A host who makes sure nobody stands alone.
- Group chat after the hang.
