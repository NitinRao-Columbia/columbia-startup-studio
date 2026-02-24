# Part A
---
# Research Synthesis

## Key Patterns Across Interviews
- Video repository of athletes' lifts, either shared w/ coach or private
- Accompanying photos/videos with programmed workouts
- Calendar/time tracking, way to track progress and strength over time
- Taper Mode
- Injury Mode
- Once in workout mode, interface should be super simple, super easy, and super quick to respond. Drag and drop, big buttons, etc.

## Top 5 Quotes
1. "Make Lifts Social"
2. "Want to click as FEW BUTTONS as possible"
3. Put a workout on "auto" – assumes you're lifting set reps, etc. and all you have to do is tap once to go through steps
4. "Make it up as I go/no structure"
5. "I want a way to communicate my current injuries with my coach/plan that doesn't require going through other sources."

## Contradictions and What They Might Mean
- Some users want more freedom to choose how they lift and have a say in the training plan that they are following, but others just want to turn their brains off and follow whatever plan is given
  - This signals that we are trying to build for more than 1 group of users
- For the same issue, "the training plan doesn't adapt to what I'm feeling," there were 2 sets of responses, one of which was a passive "Oh well i guess i'll just put half-effort in because I don't think it'll matter" and another which was that users were frustrated and going off to program their own training.
  - This ties back to the previous issue which solidifies that there are 2 groups of users, the more strength-focused athletes and those that see strength training as something they have to do, and not an area that they can use to improve their overall performance
- Want to potentially give athletes ways to add/subtract on the fly, even if there is a set plan

## Surprises — What Changed Your Thinking
- We were surprised to see that there was a desire for a social aspect
- Users want a super simple UI ("as few buttons as possible")
- Users don't necessarily want to interact with their plan themselves, some want to follow whatever the coach says

## Overall Read on the Data
- We need to build this app for those 2 different groups of athletes, and not let one group overpower the other in terms of feature selection
- Communication between athletes and coaches is key, training plans break down when the coach isn't aware of what the athlete is feeling and the athlete doesn't understand what the coach is prescribing
- Showing people how to do their assigned exercises in a seamless way is important, most people's current plans make it very difficult to learn how to do a movement

# Part B

# Strength Programming Research Synthesis
**Context:** Collegiate team strength environments across rowing, track & field, and triathlon

---

## 1. Program Delivery Methods

There is no standardized delivery method across athletes. Even within the same team environment, athletes experience programming through entirely different mediums:

- Shared Google Sheets (2)
- PDF (3)
- Training apps — TeamBuildr, TrainingPeaks, TrainHeroic, WHOOP (3)
- Verbal / in-person instruction (2)
- Self-programming / make it up (2)
- Paper printouts with pencil logging (DT, Texas Rowing)

**Emotional signals:** Athletes using apps feel more structured and "taken care of." Athletes on PDFs or Google Sheets feel moderate clarity but carry more responsibility themselves. Athletes told verbally what to do feel dependent on the coach's presence. Self-programmers express autonomy but likely inconsistency. Paper-based athletes lose data entirely.

---

## 2. Clarity of Workouts

Overall clarity is rated relatively high — most athletes know what exercises they're supposed to do. However, clarity does not equal optimization. Several athletes rated clarity high but expressed frustration elsewhere, signaling: *"I know what I'm supposed to do, but that doesn't mean it's ideal."*

Key friction points around clarity:
- Having to click external video links in spreadsheets to understand how to perform a movement
- Inconsistent exercise naming across weeks or coaches — when terminology shifts, cognitive load increases and uncertainty follows
- Paper programs (DT) provide zero historical reference once lost

---

## 3. Percentage & Max Tracking: A Broken System

This is one of the clearest and most consistent pain points across the dataset.

**When maxes improve, here's what happens:**
- 3 athletes calculate percentages themselves
- 2 have their coach manually adjust
- 1 receives automatic updates
- 6 have no idea

Half of the athletes don't know what happens when their max improves. This signals a lack of transparency, a lack of system feedback, and in many cases, maxes that simply aren't being actively tracked.

**Frequency of self-calculation:**
- Every workout: 1
- Occasionally: 5
- Never: 6

The "never" group is not receiving weights seamlessly — they've simply abandoned the percentage system entirely and are going off perceived effort. The "occasionally" group reveals normalized low-grade friction: mental math has become an accepted part of the workflow.

One athlete said explicitly: *"Having to calculate my own weights"* is the most frustrating part of their training.

25% of athletes reported being unsure what weight to use due to outdated percentages. In a high-performance environment, that's significant. People have quietly given up on precision because the system makes it too hard.

---

## 4. The Silent Modification Problem

One of the most important and underreported findings in this dataset: **athletes regularly modify their programming without telling their coach.**

