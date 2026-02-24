# Experience Architects — Google Ads Campaign Plan

**Derived from:** Synthetic user testing study (60 personas, 7 rounds, 360 evaluations)
**Date:** February 23, 2026

---

## 1. Strategy: Prove-and-Scale

Start with the highest-converting segment, prove ROI, then expand one segment at a time. Each segment only unlocks when the previous tier hits its advancement trigger. This prevents burning budget on unproven audiences.

**Expansion ladder:**

| Tier | Segment | Study Conv | Study DB | Monthly Budget | Advancement Trigger |
|---|---|---|---|---|---|
| **Tier 1** | City Explorer | 89% | ~8% | $1,500–2,500 | CPA < $15 for 2 consecutive weeks |
| **Tier 2** | FOMO Scroller | 81% | ~8% | +$1,500–2,500 | Tier 1 trigger met + CPA < $18 for 1 week |
| **Tier 3** | Social Connector | 72% | ~0% | +$1,500–2,000 | Tier 2 stable + referral loop generating organic installs |
| **Tier 4** | Taste Curator | 64% | ~0% | +$1,000–1,500 | Tier 3 stable + LTV data shows Pro conversion |
| **Tier 5** | Journal Graveyard | 56% | ~17% | +$500–1,000 | Tiers 1–4 profitable + retention data proves 30-day retention |

**Total budget at full scale:** ~$6,000–9,500/month
**Starting budget (Tier 1 only):** $1,500–2,500/month

**Why this order:**
- City Explorer has the highest conversion (89%) and the strongest unmet need — they're actively searching for solutions in new cities.
- FOMO Scroller has 81% conversion and the highest search intent — they're already Googling "things to do" and "best of" lists.
- Social Connector has zero dealbreakers but conversion depends on network effect — better to enter after organic referral loops are established.
- Taste Curator converts well but their objections are product-experience-driven — they need to see the UX, not just the ad.
- Journal Graveyard has the highest dealbreaker rate (17%) and structural barriers (behavior change). Only enter after retention data proves the product works for this segment.

---

## 2. Segment Performance Summary (from Study)

### Tier 1: City Explorer — "New to town, building my map"
- **3-run avg conversion:** 89%
- **Dealbreakers:** ~8% (all requesting community discovery — resolved by "local trending" feature)
- **Strongest lines:** "First it's your map. Then it's your map plus everyone you trust." / "Local trending" / Chicago testimonial
- **Price perception:** 87% fair/good_deal. $99/year framed as "investment in my first year"
- **Search behavior:** High intent — actively searching for city-specific recommendations, "things to do in [city]", neighborhood guides

### Tier 2: FOMO Scroller — "Scrolling for plans, never acting"
- **3-run avg conversion:** 81%
- **Dealbreakers:** ~8% (free discovery too limited)
- **Strongest lines:** "Choosing feels like work when you don't have a system" / "Discover what's next through the people you trust"
- **Price perception:** 82% fair/good_deal. Responds to forward-looking discovery framing
- **Search behavior:** Broad discovery intent — "best restaurants near me", "things to do this weekend", "date night ideas"

### Tier 3: Social Connector — "The friend everyone asks for recs"
- **3-run avg conversion:** 72%
- **Dealbreakers:** ~0%
- **Strongest lines:** "Now I just send them my profile" / "Network-powered discovery... Because it is one."
- **Price perception:** Strong. Referral incentive aligns perfectly with their natural behavior
- **Search behavior:** Lower direct search intent — better reached through social/display. On Google: "recommendation app", "share restaurant list with friends"

### Tier 4: Taste Curator — "Has taste, needs a system"
- **3-run avg conversion:** 64%
- **Dealbreakers:** ~0%
- **Strongest lines:** "Your 8/10 Thai place" / "Searchable. Sortable. Yours." / Taste analytics specificity
- **Price perception:** $99/year perceived as fair for a "real tool"
- **Search behavior:** Specific — "rate restaurants app", "experience tracker", "personal ranking app", "Beli alternative"

