---
name: devnorm
description: Handle software requirements, design, implementation, defects, review, and delivery under the project development standard. Choose direct work or the standard workflow by risk and verify actual completion.
---

# DevNorm

Read the target project's current rules and task inputs. Preserve existing work and act within existing authorization.

Use two task types: simple and formal. Handle a simple task directly when the goal, scope and authorization are clear, the impact is known, bounded and recoverable, the existing contract and critical guarantees stay intact, and an effective check can be performed independently. Text edits and bounded logic or settings repairs within an existing contract can qualify. Classify by actual impact, using the technology and file scope to investigate affected behavior.

Use the formal route for tasks that do not qualify as simple. Only formal tasks follow the standard workflow. Derive the necessary design, prior review, models, checks and actual acceptance from the change. One non-author primary reviewer checks the exact candidate.

Finish a simple task after necessary checks and a brief result with unverified limits. Skip the full workflow, capability index and task brief. If simple-task conditions cease to hold, stop affected writes, switch to the formal workflow and invalidate affected evidence. Investigate unknown impact and stop actions lacking necessary authorization. Stricter project rules and trusted full checks before integration still apply.
Regressions or repeated failure require the standard workflow and inclusion in quality statistics.

## Current action

For formal tasks, set the brief and review arrangements under [task planning](references/standard/3-workflow/3.3-task-planning.md). When applicable conditions such as changes to critical guarantees apply, first complete [design and test design review](references/standard/3-workflow/3.2-requirements-and-design.md#design-and-test-design-review). Read only the current stage: [implementation](references/standard/3-workflow/3.5-implementation.md), [independent review](references/standard/3-workflow/3.6-independent-review.md), or [acceptance](references/standard/3-workflow/3.7-verification-and-acceptance.md).

Choose one primary method: [debugging](references/methods/debugging/METHOD.md), [module design](references/methods/module-design/METHOD.md), [TDD](references/methods/tdd/METHOD.md), [code review](references/methods/code-review/METHOD.md), [runtime verification](references/methods/actual-verification/METHOD.md), or [Chinese writing](references/methods/chinese-writing/METHOD.md). Read the [method selector](references/methods/README.md) for other applicable methods, not the full capability JSON by default. Interviews, history recovery, task refinement, source maintenance and tooling setup require an explicit request. Helper skills work independently without first loading this entry.

For ordinary task-branch commits, read [commit checks](references/standard/6-version-control/6.3-staging-and-commits.md), verify the exact index and run normal quick checks. Updating an integration target requires [trusted full checks](references/standard/3-workflow/3.8-integration-and-completion.md). Push, install and release retain their own authorization and applicable acceptance.

Missing tools, permission or evidence stop only affected actions. Record why and how to resume; continue independent authorized work. Preserve initial failures and query unknown outcomes first. Changed inputs invalidate affected evidence; rework budgets remain cumulative. For user reports, handover, or completion, follow [communication and evidence retention](references/standard/3-workflow/3.8-integration-and-completion.md): reuse the authoritative record, lead with conclusions, and expand on request. [Sources and licenses](provenance.json).
