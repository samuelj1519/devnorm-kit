# Code simplification

After applicable implementation checks pass and before freezing the candidate, simplify new abstractions, forwarding chains, repeated logic, patch branches, or hard-to-trace state as needed. Identify the reading or maintenance cost to reduce.

1. Fix required public behavior, errors, and side effects. Read callers and existing behavior tests first.
2. Remove unused code and repeated conversions. Collapse single-caller forwarding without its own responsibility and narrow mutable state. Express constraints in types/data when appropriate rather than repeated guards or comments.
3. Stay within allowed scope and reduce reading and maintenance cost. Do not sacrifice boundary checks, errors, useful comments, or performance evidence for fewer lines.
4. Replay affected behavior and original failures. Return behavior changes to design. Keep existing code when there is no meaningful improvement.

Completion means preserved behavior, clear responsibility, demonstrably reduced complexity, and passing affected checks. The original executor can perform the pass. Delegate to a helper such as `code-simplifier` when justified and handoff cost is manageable. Helpers who edit code are implementers. When the task requires independent review, a non-author primary reviewer checks the final candidate.

Source: adapted from pinned pstack principle-laziness-protocol and principle-minimize-reader-load. Omits unconditional comment deletion and fixed punctuation preferences.
