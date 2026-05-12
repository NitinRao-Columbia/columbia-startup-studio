# Code Review Checklist

Use this checklist during the Review phase. Run the `code-reviewer` subagent with these items as review criteria. After the automated review, do a self-review comparing implementation against Brief + Architecture + Plan.

## How to Use

1. Launch the `code-reviewer` subagent (from the feature-dev plugin) with the checklist below as context.
2. Review the findings. Fix issues with confidence >= 80%.
3. Re-run tests after fixes to confirm nothing broke.
4. Do a manual self-review for items the automated reviewer can't catch (architecture conformance, deviation from plan).

---

## The Checklist

### Architecture Conformance
- [ ] Implementation matches the Architecture doc's design. Components, data flows, and module boundaries are as specified.
- [ ] No new patterns introduced that contradict existing project conventions (check CLAUDE.md for project conventions).
- [ ] If deviations from the Architecture were necessary, they're documented in the progress doc under "Changes from Plan" with rationale.

### Naming and Readability
- [ ] Names are descriptive and consistent with codebase conventions.
- [ ] A developer unfamiliar with this feature could understand the code without reading the PR description.
- [ ] No magic numbers or strings. Constants are named and explained if not self-evident.

### Security
- [ ] User input is sanitized. Strong Parameters (Rails), input validation (frontend), parameterized queries.
- [ ] Authentication and authorization are properly enforced on new endpoints.
- [ ] No secrets, API keys, or credentials in code, comments, or logs.
- [ ] PII is handled according to project policy. No unnecessary logging of personal data.

### API Contract Stability
- [ ] If API endpoints were added or changed: request/response format is documented or follows existing patterns.
- [ ] No breaking changes to existing API contracts without explicit versioning or migration plan.
- [ ] Error responses follow the project's standard format (check CLAUDE.md for API conventions).

### Test Quality
- [ ] Tests assert meaningful behavior, not implementation details.
- [ ] Edge cases from the Architecture doc's failure modes are covered.
- [ ] Tests are isolated and deterministic. No test depends on another test's state.
- [ ] Test names describe the behavior being tested, not the method being called.
- [ ] Mocks and stubs are used appropriately. External services are stubbed; internal logic is tested directly.

### Operational Readiness
- [ ] Appropriate log statements exist for debugging production issues.
- [ ] Error messages are actionable. They tell you what went wrong and suggest what to do.
- [ ] New database queries are indexed appropriately. No N+1 queries introduced.
- [ ] Background jobs are idempotent (if applicable).
- [ ] Feature flags are configured for gradual rollout (if applicable).
