# Code review

For cross-boundary or unexpectedly broad effects, use [change impact verification](references/impact.md) to prove critical safety facts. Use [code simplification](../code-simplification/METHOD.md) for concentrated complexity without replacing independent review.

For Git delivery, use the [collaboration standard](../../standard/6-version-control.md) to compare tested, staged, PR, and combined versions. Record independent agent review separately from platform account approval.

## Scope and inputs

Review a complete, independently judgeable semantic unit or final combination, not each commit as a separate unit. Fix the task, specification, standard, base, candidate, and author. One non-author primary reviewer starts with fresh context and continues subsequent reviews without a new session each round. A reviewer who repairs implementation becomes an author and must be replaced. Keep each round's candidate stable.

When review begins before implementation, establish the expected outcomes against the approved requirements, review the design and test scenarios in one session, and record the exact inputs. Normally continue in the same session for the fixed candidate. Use the replacement process in section 3.6 when necessary. Check the complete delta for deviations and prioritize the scenarios and implementation boundaries that could break the approved guarantees. Review materially changed design inputs again before dependent implementation.

## Procedure

1. Include committed, staged, unstaged, and relevant untracked content. Record exact commits and file hashes. Fix the comparison base. A ...HEAD diff alone can miss current work.
2. Check observable requirements, boundaries, failures, and recovery. Separately review responsibilities, input parsing, dependencies, permissions, check timing, test strength, and delivery rules. Report specification and standard conclusions separately. Parallel review depends on total cost.
3. Trace affected callers and dependencies beyond the diff. Personally run minimal proofs for critical guards, state branches, and recovery. Validate reusable trusted machine evidence under [independent review](../../standard/3-workflow/3.6-independent-review.md), naming its actual executor. A different role alone does not require repeating full checks. Author-editable success records are neither trusted results nor your own execution.
4. Reproduce original failures and verify repairs. Check that tests observe public behavior, wait for async completion, and cannot pass from probe failure, missing mounting, or substitutes. Critical protection or false-green risk needs an effective failure witness; reuse valid exact-input evidence rather than requiring a new mutation for each role. Personally run critical review paths.
5. Assess the candidate under [approval and blockers](../../standard/3-workflow/3.6-independent-review.md#approval-and-blockers). For each blocker identify the applicable requirement, impact, actual and expected behavior and evidence, or the required verification that is missing. Other findings may be recorded as nonblocking suggestions, with no required change or resubmission. Reductions require project approval and replacement protection.
6. In the original task record, retain reviewer attribution, standard/spec conclusions, unresolved issues, and original evidence links for personally run commands. Zero findings is valid; do not invent changes. Bind repairs to a new candidate; the original reviewer replays failures and affected paths. Expand scope for critical interface, permission, baseline, environment changes, or unknown effects. Isolated unit passes do not replace final-combination full checks. Reviewers do not edit implementation while approving it.

## Completion and stopping

The declared complete review scope and applicable requirements are covered, critical paths were run by the reviewer, and findings/unverified scope are traceable. Failures, timeouts, recovery, and reviewer changes consume the same predetermined budget. At exhaustion, remaining blockers stop that action without automatic approval or budget reset. Without an independent context, preserve pending scope. Changed input invalidates affected conclusions. Passing review does not authorize commit, push, merge, or installation.

## Source and adaptation

Adapted from pinned Matt Pocock code-review. Retains specification and standards checks, extends scope to a fixed complete candidate, and chooses organization by total cost. No fixed two-agent split or automatic commit.
