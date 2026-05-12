# V2 Evaluation Summary — Wardrobe Planner
**Date:** 20260224 · **Round:** V2 · **n=60** · **Copy:** v2_copy.md · **Δ from V1**

---

## Top-Line Metrics

| Dimension | V1 | V2 | Delta |
|---|---|---|---|
| Resonance | 13% | **23%** | +10pp |
| Intent | 12% | **7%** | -5pp |
| Conversion Confidence | 0% | **0%** | 0pp |
| Dealbreakers | 60% (36/60) | **67% (40/60)** | +7pp |
| Price: good_deal | 0 | **11** | +11 |
| Clarity: nailed_it | 57/60 | **60/60** | +3 |

**The headline:** Resonance went up +10pp but intent went *down* -5pp. The gap between "this is my problem" and "I trust this will solve it" widened in V2. This is a trust gap, not a framing gap.

The V2 changes correctly identified the problem more broadly — and personas noticed. But the credibility signals (social proof, onboarding mechanism) still aren't convincing them to act.

---

## Per-Bucket Breakdown (V1 → V2)

| Bucket | Resonance | Intent | Conv | Dealbreakers |
|---|---|---|---|---|
| Presenter Paul | 25% → **50%** (+25) | 25% → **8%** (-17) | 0% | 42% → **58%** (+16) |
| Resident Rachel | 8% → **33%** (+25) | 0% → **8%** (+8) | 0% | 58% → **58%** (0) |
| Vibe Coder Victor | 25% → **25%** (0) | 33% → **17%** (-16) | 0% | 42% → **42%** (0) |
| Socialite Sophia | 8% → **8%** (0) | 0% → **0%** (0) | 0% | 75% → **83%** (+8) |
| Design Student Dana | 0% → **0%** (0) | 0% → **0%** (0) | 0% | 83% → **92%** (+9) |

**Key pattern — the resonance/intent inversion:** Presenter Paul gained +25pp resonance but lost -17pp intent. They recognize their problem in the copy more clearly than before — and then distrust the solution more, because the gap between "problem I relate to" and "product that can solve it" became visible. Same dynamic in Victor (-16pp intent). Better problem framing without stronger proof of mechanism = more skepticism, not less.

**Rachel is the only segment where V2 moves in the right direction on both dimensions.** +25 resonance, +8 intent. The "wardrobe coherence" framing and the added FAQ ("what if my wardrobe doesn't work?") reached them.

---

## Clarity Accuracy

**100% nailed it (60/60).** Up from 57/60 in V1. The copy is completely clear about what the product does. Clarity is no longer a useful diagnostic — the remaining work is all trust and fit.

---

## Strongest Lines by Frequency (V2)

| Line | Mentions |
|---|---|
| *"My closet is full of pieces I like, but I never know what actually goes together."* (social proof) | **27x** |
| *"Does this look intentional, or just… random?"* | 9x |
| *"A casual Friday and a noon client lunch get different recommendations."* | 6x |
| *"A clear outfit for a client meeting at 2pm and drinks at 7pm, matched to the 42° forecast…"* | 4x |
| *"You don't need more clothes. You need one clear outfit."* | 3x |
| *"You default to the same 'safe' outfit…"* | 3x |

The **social proof quote "My closet is full of pieces I like, but I never know what goes together"** became the single most-cited strongest line at 27x — more than any line in V1. Personas resonated with the *sentiment* of that line deeply. But they then flagged the quote as fabricated. **This line is working as a problem statement. It is failing as social proof.**

The structural implication: move this framing into the problem or solution section where it doesn't need to be attributed to a real person.

---

## Top Qualitative Themes

### 1. Social proof failed again — different names, same result
V1's "Early tester" → V2's "Priya K., Marketing Director" generated nearly identical trust response: ~45/60 personas called the quotes fabricated.

**Why the fix didn't work:** The problem was never the attribution, it was the quotes themselves. "Priya K., Marketing Director" saying "I'd pay for that" sounds as much like a product brief as "Early tester" did. Adding a job title made the demographic signal more visible — not more credible.

**New secondary damage:** The three quotes are all women (Priya, Rachel, Tara). Multiple male personas — specifically in Vibe Coder Victor — explicitly flagged this:

