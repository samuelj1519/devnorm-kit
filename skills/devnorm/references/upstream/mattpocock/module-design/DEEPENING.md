<!-- DevNorm adaptation of Matt Pocock codebase-design/DEEPENING.md. MIT; source and copyright retained. Replaces blanket test deletion with coverage-preserving migration. -->

# Responsibilities and encapsulation

Keep the interface simpler than the implementation. A few domain operations should complete useful work. Reduce the state, order, and dependency details callers must remember rather than adding layers.

## Dependencies and verification

- In-process computation: verify inputs and observable output through the public interface after consolidating related logic.
- Locally replaceable dependency: use a reliable actual local implementation to test business/storage boundaries. State its limits and differences from production.
- Owned remote service: define a domain interface at a real network boundary. Production and test adapters own transport; callers do not manage it.
- Third-party service: separate external protocol from business rules. A substitute proves local handling only. The real contract needs authorized integration checks.

Add abstractions for demonstrated production/test callers, not hypothetical replacements. Keep test-only replacement points internal rather than expose them to unrelated callers.

## Migration

Freeze current public behavior first. After the new interface covers existing callers and failures, migrate every caller and delete obsolete APIs. Remove an old test only when equivalent or stronger behavior protection has actually run and the old test is redundant. Internal-test labels do not justify lower coverage or quality.

Check call-chain length, shared mutable state, error/recovery order, and how many responsibilities one requirement change affects.
