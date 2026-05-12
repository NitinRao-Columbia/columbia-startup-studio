# weekly_update_2026-04-14.md

## What we built last week
Coach program builder is live. Coaches can now create workouts with exercises, sets, reps, and percentage of max, and assign them to individual athletes or to a group. We also shipped the group and subgroup structure — coaches can create a group (e.g. Men's Rowing) and subgroups within it (e.g. Hypertrophy, Strength, Mobility) and assign different programs to each. This came directly from coach feedback — our first pilot coach manages three rowing teams each with athletes on different training plans, and the flat group structure we had originally was not going to work for him.

## What we're building this week
Athlete workout execution flow. Athletes can see their assigned program in the calendar but cannot actually execute it in the app yet. That is the next thing to ship — stepping through a workout set by set, with weights auto-calculated from their recorded maxes.

## Current user count
Signups: 48
Active users: 6

## Biggest blocker
Max entry. Several athletes skipped it during onboarding which means auto-calculation is not working for them. Adding a persistent prompt on the home screen this week.