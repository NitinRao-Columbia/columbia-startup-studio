# V4 Evaluation Results

**Version:** V4
**Personas evaluated:** 60
**Schema:** Full (13 fields)
**Prompt:** Canonical evaluation prompt with anti-sycophancy bias

---

## Changes from V3

- **NEW section: "Bring Your People"** — Full section with invite link, "when your friends join, their circles show up for you automatically," and "The more people you know on Circle, the more plans happen without effort."
  **Why:** V3's #1 remaining objection from group_chat_prisoner: "Will my friends be on it?" The invite section gives them a concrete action and addresses adoption fear.

- **CTA addition:** "Already on the waitlist? Share your invite link and bring your friends."
  **Why:** Encourages viral sharing from the CTA, which is the most common landing page endpoint.

- **"Invite your group chat"** added to the "Have friends?" track.
  **Why:** Directly targets group_chat_prisoner pain by turning the existing coordination channel into an onboarding funnel.

- **Shortened safety section** to bullet points, trimmed from V3's expanded version.
  **Why:** V3 feedback suggested the page was getting long. Safety needs to be present but not dominant.

- **Copy consistency fix:** "Then go live your life" instead of "Then go" to match V3's more natural tone.

---

## Overall Scores

| Metric | V4 | V3 | V2 | V1 | V4 vs V3 |
|--------|----|----|----|----|----------|
| **Resonance** | **33%** | 53% | 57% | 47% | **-20pp** |
| **Intent** | **25%** | 52% | 27% | 25% | **-27pp** |
| **Conversion** | **17%** | 32% | 17% | 15% | **-15pp** |
| **Dealbreakers** | **18%** (11) | 12% (7) | 13% (8) | 22% (13) | **+6pp** |

**V4 is a regression.** All metrics dropped from V3. The "Bring Your People" section was the primary cause — a polarizing addition that helped group_chat_prisoner's adoption concern but alienated new_to_campus, solo_adventurer, and staying_in_defaulter personas who don't have established friend networks.

This confirms best-practices.md's warning: structural changes produce smaller (or negative) shifts compared to framing changes. V3's framing changes produced +15pp conversion; V4's structural addition produced -15pp.

---

## Scores by Bucket

| Bucket | Resonance (V4/V3) | Intent (V4/V3) | Conversion (V4/V3) | Dealbreakers (V4/V3) |
|--------|-------------------|----------------|--------------------|-----------------------|
| staying_in_defaulter | 33% / 58% (-25) | 33% / 58% (-25) | 8% / 50% (**-42**) | 8% / 8% |
| new_to_campus | 25% / 50% (-25) | 25% / 42% (-17) | 8% / 25% (-17) | 0% / 0% |
| app_fatigued | 0% / 8% (-8) | 0% / 8% (-8) | 0% / 0% | 67% / 50% (+17) |
| group_chat_prisoner | 58% / 75% (-17) | 25% / 75% (-50) | 25% / 25% (=) | 8% / 0% (+8) |
| solo_adventurer | 50% / 75% (-25) | 42% / 75% (-33) | **42%** / 58% (-16) | 8% / 0% (+8) |

**Biggest losers:** staying_in_defaulter conversion collapsed -42pp (from 50% to 8%). The "Bring Your People" section assumes social capital these personas don't have — they want to go out but don't have a group chat to invite.

**Group_chat_prisoner stayed flat on conversion** (25%) despite the invite section being designed for them. Their objection evolved: "I'd send the invite link and get ignored, like everything else in the group chat."

**Solo_adventurer held up best** at 42% conversion (-16pp), demonstrating that V3's framing continues to work for this bucket even with the V4 additions.

---

## Clarity Accuracy

| Score | V4 | V3 | V2 | V1 |
|-------|----|----|----|----|
| Nailed it | 17 (28%) | 16 (27%) | 37 (62%) | 25 (42%) |
| Partial | 43 (72%) | 44 (73%) | 22 (37%) | 35 (58%) |
| Wrong | 0 | 0 | 1 | 0 |

Clarity is stable. The product concept is well-understood regardless of copy version.

---

## Top Qualitative Themes

### 1. "Bring Your People" was the most polarizing section across all versions
It directly solved group_chat_prisoner's adoption fear but created three new problems:
- **Contradicted "You don't need to know anyone"** — Personas 21 (Fatima), 49 (Priya), 52 (Freya) flagged this as the copy saying two opposite things.
- **Signaled "this is for people with friends"** — Solo and new personas felt the section made them secondary users.
- **Triggered growth-hacking suspicion in app_fatigued** — Personas 25 (Hannah), 29 (Jade), 32 (Mateo) read the invite link as a referral engine, not a feature.

### 2. Copy consistency problem: "feed" vs "No feed"
Person 35 (Amara, app_fatigued MBA) caught that V4 uses "their circles show up in your feed automatically" in the Bring Your People section while claiming "No feed" elsewhere. A meaningful inconsistency.

### 3. Staying_in_defaulter collapsed because V4 assumed social capital
The "Bring Your People" framing works for people who HAVE a group chat to invite. Staying_in_defaulter personas DON'T — their problem is that their social connections atrophied. "Invite your group chat" is irrelevant if your group chats are dead.

### 4. Group_chat_prisoner objection evolved from "will they join?" to "they won't respond to my invite either"
The invite link addresses the abstract adoption concern but introduces a concrete new one: these personas have already experienced being ignored in group chats. Sending an invite link into the same group chat feels like more of the same.

---

## Strongest Lines (V4)

| Line | Count |
|------|-------|
| "Last Friday, You Almost Went Out." | 6x |
| "Everyone there chose to be there. That's the whole icebreaker." | 5x |
| "Invite your group chat — when they join, their plans show up for you automatically." | 5x |
| "You don't need to know anyone." | 4x |

The invite line was a top-5 strongest line AND the most-criticized section — a clear indicator of polarization.

---

## Dealbreaker Analysis (11/60 = 18%)

| Bucket | V4 | V3 | V2 | V1 |
|--------|----|----|----|----|
| app_fatigued | 8 | 6 | 6 | 8 |
| group_chat_prisoner | 1 | 0 | 0 | 0 |
| solo_adventurer | 1 | 0 | 2 | 3 |
| staying_in_defaulter | 1 | 1 | 0 | 1 |
| new_to_campus | 0 | 0 | 0 | 1 |

App_fatigued dealbreakers rose back to 8 (from 6 in V3). The invite link specifically triggered 3 new dealbreakers in this bucket (growth-hacking suspicion). One new group_chat_prisoner dealbreaker: Leah (44) who found peace in muted silence.

---

## Recommendations for V5

1. **Revert "Bring Your People" from a full section to a lightweight mention.** Keep the invite concept but demote it to a single line within the CTA: "Know someone who'd use this? Share your invite link." Don't make it a section header. Don't say "Circle works best when your friends are on it" — this directly contradicts the solo track.

2. **Return to V3's emotional framing balance.** V3 had the best resonance-to-conversion funnel. V5 should use V3's core structure with V4's best elements (invite link in CTA) while removing V4's worst (dedicated section, "works best with friends").

3. **Fix the "feed" inconsistency.** Remove any use of the word "feed" from the copy. It contradicts the core "no feed" promise.

4. **Strengthen the solo track.** Give the "New, solo, or starting over" path equal visual weight and don't undermine it with friend-dependent messaging elsewhere.

5. **Add a small proof element for group_chat_prisoner.** Instead of "invite your group chat," try: "Last week, one group chat of 8 friends discovered 12 plans they would have missed." Specific > generic.
