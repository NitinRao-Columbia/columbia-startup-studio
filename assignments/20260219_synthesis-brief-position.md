# Submission: Product Brief, Brand Position & Synthetic User Testing

**Due:** Thursday, February 19, 2026
**Submit via:** GitHub (public repo)
**Deck:** [c8 Synthetic Testing](../classes/20260217_c8w5_tue_synthetic-testing/slides_c8w5_tue_synthetic-testing.pdf) / [c9 Synthetic Testing](../classes/20260219_c9w5_thu_synthetic-testing/slides_c9w5_thu_synthetic-testing.pdf)

---

## What to Submit

Create a folder `20260219/` inside your team folder in the public repo:

```
teams/your-team-name/20260219/
```

Include the following:

### 1. Product Brief

One-page document covering what you're building, who it's for, and what problem it solves. Use the template at the bottom of this document.

**Use AI to help draft this.** Feed your synthesis and interview notes into an LLM and ask it to help fill out the template. Edit and refine the output — don't just submit raw AI output, but don't do this by hand either.

### 2. Brand Position

Internal document capturing your brand's thesis, identity, and canonical language. Use the template at the bottom of this document.

**Use AI to help draft this.** Same approach: feed your synthesis into an LLM, use the template as a structure, and refine what it gives you. The brand position builds directly on your synthesis and product brief.

### 3. Synthetic User Testing (In-Class Exercise)

Run at least **5 rounds** of synthetic user testing on your landing page copy. Include:

- The copy versions you tested (V1 through V5+)
- Feedback summaries from each round
- What you changed between rounds and why

Use the synthetic testing skill from class: `exercise/synthetic-user-testing/SKILL.md`

---

## How to Submit

Submissions are made via **pull request** on the public repo.

### Step 1: Fork the repo (first time only)

If you haven't already, fork the public repo on GitHub. Click the **Fork** button at the top right of the repo page. This creates your own copy.

### Step 2: Sync your fork

Make sure your fork is up to date with the main repo before starting:

```bash
# If you haven't added the upstream remote yet:
git remote add upstream https://github.com/kenxle/columbia-startup-studio.git

# Sync your fork
git fetch upstream
git checkout main
git merge upstream/main
```

### Step 3: Create your submission

```bash
cd teams/your-team-name
mkdir 20260219
# add your files to the folder
git add 20260219/
git commit -m "Add product brief, brand position, and synthetic testing"
git push origin main
```

### Step 4: Open a pull request

1. Go to the **original repo** on GitHub (not your fork)
2. Click **Pull Requests** → **New Pull Request**
3. Click **"compare across forks"**
4. Set **base** to the original repo's `main` and **head** to your fork's `main`
5. Title your PR: `[Your Team Name] Product Brief, Brand Position & Synthetic Testing`
6. Submit the pull request

---

## Folder Structure Example

```
teams/your-team-name/
├── 20260206/          ← divergent thinking
├── 20260217/          ← interview materials + synthesis
├── 20260219/          ← this submission
│   ├── product_brief.md
│   ├── brand_position.md
│   └── synthetic_testing/
│       ├── v1_copy.md
│       ├── v1_results.md
│       ├── v2_copy.md
│       ├── v2_results.md
│       ├── ...
│       ├── v5_copy.md
│       └── v5_results.md
└── README.md
```

File names are flexible. Just make sure all three deliverables are included.

---

## Template: Product Brief

**Team Name:**
**Date:**

### The Problem

What problem are you solving? Describe it in the language your interviewees used, not startup jargon.

- Who has this problem?
- How do they currently deal with it?
- How painful is it? (What evidence do you have from interviews?)

### The Solution

What are you building? Describe the core product in 2-3 sentences.

- What does it do?
- How does the user interact with it?
- What makes it different from how people solve this problem today?

### Target User

Who specifically is this for? Be as concrete as your interview data allows.

- **Demographics:** Age, occupation, location, life stage
- **Defining behavior:** What do they do that makes them your user? (e.g., "spends $50+/week on takeout," "manages a team of 5-10")
- **How they describe the problem:** Use exact phrases from interviews

### Why Now

Why does this product need to exist right now? What has changed that makes this solvable or urgent?

### Key Interview Evidence

Summarize the strongest signals from your interviews:

- **Strongest quote:** [exact words from an interviewee]
- **Pattern:** [what came up across 3+ interviews]
- **Surprise:** [what you didn't expect to learn]
- **Current spend/effort:** [what people already do or pay to solve this]

### Open Questions

What don't you know yet? What assumptions still need testing?

1.
2.
3.

*Keep this to one page. This document feeds directly into your brand position and landing page copy.*

---

## Template: Brand Position

**Team Name:**
**Date:**

**Purpose:** This is an internal document. It captures your brand's thesis, identity, and canonical language so that everything you build — landing page, copy, features, pitch — speaks with one voice. This is not marketing copy. It is a decision reference.

### Brand Thesis

What is the one-sentence emotional and philosophical anchor of your brand? This is the big idea, not a feature description.

> **[Your brand thesis here]**

### Core Product Definition

Complete this sentence with maximum clarity:

> **[Product Name] helps [who] [do what] by [how].**

### Existence Statement

Why does this product exist? Not what it does, but why it needs to be in the world.

> **[Product Name] exists to [purpose].**

### Target Identity

Who is your user, described in aspirational but honest terms? Not demographics — identity.

> **[Product Name] is for someone who [identity description].**

### Canonical Language

List 4-6 phrases that capture your brand voice. These are the words and phrases you use repeatedly across all surfaces.

- **[Phrase 1]**
- **[Phrase 2]**
- **[Phrase 3]**
- **[Phrase 4]**

### Language to Avoid

What words or framings are off-brand? What do competitors say that you deliberately don't?

- **Avoid:** [word/phrase] — **Because:** [reason]
- **Avoid:** [word/phrase] — **Because:** [reason]
- **Avoid:** [word/phrase] — **Because:** [reason]

### Tone Guidelines

Describe your brand's voice in 3-4 short rules:

- **[Adjective] not [adjective]** — [brief explanation]
- **[Adjective] not [adjective]** — [brief explanation]
- **[Adjective] not [adjective]** — [brief explanation]

### Positioning Statement

Complete this sentence:

> **For [target user], [Product Name] is the [category] that [key benefit] because [reason to believe].**

### Brand Values

What 2-3 principles guide decisions when the team disagrees? These are tiebreakers, not aspirations.

- **[Value]** — [what it means in practice]
- **[Value]** — [what it means in practice]

### Objection Handling

What did skeptics say in your interviews? What are the top 2-3 reasons someone would say no, and how would you respond?

| Objection | Your Response |
|-----------|--------------|
| "[what they said or would say]" | [how you address it] |
| "[what they said or would say]" | [how you address it] |
| "[what they said or would say]" | [how you address it] |

### Key Interview Language

Pull the 3-5 most vivid phrases from your interviews that should influence your copy. These are your users' actual words.

1. "[exact quote]" — [context]
2. "[exact quote]" — [context]
3. "[exact quote]" — [context]

*This document is the foundation for your landing page copy and synthetic testing. When copy conflicts with this document, the copy is wrong.*
