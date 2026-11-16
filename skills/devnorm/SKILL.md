---
name: devnorm
description: Handle software requirements, design, implementation, defects, review, and delivery under the project development standard. Choose direct work or the standard workflow by risk and verify actual completion.
---

# DevNorm

Read the target project's current rules and task inputs. Preserve existing work and act within existing authorization.

Proceed directly when goal, scope and authorization are clear, impact is known and recoverable, critical guarantees stay intact, and you can independently verify the result. Text edits and bounded logic or settings repairs within an existing contract can qualify. Technology and file count alone do not determine risk.

For functional, interface or cross-module changes with bounded risk and unchanged critical guarantees, use the ordinary workflow: a short brief, necessary design, affected checks, brief independent review and applicable acceptance.

Changed permissions or trust boundaries, shared-write or transaction ordering, data integrity/migration/recovery guarantees, irreversible real effects, or unknown impact require the high-risk workflow: prior plan/architecture review, applicable models, full independent review and real acceptance.

Finish direct work after necessary checks and a brief result with unverified limits. Do not load the full workflow, capability index or task brief for it. New risk stops affected writes and escalates the task, invalidating affected evidence. Stricter project rules, actual authorization and full checks before updating integration targets still apply.
Regressions or repeated failure require the standard workflow and inclusion in quality statistics.

## Current action

Ordinary tasks use [task planning](references/standard/3-workflow/3.3-task-planning.md) and a short brief. High-risk work first completes [design review](references/standard/3-workflow/3.2-requirements-and-design.md). Read only the current stage: [implementation](references/standard/3-workflow/3.5-implementation.md), [independent review](references/standard/3-workflow/3.6-independent-review.md), or [acceptance](references/standard/3-workflow/3.7-verification-and-acceptance.md).

Choose one primary method: [debugging](references/methods/debugging/METHOD.md), [module design](references/methods/module-design/METHOD.md), [TDD](references/methods/tdd/METHOD.md), [code review](references/methods/code-review/METHOD.md), [runtime verification](references/methods/actual-verification/METHOD.md), or [Chinese writing](references/methods/chinese-writing/METHOD.md). Read the [method selector](references/methods/README.md) for other applicable methods, not the full capability JSON by default. Interviews, history recovery, task refinement, source maintenance and tooling setup require an explicit request. Helper skills work independently without first loading this entry.

For ordinary task-branch commits, read [commit checks](references/standard/6-version-control/6.3-staging-and-commits.md), verify the exact index and run normal quick checks. Updating an integration target requires [trusted full checks](references/standard/3-workflow/3.8-integration-and-completion.md). Push, install and release retain their own authorization and applicable acceptance.

Missing tools, permission or evidence stop only affected actions. Record why and how to resume; continue independent authorized work. Preserve initial failures and query unknown outcomes first. Changed inputs invalidate affected evidence; rework budgets remain cumulative. Report changes, actual checks and unverified limits. [Sources and licenses](provenance.json).
