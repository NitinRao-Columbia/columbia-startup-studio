# Submission: Idea Brief + Team Formation

**Due:** Part 1 (Idea Brief) — Thursday, February 5, 2026 (bring to class)
**Due:** Part 2 (Team Submission) — Friday, February 6, 2026
**Submit via:** Part 2 via GitHub (public repo)

**Reference decks:**
- `../classes/20260203_c4w3_tue_team-formation/slides_20260203_c4w3_tue_team-formation.pdf`
- `../classes/20260205_c5w3_thu_divergent-thinking/slides_20260205_c5w3_thu_divergent-thinking.pdf`

---

## Part 1: Idea Brief

### Due Thursday, February 5 — Bring to Class

Bring a completed idea brief to class on Thursday. Use AI to help draft it.

Your brief has three sections:

### 1. Core

- **Problem:** What's broken?
- **Context:** Why does it matter now?
- **Idea:** How might you solve it?

### 2. The 4 W's

- **Who:** Who is your target customer?
- **What:** What do they need?
- **Where:** Where does this problem happen?
- **Why:** Why would they use your solution?

### 3. AEIOU

- **Activities:** What are they doing when this problem occurs?
- **Environments:** Where are they?
- **Interactions:** With whom?
- **Objects:** What tools or things are involved?
- **Users:** Who are they specifically?

---

## Part 2: Team Submission

### Due Friday, February 6 — via GitHub Pull Request

### What to Submit

Create a folder `20260206/` inside your team folder in the public repo:

```
teams/your-team-name/20260206/
```

Include the following:

### 1. Team Name and Members

A `README.md` (or included in another file) with:
- Your team name
- All team member UNIs

### 2. All Ideas Generated

Every idea your team explored during the divergent thinking exercises — not just the ones you kept. Submit as:
- FigJam screenshots, or
- Photos of your sticky notes (LLMs can read handwritten notes)

Include ideas from the Exquisite Corpse combinations and the MIT Ideator output.

### 3. Lean Canvases

Lean Canvas outputs for your top 3-5 concepts. Submit as:
- Screenshots of AI-generated canvases, or
- Text files with the canvas content

---

## How to Submit

Submissions are made via **pull request** on the public repo.

### Step 1: Fork the repo (first time only)

If you haven't already, fork the public repo on GitHub. Click the **Fork** button at the top right of the repo page. This creates your own copy under your GitHub account.

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

### Step 3: Create a branch and add files

```bash
git checkout -b team-submission
mkdir teams/your-team-name
mkdir teams/your-team-name/20260206
# Add your files to the folder
git add teams/your-team-name/
git commit -m "Add team submission"
git push -u origin team-submission
```

### Step 4: Open a pull request

1. Go to the **original repo** on GitHub (not your fork)
2. Click **Pull Requests** → **New Pull Request**
3. Click **"compare across forks"**
4. Set **base** to the original repo's `main` and **head** to your fork's `team-submission` branch
5. Title your PR: `[Your Team Name] Week 3 Team Submission`
6. Submit the pull request

---

## Folder Structure Example

```
teams/your-team-name/
├── 20260206/          ← this submission
│   ├── README.md      ← team name + member UNIs
│   ├── ideas_01.png   ← FigJam screenshot or sticky note photo
│   ├── ideas_02.png
│   ├── canvas_concept_a.md
│   ├── canvas_concept_b.md
│   └── canvas_concept_c.md
└── ...
```

File names and organization are flexible. Just make sure all three categories are represented: team info, all ideas generated, and your lean canvases.
