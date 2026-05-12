# Product Brief

**Team Name:** Standard Deviants
**Date:** 2026-02-19

---

## The Problem

People who collect qualitative data — interviews, surveys, observations, open-ended responses — have questions about what it means but can't get to answers without skills they don't have. They're "brute forcing" analysis: consulting experts to find the right statistical test, pasting R errors into ChatGPT in a loop, and unable to tell whether their own analysis is meaningful until they happen to visualize it. The workflow spans 4-6 disconnected tools (Excel, Word, R, ChatGPT, email, Google Drive) and the friction is constant, compounding, and normalized.

- **Who has this problem?** Anyone whose real work involves understanding people — not crunching numbers. PhD students analyzing thesis data, nonprofit directors evaluating programs, UX designers synthesizing user interviews, consultants making sense of client feedback, public health teams tracking outcomes. Their expertise is the domain. The data is a means to their work, not the work itself.
- **How do they currently deal with it?** They duct-tape tools together: Excel for data storage, Word for codebooks, R or SPSS for statistics (reluctantly), ChatGPT for code generation and debugging, email for collaboration, and manual file-naming conventions for version control (`v2_final_FINAL.xlsx`).
- **How painful is it?** Chronic, not catastrophic. Two of seven interviewees gave GREEN signals (willing to pay, offered referrals). One participant said "If I could change anything, it would be have someone else do my data analysis." Another described being stuck in a loop: "I do not have the capacity to figure it out myself, just to copy and paste it again to GPT."

---

## The Solution

A web-based analysis platform that lets people go from raw data to understood results by clicking, not coding. Upload a messy CSV or interview transcripts, and the product guides you to the right analysis — choosing the appropriate statistical test, running it, visualizing it, and explaining what it means.

- **What does it do?** Upload, clean, analyze, and visualize qualitative and mixed-methods data in one place.
- **How does the user interact with it?** Point-and-click. "Is there a correlation?" becomes a button, not a script. The product selects the right method (Spearman vs. Pearson, chi-square vs. logistic regression) based on the data types.
- **What makes it different?** Existing tools assume you already know what test to run and how to code it. This assumes you have a question and data — and handles the methodological plumbing in between.

---

## Target User

- **Demographics:** 22-55, graduate students to mid-career professionals. University-based, nonprofit, consulting, or in-house UX/product teams. Limited personal budgets but some organizational or grant funding access.
- **Defining behavior:** They collect qualitative data as part of their real job — interviews, surveys, observations — but analysis is the part they dread. They attempt statistical or computational work using AI as a crutch, generating code with ChatGPT and pasting errors back in. They spend $10-20/month on AI subscriptions already. They would hire someone to do their analysis if they could afford it.
- **How they describe the problem:**
  - "I'm just not really a stats person." (AP4533)
  - "Truly, I'm literally just brute forcing this." (AP4533)
  - "I do not have the capacity to figure it out myself." (TRK2121-02)
  - "I rely too much on GPT." (TRK2121-02)
  - "Time-intensive, manual, dependent on researcher skill." (Liz)

---

## Why Now

AI has created a new category of frustrated user. People who work with qualitative data can now *envision* computational analysis that was unthinkable two years ago — network analysis, automated coding, pattern detection — but actually executing it means copy-pasting code they can't debug, waiting on machines they don't understand, and trusting outputs they can't verify. The gap between what's theoretically possible and what's practically controllable is widening, not closing. Meanwhile, the incumbent tools (NVivo at $500-1,000+, Atlas.ti, SPSS) remain desktop-bound, expensive, and designed for methodologists — not the growing population of people who need analysis but aren't analysts.

---

## Key Interview Evidence

- **Strongest quote:** "If I could change anything, it would be have someone else do my data analysis." (AP4533 — GREEN signal, willing to pay $10/month immediately, offered to recruit classmates next day)
- **Pattern:** Tool fragmentation and the AI-assisted-but-uncontrollable analysis loop appeared across 3+ interviews (AP4533, TRK2121-02, Liz). Every participant described spending more time fighting tools than generating insight.
- **Surprise:** AP4533's therapist casually mentioned that PhD students used to just hire someone to do their data analysis. An existing market for analysis-as-a-service exists — this product could partially automate that. Also: AP4533 couldn't tell their K-means clustering was meaningless until they *saw* the visualization. Visualization isn't decorative — it's how these users evaluate their own work.
- **Current spend/effort:** $10-20/month on AI subscriptions (Claude, ChatGPT). Campus or organization covers most tool costs. One participant said she would "break the law" to get Excel rather than pay out of pocket — price sensitivity is extreme at the individual level.

---

## Open Questions

1. Is guided analysis (click-to-correlate, auto-selected tests) enough of a wedge, or do users expect qualitative coding features from day one?
2. What's the right price? AP4533 benchmarked against Claude at $10/month, but MA4254-01 won't pay for anything out of pocket. Freemium vs. flat rate?
3. How do we handle the "it feels like a toy" risk? Canva overcame this, but credibility matters — will users trust a tool that abstracts away the methodology?

---

*This document feeds directly into the brand position and landing page copy.*
