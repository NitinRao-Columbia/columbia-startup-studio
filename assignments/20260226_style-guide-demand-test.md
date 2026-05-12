# Submission: Style Guide, Landing Page + Demand Test

**Due:** Thursday, February 26, 2026
**Submit via:** GitHub (public repo)

**Reference deck:**
- `../classes/20260224_c10w6_tue_demand-gen-style-guide/slides_c10w6_tue_demand-gen-style-guide.pdf`

---

## What to Submit

Create a folder `20260226/` inside your team folder in the public repo:

```
teams/your-team-name/20260226/
```

Include the following:

### 1. Live Landing Page

Your landing page must be **live and publicly accessible** by class time on Thursday.

Required elements:
- Headline that matches your tested copy
- Value propositions (what it does, who it's for)
- Clear call to action (CTA)
- Email capture (waitlist signup)
- Styled using your style guide (colors, fonts, visual tone)

Accepted platforms: Carrd, Framer, Webflow, or built with a code agent (Claude Code, Cursor). Include the live URL in your submission.

### 2. STYLE_GUIDE.md

A completed `STYLE_GUIDE.md` covering:

- **Color palette:** Primary, secondary, accent, background, and text colors. Hex codes for every color. Use coolors.co to generate and export.
- **Typography:** Heading font and body font. Size hierarchy from h1 through body text.
- **Visual tone:** One sentence that captures the feel (minimal, bold, playful, corporate, etc.).
- **Component patterns:** Button style, CTA style, card style. Light touch — just enough to keep things consistent.

Tip: hand the STYLE_GUIDE template + your `BRIEF.md` + `BRAND_POSITION.md` to an AI and ask it to walk you through filling it out. It will suggest colors, fonts, and visual direction that match your brand.

### 3. Demand Test Plan

A written plan for your demand test, covering:

- **Audience:** One specific target audience
- **Angles:** Two message angles (A/B) you are testing
- **Budget:** Approximately $200 total (~$40/day x 5 days)
- **Success threshold:** The conversion rate or number of signups you commit to in advance before interpreting results

Pre-flight checklist (confirm all before launching):
- [ ] Conversion works end-to-end (thank-you page fires after signup)
- [ ] UTMs on every ad link
- [ ] Simple creative ready (1 static image; optional 1 video)
- [ ] Clean naming convention for campaigns (`Team_Product_Angle_Date`)

### 4. MVP Feature List

A list of 3-5 core features for your v1 product. These are the features you need for a functional MVP — not a wishlist, not a roadmap. Each feature will go through the feature-forge process (brief, architecture, plan, implement) in the Build phase.

### 5. Google Analytics Certification (In Progress)

Begin the Google Analytics certification this week. You do not need to complete it for this submission, but include a note confirming you have started.

Certification link: [Google Skillshop](https://skillshop.docebosaas.com/learn/courses/14810/google-analytics-certification) — free, approximately 5 hours.

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

### Step 3: Create your submission

```bash
git checkout -b week6-submission
cd teams/your-team-name
mkdir 20260226
# Add your files to the folder
git add 20260226/
git commit -m "Add Week 6 submission"
git push -u origin week6-submission
```

### Step 4: Open a pull request

1. Go to the **original repo** on GitHub (not your fork)
2. Click **Pull Requests** → **New Pull Request**
3. Click **"compare across forks"**
4. Set **base** to the original repo's `main` and **head** to your fork's `week6-submission` branch
5. Title your PR: `[Your Team Name] Week 6 Submission`
6. Submit the pull request

---

## Folder Structure Example

```
teams/your-team-name/
├── 20260217/          ← previous submission
├── 20260226/          ← this submission
│   ├── STYLE_GUIDE.md
│   ├── demand_test_plan.md
│   ├── mvp_feature_list.md
│   └── landing_page_url.md   ← or include URL in README
└── README.md
```

File names and organization are flexible. Just make sure all five deliverables are represented: live landing page URL, style guide, demand test plan, MVP feature list, and Google Analytics cert status.
