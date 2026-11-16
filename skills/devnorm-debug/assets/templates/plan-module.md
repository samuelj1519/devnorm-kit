# <Module> (current <version>)

Maintain the current plan under the [workflow](../../references/standard/3-development-workflow.md).

## Current decision (<version>, <date>)

<Complete goal, scope, choices, state owners, interfaces/data, failures, unknown results, and recovery. Do not leave the plan as patches to an old draft.>

- Standard: <approved DevNorm version and commit>; project rules: <path and version>
- Status: <approved / pending / draft>; approval source and scope: <exact reference or unknown>
- Downstream versions: <compatible prototype, detailed design, task, test, and model versions>

## Contracts

<Reason, behavior protection, inputs, outputs, errors, exclusions, cross-module dependencies, and owner for each decision.>

## Verification and unresolved issues

<Applicability of constraints, empirical checks, and formal checks. Invariants, evidence, verified and unverified scope, method, and owner.>

## State modeling and design review

Assess applicability under [section 3.2.1](../../references/standard/3-workflow/3.2-requirements-and-design.md#321-plan-state-modeling-and-review). Explain N/A.

- Applicability: <complex transitions, event interleavings, consistency risk, or N/A reason>
- Scope: <states, events, transitions, invariants, termination, bounds, assumptions>
- Correspondence: <exact plan, model, config, chart, and report versions>
- TLC: <rerun command, actual exit, each property, deadlock, termination, reachability, unchecked items>
- Chart review: <reviewer, normal/abnormal paths, exits, returns, responsibilities, conflicts, chart omissions>
- Counterexamples: <model or design defect, original failure, repair, rerun, remaining blockers>
- Decision: <pass / fail / incomplete, confirmation of critical semantics, implementation conditions>
- Implementation: <model/code entry mappings, executable counterexample tests, re-review after state-contract changes>

## Prototype and detailed-design overrides

| Old clause and version | New clause and approval scope | Retained behavior, replacement, and downstream impact |
| --- | --- | --- |
| <value or N/A> | <value> | <value> |

## Change record

| Version and date | Proposer and approver | Original statement or complete original record | Superseded scope and changes |
| --- | --- | --- | --- |
| <version/date> | <role> | <exact source; preserve original wording> | <changes and affected tasks/models> |

Keep the active decision in the body. Preserve original statements in this table or an explicit historical record. Historical content is not an execution target.

## Optional read-only preparation for delegation

<Read the existing implementation, then state goal, scope, steps, acceptance, and return conditions. Select an executor by capability and total cost.>
