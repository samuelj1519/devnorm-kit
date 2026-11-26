# 3. Development workflow

Handle simple low-risk tasks directly. Use the seven-step standard workflow for other work. Complete full checks before an actual merge. See the [overview](3-workflow-overview.md) and complete [project setup](2-project-setup.md) for a new project.

Follow the evidence dependencies in sections 3.2–3.8 for formal tasks. Complete applicable design, test design and state-model review before the affected implementation. After author checks, hand off the exact candidate. Review and acceptance can proceed according to their dependencies. Keep mandatory gaps pending. After independent review, verify the exact combination with the current integration target. Agree on waiting and rework counts or time limits in the task brief before execution. At a limit, preserve progress, notify the coordinator, stop, and report `BLOCKED`. Send approval decisions to the requirements owner. On resumption, recheck versions, inputs, and permissions, then return to the original step without expanding authority. Direct tasks do not require a retroactive task brief.

## 3.1 Task classification

Decide whether the change can proceed directly. If impact is unknown, pause affected writes and investigate. [Task classification](3-workflow/3.1-task-classification.md)

## 3.2 Requirements and design

Determine impact, design and acceptance criteria. Check whether critical guarantees are affected and which implementation needs prior review. [Requirements and design](3-workflow/3.2-requirements-and-design.md) · [Design and test design review](3-workflow/3.2-requirements-and-design.md#design-and-test-design-review)

### 3.2.1 Plan state modeling and review

[Read details](3-workflow/3.2-requirements-and-design.md#321-plan-state-modeling-and-review).

## 3.3 Task brief and work allocation

[Read this section](3-workflow/3.3-task-planning.md).

## 3.4 Execution environment

[Read this section](3-workflow/3.4-execution-environment.md). For permission provisioning when dispatching other assistants, see [section 3.4.1](3-workflow/3.4-execution-environment.md#341-agent-permission-provisioning).

## 3.5 Implementation and self-check

[Read this section](3-workflow/3.5-implementation.md).

### 3.5.1 Task-specific methods

[Read details](3-workflow/3.5-implementation.md#351-task-specific-methods).

### 3.5.2 Conditional test-driven development

[Read details](3-workflow/3.5-implementation.md#352-conditional-test-driven-development).

## 3.6 Independent review

[Read this section](3-workflow/3.6-independent-review.md). For exact candidates and trusted re-verification, see [section 3.6.1](3-workflow/3.6-independent-review.md#361-exact-candidate-and-trusted-re-verification).

## 3.7 Verification and acceptance

[Read this section](3-workflow/3.7-verification-and-acceptance.md).

## 3.8 Merge and completion

Obtain trusted full-check results for the exact combination before any authorized integration update. Close out applicable commits, remote delivery, and any version release before reporting completion. [Integration](3-workflow/integration.md) · [Integration and completion](3-workflow/3.8-integration-and-completion.md)
