# TDD Guide

Test-Driven Development as the default approach during the Implement phase. Based on Kent Beck's Canon TDD.

## The Loop

### Step 1: Write the Test List

Before writing any code, convert the Plan's Test List into a prioritized list of behavioral variants. Each item is a specific behavior or edge case that needs a test. This list comes from:
- Brief requirements
- Architecture failure modes / edge cases
- Plan test criteria

Don't write all the tests at once. The list guides which test to write next.

### Step 2: For Each Item

**RED:** Write one failing test. The test should express the desired behavior, not the implementation. Run it and confirm it fails for the right reason.

**GREEN:** Write the simplest code that makes the test pass. Don't optimize. Don't refactor. Don't add anything the test doesn't require.

**REFACTOR:** Now clean up both the test and the production code. Remove duplication, improve names, simplify structure. All tests should still pass after refactoring.

**COMMIT:** Make a small, focused commit. The commit message should describe the behavior added, not the implementation detail.

### Step 3: Repeat

Pick the next item from the test list. If implementing the current item revealed new cases, add them to the list. Continue until the list is empty.

## Test Types and When to Use Them

| Type | When | Examples |
|------|------|---------|
| **Unit tests** | Business logic, validations, calculations, service objects | Model specs, service specs, utility functions |
| **Integration tests** | API contracts, auth, error responses, multi-component flows | Request specs, controller specs |
| **E2E / System tests** | Critical user journeys | Onboarding flow, payment flow, login flow |

**General ratio:** 70% unit, 20% integration, 10% e2e. For API-first products, shift toward 60/30/10 since API contract stability matters more than internal implementation.

## When TDD Breaks Down

TDD is the strong default, but test-after is acceptable in these cases:

**UI / Visual work:** Write the component first, then add tests for behavior (click handlers, state changes, accessibility). Visual correctness is verified by looking at it, not by assertion.

**Exploratory / Recon work:** When you don't yet know what the behavior should be. Spike first, then write tests for the behavior you discovered. Delete the spike code and rebuild with TDD if time allows.

**Performance optimization:** Profile first to identify the bottleneck. Write a benchmark test, then optimize. The benchmark test is written first, but the optimization work itself isn't test-driven.

**Third-party API integrations:** Mock the external API first. Write tests against the mocks. Then write a small number of integration tests against the real API as secondary verification (these may be slow and flaky; that's OK).

## Common Mistakes

- **Writing too many tests at once.** One test at a time. The list tells you what's next.
- **Making the test pass with complex code.** GREEN means the simplest possible code, even if it's ugly. Refactor comes next.
- **Skipping REFACTOR.** The refactor step is where design emerges. Without it, you accumulate mess.
- **Testing implementation details.** Test behavior ("when I submit the form, the user is created") not implementation ("the create method calls save"). Implementation-coupled tests break on every refactor.
- **Not committing after each cycle.** Each RED-GREEN-REFACTOR is a commit. This gives you safe rollback points.
