# Development standard 1.0 draft

Help developers and agents deliver efficiently, correctly, and at low total cost. Select preparation, implementation, and verification by task risk to reduce waiting, duplicate work, and rework. Continue within existing authorization. Clarify material gaps in goal, scope, or permission. Prove completion with actual results.

## Common decisions

- **Can I make this change directly?** Proceed when the goal, scope and authorization are clear, the impact is known, bounded and recoverable, existing contracts and critical guarantees stay intact, and you can run an effective check independently. [Task classification](3-workflow/3.1-task-classification.md)
- **What if I do not know the impact yet?** Pause affected writes, trace callers and investigate the actual impact, then classify the work. [Requirements and design](3-workflow/3.2-requirements-and-design.md#32-requirements-and-design)
- **When does the architecture need another review?** A non-author must review the design, applicable architecture and test design before affected implementation changes critical guarantees or causes irreversible real effects. [Design and test design review](3-workflow/3.2-requirements-and-design.md#design-and-test-design-review)
- **What is still needed to merge after workspace checks pass?** Confirm authorization, the current target and the exact combination. Obtain trusted full-check results for that combination. [Integration](3-workflow/integration.md)

## Chapter index

| Reading order | Content | Use |
| --- | --- | --- |
| [1. Development principles](1-principles.md) | Scope, code design, tests, acceptance, and maintenance | First reading, planning, and code review |
| [2. Project setup](2-project-setup.md) | Project rules, current plan, tools, records, and evidence | First adoption or a material change |
| [3. Development workflow](3-development-workflow.md) | Task classification, design, implementation, review, and acceptance, including applicable state-model review before implementation | Every task. Use the [overview](3-workflow-overview.md) to locate a step. |
| [4. Periodic review](4-periodic-review.md) | Accumulated issues, new automated checks, and temporary measures | Each milestone or agreed interval |
| [5. Interaction and interface](5-interaction-and-interface.md) | Interaction and interface requirements, acceptance checklist, and evidence | UI tasks |

For Git operations, read [6. Git and GitHub collaboration](6-version-control.md) on demand: starting work, commits, pushes, merges, undo, and cleanup. It does not add a workflow stage.

Use [requirements and design](3-workflow/3.2-requirements-and-design.md#32-requirements-and-design) and [task-specific methods](3-workflow/3.5-implementation.md#351-task-specific-methods). Read templates and verification material on demand.

Report simple-task results and remaining verification briefly. Formal tasks follow the standard workflow. No UI or an existing prototype means no extra prototype. Before delegating, compare work, task relationships, and the total cost of receiving and integrating results.

| Role | Responsibility |
| --- | --- |
| Requirements owner | Sets goals and approves key choices and exceptions, with an explicitly delegated approver where needed. |
| Coordinator | Assigns work, checks evidence, resolves blockers, and advances delivery. The current executor may act as coordinator. |
| Implementer | Works and verifies within scope. Only one writer owns a file or branch at a time. |
| Independent reviewer | One non-author primary reviewer starts in a fresh session, then continues; checks results and retains attributed conclusions and original evidence. |

Use the [templates](../../assets/templates). Model scope and results are in the [verification guide](../provenance.md) and [report](../provenance.md).
