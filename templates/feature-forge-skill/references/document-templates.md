# Feature Document Templates

Use these templates when creating feature docs. Each template provides section headings and guidance. Adapt as needed, but don't remove required sections (marked with *).

---

## Brief Template (`01_brief_[name].md`)

```markdown
# Feature Brief: [Feature Name]

## Context

Background and motivation. Why does this feature exist? What preceded it?
Link to related reports, discussions, or prior work. Use Mermaid diagrams where helpful.

## Goal / Problem *

What we're building and why. Be specific about the desired outcome.
If there's a key design question, state it here.

## Non-Goals *

What's explicitly out of scope. Helps prevent scope creep and sets expectations.
Use bullet points starting with "Not..."

## User Stories

Who does what and why. Format:
- **As [persona]**, I want [action] so that [benefit].

## Requirements *

Concrete, testable requirements organized by category.
Use sub-headers for groups (e.g., "Core Workflow", "API Changes").

## Success Metrics *

Measurable criteria for whether the feature worked. Examples:
- "60% of users complete the onboarding quiz"
- "P95 response time under 200ms"
- "Zero unhandled errors in logs for first 48 hours"

If you can't define metrics yet, add it as an open question.

## UX Notes

UI/UX considerations (if relevant). Cross-platform behavior, responsive design.

## Analytics / Logging

What to track (if relevant). Events, metrics, log entries.

## Rollout / Flags

Feature flags, migrations, backward compatibility (if relevant).

## Open Questions *

Numbered questions that need answers before proceeding.
As decisions are made, move them to a "Decisions (Resolved)" section.
```

**Tips:**
- Open Questions drive the review conversation. Make them specific and numbered.
- Non-Goals prevent the most common misunderstandings. When in doubt, add one.
- Success Metrics force you to define what "done" looks like beyond "code works."
- If the feature is small, some sections can be a single line or "N/A."

---

## Architecture Template (`02_architecture_[name].md`)

```markdown
# Architecture: [Feature Name]

## Summary

One paragraph: what will be built at system level.

## Analysis of Existing Structure

What exists today that's relevant. Current state of files, modules, patterns.
What changes and what stays the same.

## Components / Modules Touched

List by name. No code in this doc.

## Data / State Changes

Conceptual data contracts. New fields, new tables, state transitions.

## Key Flows

Primary workflow as a description or Mermaid diagram.
Secondary/alternative flows if they exist.

## Alternatives Considered *

Document at least one rejected approach:
- **[Approach Name]**: What it was, why it was considered, why it was rejected.
This prevents relitigating settled decisions later.

## Failure Modes / Edge Cases

Unusual scenarios and how they're handled. Loading states, empty states, error states.

## Security & Privacy Notes

If relevant. Auth, input sanitization, PII handling.

## Test Strategy

What to test and how. Unit vs integration vs e2e. What constitutes a passing test.

## Open Questions

Only if new unknowns surfaced during architecture (don't repeat brief questions).
```

**Tips:**
- Alternatives Considered is the most valuable section for future-you. Document why you didn't choose the obvious approach.
- Key Flows with Mermaid diagrams are worth the effort. They catch misunderstandings before code.
- Failure Modes become test cases in the Plan phase.

---

## Plan Template (`03_plan_[name].md`)

```markdown
# Plan: [Feature Name]

## Phase 1: [Name]

**Tasks:**
1. Specific task
2. Specific task

**Test:** How to verify this phase worked.

## Phase 2: [Name]

**Tasks:**
1. Specific task
2. Specific task

**Test:** How to verify this phase worked.

## Test List *

Derived from Brief requirements and Architecture failure modes.
Enumerate behavioral variants and edge cases that become failing tests:

- [ ] [Behavior or edge case to test]
- [ ] [Behavior or edge case to test]
- [ ] [Behavior or edge case to test]

## Definition of Done *

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2
- [ ] Human has reviewed and approved
```

**Tips:**
- Testing is integrated into each phase. Never a separate final phase.
- No time estimates. They create false precision and pressure.
- Phases should be small enough to complete and verify independently.
- 3-5 phases is typical; more than 7 suggests the feature should be split.
- The Test List is the bridge between documentation and implementation. Each item becomes a failing test in the Implement phase.

---

## Progress Template (`04_progress_[name].md`)

```markdown
# Progress: [Feature Name]

## Status

Current state in one sentence.

## Completed

- [x] Task that was finished
- [x] Another completed task

## In Progress

- [ ] Currently working on this

## Remaining

- [ ] Still needs to be done
- [ ] And this

## Files Touched

- `path/to/file.rb` — Created
- `path/to/other.js` — Modified (added validation)

## Test Results

Link to test output or summary of results.

## Changes from Plan

Document any deviations from the original plan and why they happened.

## Follow-ups

Items discovered during implementation that should be addressed later.

## Feedback (Round 1)

[Human adds feedback here via their text editor. Claude re-reads the doc when told feedback is ready.]
```

**Tips:**
- Don't delete prior entries. Check them off. The log shows the path taken.
- "Changes from Plan" is the most important section for learning. Capture why the plan was wrong.
- Update this file as you work, not just at the end.
- The Feedback section is the bidirectional communication channel. Add a new `## Feedback (Round N)` section for each round.
