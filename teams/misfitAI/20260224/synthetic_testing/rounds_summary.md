# Synthetic User Testing — Rounds Summary (V1–V6)

**Product:** Wardrobe Planner (outfit autopilot: calendar + weather + your closet → daily outfit suggestions)  
**Rounds:** 6 (V1–V4 on original 5-bucket audience; V5–V6 on ICP audience)

---

## V1

**Copy:** `v1/v1_copy.md`  
**Audience:** 60 personas, 5 buckets (Presenter Paul, Design Student Dana, Socialite Sophia, Resident Rachel, Vibe Coder Victor).

**What happened:**
- Resonance 13%, intent 12%, conversion confidence 0%, dealbreakers **60%** (36/60).
- Best fit: Vibe Coder Victor (33% intent) and Presenter Paul (25% intent). Dana and Sophia were near-total mismatches (0% intent, 83% and 75% dealbreakers).
- Themes: Social proof (“Early tester”) was dismissed as fake; price was hidden and felt evasive; “a few quick questions” for Step 2 was not trusted; “what if my wardrobe is bad?” was unanswered.

**What we changed for V2:**
- Showed $1.99/mo in hero and FAQ. Reframed problem beyond “morning decision fatigue” to include safe outfits + second-guessing. Added FAQ “What if my wardrobe doesn’t work together?” Rewrote Step 2 with specific inputs (go-to pieces, avoid list, vibe). Replaced “Early tester” with named testimonials. Removed “friend who checked your calendar” line.

---

## V2

**Copy:** `v2/v2_copy.md`  
**Audience:** Same 5 buckets.

**What happened:**
- Resonance **23%** (+10pp), intent **7%** (-5pp), dealbreakers **67%** (+7pp). Price visible → 11 “good_deal”; clarity 60/60.
- Problem framing improved but intent dropped: personas recognized their problem more and trusted the solution less. Testimonials (Priya K., Rachel, Tara) were still called fabricated; some Victor personas noted testimonials were all women.

**What we changed for V3:**
- Removed testimonials entirely and added a “What It Looks Like” section with concrete sample output (two outfit options + why + accept/swap/hide). Moved the top-cited line (“closet full of pieces… never know what goes together”) into the problem section. Added “Why it’s $1.99” line. Added optional closet-scan to Step 2 and a calendar-privacy FAQ.

---

## V3

**Copy:** `v3/v3_copy.md`  
**Audience:** Same 5 buckets.

**What happened:**
- Resonance 23% (flat), intent **12%** (+5pp), dealbreakers **33%** (-12pp). Price “good_deal” 40/60.
- Victor and Rachel improved: Victor 33% intent and 0% dealbreakers; Rachel 17% intent and 8% dealbreakers. Paul stayed high resonance but 0% intent (sample output felt too casual for exec stakes). Dana and Sophia remained poor fit.

**What we changed for V4:**
- V4 copy was effectively the same as V3; we ran another round to confirm stability before refocusing the audience.

---

## V4

**Copy:** `v4/v4_copy.md`  
**Audience:** Same 5 buckets.

**What happened:**
- Resonance 23%, intent 12%, conversion confidence 0%, dealbreakers 35%. No meaningful shift from V3.
- Confirmed: Victor and Rachel are the real ICP; Dana and Sophia are product mismatches (style identity / event-dressing, not decision reduction).

**What we changed for V5:**
- Refocused the test on the ICP. Created a new brief and new audience (audience_v2.json) with five buckets: Vibe Coder Victor, Resident Rachel, Recently Promoted Priya, Hybrid Office Owen, Light-Touch Styler Sam. Dropped Paul, Dana, Sophia. V5 copy was the same as V4; only the audience changed.

---

## V5

**Copy:** `v5/v5_copy.md`  
**Audience:** 60 personas from **audience_v2.json** (ICP: Victor, Rachel, Priya, Owen, Sam).

**What happened:**
- Resonance **32%**, intent **20%**, conversion confidence 0%, dealbreakers **7%** (4/60). Clarity 60/60, price mostly “good_deal.”
- By bucket: Victor 25% resonance, 25% intent, 0% dealbreakers; Rachel 33% resonance, 17% intent, 17% dealbreakers; Owen, Sam, Priya in the mix with low or zero dealbreakers. Hitting the brief’s stopping criteria (intent ≥ 20%, Victor + Rachel dealbreakers ≤ 10%).

**What we changed for V6:**
- Set up V6 with the same copy as V5 to run an additional round and capture more qualitative signal; no major copy changes.

---

## V6

**Copy:** `v6/v6_copy.md`  
**Audience:** Same ICP (audience_v2.json).

**What happened:**
- Resonance **43%** (+11pp), intent **32%** (+12pp), conversion confidence 0%, dealbreakers **2%** (1/60).
- Victor: 50% resonance, 44% intent, 0% dealbreakers. Rachel: 53% resonance, 33% intent, 7% dealbreakers. Priya dealbreakers dropped to 0%. Strongest overall round on resonance and intent; conversion confidence remains the main gap (personas like the product but aren’t yet confident it will work for their real closet / context).

**Winning version:** V6 is the final copy for submission. Next step is to take this version to real users or to iterate further on conversion-confidence (e.g. stronger “proof it works” or dress-code handling).

---

## File reference (this folder)

| Version | Copy | Results | Charts | Other |
|--------|------|---------|--------|-------|
| V1 | v1/v1_copy.md | v1/results_v1.json | v1/charts_v1.html | v1/summary_v1.md |
| V2 | v2/v2_copy.md | v2/results_v2.json | v2/charts_v2.html | v2/summary_v2.md, v2/v1_changes.md |
| V3 | v3/v3_copy.md | v3/results_v3.json | v3/charts_v3.html | v3/summary_v3.md, v3/v2_changes.md |
| V4 | v4/v4_copy.md | v4/results_v4.json | v4/charts_v4.html | v4/summary_v4.md, v4/v3_changes.md |
| V5 | v5/v5_copy.md | v5/results_v5.json | v5/charts_v5.html | v5/summary_v5.md, v5/v4_changes.md |
| V6 | v6/v6_copy.md | v6/results_v6.json | v6/charts_v6.html | v6/summary_v6.md, v6/v5_changes.md |