> *"The testimonials are all women — Priya, Rachel, Tara — which immediately makes me feel like this wasn't built for me. I'm a 40-year-old VP of Engineering."* — Victor #60

> *"The testimonials are all women, and I'm supposed to be the target user here? That's a weird miss."* — Victor #52

**The fix for V3:** Social proof cannot be fixed with better names or different roles. Either source real quotes from beta users, or replace the entire section with a different credibility mechanism (outcome data, week-1 results, or a concrete "what a suggestion looks like" mockup).

### 2. The resonance→intent gap: problem framing outran proof of mechanism
V2 got better at describing problems people recognize — and then left them with no new evidence that the product could actually solve those problems. The top objection in V2 (across nearly every segment) is:

> *"How does it know what I own if I only answer a few questions?"*

Naming the questions (go-to pieces, vibe, avoid list) was better than V1's vague "a few quick questions" — but it raised a new, sharper question: **"A 2-minute quiz tells you what's in my wardrobe?"** Personas are now more clearly aware of the gap between the setup input and the output promise.

> *"Step 2 says 'answer a few questions' but gives me zero confidence the output will actually be good."* — Victor #49

> *"I have no idea how this actually maps my wardrobe without photos. 'Answer a few questions' is vague to the point of being meaningless to me."* — Victor #50

> *"I've answered style quizzes before. They always give me generic stuff and I stop using the app in three days."* — Rachel #45

### 3. $1.99 is confirmed to be noticed — but creates a new trust problem
In V1, price was hidden and flagged as evasive. In V2, showing $1.99 fixed the evasion problem: 11 personas explicitly called it a "good deal" and price stopped being a barrier for most.

But a new secondary reaction emerged consistently: **"So cheap I trust it less."**

> *"$1.99 signals this is a hobby project, not a serious product."* — Paul #07

> *"$1.99/mo is basically nothing, which makes me question whether there's real intelligence behind this."* — Sophia #29

> *"It's priced like a utility. If it was actually good for someone who cares about fashion, it would cost more."* — Sophia #26

This is a real signal worth addressing in V3. Options: explain why it's priced low ("we're early, we want to earn trust before we earn revenue"), or reframe it as a deliberate positioning choice ("most style apps charge $20+; we charge $1.99 because outfit suggestions should be accessible, not a luxury").

### 4. The corporate framing still lands as too narrow
The examples (client meeting, client lunch, 42° forecast for a work commute) and the social proof (marketing director, UX designer, account executive) together signal: "this is for office workers."

- Vibe Coder Victor sees it as corporate and slightly off (they skew tech-casual, not corporate)
- Resident Rachel sees corporate examples as aspirational/aspirationally distant from their life
- Socialite Sophia sees it as built for "someone at Banana Republic" — not them

The broader problem statement in V2 ("you default to the same safe outfit") landed better. The specific examples undercut it.

