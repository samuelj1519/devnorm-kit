# Module design

For ambiguous concepts or terms, apply [domain concepts and decisions](references/domain.md) to scenarios, names, and record ownership.

## Scope and inputs

Use for new capabilities, unclear interfaces, frequent cross-module edits, or difficult tests. Define observable behavior, callers, constraints, and allowed changes.

## Procedure

1. Trace actual calls and list core objects, states, writers, dependency directions, and external boundaries. Map user concepts to code names and locate current complexity.
2. Design interfaces before implementation: core types, signatures, errors, and recovery outcomes. Represent legal states with explicit variants and parse external inputs at boundaries. Expose only concepts callers need.
3. For leaked implementation details or repeated caller orchestration, read [responsibilities and encapsulation](../../upstream/mattpocock/module-design/DEEPENING.md). Put complete work behind a simpler interface rather than splitting code into forwarding layers.
4. For a novel interface or responsibility with important downstream trade-offs, read [compare designs](../../upstream/mattpocock/module-design/DESIGN-IT-TWICE.md). Compare a few different shapes using the same caller, complexity, failure, testability, and migration criteria.
5. For concurrency, retries, and recovery, specify shared targets and commit order. Eliminate unnecessary sharing before serializing true single-writer constraints. Define idempotent side effects. Use [state modeling](../statechart/METHOD.md) where applicable.
6. Deliver implementable interfaces, responsibilities, ownership, inputs/outputs, transaction/recovery order, caller migration, legacy removal, checks, and acceptance. Record key decisions and sequence verifiable units as needed.

## Completion and stopping

Normal and failing caller examples work through the interface. Responsibilities, write targets, recovery, and check ownership are explicit. Unsettled semantics remain in design. Unapproved scope returns to requirements. A passing model proves its declared scope only; implementation and external hosts need runtime evidence.

## Source and adaptation

Adapted from pinned Matt Pocock codebase-design with both design references. Integrated with interface, state, and migration requirements. No fixed model, roles, or parallel count.
