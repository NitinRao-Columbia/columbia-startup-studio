# 20260219 — Product Brief, Brand Position & Synthetic User Testing

## What's in here

| File | Description |
|------|-------------|
| `product_brief.md` | One-page product brief — what we're building, who it's for, the core problem |
| `brand_position.md` | Internal brand positioning document — thesis, identity, canonical language |
| `synthetic_testing/` | 5 rounds of synthetic user testing on our V1 landing page copy |

## Synthetic Testing

We ran synthetic user testing using the [synthetic-user-testing skill](https://github.com/kenxle/columbia-startup-studio/tree/main/synthetic-user-testing) against landing page copy built from 10 real user interviews.

**Audience:** 60 AI-generated personas across 5 behavioral archetypes drawn from our interview data:

1. **Overwhelmed Planner** — decision fatigue, uses 3-6 platforms, "planning friend"
2. **Routine Breaker** — socially active but stuck in habit loops, wants novelty
3. **Quiet Explorer** — intentional, skeptical of hype, quality-over-quantity
4. **Culture Seeker** — wants ephemeral cultural events, frustrated by information asymmetry
5. **Budget-Conscious Socializer** — cost-aware, wants quality free/cheap activities

**Rounds:**

| Version | Copy file | Results | Key change |
|---------|-----------|---------|------------|
| V1 | `v1_copy.md` | `v1_results.md` | Initial copy from interviews |
| V2 | `v2_copy.md` | `v2_results.md` | Added example cards, elevated budget filter, algorithmic transparency line |
| V3 | `v3_copy.md` | `v3_results.md` | Reframed hero for routine breakers, added group planning mention |
| V4 | `v4_copy.md` | `v4_results.md` | Reworked social proof with beta-tester language, privacy line for quiet explorers |
| V5 | `v5_copy.md` | `v5_results.md` | Tightened CTA, added launch timeline, final polish |

### Extra files

`extra_files/v1/` through `extra_files/v5/` contain the full evaluation artifacts for each round: audience JSON, raw results JSON, charts (HTML), and detailed summaries. These aren't required but are included for reference.

```
extra_files/
├── v1/
│   ├── audience.json
│   ├── results_v1.json
│   ├── charts_v1.html
│   └── summary_v1.md
├── v2/
│   ├── copy_v2.md
│   ├── copy_v2_changes.md
│   ├── results_v2.json
│   ├── charts_v2.html
│   └── summary_v2.md
└── v5/
    └── ...
```

## Process

1. Drafted product brief and brand position using interview synthesis + LLM assistance, then edited for accuracy and voice
2. Wrote V1 landing page copy grounded in interview pain points and brand positioning
3. Generated 60 synthetic personas from interview archetypes (deterministic skeleton + qualitative enrichment)
4. Ran baseline evaluation against generic copy to calibrate the floor
5. Iterated V1 → V5 based on per-round feedback, tracking changes and rationale between versions

<br>
<br>

---

# Synthetic User Testing — Copy Changes by Round

NYC event app landing page. 5 rounds of synthetic testing across 60 personas (5 audience buckets × 12 personas each). Conversion went from 28% → 100% over four active iterations, with a fifth round confirming stability.

---

## Conversion arc

| Round | Conversion | Δ |
|-------|-----------|---|
| V1 (baseline) | 28% | — |
| V2 | 77% | +49pp |
| V3 | 97% | +20pp |
| V4 | 100% | +3pp |
| V5 | 100% | 0pp (stable) |

---

## V1 → V2 (+49pp conversion)

### Hero headline
**Before:** "Stop scrolling six apps just to figure out what to do this weekend."  
**After:** "Stop ending up at the same place again."  
**Why:** Routine_breakers (17% conversion in V1) consistently said "I don't search six apps — I just go where my friends go." The old headline assumed a research behavior that half the audience doesn't have. The new one targets the outcome — the same bar, every weekend — which lands for both researchers and non-researchers.

### Hero subheadline
**Before:** "You don't need more options. You need the right 3–5…"  
**After:** "You don't have a research problem. You have a 'nothing felt worth it' problem."  
**Why:** Routine_breaker signal: "The framing assumes my problem is too many options. My problem is too little motivation." This reframe names the felt experience without requiring the user to see themselves as someone who researches.

### Step 1 — solo-friendly callout
**Before:** Category list only.  
**After:** Added "Including quiet, solo-friendly, and low-key options."  
**Why:** Quiet_explorer's #1 dealbreaker across V1: "If the categories don't include quiet or solo activities, this isn't for me." One sentence, zero dealbreakers.

### Budget filter tiers
**Before:** "free only, under $20, or no limit"  
**After:** "free only, under $10, under $20, or no limit"  
**Why:** Budget_conscious_socializer signal across 4+ personas: "$5–$10 is my actual sweet spot. The jump from free to $20 is too big." The missing tier was a dealbreaker for this bucket.

### Example cards
**Before:** Single Kehinde Wiley card (Sean Kelly Gallery).  
**After:** Three-card shortlist: free art show / $15 jazz residency / free park walk.  
**Why:** Culture_seeker #1 objection: "Show me the actual shortlist experience — not one card." Three cards also proved catalog variety, price range, and outer-borough coverage (Washington Heights), which addressed a budget_conscious_socializer dealbreaker.

### Social proof stats
**Before:** "87% of people we interviewed" and "6 out of 10" claims.  
**After:** Removed entirely. Replaced with a plain summary sentence.  
**Why:** Flagged as the weakest element across all five buckets. "Stats feel made up — 50 people isn't a real stat." Removing them increased credibility.

### New objection handler: behavior-change skepticism
**Before:** Not addressed.  
**After:** "I'm skeptical an app changes behavior. I already know what's out there." + reframe as removal, not discovery.  
**Why:** Routine_breaker signal in 4/12 V1 responses: "I know what's out there — I just default to easy." None of the V1 copy addressed this. The reframe ("it's about removal, not discovery") targets the actual barrier.

### Objection: privacy / account
**Before:** No account language.  
**After:** Added "No account required to browse."  
**Why:** Quiet_explorer trust gap. Addressed the hesitation around commitment and data without restructuring the section.

### CTA
**Before:** "Join the waitlist"  
**After:** "Get early access"  
**Why:** Cross-bucket signal: "A waitlist with no timeline feels like it might never happen." "Get early access" implies active progress and a real product rather than indefinite waiting.

---

## V2 → V3 (+20pp conversion)

### Example cards — full replacement
**Before:** Kehinde Wiley / Nublu jazz / Fort Tryon park walk.  
**After:** "Stitched Futures" (Bronx textile show, emerging artists) / Taiwanese pop-up dinner ($12) / site-specific theater, Navy Yard ($10, "Not on Eventbrite").  
**Why:** Culture_seeker and quiet_explorer converged on the same critique: "These examples aren't proof of discovery — they're curated versions of things I could find myself." Kehinde Wiley is well-known. Nublu is on every jazz list. The park walk was called out as "not really curated — parks are free by default." The replacements are: genuinely obscure (emerging Bronx artists not in major galleries), a food pop-up with real scarcity (sells out Wednesday), and site-specific theater that isn't on Eventbrite.

### New section: "How We Decide What's Worth Your Time"
**Before:** No explanation of curation methodology.  
**After:** Full section explaining sourcing (gallery mailing lists, community boards, organizer networks), quality bar (credibility review, "would we go ourselves"), and personalization mechanism (skip/save signals, not social graph).  
**Why:** The single most consistent quiet_explorer objection across V2: "We filter for quality" is a promise, not a feature. Adrienne Cole (UX researcher): "What does quality mean? Who defines it?" The section is written in plain factual language, not marketing copy — which is what high-skepticism personas need to trust, not just want.

### CTA — free tier introduced
**Before:** No mention of app pricing.  
**After:** Added "Free to get started. No account required to browse your first shortlist."  
**Why:** 10 of 12 budget_conscious_socializer personas asked "Is the app free?" as their #1 unanswered question in V2. Jasmine Wright: "If the app costs money, I can't use it." One sentence, zero remaining pricing questions.

### CTA button
**Before:** "Get early access →"  
**After:** "Get your first shortlist →"  
**Why:** "Early access" frames a wait. "Get your first shortlist" implies immediate value. The new copy echoes the product's actual promise rather than its business status.

### 48-hour promise
**Before:** No delivery timeline.  
**After:** "We'll send your first shortlist within 48 hours."  
**Why:** Tara Patel (quiet_explorer): "I don't want to give my email to something that might not launch." Ben Shapiro-Stein: "The early access framing is slightly concerning." A concrete 48-hour commitment converts "is this real?" into "I can test this immediately."

### Step 3 — sharing callout
**Before:** No mention of sharing.  
**After:** Added "Share it with your group chat or keep it to yourself."  
**Why:** Group/sharing mentioned by 10+ personas across overwhelmed_planner and routine_breaker as an unanswered question. Gabrielle Moreau: "If I can't send this to my group chat, it loses half its value." One sentence acknowledges the use case without promising a feature that doesn't exist.

### Category list — expanded
**Before:** Standard category list.  
**After:** Added "photography shows, design talks."  
**Why:** Sofia Reyes (architect) and Priya Nair (photographer) both flagged their professional categories as invisible in V2. Niche creative categories signal depth of coverage to culture_seeker and quiet_explorer personas with developed specific interests.

### Objection: niche events
**Before:** "Yes, we'll have pop-ups and one-night-only things."  
**After:** Added "and the example cards above are typical, not cherry-picked."  
**Why:** Culture_seekers were enthusiastic but skeptical the examples were representative. "Typical, not cherry-picked" directly addresses the concern that the cards are marketing artifacts.

### "Actively building" language
**Before:** "We're actively building"  
**After:** "We're in early access"  
**Why:** "Actively building" signals an incomplete product. "Early access" signals a live product being expanded.

---

## V3 → V4 (+3pp conversion)

### "How We Decide" section — restructured
**Before:** 3 dense paragraphs (~200 words).  
**After:** 2-sentence lead + 3 scannable bullet points (~80 words).  
**Why:** 7 personas across overwhelmed_planner and routine_breaker flagged the section as page-flow friction — they were already sold by the example cards. Chloe Bernstein: "By the time I get to it, I've already decided." Natasha Ivanova: "The people who need it most (skeptics) are also most likely to be put off by a wall of explanation." The section was essential for quiet_explorers but was penalizing fast-converting segments. Bullets cut reading time by ~60% while preserving all the information.

### Editorial identity line
**Before:** Section opened with no attribution.  
**After:** Added "Curated by a small team of New Yorkers who use this product themselves." at the top of the section.  
**Why:** Raj Patel (quiet_explorer, last remaining neutral in V3): "The sourcing is credible but taste alignment remains unproven." Ben Shapiro-Stein: "I still worry this is a team of 2 people who can't scale this manually." This single sentence converts "I trust people, not apps" into "this is close enough to a trusted recommendation to try." Doesn't overclaim ("expert curators") or underclaim ("an algorithm").

### Example cards — geographically anchored
**Before:** Cards spanning Bronx / Crown Heights / Navy Yard (geographically scattered).  
**After:** All three cards in Brooklyn (Bushwick / Crown Heights / Red Hook) with explicit distances (1.2 mi, 2.1 mi).  
**Why:** 7+ personas flagged geographic scatter as a trust gap for the proximity filter. Elena Petrov: "Crown Heights isn't near Harlem. Does the distance filter actually work?" Jamal Carter: "The shortlist needs to be geographically coherent for a single user." David Kim: "A free event in the Bronx isn't useful if I'm in SoHo." Added the frame: "Everything here is within Brooklyn this weekend."

### Free tier language
**Before:** "Free to get started."  
**After:** "Free to use. Full shortlist, no features locked."  
**Why:** 3 budget_conscious_socializer personas (Leah Goldstein, Maya Chen, Isabel Torres) explicitly asked in V3: "Is the free tier full-featured or limited?" "Free to get started" implies a freemium ladder where quality features are paywalled. The new language removes all ambiguity.

### Sourcing — Instagram reference removed
**Before:** "artist Instagram accounts"  
**After:** "artist and organizer social accounts"  
**Why:** Marcus Thompson: "The sourcing section names Instagram — so they do use Instagram, just not your social profile. That distinction could be clearer." Removing the platform name avoids the confusion between monitoring Instagram for events (fine) and using your Instagram profile (not fine).

### CTA subtext
**Before:** "Tell us your neighborhood and we'll send your first shortlist within 48 hours."  
**After:** Added "no credit card" to CTA subtext.  
**Why:** "No credit card" reinforces the free-tier clarity and removes any residual friction for budget-conscious personas.

---

## V4 → V5 (0pp — stability confirmed)

**Purpose:** Minimum-5-round compliance. Copy had reached 100% conversion in V4. Goal was to confirm stability, test two small polish items, and verify the ceiling was real rather than lucky.

### Example card — daytime swap
**Before:** Taiwanese pop-up dinner (7:30pm Saturday, $12).  
**After:** Fermentation workshop + tasting, Prospect Park (Saturday 10am–1pm, free, labelled "Low-key, solo-friendly").  
**Why:** Morgan Reilly (routine_breaker) had flagged all-evening example cards across V3 and V4. Fatima Al-Hassan (routine_breaker) had noted solo-friendly events weren't shown in example cards. The swap addresses both with one card, and explicitly labels it "low-key, solo-friendly" — the first time this framing appeared on a card itself rather than just in the category list.

### Step 2 — time-of-day filter expanded
**Before:** "When are you free?"  
**After:** "When are you free — mornings, evenings, weekdays, or weekends?"  
**Why:** Amira Khalil (routine_breaker, irregular schedule) had asked in V2 whether the filter handled any day of the week. This had never been directly addressed across V3 or V4. One phrase made the filter's full scope explicit. Directly converted her from the V2 open question to "the first version that makes me feel like a primary use case."

**Result:** Zero metric movement. All five buckets held at 100% conversion V4→V5. The two changes produced positive qualitative signals with no tradeoffs, confirming both the stability of V4 and that the residual items were addressable without risk.

---

## What didn't change (and why)

Several things were flagged as missing across multiple rounds but were deliberately not addressed in copy, because they were product-level gaps, not copy-level ones:

- **Couple/date use case** — 4+ personas every round. Needs a filter or use-case card in the product, not a line of copy.
- **Film events** — Yara Nazari (culture_seeker) every round. Needs a category addition to the intake quiz.
- **Team identity depth** — Multiple quiet_explorers wanted a "meet the team" page or author credits. Needs a product page, not a landing page change.
- **Scarcity signal accuracy** — "6 remaining tickets" flagged as potentially manufactured (Jenna Liu, V3–V5). This is an implementation requirement: the signals must be accurate in the live product or they will erode the trust the copy built.

---