### 5. Google Calendar privacy was flagged for the first time
Only one persona (Victor #58) explicitly raised it but the concern is important: "The Google Calendar integration is a privacy red flag they don't address at all. No mention of data handling, what they read, what they store." No FAQ addresses calendar data privacy. Worth adding one line in V3.

---

## Objection Analysis (V2)

| Objection | Segments | Frequency |
|---|---|---|
| "How does it know my wardrobe from a 2-min quiz?" | All | Very high |
| Social proof is fabricated | All | Very high |
| Corporate examples don't fit my life | Rachel, Sophia, Victor | High |
| Price signals low quality / hobby project | All | Medium-high |
| Product solves logistics, not style judgment | Dana, Sophia, Paul | High |
| Only women in testimonials | Victor | Medium (new) |
| No privacy explanation for Calendar access | Victor | Low (new) |

---

## Dealbreaker Analysis — 40/60 (67%)

Dealbreakers increased by 4 personas (36→40). The breakdown:

- **Dana:** 10→11 dealbreakers. V2 made the product's premise even clearer — which hardened rejection. Dana now sees exactly how far this is from what they need.
- **Sophia:** 9→10 dealbreakers. Same dynamic. Clearer corporate framing = faster rejection.
- **Paul:** 5→7 dealbreakers. Problem resonated more (+25pp) but solution trust fell — two personas who previously didn't dealbreak now did because they could articulate more precisely why the product wouldn't work for their specific variant.
- **Rachel:** 7→7 (unchanged). The wardrobe-gap FAQ addition held the line.
- **Victor:** 5→5 (unchanged). Resonance held; intent dropped but dealbreaker rate stayed flat.

---

## What V2 Fixed and What It Didn't

### Fixed
- Resonance: +10pp overall; +25pp each for Paul and Rachel
- Price: no longer hidden; 11 "good deal" reactions vs 0 in V1
- Clarity: 100% (up from 95%)
- Problem framing: "you default to safe outfits" / "does this look intentional?" resonates more broadly than the pure morning-rush frame
- Rachel's intent: moved from 0% to 8% — first non-zero showing for this segment

### Didn't fix
- Social proof: identical failure mode, different names
- Mechanism trust: naming the questions in Step 2 raised the bar but didn't meet it
- Intent: fell -5pp overall despite resonance climbing
- Conversion: still 0%
- Dana and Sophia: both worsened — fundamental mismatch that copy can't close

---

## Price Perception Summary

| | V1 | V2 |
|---|---|---|
| too_expensive | 1 | 0 |
| fair | 59 | 49 |
| good_deal | 0 | 11 |

Showing $1.99 shifted 11 personas from "fair" (neutral) to "good deal" (positive). The price evasion problem is solved. The new problem: the low price is interpreted as a quality signal. V3 should address this directly in the FAQ or a brief line near the price.

---

## Recommendations for V3

**1. Retire the social proof section — replace with outcome proof**
Three polished quotes from corporate women cannot be fixed by changing the names, the jobs, or the gender mix. The format reads as fabricated regardless of content. For V3:
- If you have real beta users: use raw, unpolished quotes with full names
- If you don't: replace social proof entirely with a "here's what a real suggestion looks like" mockup (a concrete day — "8am, rainy, client call + happy hour → here are your two options") or an early-access stat ("Used by 200+ people in beta. 78% accepted the first suggestion they got.")

**2. Move "My closet is full of pieces I like but I never know what goes together" into the problem section**
It was the most resonant line in the copy (27x) — as social proof, attributed to "Rachel, UX Designer." Stripped of attribution, it's a perfect problem statement that covers Paul, Rachel, and Victor simultaneously. It shouldn't need a person behind it to land.

**3. Answer the mechanism question — show, don't tell**
The single biggest remaining trust gap: "how does a 2-minute setup know my wardrobe?" Options:
- Show the first three actual questions with example answers
- Add a line like: "Tell us your go-to pieces, and we'll build from there. You can add more over time or show us what didn't work — the app gets sharper from how you actually use it, not just what you type in upfront."
- Or add a mini-mockup of what a Day 1 suggestion looks like for a real calendar event

**4. Explain the price**
Add one sentence near $1.99: *"Priced low because we're early — we'd rather earn trust than charge for potential."* This reframes cheap-as-humble rather than cheap-as-thin.

**5. Add one male testimonial for Vibe Coder Victor reach**
Victor (#52, #60) explicitly noticed all-women social proof. If you keep the quote format in V3, balance the attributions.

**6. Add one line on Google Calendar privacy**
Brief, in the FAQ or near Step 1: *"We read event names and times only. We don't access your invitees, notes, or anything outside of scheduling context."*

**7. Consider audience swap for V3: retire Dana, pilot a new segment**
Design Student Dana: 92% dealbreaker rate across two rounds. Fundamental product-problem mismatch. A replacement segment — "recently promoted professional" (someone who jumped from IC to manager/director and whose wardrobe hasn't caught up) — would be closer to the product's actual sweet spot and reduce the noise from an unsalvageable mismatch.

---

## What to Keep in V3

- "You default to the same safe outfit" problem framing — it's landing
- "Does this look intentional, or just… random?" — 9x resonance, keep it
- The three-step structure — clear and logical
- $1.99 price, visible, in hero and FAQ
- The wardrobe-gap FAQ ("what if my wardrobe doesn't work?") — helped Rachel
- The 42° specificity line — still working (4x strongest line)

---

*V2: resonance +10pp, intent -5pp. Wider resonance/intent gap = trust problem, not framing problem. V3 needs proof of outcome, not better problem description.*

*Next: write v3_copy.md + v2_changes.md, then run V3 evaluation.*
