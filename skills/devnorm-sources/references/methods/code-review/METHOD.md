# Code review

Review the complete candidate under [independent review](../../standard/3-workflow/3.6-independent-review.md). For cross-boundary or unexpectedly broad effects, follow [change impact verification](references/impact.md). Trace callers, dependencies, shared writes, state branches and recovery. Personally run the smallest proof for required critical paths.

Confirm that tests observe public behavior, wait for async completion and detect invalid results from failed probes, missing mounts or substitutes. Critical protections or false-pass risks need a runnable failure witness. Reuse valid exact-input evidence under the review rules. For Git delivery, use the [collaboration standard](../../standard/6-version-control.md) to compare tested, staged, PR and combined versions. Record independent agent review separately from platform account approval.

Implementers can use [code simplification](../code-simplification/METHOD.md) for concentrated complexity before freezing the candidate. Treat optional simplification found during review as a nonblocking suggestion.

## Source and adaptation

Adapted from pinned Matt Pocock code-review. The standard governs review of both specifications and requirements. This method adds impact tracing and false-pass checks.
