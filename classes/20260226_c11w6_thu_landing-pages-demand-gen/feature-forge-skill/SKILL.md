---
name: feature-forge
description: >-
  Use this skill for guided feature development from brief through PR.
  Triggered by "let's build a feature", "new feature", "feature-forge",
  "/feature-forge", "start a feature", or "build [feature name]".
  Covers 7 phases: Brief, Architecture, Plan, Implement, Review, Push,
  Cleanup. Enforces TDD, structured code review, success metrics,
  and human review gates between phases. Do not use for quick fixes,
  single-file changes, or trivial features that touch fewer than 3 files.
argument-hint: "[phase] or [feature description]"
user-invocable: true
---

# Feature Forge

Guided feature development from problem definition through PR. Seven phases, each with clear entry/exit criteria and human review gates where it matters.

## Phases

1. **Brief** — Define the problem, goals, non-goals, success metrics
2. **Architecture** — Design the solution, document alternatives considered
3. **Plan** — Break into phased tasks with a test list
4. **Implement** — Build with TDD (red-green-refactor)
5. **Review** — Automated code review + self-review against docs
6. **Push** — Branch push, PR creation, readiness checklist
7. **Cleanup** — Update docs, outcome review, propose process improvements

## When NOT to Use

- Quick fixes, typos, single-line edits
- Single-file changes with obvious implementation
- Features touching fewer than 3 files with no design decisions
- Pure research or exploration (use research-report or Task tool with Explore agent)

## Argument Handling

If `$ARGUMENTS` is provided:
- If it exactly matches a phase name (brief, architecture, plan, implement, review, push, cleanup) as a single word, jump to that phase. Look for the most recent in-progress feature folder (has a progress doc with incomplete items). If multiple candidates exist, list them and ask the user to pick. If none exist, ask what feature they're working on.
- Otherwise, treat `$ARGUMENTS` as a feature description and start at Brief.

If no arguments, start at Brief and ask the user to describe the feature.

## Project Setup (First Run)

On first invocation in a project, check for a feature documentation folder (commonly `docs/features/` or `features/`). If none exists:

1. Recommend this folder structure:
   - `docs/features/` for feature documentation
   - `docs/ongoing/` for living documentation (optional but recommended)
   - Feature folder naming: `yyyymmdd.nn_[feature_name]/`
     - `yyyymmdd` = date, no hyphens
     - `nn` = 2-digit daily index starting at 01
     - `feature_name` = lowercase with underscores
2. If the user specifies different conventions, note them and adapt for all subsequent phases.
3. Don't block on setup; recommend and proceed.

Check CLAUDE.md for any project-specific conventions about documentation locations, git workflow, or testing patterns. These override the skill's defaults.

## Documentation Style

**Use Mermaid diagrams liberally.** Whenever you're describing a flow, sequence, state machine, data relationship, or decision tree, default to a Mermaid diagram over prose or ASCII art. Diagrams are faster to read, more precise, and consume less context than equivalent text explanations.

Specifically:
- **Architecture (Phase 2):** Key Flows should always be Mermaid sequence or flowchart diagrams. State transitions should use Mermaid state diagrams. Data relationships should use Mermaid ER diagrams.
- **Brief (Phase 1):** Use diagrams for user flows or system context when they clarify the problem.
- **Plan (Phase 3):** Use diagrams for dependency graphs between phases when ordering matters.

A Mermaid diagram is almost always better than a bulleted list of steps. When in doubt, diagram it.

---

## Phase 1: Brief

**Goal:** Define the problem clearly before designing a solution.

**Done when:** The brief has Context, Goal, Non-goals, User Stories, Requirements, Success Metrics, and Open Questions. Human has reviewed and approved.

1. Create the feature folder: `docs/features/yyyymmdd.nn_[feature_name]/`
2. Create the progress doc (`04_progress_[feature_name].md`) immediately. Update it continuously from here on. Don't delete prior entries; use checklists.
3. Read [references/document-templates.md](references/document-templates.md) for the Brief template.
4. Write `01_brief_[feature_name].md` using the template.
5. **Success Metrics are required.** If measurable criteria can't be defined, add it as an open question to resolve before proceeding.

**STOP — Brief phase complete. Ready for human review.**

Wait for feedback. Update the brief to reflect decisions and answered questions. Move resolved questions to a "Decisions (Resolved)" section.

---

## Phase 2: Architecture

**Goal:** Design the solution at system level. Document what you chose and what you rejected.

**Done when:** The architecture doc has Summary, Analysis of Existing Structure, Components, Key Flows, Alternatives Considered, Failure Modes, and Test Strategy. Human has reviewed and approved.

1. Read [references/document-templates.md](references/document-templates.md) for the Architecture template.
2. Write `02_architecture_[feature_name].md` using the template.
3. **Alternatives Considered is required.** Document at least one rejected approach with rationale. This prevents relitigating settled decisions later.
4. **Recon sub-step (optional):** If feasibility is uncertain, do timeboxed exploratory work before committing to the design. For deeper investigation, suggest the research-report skill. Recon output feeds into the architecture doc as findings, not a separate artifact.