If a lift feels off, if someone's lower back is stressed, if progression doesn't make sense, or if they don't understand why something is programmed — a lot of athletes won't say anything. They'll just tweak it.

This shows up as:
- Dropping the weight slightly without saying anything
- Skipping accessories they don't see value in
- Swapping in a lift they prefer
- Adding extra sets because it "didn't feel like enough"
- Going heavier than prescribed because they "felt good"

From the athlete's perspective, this feels like optimizing. But the result is a broken feedback loop:
- The coach thinks the athlete is following the plan
- The athlete thinks they're improving the plan
- Neither knows what the other is thinking

Over time this means slower progression, unexpected fatigue, injury risk from drifting volume or intensity, and no clean data on what's actually working.

This usually stems from one of two things: the athlete doesn't feel strongly enough to bring it up, or they're not fully bought into the logic of the program. **If athletes understand why something is programmed and trust that it's built around them, they're far more likely to follow it closely and speak up when something feels wrong.**

---

## 5. Frustration Themes

**Manual Calculation Burden**
Persistent, low-grade friction that accumulates over time. Athletes are running quick calculations mid-session, keeping maxes in their Notes app, saving screenshots of previous weeks, or maintaining private Google Sheets as shadow systems. If the official system were seamless, none of this redundant tracking would be necessary.

**Lack of Injury Foundation**
*"Not based on injury prevention as a foundation"* — concern about stress on the lower back came up unprompted. This is deeper than UI/UX. Athletes are thinking about longevity. There is a trust gap between program structure and injury prevention philosophy. DT (Texas Rowing) and others referenced making quiet modifications based on how their body felt, without communicating this to their coach.

**Inconsistency**
*"Lack of consistency"* — exercise names changing week to week, confusion when terminology shifts. System fragmentation creates unnecessary cognitive overhead.

**Tech Limitations**
*"Not being able to send reps to watch"* — athletes want feedback loops. There's an implicit desire for deeper integration: video, wearables, rep tracking.

---

## 6. Individual Athlete Profiles

