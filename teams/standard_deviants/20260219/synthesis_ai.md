# Interview Synthesis (AI-Generated)

**Date:** 2026-02-19
**Interviews analyzed:** 7 unique participants across 11 files (transcripts + snapshots)
**Interviewers:** Anuraag (ap4533), ma4254, Thomas (trk2121), Mike

---

## Signal Summary

| Participant | Role | Interviewer | Signal | WTP | Referral |
|-------------|------|-------------|--------|-----|----------|
| Senior thesis student | Undergrad, learning theory research, 225 participants | Anuraag | **GREEN** | $10/mo, immediate | Yes — senior seminar next day |
| PhD sociologist | 2nd-year, Columbia, medicalization/networks research | Thomas | **GREEN** | Already pays for LLMs | Forgot to ask |
| Liz | Consultant, Scimitar Consulting, qualitative research | Mike | **YELLOW-GREEN** | Not asked | Not asked |
| Research Director | S.T.O.P. nonprofit, surveillance oversight | Thomas | **YELLOW** | Blocked by privacy policy | Forgot to ask |
| Jannatul | CIS senior, Baruch College, data analytics | ma4254 | **YELLOW** | No — won't pay out of pocket | No |
| Jaren | 2nd-year EE student, Canada | ma4254 | **YELLOW** | Conditional | No |
| John | Former CFO, Clarity Software Solutions | Mike | **N/A** | Advisory only | N/A |

**Result: 2 GREEN, 1 YELLOW-GREEN, 3 YELLOW, 1 advisory (N/A), 0 RED.**

---

## The Core Pattern

Across every interview where the problem was confirmed, the same condition appeared: **people who have data and questions but lack the skills to get from one to the other.** They are not data people. They are domain experts — in learning theory, sociology, public health advocacy, consulting — who run into data analysis as a necessary but dreaded part of their real work.

The pain is chronic, not catastrophic. Nobody's workflow is failing spectacularly. Instead, it's a steady grind of:

1. **Tool fragmentation** — 4-6 disconnected tools duct-taped together (Excel, Word, R, ChatGPT, email, Google Drive)
2. **The AI-assisted-but-uncontrollable loop** — generating code with ChatGPT, getting errors, pasting errors back in, waiting, not understanding what went wrong
3. **Statistical reasoning they find unintuitive** — not impossible, just effortful and uncertain
4. **Organization overhead** — file naming, version control, pipeline management eating into the actual work

Nobody described a single catastrophic failure. They described friction that has become so normal they barely notice it anymore — until asked directly.

---

## What the GREEN Signals Have in Common

The two strongest signals (thesis student, PhD sociologist) share a specific profile:

- **Deeply invested in their questions** — they care about the substance, not the methodology
- **Semi-technical** — capable enough to attempt analysis, not fluent enough to own it
- **Using AI as a crutch** — ChatGPT/Claude for code generation, but stuck when it breaks
- **Already spending money** — $10-20/month on AI subscriptions
- **Would outsource if they could** — the thesis student's therapist asked: "Why are you doing your own analysis? When I did my PhD, I just hired someone."

The YELLOW signals either lacked sufficient experience (Jannatul), worked in a domain too niche for a horizontal tool (Jaren), or had adjacent but different problems (Research Director — privacy-constrained document collaboration, not data analysis).

---

## Top Quotes

### Pain

| Quote | Who | Context |
|-------|-----|---------|
| "If I could change anything, it would be have someone else do my data analysis." | Thesis student | Describing what they'd change about their research process |
| "I do not have the capacity to figure it out myself, just to copy and paste it again to GPT to just correct the error for me." | PhD sociologist | Describing the AI-assisted debugging loop |
| "Truly, I'm literally just brute forcing this." | Thesis student | On their current analysis approach |
| "I literally had to meet four different professors." | Thesis student | Trying to figure out which statistical test to use |
| "It was awful. It was awful." | Research Director | Sending the wrong version of a paper to her Executive Director |
| "I had to use Google Sheets once and I wanted to die." | Jannatul | On tool preference (extreme loyalty to Excel) |
| "Word will freeze up when we have too many track changes and so we end up accepting track changes and losing the record." | Research Director | Version control breaking down in Word |

### Desire

| Quote | Who | Context |
|-------|-----|---------|
| "Oh my gosh, wait, there's a correlate button. Oh, I love that." | Thesis student | Reacting to the product demo |
| "I'm using Spearman's rank for mine. This is so great." | Thesis student | Seeing the analysis tool match their actual needs |
| "More visualizations, please." | Thesis student | Key feature request — visualization is how they evaluate their own work |
| "A smart structured excel sheet to adapt to the assignments needs." | Jaren | What he wishes existed |

### Insight