**STOP — Architecture phase complete. Ready for human review.**

Wait for feedback. Incorporate changes, then review all docs (Brief + Architecture) for consistency before proceeding. Edits may have caused drift; reconcile.

---

## Phase 3: Plan

**Goal:** Break the work into ordered, testable phases.

**Done when:** The plan has phased tasks, a test list derived from Brief + Architecture, and a definition of done. Human has reviewed and approved.

1. Read [references/document-templates.md](references/document-templates.md) for the Plan template.
2. Write `03_plan_[feature_name].md` using the template.
3. **Test List is required.** Derive it from Brief requirements and Architecture failure modes. Enumerate behavioral variants and edge cases. These become failing tests in the Implement phase. This is the bridge between documentation and implementation.
4. Testing is integrated into each plan phase, not a separate final phase.
5. No time estimates. They create false precision.
6. Review all docs (Brief + Architecture + Plan) for consistency.

**STOP — Plan phase complete. Ready for human review.**

---

## Phase 4: Implement

**Goal:** Build the feature following the plan, with tests driving the implementation.

**Done when:** All plan phases are complete, all tests pass, progress doc is current.

1. Create a git branch for the feature. Recommended: `feat/[feature_name]`. Follow project-specific git conventions from CLAUDE.md if they exist (e.g., worktrees).
   - **If the project has `scripts/worktree.sh`**, run `bash scripts/worktree.sh setup [feature_name]` from the repo root. This creates the worktree, installs dependencies, sets up the database, starts dev servers on offset ports, and opens the browser. The script prints the URLs and database name. All code changes happen in the worktree directory from this point forward.
   - Continue editing docs in the main repo directory (per project CLAUDE.md conventions).
2. Read [references/tdd-guide.md](references/tdd-guide.md) for the TDD workflow.
3. Follow the TDD loop: start from the test list in the Plan. For each item:
   - Write one failing test (RED)
   - Make it pass with the simplest code (GREEN)
   - Refactor both test and production code (REFACTOR)
   - Commit
4. **TDD exceptions** (test-after is acceptable): UI/visual work, exploratory/recon work, performance optimization, third-party API integrations where mocking comes first.
5. Update the progress doc continuously. Don't delete prior entries.

---

## Phase 5: Review

**Goal:** Catch issues before push. Verify the implementation matches the design.

**Done when:** Code review is clean, all tests pass after fixes, self-review confirms alignment with Brief + Architecture + Plan.

1. Read [references/code-review-checklist.md](references/code-review-checklist.md).
2. Run automated code review using `code-reviewer` subagent. Pass the checklist items as review criteria.
3. Fix any issues found. Re-run tests to confirm fixes don't break anything.
4. Self-review: compare the implementation against Brief + Architecture + Plan. Flag any deviations in the progress doc under "Changes from Plan."

---

## Phase 6: Push

**Goal:** Get the code into a PR with confidence.

**Done when:** PR is created, readiness checklist passes, progress doc notes the PR link.

1. **Readiness checklist** (all must be true before pushing):
   - [ ] All tests pass
   - [ ] Code review is clean (no unresolved issues)
   - [ ] No known regressions
   - [ ] Progress doc is up to date
2. Push the branch. Never push main.
3. Create a PR. PR description should reference the feature docs and summarize changes.
4. Read [references/post-deploy-checklist.md](references/post-deploy-checklist.md) and surface the post-deploy checklist for the human.
5. Note the PR link in the progress doc.
6. **Feedback loop:** The progress doc is the feedback channel. After pushing, tell the human it's ready for review. They add feedback in the progress doc via their text editor. When they say they've added feedback, re-read the doc and address all items.

---

## Phase 7: Cleanup

**Goal:** Close the loop. Update docs, measure outcomes, improve the process.

**Done when:** Progress log is final, ongoing docs are updated, process improvements are proposed.

1. Finalize the progress doc. Ensure all items are checked off. Document final test results, files touched, and any deviations from plan.
2. **If the project has `scripts/worktree.sh`**, run `bash scripts/worktree.sh teardown [feature_name]` from the repo root. This stops servers, drops the worktree database, and removes the worktree. The branch is deleted only if it has been merged into main.
3. Update ongoing/living documentation if the feature changed system behavior. Check project-specific docs (e.g., `docs/ongoing/` if it exists) for anything that needs updating: PRD, style guide, analytics catalog, diagrams.
3. Read [references/post-deploy-checklist.md](references/post-deploy-checklist.md) and surface the outcome review checklist.
4. Propose process improvements:
   - CLAUDE.md updates: new rules, patterns, warnings based on lessons learned
   - Skill updates: anything about feature-forge itself that should change
   - Flag existing instructions that were found to be incorrect or incomplete
   - **Do not edit CLAUDE.md or SKILL.md without human approval.**