**Noa Klein — Columbia Women's Rowing**
Self-motivated lifter who uses TrainHeroic (originally from her high school coach's account) to manually track team workouts on her own. She's proactively solved the problem the team system doesn't address. Wants video integration for form review, a timer, and a social layer — specifically called out Strava as a model. Wants lifts to feel social.

**DT — Texas Rowing**
Paper printouts, pencil, no phones allowed during training. Programs get lost. She uses a Garmin but never uses its lifting features — too cumbersome mid-session. Falls back to a Notes app for personal tracking. Doesn't see lifting as central to her sport, so her current system is "good enough" — but acknowledged that more serious lifters would outgrow it quickly. **Signal: low-friction, minimal input matters more than sophisticated tracking for some athletes.**

**RC — Columbia Track & Field**
Coach-driven programming with limited personalization around race schedules. The critical pain point: a new lift introduced right before a race caused unexpected soreness and hurt performance. Not every athlete competes every week, but strength loads aren't always adjusted accordingly. **Signal: personalization around competition schedule and taper management is a real unmet need.**

**NV — Stanford Triathlon**
Uses WHOOP Strength Trainer but finds it too general and manual. Her current workflow: ask ChatGPT for a workout → manually input to WHOOP → manually log every weight. Stopped using the feature because it wasn't tailored to her and required too much setup. For endurance athletes, lifting is secondary and friction tolerance is extremely low. **Signal: if it requires manual setup + manual logging + manual adjustments, drop-off risk is high.**

---

## 7. How Athletes Relate to Strength Training

A clear split emerged across interviews and the survey:

**Group 1 — The Optimization-Oriented Athlete**
Thinks about progression constantly. Wants to know if their numbers are moving. Expects the program to reflect a new PR. Gets frustrated when they have to do their own math or when it's unclear if their updated max is being used. Wants precision, responsiveness, and control.

**Group 2 — The Trust-and-Follow Athlete**
Shows up, reads what's written, lifts. Not concerned about whether percentages are perfectly dialed in. If the coach says "this is the plan," they follow it. Doesn't get particularly excited about automation or dynamic adjustments. Values simplicity and consistency.

What stood out is that neither group is wrong — they just engage differently. Any system we build has to serve both without letting one overpower the other. The risk: build something too technical and you lose Group 2. Build something too simple and Group 1 will work around it.

---

## 8. Inferred Workarounds & Behavioral Adaptations

Athletes have built a parallel ecosystem of compensating behaviors because the official systems don't fully serve them:

**Shadow Tracking Systems** — Notes apps, phone calculators, private Google Sheets, mental "working weights." If the system were seamless, none of this would exist.

**Rounding & Approximation** — Athletes use last week's weight rather than recalculating. Small percentage increases get ignored. Prescribed precision drifts into estimated effort. Athletes don't see this as a problem, but it weakens program efficacy over time.

**Avoiding Max Updates** — Half of athletes don't know what happens when maxes improve. Many likely delay testing, underreport improvements, or continue training off old numbers to avoid the administrative friction of recalculating. This resistance doesn't show up as a complaint — it just quietly stalls progression.

**Self-Modification for Injury or Comfort** — Athletes quietly reduce weight, modify reps, skip accessories, substitute exercises. They don't tell their coach. The coach can't adapt the plan. The feedback loop breaks.

**Social Calibration** — In team environments, when clarity is low, athletes ask teammates what weight they're using. Peer comparison becomes a proxy for system clarity. This also creates social pressure to lift heavier than prescribed, leading to technical breakdown and elevated injury risk. Athletes were less likely to take deload weeks because of how it looked.

**Supplementing With External Apps** — Wearables (Apple Watch, Garmin), recovery apps, nutrition tracking. Athletes care about performance data. Strength programming just isn't integrated into that ecosystem yet.

**Lowered Expectations** — Athletes who've never experienced seamless dynamic programming don't expect it. They don't identify its absence as a pain point. Lack of demand doesn't equal lack of opportunity — it reflects normalization of inefficiency.

---

## 9. Emotional Synthesis

The dominant emotional tone across the dataset is **mild friction and passive inefficiency**. No one described their current system as elegant, seamless, or exciting. The consistent undercurrent was: *"It works fine… but it could be smoother."*

Friction accumulates in small ways:
- Calculating percentages occasionally
- Not knowing if the program adjusts after a PR
- Inconsistent naming and terminology
- Injury concerns not clearly addressed
- No integrated feedback loop
- Data that exists but isn't structured or usable

None of these individually feel like crises. Together, they represent a system that asks athletes to do a lot of low-value administrative work that quietly erodes trust in and engagement with their programming.

---

## 10. Key Opportunities

**1. Automated Percentage Handling**
The single most consistent technical pain point. Even moderate annoyance here is highly leverageable. If athletes never have to calculate their own working weights, one of the biggest sources of friction disappears.

**2. Transparent Max Update Logic**
Athletes don't know what happens when they hit a PR. Visibility into how the program responds to new maxes builds trust and closes the feedback loop between athlete and program.

**3. Injury-Aware Programming Layer**
Framing lifts as performance + longevity, not just load. Giving athletes a clear, low-friction way to communicate physical status (injury, soreness, fatigue) to their coach without going through separate channels.

**4. Coach-Athlete Communication Built Into the Workflow**
The silent modification problem is a communication problem. If athletes had an easy, non-confrontational way to flag concerns, ask questions, or log deviations, the feedback loop that currently breaks down silently would stay intact.

**5. Competition-Aware Taper & Load Management**
Especially relevant in multi-sport team environments. Not every athlete competes every week. Strength loads should reflect that. Individualized modulation within a team structure is an unmet need.

**6. Consistency of Language & Movement Education**
Standardized exercise naming. Integrated video or visual demos that don't require clicking out to YouTube mid-session. Reducing the cognitive load of understanding what's actually being asked.

**7. Feedback Loop Integration**
Video for form review (Noa's explicit request), wearable data, rep tracking. Athletes are already investing in performance data — strength programming is simply lagging behind the rest of their ecosystem.

---

## 11. Strategic Implication

Athletes have already built shadow systems, normalized manual calculations, avoided updating maxes, socially calibrated weights, and quietly modified their plans. The opportunity is not simply automation.

It is: **reducing cognitive load, increasing trust, and centralizing progression logic into something seamless enough that workarounds disappear.**

The goal is not more features. It is eliminating the need for behavioral compensation.

The two user groups — optimization-oriented athletes and trust-and-follow athletes — are both real and both valid. Any design that ignores one will fail the other. The interface must be powerful enough for athletes who want precision, and simple enough that athletes who just want to lift never have to think about it.

---
# Part C

The AI missed out on a lot of the emotional aspect of the interviews (of course), so we had to go in and emphasize when people were getting frustrated, and when people were feeling indifferent about their issues, and notably when people just seemed tired out by the friction of their current training plan delivery system. The thing that the AI picked up on that was helpful was the general themes that were occurring across interviews by different people. Issues that cropped up across Jackie's Interviewees and Andrea's, and Mine/Arin's Interviewees were given emphasis which we hadn't thought to look at up to that point. 

I trust the AI when it brings up issues that I have seen and picked upon from the interviews and reading the notes, but when it brings up an issue that I don't remember seeing (such as the percentages not being exact enough), I have to quickly go through to make sure no one actually brought it up. These hallucinations are infrequent, but happen enough to hurt our trust in the LLM.