| Quote | Who | Context |
|-------|-----|---------|
| "I am also doing work that was unthinkable for me now in the AI era." | PhD sociologist | AI widens ambition but not capability |
| "The biggest risk is that within the process you give up thinking about the questions yourself, you outsource to AI." | PhD sociologist | The downside of AI dependence |
| "I don't have the energy to think about [new tools] right now. It's a risk." | Research Director | Inertia as a barrier — not disinterest, exhaustion |
| "Companies assemble tool stacks, not single solutions." | John (CFO) | Strategic framing of how organizations actually buy software |
| "Pick a niche and go deep." | John (CFO) | Advice against building an all-in-one platform |

---

## Patterns Across Interviews

### 1. AI creates a new kind of frustration

Every participant who does analysis uses AI — ChatGPT, Claude, or both. But AI doesn't solve the problem; it shifts it. Instead of "I can't do this analysis," the frustration becomes "I can't control this analysis." The thesis student brute-forces code with Claude. The PhD sociologist pastes R errors into ChatGPT in a loop. Neither can debug what the AI produces. AI has widened the gap between what's imaginable and what's executable.

### 2. Visualization is epistemological, not decorative

The thesis student could not tell their K-means clustering was meaningless until they saw the visualization. They described themselves as a visual learner, but the implication is broader: for this audience, visualization isn't a reporting feature — it's the primary way they evaluate whether their analysis makes sense. "It wasn't until I got to the visual stage that I was like, oh, this is starting to mean something."

### 3. Excel is the universal fallback — and the universal complaint

Every single participant uses Excel or Google Sheets. Nobody loves it for analysis, but everybody defaults to it. Jannatul's extreme loyalty ("I'd break the law to get it") is the outlier, but the pattern is consistent: Excel is the known quantity, the thing that "won't throw curveballs" even when it's inadequate.

### 4. Inertia is the real competitor

The Research Director articulated this most clearly: "Word is not great, but I know how it's going to malfunction." Switching tools has a real cost — learning curves, workflow disruption, the risk that the new thing doesn't work. Any replacement has to be categorically better, not marginally better.

### 5. People who work alone suffer most

The PhD sociologist: "As a qualitative researcher, it's a lonely journey." The thesis student consulted four professors because they had no one else to ask. The people with the deepest pain tend to work in isolation — no team to distribute the analysis burden, no colleague to debug with.

### 6. Price sensitivity is extreme at the individual level

Jannatul would "break the law" for Excel but won't pay $10/month for anything out of pocket. The thesis student benchmarked against Claude at $10/month and said yes immediately. The split is clear: individuals resist paying, but people who already pay for AI subscriptions have crossed the mental threshold for tool spending.

---

## Surprises

1. **The therapist anecdote.** The thesis student's therapist casually asked why they were doing their own data analysis — "When I did my PhD, I just hired someone." An existing market for analysis-as-a-service exists.

2. **AI dependency as a moral concern.** The PhD sociologist explicitly worried about outsourcing thinking to AI: "the biggest risk is that you give up thinking about the questions yourself." This isn't just a usability problem — it's an intellectual integrity concern that shapes how these users approach tools.

3. **Privacy as a total blocker.** The Research Director cannot use most SaaS tools due to the nature of surveillance-related research. This creates a severe collaboration bottleneck and echoes John's strategic insight about "customer-understanding tools that work on regulated data."

4. **The engineering student doesn't fit.** Jaren's wish list — combining all niche engineering simulation software — is a fundamentally different product category. This confirms the target should be people working with qualitative/mixed-methods data, not all people who analyze data.

5. **The referral loop is real.** The thesis student offered to pitch the product in their senior seminar the next morning, unprompted. Academic departments are tight networks — one enthusiastic user in a methods class could seed organic growth.

6. **LLM-era plagiarism.** The Research Director flagged a genuinely new problem: interns using LLMs that don't cite properly, creating inadvertent plagiarism that's extremely hard to detect. Tangential to the product but relevant to the broader AI-in-research landscape.

---

## Contradictions

- **Jannatul says AI does "half of it" but also says she doesn't have enough experience to identify pain points.** She may be describing aspiration, not reality.
- **The PhD sociologist calls AI "unthinkable" (in a positive sense) but also describes it as the "biggest risk."** The same tool that enables new methods also threatens intellectual independence.
- **The Research Director acknowledges severe version control problems but says "I don't have the energy to think about new tools."** The pain is real but the activation energy to switch is higher.

---

## What We Still Don't Know

1. **Does the product need qualitative coding from day one?** The GREEN signals both do qualitative work, but their sharpest pain was quantitative analysis. Is guided stats the wedge, or will users expect coding features before they take the product seriously?
2. **Where is the willingness-to-pay threshold?** $10/month works for the thesis student (benchmarked against Claude). But Jannatul won't pay anything. Is freemium necessary to get adoption, with conversion on power features?
3. **Do team-based users exist in meaningful numbers?** The strongest signals came from solo workers. The Research Director manages a team but has adjacent problems. Is collaboration a must-have or a later feature?
4. **What happens after the thesis?** The thesis student graduates. The PhD sociologist finishes the dissertation. Is this a tool people use for 1-2 years and churn, or does it follow them into careers?
5. **Thomas forgot to ask about referrals in both interviews.** Two GREEN/YELLOW participants were never asked. That signal is missing.
