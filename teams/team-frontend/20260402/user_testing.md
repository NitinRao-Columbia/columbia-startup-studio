# Freeweight User Testing

## Session Overview

We ran 4 user testing sessions with athletes unfamiliar with the product. Sessions were conducted by having users attempt to onboard and complete a workout without assistance.

---

## What We Observed

The most consistent point of confusion was around the coach connection flow. Several users, unsure of what to do after signing up, navigated to the workout section and began generating or building their own workout plan before entering a coach invite code. When they later entered the code and received their coach-assigned program, they had two plans sitting in their calendar with no clear indication of which one to follow or how the two related to each other. This created visible confusion and in one case a user assumed the app had glitched.

Secondary observations:
- Users were not sure what the invite code field was for or where to find the code. The label was not descriptive enough to communicate that this was how they connected to their coach.
- The home screen did not clearly differentiate between a self-created workout and a coach-assigned one, which compounded the duplicate plan problem.
- One user skipped onboarding steps entirely by tapping past them quickly and then could not figure out how to go back and enter their max lifts, which meant weight auto-calculation was not working for them during their first session.

---

## What We Are Changing

1. **Gate self-programming behind coach connection.** If a user has not yet entered a coach invite code, prompt them to do so before allowing them to create their own workout. If they explicitly indicate they do not have a coach, allow self-programming but make that a deliberate choice rather than a default fallback.

2. **Differentiate coach-assigned and self-programmed workouts visually.** Add a clear label on the calendar and workout cards indicating whether a workout came from a coach or was self-created, so users with both types never wonder which is which.

3. **Make the invite code step more legible.** Rewrite the label and helper text so it is immediately clear that this is how the athlete connects to their coach and receives their program. Add a sub-label: "Get this from your coach."

4. **Make max entry skippable but surfaced again.** Allow users to skip max entry during onboarding but surface a persistent prompt on the home screen until they complete it, with a clear explanation of why it matters for weight calculation.

---

## Why

The duplicate plan issue is a direct product trust problem. If an athlete sees two workouts and does not know which one is theirs, they lose confidence in the app before they have completed a single session. The fix is structural: the product should not allow a state where that confusion is possible. Every other observation pointed to the same root cause — onboarding is moving users into the product before they have the context they need to use it correctly.