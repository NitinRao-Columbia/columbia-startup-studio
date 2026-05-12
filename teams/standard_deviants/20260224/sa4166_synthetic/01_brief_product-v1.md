# Synthetic Test Brief — product-v1

- Date: 2026-02-24
- Test ID: 20260224.01_product-v1
- Phase: 1 (Brief Creation)

## 1) What we're testing

- Copy/messaging under test: landing page messaging for Product v1.
- Source location: `/Users/saanviaima/Documents/GitHub/standard_deviants/sa4166`.
- Primary artifact in scope: landing page sectioned copy (Hero, How It Works, Social Proof, Objection Handling, CTA + Pricing section).

## 2) Who's seeing this

- Arrival context for this round: **Ad click**.
- Evaluation context: first-touch users coming from paid channels with low prior trust and limited context.

## 3) Persona buckets

### Bucket 1: duct_tape_analyst
- Behavioral description: Relies on complex, fragile systems of manual "Band-Aid" fixes and fragmented files to get through meetings. Often the only person who understands the workflow, making execution high-risk and unwieldy.
- In-their-voice quote: "I’m the only person on earth who knows what to do just because I’ve done it. So the workflow sucks."
- Expected prevalence: 25%

### Bucket 2: ai_loop_prisoner
- Behavioral description: Uses AI to help with coding but frequently gets stuck in repetitive, non-functioning logic loops. Struggles with AI not actually "looking" at outputs to debug effectively.
- In-their-voice quote: "We found that it would get stuck in these loops... if we just looked at what it was outputting, we could figure out what was wrong and [the AI] wouldn't be able to do that."
- Expected prevalence: 20%

### Bucket 3: skeptical_quant_methodologist
- Behavioral description: Highly protective of methodological rigor and distrustful of black-box automation. Needs to see underlying code/math to defend results to stakeholders.
- In-their-voice quote: "I’d be very nervous about telling [my bosses] that I just let AI handle it 'cause they'd be like, 'Why did you do it that way?'"
- Expected prevalence: 15%

### Bucket 4: social_science_thesis_dreader
- Behavioral description: From non-technical backgrounds; sees spreadsheets/data management as intimidating and accessible only to technical specialists. Prefers human-centric workflows and worries technical tooling may conflict with social-focused mission.
- In-their-voice quote: "The concept of Excel is just scary to them... they think you have to be a CS or stats major to work with."
- Expected prevalence: 15%

### Bucket 5: budget_gatekeeper
- Behavioral description: Focused on organizational effectiveness while operating with scattered spreadsheets and manual calculations. Will pay for tools that normalize and streamline tedious work if adoption burden is reasonable.
- In-their-voice quote: "I can only assume they don’t have a streamlined system because I think they would have told us... guidance was basically about doing manual calculations."
- Expected prevalence: 10%

### Bucket 6: ai_weary_old_school_analyst
- Behavioral description: Values manual process for learning data and methods (R/MATLAB). Believes AI lacks intuition for exploratory work and is less trustworthy for unstudied problems.
- In-their-voice quote: "I wrote it all up by myself because I wanted to learn R... I’m not sure I’d trust [AI] for [exploration]."
- Expected prevalence: 15%

## 4) Product description (for clarity scoring)

A unified data workspace that turns scattered spreadsheets and legacy code into a visual, indestructible timeline of logic. It maps your data health instantly and provides a transparent paper trail for every change, so results remain defensible and reproducible.

## 5) Pricing

Include pricing reaction testing in this round.

- Individual Researcher — $29/month (monthly)
- Lab / Small Team — $149/month (monthly)
- Institutional — $2,500/year (annual)

## 6) Copy skeleton

Use this structural flow for the tested copy:

1. Hero
2. How It Works
3. Social Proof
4. Objection Handling
5. Pricing
6. CTA

## 7) Evaluation criteria

Use standard schema from `references/evaluation-schemas.md` (including mandatory `clarity_response`), plus these test-specific additions:

- Transparency Trust: "On a scale of 1-5, how confident are you that you could explain the logic behind these results to a supervisor or PI?"
- Manual Friction Relief: "Does this copy clearly address the specific 'grunt work' (e.g., folder management, manual cleaning) that currently slows you down?"

## 8) Stopping criteria

Use default stopping criteria:

- Minimum 5 rounds
- Stop if conversion agree+ exceeds 50%
- Hard cap at 10 iterations
- Stop on convergence if no meaningful signal change

## Notes

- Additional constraints provided: none.
- Next step after approval: produce audience config + deterministic skeleton, then execute round workflow.
