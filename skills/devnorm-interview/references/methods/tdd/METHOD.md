# Conditional test-driven development

Use for defined business rules, calculations, parsing, state decisions, and cheaply reproducible defects, or when the user explicitly requests TDD. Establish public behavior, representative inputs, and the test boundary, then implement one behavior at a time instead of writing every unit test first.

## Choose the test level

- Prefer unit tests for pure logic. Use integration or contract tests for persistence, protocols, and service boundaries. Concurrency, retries, and recovery still require applicable modeling and real acceptance.
- Turn a stable defect reproduction into a failing regression test before repair. Preserve existing behavior before refactoring without mixing requirement changes.
- Verify UI exploration, prototypes, copy, and simple configuration according to risk. Investigate unclear behavior or use a minimal experiment when tests are disproportionately costly; record the alternative. Do not add extensive mocks merely to claim TDD.

## Small cycles

1. Derive one observable expectation from confirmed requirements or an independent example and exercise the public interface. Confirm it fails because behavior is missing or wrong. Compilation, import, environment, and probe failures are not a valid red.
2. Implement only the current behavior, pass the same test, and check affected behavior. Do not copy the implementation algorithm or generate expectations from its incorrect output.
3. Make necessary local structural improvements while tests stay green. Preserve boundaries, errors, and side effects. Return behavior changes to design; never alter assertions or skip checks just to pass.
4. Select the next behavior and repeat. Preserve actual red/green commands and exits. Do not seek separate approval for each already clear interface within existing scope.

## Completion and stopping

Use appropriate tests for agreed behavior, failures, and side effects. Prove critical protection rejects a runnable wrong version. TDD does not replace independent review, actual-host acceptance, or full merge checks. Existing budget, test-protection, and stop rules remain effective. State unexecuted or inapplicable scope; test counts are not quality evidence.

Source: informed by pinned Matt Pocock tdd on public behavior, independent expectations, and small cycles. Adapts it to conditional red-green-refactor without per-interface approval or excluding refactoring from the cycle. See [Martin Fowler](https://martinfowler.com/bliki/TestDrivenDevelopment.html) for the classic cycle.
