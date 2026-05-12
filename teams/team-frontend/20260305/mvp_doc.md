# Freeweight MVP Document

## Overview

Freeweight is a strength training app that eliminates the spreadsheet, the mental math, and the communication gap between athlete and coach. The MVP targets strength coaches and athletes at the collegiate level, starting with Columbia Athletics.

There are two user types: **Athlete** and **Coach**. The core value proposition is simple: coaches program once, athletes execute with zero manual calculation, and coaches get real-time visibility into completions and flags.

---

## User Types

### Athlete
Program. Execute. Log. Progress.
- Join via coach's invite link
- See today's workout on the calendar
- Walk through session step-by-step
- Log weights, reps, RPE, and notes
- Track strength progress over time
- Flag injuries directly on workout log
- Self-program if no coach assigned

### Coach
Program. Monitor. Adapt.
- Build workouts with sets, reps, and % of max
- Assign to individuals, groups, or subgroups
- Embed video demos and notes per exercise
- Send invite links to athletes
- See who completed workouts today
- Monitor athlete flags and injury notes
- View completion rate and strength progress

---

## Onboarding

### Shared Flow
1. **Download and open app** — available on iOS, Android, and web. Athletes primarily use mobile in the gym; coaches may prefer web for program building.
2. **Select user type** — first screen after signup: choose between Athlete or Coach. This determines the onboarding path and app experience.

### Athlete Path
- Name and profile photo
- Sport and team
- Training goals / focus area
- Current maxes (squat, deadlift, bench, etc.)
- Enter coach invite code to connect to coach (coach generates this from their dashboard)
- If no coach: option to self-program

### Coach Path
- Name and profile photo
- Sport and institution
- Create one or more **Groups** (e.g. Men's Rowing, Women's Rowing)
- Within each group, create **Subgroups** (e.g. Hypertrophy, Strength, Mobility)
- Generate invite link/code to share with athletes

---

## Coach-Athlete Connection

Coaches generate a unique invite code or link from their dashboard. Athletes enter this code during onboarding or from their settings. Once connected, the athlete appears on the coach's roster and can be assigned to a group and subgroup.

---

## Athlete Experience

### Home / Calendar
- Default view is the calendar with today's workout prominently displayed
- Upcoming sessions visible by date
- Rest days explicitly marked
- One tap to open today's workout

### Workout Execution
- Exercises displayed one at a time or in a scrollable list
- Each exercise shows:
  - Exercise name
  - Sets and reps
  - Weight auto-calculated from athlete's recorded max (e.g. 80% of squat max)
  - Embedded video demo if coach has attached one
  - Coach notes per exercise
- Athlete logs each set: weight used, reps completed, RPE (1–10), optional notes
- Modifications can be made mid-workout (swap exercise, adjust weight, skip set) — all logged and visible to coach
- Injury flag can be added directly on the workout log without leaving the flow

### Post-Workout
- Session marked complete
- App may prompt athlete to update a max if a relevant lift was included
- Maxes can be updated by athlete manually, by coach on athlete's behalf, or via app prompt

### Progress View
- Per-lift max charts over time
- Workout completion rate

### Self-Programming
- Athletes without a coach, or those adding sessions alongside programmed work, can build their own workouts and schedule them on the calendar

---

## Coach Experience

### Dashboard
- Who has completed today's workout
- Athletes with active injury flags or notes
- Upcoming sessions scheduled this week

### Roster — Groups and Subgroups
- Coach creates Groups (e.g. Men's Rowing)
- Within each group, creates Subgroups (e.g. Hypertrophy, Strength, Mobility)
- Athletes are assigned to a group and optionally a subgroup
- Workouts can be assigned to individuals, entire groups, or specific subgroups

### Program Building
Each exercise in a session includes:
- Exercise name
- Sets and reps
- Percentage of max (app auto-calculates weight per athlete from their recorded max)
- Embedded video demo (optional)
- Coach notes per exercise

Workouts are scheduled on specific dates and assigned to an individual, group, or subgroup. Rest days are explicitly marked. Coaches can program as far in advance as they wish.

### Athlete Monitoring
- View any athlete's completed workout logs
- See modifications made mid-session
- View injury flags and notes
- Track completion rate and strength progress per athlete

---

## Key Technical Notes

- Weight auto-calculation is the core technical feature: coach inputs % of max, app fetches athlete's current max for that lift and displays calculated weight
- Invite code system for coach-athlete connection
- Coach-optimized for web; athlete-optimized for mobile
- Video embeds per exercise in program builder
- Modification logging must be lightweight and not interrupt workout flow

---

## Out of Scope for MVP
- In-app messaging between coach and athlete
- Nutrition tracking
- Integration with wearables
- Payment / subscription management
- Public profiles or social features