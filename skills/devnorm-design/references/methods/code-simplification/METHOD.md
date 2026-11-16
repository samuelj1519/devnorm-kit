# Code simplification

Use for new abstractions, forwarding chains, repeated shapes, patch branches, or hard-to-trace state. Length alone is not a reason to rewrite.

1. Fix required public behavior, errors, and side effects. Read callers and existing behavior tests first.
2. Remove unused code and repeated conversions. Collapse single-caller forwarding without its own responsibility and narrow mutable state. Express constraints in types/data when appropriate rather than repeated guards or comments.
3. Stay within allowed scope and reduce reading and maintenance cost. Do not sacrifice boundary checks, errors, useful comments, or performance evidence for fewer lines.
4. Replay affected behavior and original failures. Return behavior changes to design. Keep existing code when there is no meaningful improvement.

Completion means preserved behavior, clear responsibility, and demonstrably reduced complexity. The executor can perform this pass; additional agents depend on project rules and total cost. No custom role is required. Acceptance and independent review remain applicable.

Source: adapted from pinned pstack principle-laziness-protocol and principle-minimize-reader-load. Omits unconditional comment deletion and fixed punctuation preferences.
