# Test Brief: Experience Architects Landing Page

**Test name:** `experience_architects_lp`
**Date created:** February 23, 2026
**Asset type:** Landing page (built from scratch)
**Primary CTA:** Dual — join waitlist + app store download

---

## 1. What We're Testing

A new landing page for Experience Architects, a taste-based experience journal app. No existing copy — we're writing V1 from scratch and iterating through synthetic user evaluation.

**Goal:** Find the messaging, framing, and structure that converts social, active people into signups/downloads.

---

## 2. Traffic Sources

| Source | Mindset | Referrer tag |
|---|---|---|
| Instagram / TikTok ads | Curious but uncommitted; short attention span; saw a 5-15s hook | `instagram_ad`, `tiktok_ad` |
| Word of mouth / friend referral | Arrives with built-in trust; someone they know vouched for this | `word_of_mouth` |

Audience should reflect both referrer types in roughly equal proportions.

---

## 3. Persona Buckets

**5 buckets × 12 personas = 60 total**

| Bucket | Description | Typical quote | Skepticism |
|---|---|---|---|
| `taste_curator` | Already tracks restaurants/bars/trips mentally or in Notes app. Wants a system for what they already do. Has looked for this before and nothing fit. | "I have a list in my Notes app but it's a mess and I can never find anything when someone asks me for a rec." | Moderate |
| `social_connector` | The friend everyone asks "where should we go?" Motivated by being a better recommender. Won't use anything that takes time. | "People always ask me for recs and I just go off memory. Half the time I forget the good ones." | Low |
| `journal_graveyard` | Has tried journaling apps, review apps, spreadsheets — all abandoned within weeks. High skepticism that this will be different. | "I've downloaded like five apps for this. Used each one for a week. They're all sitting there with 3 entries." | High |
| `fomo_scroller` | Sees friends doing cool stuff on Instagram, feels like their own social life is scattered and forgettable. Emotionally motivated but skeptical of apps that promise to fix lifestyle problems. | "Everyone's always doing something cool and I can't even remember what I did last weekend." | Moderate |
| `city_explorer` | Recently moved or actively exploring a new city. Goes to meetups, tries neighborhoods solo, says yes to invitations from near-strangers. Overwhelmed by options and wants to remember what's actually good vs. what was just new. | "I've tried so many places since I moved but I couldn't tell you which ones were actually worth going back to." | Moderate |

**Demographics:**
- Age: 18–40, with ~60-65% in the 18–30 range
- Gender: Balanced mix
- Names: Generated via Faker, not LLM-invented

---

## 4. Product Description (for clarity scoring)

> Experience Architects is an app that helps social, active people remember and rank their real-world experiences — restaurants, trips, bars, activities — turning them into a living taste profile. It uses your friends' activity and ratings to help you discover better plans, so you skip the mediocre stuff and recommend confidently.

**Core claim (`nailed_it` must capture):** It's a personal experience ranking system that uses your friends' network to help you discover and choose better things to do.

---

## 5. Pricing

**Model:** Freemium

| Tier | What's included | Price |
|---|---|---|
| Free | Basic tracking, solo ranking, personal taste profile | $0 |
| Paid | Full network discovery, advanced taste analytics, unlimited history, full features | $7–18/month (range under test) |

**Pricing psychology note:** Low end ($6-7) targets impulse accessibility. High end (~$18) plays on aspirational "feel 18" positioning. Synthetic personas will test perception across this range.

---

## 6. Copy Skeleton

1. **Hero** — Headline + subhead + dual CTA (waitlist + app store)
2. **Problem** — Your social life is scattered, forgettable, full of mediocre picks
3. **Solution** — One-tap rating → living taste profile
4. **Network discovery** — Your friends' activity helps you choose better
5. **How it works** — 3-step visual (rate → build profile → discover)
6. **Social proof** — Testimonials, user quotes, or early traction numbers
7. **Pricing** — Free vs. paid comparison
8. **Final CTA** — Closing push + download/signup

---

## 7. Evaluation Schema

**Using: Full schema (V1-V5) + 1 custom field**

```json
{
  "person_id": "<number from profile>",
  "bucket": "<bucket from profile>",
  "resonance": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "clarity_response": "<describe in one sentence what this product does>",
  "intent": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "conversion_confidence": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "price_perception": "<too_expensive|fair|good_deal>",
  "network_believability": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "strongest_line": "<single line from the copy that resonated most>",
  "what_feels_off": "<anything generic, try-hard, or dishonest-feeling>",
  "objections": "<what's stopping you from signing up>",
  "dealbreaker": "<true|false>",
  "dealbreaker_reason": "<why, or null if dealbreaker is false>",
  "gut_reaction": "<1-2 sentences, first impression>",
  "unanswered_questions": "<what the page didn't answer>",
  "price_reaction": "<specific thoughts on pricing tiers>"
}
```

**Custom field:**
- `network_believability`: "Do you believe this app's friend-based recommendations would actually be better than what you already do?" — Tests whether the network discovery promise lands or feels like empty marketing.

---

## 8. Stopping Criteria

| Condition | Threshold |
|---|---|
| Minimum rounds | 5 |
| Conversion target | >50% agree+ on `conversion_confidence` |
| Max iterations | 10 |
| Convergence | <3pp movement across 2 consecutive rounds |
| Pivot trigger | Bucket shows 0% conversion across 3+ versions with high dealbreakers → swap bucket |

---

## 9. Canonical Language Reference

From brand position doc:

**Use:** "Beli for experiences," "your taste profile," "your social life, ranked," "less mediocre, more you," "a resume of what you've done," "network-powered discovery"

**Avoid:** social planning, event calendar, reviews, luxury/exclusive

**Tone:** Tasteful not hype. Specific not generic. Social not spammy. Effortless not demanding.

---

## 10. File Naming Conventions

| File | Purpose |
|---|---|
| `01_brief_experience_architects.md` | This brief |
| `audience_v1.json` | Persona profiles (60 people) |
| `copy_v1.md` | Landing page copy, version 1 |
| `copy_v1_changes.md` | Changelog for V1 decisions |
| `results_v1.json` | Raw evaluation results |
| `narrative_v1.json` | Researcher interpretation |
| `clarity_v1.json` | Clarity scoring results |
