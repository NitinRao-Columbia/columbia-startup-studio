# Feature-Forge Skill

This folder contains the **feature-forge** skill for Claude Code — a structured workflow for building features from brief through PR.

## What is Feature-Forge?

Feature-forge is a 7-phase process for guided feature development:

1. **Brief** — Define the problem, goals, and success metrics
2. **Architecture** — Design the solution, document alternatives
3. **Plan** — Break into phased tasks with test list
4. **Implement** — Build with TDD (red-green-refactor)
5. **Review** — Code review against docs + automated checks
6. **Push** — Branch push + PR creation
7. **Cleanup** — Update docs, review outcomes

## Why Use Feature-Forge?

- **Stop gates prevent scope creep** — Human reviews after Brief, Architecture, and Plan ensure the AI builds exactly what you want
- **Documentation-driven development** — Write docs first, AI builds from your spec
- **Quality over speed** — TDD, code review, and structured deployment
- **Great for learning** — Forces you to think through architectural decisions before coding

## How to Install

### Option 1: Copy to Your Project (Recommended for Teams)

```bash
# Copy the skill folder to your project
cp -r feature-forge-skill ~/.claude/skills/feature-forge
```

### Option 2: Use Directly from This Folder

If you're working solo and want to keep the skill in the Columbia repo:

```bash
# Create a symlink in your global skills folder
ln -s "$(pwd)/feature-forge-skill" ~/.claude/skills/feature-forge
```

## How to Use

Once installed, trigger the skill in Claude Code with:

```
/feature-forge [feature description]
```

Or just:

```
Let's build a feature: [description]
```

### Example: Building a Landing Page

```
/feature-forge landing page with waitlist signup
```

Claude will guide you through:
1. Writing a brief (what's the one job of this page?)
2. Designing the architecture (where do emails go? analytics setup?)
3. Creating a plan (phases, tests, definition of done)
4. **STOP** — You review and approve before any code is written
5. Implementation with tests
6. Code review
7. PR creation and deployment

## When NOT to Use Feature-Forge

- Quick fixes or typos (just edit directly)
- Single-file changes with obvious implementation
- Features touching fewer than 3 files with no design decisions

For those, just prompt Claude Code normally.

## Files in This Folder

- **SKILL.md** — The main skill definition (what Claude Code reads)
- **references/** — Supporting documentation:
  - `document-templates.md` — Templates for brief, architecture, plan docs
  - `code-review-checklist.md` — What to check during code review
  - `tdd-guide.md` — Test-driven development workflow
  - `post-deploy-checklist.md` — Deployment readiness checks

## Learn More

See the slides from c11w6 (Landing Pages + Demand Gen) for a deep dive on how feature-forge works and why it matters.

---

**Questions?** Ask in class or in the course Slack.
