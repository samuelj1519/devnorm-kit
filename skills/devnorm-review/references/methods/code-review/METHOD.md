# Code review

For cross-boundary or unexpectedly broad effects, use [change impact verification](references/impact.md) to prove critical safety facts. Use [code simplification](../code-simplification/METHOD.md) for concentrated complexity without replacing independent review.

For Git delivery, use the [collaboration standard](../../standard/6-version-control.md) to compare tested, staged, PR, and combined versions. Record independent agent review separately from platform account approval.

## Scope and inputs

Review the complete candidate before acceptance or merge. Fix the task, specification, standard, base, candidate, and author. Use a fresh non-author context and keep the candidate stable.

## Procedure

1. Include committed, staged, unstaged, and relevant untracked content. Record exact commits and file hashes. Fix the comparison base. A ...HEAD diff alone can miss current work.
2. Check observable requirements, boundaries, failures, and recovery. Separately review responsibilities, input parsing, dependencies, permissions, check timing, test strength, and delivery rules. Report specification and standard conclusions separately. Parallel review depends on total cost.
3. Trace affected callers and dependencies beyond the diff. Personally run minimal proofs for critical guards, state branches, and recovery. Author logs help locate commands; they are not your execution.
4. Reproduce original failures and verify repairs. Check that tests observe public behavior, wait for async completion, and cannot pass from probe failure, missing mounting, or substitutes. Critical protection or false-green risk needs an effective failure witness; reuse valid exact-input evidence rather than requiring a new mutation for each role. Personally run critical review paths.
5. Keep evidenced findings with location, trigger input, actual/expected behavior, impact, and minimal reproduction. Separate blockers, suggestions, environment failures, and unrun work. Reductions require the project approval and replacement protection.
6. Deliver standard/spec conclusions and personally run commands. Bind repairs to the new candidate and replay original/affected paths. Reviewers do not edit implementation while approving it.

## Completion and stopping

The complete candidate and applicable requirements are covered, critical paths were run by the reviewer, and findings/unverified scope are traceable. Without an independent context, preserve pending scope. Changed input invalidates affected conclusions. Passing review does not authorize commit, push, merge, or installation.

## Source and adaptation

Adapted from pinned Matt Pocock code-review. Retains specification and standards checks, extends scope to a fixed complete candidate, and chooses organization by total cost. No fixed two-agent split or automatic commit.