### Tier 5: Journal Graveyard — "Tried everything, nothing stuck"
- **3-run avg conversion:** 56%
- **Dealbreakers:** ~17% (no passive tracking, retention unproven)
- **Strongest lines:** "Most apps like this die after a week. We know that." / "One tap. That's it."
- **Price perception:** Free-only until behavior change is proven (3+ months)
- **Search behavior:** Low direct search intent — they've stopped looking. Better reached through retargeting or social. If searching: "simple experience tracker", "app that doesn't require reviews"
- **⚠️ Alternative path:** Don't target with cold Google Ads until 30-day retention data exists. Instead, retarget users who downloaded but went inactive with honesty-driven messaging ("We know you stopped. Here's why it's worth opening again."). This segment converts through product experience, not advertising.

---

## 3. Campaign Setup

### Campaign Type
**App campaigns (Google App Campaigns)** for app installs as primary. If driving to landing page first, use **Search campaigns** for Tiers 1–2 and **Display/Discovery** for Tiers 3–5.

### Bidding Strategy
- **Launch (weeks 1–4):** Target CPA bidding. Set initial tCPA at $12 for Tier 1 (city_explorer has high intent and high conversion — expect efficient CPAs). Adjust weekly.
- **Scale (weeks 5+):** Shift to Maximize Conversions with a CPA cap once you have 30+ conversions per ad group (Google's learning threshold). For App campaigns, use Target Cost Per Install.
- **Never use:** Maximize Clicks. This campaign is conversion-driven, not traffic-driven.

### Budget
- **Daily budget (Tier 1 launch):** $50–85/day ($1,500–2,500/month)
- **Ramp:** Start at $50/day for week 1. If CPA is on target, increase by 20% weekly.
- **Circuit breaker:** If CPA exceeds 2× target for 5 consecutive days, pause and review ad copy + targeting before resuming.

### Networks
- **Search Network:** Yes (Tiers 1, 2, 4)
- **Display Network:** Yes for Tier 3 (social connector — visual/social framing). No for Tiers 1–2 during launch (search intent is stronger).
- **YouTube:** Test for Tier 2 (fomo_scroller responds to aspirational content) in Tier 2 expansion phase.
- **Discovery/Demand Gen:** Test for Tier 3 (social connector) and Tier 5 (journal_graveyard) when those tiers unlock.

### Locations
Start with the top 15 US metros by population density (where network effects are most likely to take hold). Prioritize cities with high transplant populations (city_explorer's strongest signal):

**Launch cities (Tier 1):** New York, Los Angeles, Chicago, Austin, Denver, Seattle, San Francisco, Portland, Nashville, Miami

**Expansion cities (Tier 2+):** Boston, DC, Atlanta, Dallas, Minneapolis, Philadelphia, San Diego, Charlotte, Raleigh, Phoenix

### Schedule
- **Days:** All 7 (experience-discovery behavior doesn't have a weekday pattern)
- **Hours:** Increase bids 20% for 11am–2pm and 5pm–10pm (decision windows — lunch and after-work planning)
- **Weekend boost:** Increase bids 15% Fri 4pm–Sun 8pm (peak "what should we do" moments for fomo_scroller)

### Device
- **Mobile-first:** 80%+ of target audience (18–35, Instagram/TikTok referrers) will see ads on mobile. Ensure landing page is mobile-optimized.
- **Desktop:** Don't exclude, but don't optimize for.

---

## 4. Conversion Tracking — Set Up Before Spending

**⚠️ Do not launch ads until all of these are verified in Google Ads:**

### Primary Conversions (counted)
1. **App Install** — Firebase/Adjust/AppsFlyer SDK event. This is the primary optimization signal.
2. **First Rating** — Custom event: user rates their first experience. This is the true activation metric (install without rating = wasted spend).

### Secondary Conversions (observed, not optimized)
3. **Day 7 Retention** — User opens app on day 7+ post-install. Critical for journal_graveyard viability assessment.
4. **Pro Upgrade** — User converts to paid Pro plan. Revenue signal for LTV calculation.
5. **Referral Sent** — User invites a friend. Network growth signal — especially important for social_connector segment.

### Attribution
- **Window:** 7-day click, 1-day view (standard for app installs)
- **Model:** Data-driven attribution (Google's default for App campaigns)
- **Cross-device:** Enable (users discover on mobile, may install later)

### Landing Page Conversion (if using Search → LP → App Store flow)
6. **LP Click-through** — Click on "Download the App" or "Get Early Access" CTA
7. **LP Scroll Depth** — 75%+ scroll (indicates engagement — useful for audience building)

---

## 5. Ad Extensions

Derived from the strongest-performing copy elements across the study.

### Sitelink Extensions
| Sitelink | URL | Description |
|---|---|---|
| How It Works | /how-it-works | Rate in 2 seconds. Build your taste profile. Discover through friends. |
| Free Forever | /pricing | Full taste profile, unlimited ratings, friend activity. Not a trial. |
| Pro — $99/year | /pricing#pro | Network discovery, local trending, taste analytics. |
| Invite Friends, Get Pro Free | /referral | Invite 3 friends → your first month of Pro is free. |

### Callout Extensions
- One tap. No reviews required.
- Free — not a trial
- Friend-powered discovery
- $99/year for Pro
- Rate any experience in 2 seconds
- See what friends rate nearby
- Local trending in your area
- Works solo from day one

### Structured Snippets
- **Types:** Restaurants, Bars, Hikes, Day trips, Shows, Classes, Pop-ups, Comedy, Concerts
- **Features:** Taste profile, Friend discovery, Local trending, Weekly recaps, Taste analytics

### Image Extensions (if using Demand Gen / Discovery)
- App screenshot showing a taste profile with ratings
- Friend network discovery interface
- "Your 8/10 Thai place" visual concept

---

## 6. Per-Segment Ad Groups

### Tier 1: City Explorer

**Ad Group: new-city-discovery**

**Keywords:**
- things to do in [city] (broad match modified → phrase match)
- best restaurants [city] new
- new to [city] recommendations
- explore [city] neighborhoods
- [city] local guide app
- best spots in [city]
- hidden gems [city]
- neighborhood guide [city]
- what to do in [city] this weekend
- restaurant recommendations [city]

**Responsive Search Ad 1:**

Headlines (max 30 chars each):
1. New to Town? Map Your Taste
2. Your City, Ranked by You
3. Discover Through Locals
4. Build Your Taste Profile
5. Better Than "Best Of" Lists
6. One Tap. Rate Anything.
7. Free — Not a Trial
8. Friends' Picks > Algorithms
9. Local Trending in Your Area
10. Rate Restaurants, Bars & More
11. $99/yr for Full Discovery
12. Your Map. Your Network.
13. Stop Defaulting to the Same 3
14. Find What Locals Actually Love
15. Beli, But for Everything

Descriptions (max 90 chars each):
1. Build a living taste profile of your new city. Rate anything in 2 seconds flat.
2. See what locals rate highest in your neighborhood. Friend-powered, not algorithm-driven.
3. Start with your personal taste map. Add friends' signal as your network grows.
4. First it's your map. Then it's your map plus everyone you trust. Download free.

Pin: Headline 1 or 2 in position 1. Description 1 in position 1.

**Responsive Search Ad 2:**

Headlines:
1. Moved Recently? Start Here
2. Build Your City Taste Map
3. Rate. Rank. Discover.
4. Your Neighborhood, Decoded
5. Friends' Ratings > Yelp
6. See What's Trending Nearby
7. One Tap Ratings. Zero Reviews
8. Free Taste Profile Forever
9. Explore Smarter, Not Harder
10. Invite Friends, Get Pro Free
11. Local Discovery That Works
12. 2 Seconds to Rate Anything
13. Stop Googling "Best Of"
14. Network-Powered Discovery
15. Your Social Life, Ranked

Descriptions:
1. Your friends' ratings are better than any "best of" list. See their top spots nearby.
2. Moving to a new city? Build your taste map from day one. Free, with local trending.
3. Rate experiences with one tap. No reviews, no writing. Just your honest rating.
4. Local trending shows you what's popular beyond your friend group. Try Pro free.

---

### Tier 2: FOMO Scroller

**Ad Group: weekend-plans-discovery**

**Keywords:**
- things to do this weekend
- what to do tonight
- fun things to do near me
- date night ideas [city]
- best bars near me
- new restaurant near me
- tired of same restaurants
- need plans this weekend
- what should I do today
- cool things to do [city]
- something different to do
- stop staying in

**Responsive Search Ad 1:**

Headlines:
1. Stop Scrolling. Start Going.
2. Your Taste Deserves a System
3. Discover What's Next
4. Friends' Picks, Not Algorithms
5. End the "Same 3 Places" Loop
6. One Tap. Rate Anything.
7. Free — See Friends' Ratings
8. Plans > Scrolling
9. What to Do This Weekend?
10. Local Trending Near You
11. Choosing Shouldn't Feel Hard
12. Your Social Life, Ranked
13. Find Better Plans. Easily.
14. Done With Best-Of Lists?
15. Less Mediocre. More You.

Descriptions:
1. Choosing feels like work without a system. Build your taste profile. Discover through friends.
2. Stop scrolling "best of" lists. See what people you actually trust rate highest nearby.
3. Rate experiences in 2 seconds. Discover better plans through your friend network. Free.
4. Your friends' top-rated spots surface when you need them. Network-powered discovery.

**Responsive Search Ad 2:**

Headlines:
1. Your Weekend Upgrade
2. Discover Through Friends
3. Better Plans in One Tap
4. Beyond Yelp & Google Reviews
5. See What Friends Rate Nearby
6. Build Your Taste Profile Free
7. Friend-Powered Discovery
8. Not Another "Top 10" List
9. Rate Anything. Find Better.
10. Trend-Aware. Friend-Driven.
11. Two Seconds. Honest Rating.
12. Explore Your Own City
13. Plans That Match Your Taste
14. Local Trending + Friends
15. Free Download. Real Product.

Descriptions:
1. Their discoveries become yours. See friends' top-rated restaurants, bars, and activities.
2. Build a living taste profile and discover what's next through people you actually trust.
3. Done with generic recommendations? Get friend-powered discovery. Free to start.
4. One tap to rate. Zero reviews required. Your taste profile builds automatically.

---

### Tier 3: Social Connector

**Ad Group: recommendation-sharing**

**Keywords:**
- share restaurant recommendations
- recommendation app for friends
- best way to share restaurant list
- send food recs to friends
- social recommendation app
- friends restaurant picks
- share my favorite places
- group restaurant recommendations
- friend recommendation sharing
- taste profile app

**Responsive Search Ad 1:**

Headlines:
1. Send Your Profile, Not Texts
2. Your Recs, Always Ready
3. Friends Ask You for Recs?
4. Stop Typing the Same List
5. Share Your Taste in One Link
6. Invite 3 Friends, Get Pro Free
7. Friend-Powered Discovery
8. Your Network's Best Picks
9. Beyond Group Chat Recs
10. Rate Once. Share Forever.
11. One Tap. No Reviews.
12. Free Taste Profile
13. Network Discovery App
14. Your Social Life, Ranked
15. See Friends' Top Spots

Descriptions:
1. Your friends always ask for recs? Now you just send them your profile. One link, done.
2. Build a taste profile from one-tap ratings. Friends see your picks. You see theirs. Free.
3. Network-powered discovery from the people you trust. Not strangers. Not algorithms.
4. Invite 3 friends and get your first month of Pro free. The app grows with your network.

---

### Tier 4: Taste Curator

**Ad Group: experience-ranking**

**Keywords:**
- rate restaurants app
- experience tracker app
- personal ranking app
- beli alternative
- rank experiences app
- taste profile app
- rate and rank activities
- experience journal app simple
- track restaurants visited
- rate bars and restaurants

**Responsive Search Ad 1:**

Headlines:
1. Your Taste. Ranked & Searchable
2. Rate Anything. One Tap.
3. Your 8/10 Thai Place? Saved.
4. A System for Your Taste
5. Beli, But for Everything
6. Living Taste Profile
7. Beyond Google Maps Saves
8. Rate Now or Add Later
9. Searchable. Sortable. Yours.
10. No Reviews. Just Ratings.
11. Free Taste Profile Forever
12. Taste Analytics in Pro
13. See Your Patterns
14. Experience Architects
15. $99/yr — Full Discovery

Descriptions:
1. Not a list. Not a journal. A living, ranked record of what you've done and what you thought.
2. One tap, one number. No review, no paragraph, no photo. Your taste profile builds itself.
3. See which neighborhoods you rate highest and how your taste compares to friends. Pro $99/yr.
4. Your taste already exists — scattered across apps and memory. Give it a system. Free.

---

## 7. Negative Keywords

Apply at campaign level to prevent wasted spend.

### Universal Negatives
- free food
- coupon
- discount code
- promo code
- cheap restaurants
- fast food
- delivery
- food delivery
- uber eats
- doordash
- grubhub
- reservation
- book a table
- opentable
- resy
- yelp login
- google maps download
- tripadvisor
- jobs
- hiring
- salary
- careers
- recipe
- how to cook
- how to make
- DIY

### Category-Specific Negatives
- review writing (we're not a review platform)
- blog
- wordpress
- social media management
- event planning software (we're not a planning tool)
- wedding
- corporate event
- catering
- food critic
- restaurant owner
- business listing

### Competitor Brand Negatives (monitor, don't block initially)
- beli app (consider bidding on this — direct positioning "Beli, but for everything")
- yelp
- google maps
- tripadvisor

---

## 8. Post-Launch Optimization Playbook

### Week 1: Learn
- Monitor CPA daily. Do not change bids.
- Review search terms report on day 3 and day 7. Add negatives aggressively.
- Confirm conversion tracking is firing correctly (check Firebase/Adjust events vs. Google Ads reported conversions).
- Note: Google's smart bidding needs ~50 conversions to optimize. Be patient.

### Week 2: Prune
- Pause any keyword with >$50 spend and 0 conversions.
- Add negative keywords from search terms report (expect 20–40 new negatives).
- Review ad copy performance: which headlines/descriptions have the highest CTR and conversion rate? Start identifying winners.
- Check device performance: if desktop CPA is 3×+ mobile, reduce desktop bids 50%.

### Week 3: Optimize
- If CPA is on target: increase daily budget 20%.
- If CPA is 1.5×+ target: review landing page bounce rate, check keyword-ad-LP alignment, tighten match types.
- Pin winning headlines in RSA position 1. Test new variations in positions 2–3.
- Review location performance. Pause any city with CPA 2×+ average.

### Week 4: Decide
- **If Tier 1 CPA < $15 for 2 consecutive weeks:** Unlock Tier 2 (FOMO Scroller). Keep Tier 1 running.
- **If Tier 1 CPA is $15–25:** Continue optimizing. Don't expand yet. Test new ad copy variations targeting city_explorer pain points more specifically.
- **If Tier 1 CPA > $25:** Pause, review landing page, review targeting. May need to test Search → LP flow vs. direct App campaign.

### Monthly Ongoing
- Search terms review: weekly (minimum)
- Ad copy rotation: test 2 new RSAs per ad group per month
- Audience signals: build remarketing lists from LP visitors who didn't install (retarget with social proof messaging)
- Segment unlock: follow the expansion ladder triggers
- LTV tracking: once Pro conversion data exists (month 2+), calculate LTV by segment. Adjust CPA targets to reflect actual revenue, not just installs.

### Quarterly
- Review segment performance across the full funnel: install → first rating → day 7 retention → Pro conversion
- Kill any segment where install-to-retention drops below 15%
- Consider expanding to Instagram/TikTok paid (especially for fomo_scroller and social_connector — these segments were primarily Instagram/TikTok referrers in the persona profiles)

---

## 9. Landing Page Notes (from Persona Feedback)

The study produced specific landing page recommendations that directly impact ad → conversion performance.

### Critical for Ad-to-LP Alignment

| Segment | What They Need to See on the LP | Study Evidence |
|---|---|---|
| City Explorer | Solo value from day one + "local trending" | Cold-start was #1 objection. "First it's your map" line resolved it. LP must lead with solo utility, not network dependency. |
| FOMO Scroller | Forward-looking discovery, not backward tracking | V1 had 75% resonance but 17% conversion because LP was backward-looking. The hero must say "discover what's next" — not just "record what you did." |
| Social Connector | What free includes + referral incentive | Conversion jumped 25pp when LP clarified "basic friend activity" in free and added the referral incentive. Both must be above the fold for this segment. |
| Taste Curator | Specific examples (8/10, 4/10) + taste analytics | Abstract descriptions don't convert this segment. "Your 8/10 Thai place" was load-bearing. They need to see what their profile would look like. |
| Journal Graveyard | Honesty about abandonment + one-tap simplicity | "Most apps die after a week. We know that." is the trust-builder. Without it, resonance dropped 25pp. Lead with honesty for retargeting this segment. |

### LP Optimization Priorities
1. **Mobile speed:** 80%+ of traffic will be mobile. Target <2s load time. Multiple personas noted "the page is long for mobile" — consider a shorter mobile variant for ad traffic.
2. **Screenshots/demo:** The #1 unresolved objection across all segments was "I need to see the interface." Adding 1–2 app screenshots to the LP would address this. Place them in the "How It Works" section.
3. **Social proof placement:** The Chicago testimonial ("moved 2 months ago, friends' ratings better than any best-of list") should be visible without scrolling for city_explorer traffic. The three-month testimonial is critical for journal_graveyard retargeting.
4. **Segment-specific LP variants:** Consider creating 2–3 LP variants that lead with different hero messaging by segment. Route ad groups to the matching variant. This alone could improve ad-to-LP conversion 10–20%.

### Recommended LP Variants

| Variant | Hero | Routed From |
|---|---|---|
| **A: Discovery** | "Discover what's next through the people you trust." | FOMO Scroller, City Explorer ad groups |
| **B: Taste System** | "Your taste deserves a system." | Taste Curator ad groups |
| **C: Rec Sharing** | "Your friends ask for recs? Send them your profile." | Social Connector ad groups |

---

## 10. Budget Summary & Projections

### Conservative Scenario (Tier 1 only, month 1)
- **Budget:** $1,500/month
- **Est. CPA:** $8–15 (city_explorer has high intent)
- **Est. installs:** 100–190
- **Est. first ratings (50% activation):** 50–95
- **Est. Pro conversions at 10% (month 2):** 5–10
- **Est. Pro revenue (month 2):** $50–100/month or $500–1,000 annual

### Full Scale Scenario (all tiers, month 6+)
- **Budget:** $6,000–9,500/month
- **Est. CPA blended:** $10–18
- **Est. installs:** 350–950/month
- **Est. Pro conversions at 8%:** 28–76/month
- **Est. Pro revenue:** $280–760/month recurring

**Break-even:** With $99/year Pro pricing and 8% conversion-to-Pro rate, you need ~60–95 installs/month per $1,000 ad spend to break even within 12 months, depending on blended CPA. The city_explorer and fomo_scroller segments are most likely to hit this threshold first.

---

## Appendix: Segment Prioritization Matrix

| Segment | Conv | DB | Search Intent | Cold Traffic Viability | Priority |
|---|---|---|---|---|---|
| City Explorer | 89% | 8% | High (actively searching) | ✅ Strong | **#1** |
| FOMO Scroller | 81% | 8% | High (browsing "things to do") | ✅ Strong | **#2** |
| Social Connector | 72% | 0% | Medium (niche queries) | ⚠️ Better via social/referral | **#3** |
| Taste Curator | 64% | 0% | Medium (specific app searches) | ⚠️ Needs product experience | **#4** |
| Journal Graveyard | 56% | 17% | Low (stopped searching) | ❌ Retarget only | **#5 (retarget)** |