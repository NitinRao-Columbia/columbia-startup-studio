# Synthetic User Testing Brief: Landing Page V1

**Test Name:** Landing Page Copy V1
**Date:** 2026-02-19
**Team:** Standard Deviants

---

## 1. What We're Testing

The full V1 landing page copy (`copy_v1.md`) — end-to-end evaluation of whether the messaging resonates with target users and drives free trial sign-ups.

**Governing question:** Would this person start a free trial after reading this landing page?

---

## 2. How People Arrive

Mixed channels across the persona pool to simulate realistic traffic:

- **Google search** (~30%) — searched for terms like "analyze interview data," "qualitative data analysis tool," "statistics without coding"
- **Word of mouth** (~30%) — classmate, colleague, or professor mentioned it
- **Social media ad** (~20%) — LinkedIn or Instagram targeted ad, cold traffic
- **Direct/organic** (~20%) — found through a blog post, tweet, or academic forum

Referrer is assigned per persona in the audience file.

---

## 3. Persona Buckets

5 buckets, 12 personas each = **60 total**.

### thesis_dreader
Grad students (MA/PhD) with data collected and analysis chapter looming. Currently brute-forcing with ChatGPT + R or Excel. High urgency, low stats confidence, tight personal budgets. They want someone else to do their analysis.

> "I've been staring at this spreadsheet for two weeks and I still don't know if my results mean anything."

**Expected prevalence:** Primary target. These are the early adopters and word-of-mouth drivers.

### duct_tape_analyst
Mid-career professionals — nonprofit directors, consultants, program evaluators, UX researchers — who've normalized a 4-6 tool workflow (Excel → Word → R/SPSS → ChatGPT → email → Google Drive). Pain is chronic but tolerable. Switching cost and inertia are the real barriers.

> "I know my process is inefficient, but I don't have the energy to learn something new right now."

**Expected prevalence:** Large addressable segment. Harder to convert but higher lifetime value.

### ai_loop_prisoner
People actively using ChatGPT or Claude to generate and debug analysis code, stuck in the paste-error-paste cycle. They've tasted what AI can do but can't make it reliably work. They know the gap between "theoretically possible" and "practically controllable."

> "I paste the error back into ChatGPT and it gives me new code that creates a different error."

**Expected prevalence:** Growing fast. Overlaps with thesis_dreader and duct_tape_analyst but the defining behavior is the AI dependency loop.

### budget_gatekeeper
People with organizational purchasing authority or grant/institutional budgets who evaluate tools for their teams. They care about audit trails, compliance, data security, and whether this replaces existing spend (NVivo licenses, SPSS seats). More rational, less emotional.

> "Show me what it does, how much it costs, and whether I can justify it to my department."

**Expected prevalence:** Smaller segment but critical for revenue. They buy seats, not subscriptions.

### skeptical_methodologist
Someone with enough statistical training to be dangerous — they've used SPSS or R, they know what a p-value is, they might teach a methods course. They'll scrutinize whether the tool picks the right test and whether "click to analyze" produces defensible results. Trust is the barrier, not capability.

> "If it picks Pearson when the data is ordinal, I can't use it."

**Expected prevalence:** Smallest segment but loudest voice. If they endorse it, others follow.

---

## 4. Product Description

**Canonical (for clarity scoring):**
A web-based platform that lets people go from raw qualitative data — interviews, surveys, spreadsheets — to understood results by clicking, not coding. It chooses the right statistical test, runs it, visualizes it, and explains what it means.

**Core claim (for "nailed_it" clarity scoring):**
A point-and-click data analysis platform that selects the right statistical method for you and explains results in plain language.

---

## 5. Pricing

| Tier | Price | Includes |
|------|-------|----------|
| Free | $0 | 3 projects, core analysis, unlimited exports |
| Pro | $10/month | Unlimited projects, advanced viz, collaboration, priority support |
| Team | $25/month | Pro + shared workspaces, inter-rater reliability, role-based permissions |

---

## 6. Copy Skeleton

| Section | Purpose |
|---------|---------|
| **Hero** | Headline + subhead + CTA. Sets the frame. |
| **Problem** | Names the pain — tool fragmentation, ChatGPT loops, feeling lost. |
| **Solution** | Click-to-analyze, auto-selected methods, visualization as primary interface. |
| **Who It's For** | Specific user types with their context. |
| **How It Works** | 5-step process: Upload → Clean → Analyze → Visualize → Export. |
| **Pricing** | Three tiers with anchor to ChatGPT spend. |
| **Objection Handling** | Preempts Excel inertia, trust, and budget concerns. |
| **Final CTA** | Callback to "brute forcing" + action prompt. |

---

## 7. Evaluation Schema

Full schema (V1-V5):

```json
{
  "person_id": "<number from profile>",
  "bucket": "<bucket from profile>",
  "resonance": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "clarity_response": "<describe in one sentence what this product does>",
  "intent": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "conversion_confidence": "<strongly_disagree|disagree|neutral|agree|strongly_agree>",
  "price_perception": "<too_expensive|fair|good_deal>",
  "strongest_line": "<single line from the copy that resonated most>",
  "what_feels_off": "<anything generic, try-hard, or dishonest-feeling>",
  "objections": "<what's stopping you from signing up>",
  "dealbreaker": "<true|false>",
  "dealbreaker_reason": "<why, or null if dealbreaker is false>",
  "gut_reaction": "<1-2 sentences, first impression>",
  "unanswered_questions": "<what the page didn't answer>",
  "price_reaction": "<specific thoughts on pricing tiers>"
}
```

---

## 8. Stopping Criteria

- **Minimum:** 5 rounds
- **Target:** >50% conversion confidence at agree+
- **Maximum:** 10 iterations
- **Convergence:** Two consecutive rounds with no meaningful change
- **Qualitative:** Feedback themes stabilize
- **User override:** Stop when satisfied

---

## 9. Template Inputs

| Variable | Value |
|----------|-------|
| `{SCHEMA}` | Full schema above |
| `{PRODUCT_DESCRIPTION}` | See Section 4, canonical |
| `{PRODUCT_CORE_CLAIM}` | See Section 4, core claim |
| Audience file | `audience.json` |
| Copy file (V1) | `copy_v1.md` |

---

*Brief approved: [pending user review]*
