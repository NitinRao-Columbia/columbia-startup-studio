# Post-Deploy and Outcome Review Checklists

These are human-driven checklists. The skill surfaces them at the right time; the human works through them.

---

## Post-Deploy Checklist

Surface this after the PR is merged and deployed. These are recommendations, not gates.

- [ ] **Smoke test:** Feature works in production as expected (manual verification)
- [ ] **Error monitoring:** No new errors in logs, error tracking, or monitoring dashboards
- [ ] **Performance:** No significant degradation in response times or resource usage
- [ ] **Feature flag:** Enabled for target audience (if applicable)
- [ ] **Rollback plan:** Know how to revert if something goes wrong (revert commit, disable flag, etc.)
- [ ] **Data integrity:** Any migrations ran cleanly; data looks correct in production

Not every item applies to every feature. Check what's relevant and move on.

---

## Outcome Review Checklist

Surface this during the Cleanup phase. Revisit the success metrics defined in the Brief.

- [ ] **Success metrics reviewed:** Pull up the metrics from the Brief's Success Metrics section
- [ ] **If deployed and measurable:** Record actual results against targets
  - Met target? Note it.
  - Missed target? Note by how much and hypothesize why.
  - Can't measure yet? Note when to check back and what to look for.
- [ ] **If not yet deployed:** Document what to measure and when to check
- [ ] **Unexpected outcomes:** Anything surprising (positive or negative) that wasn't in the success metrics
- [ ] **Follow-up tasks:** Create tasks for anything that needs attention (Trello cards, GitHub issues, etc.)

The goal is to close the loop: did we build the right thing? This is the weakest muscle in most development workflows. Building the habit matters more than getting the measurement perfect.
