# Select a method when needed

## Select a method

| Condition | Method |
| --- | --- |
| Critical requirements gaps or settled discussion needing consolidation | [Requirements and specification](requirements/METHOD.md) |
| Important uncertainty requiring primary evidence or a minimal experiment | [Research](research/METHOD.md) |
| New or changed modules, interfaces, shared state, or responsibilities | [Module design](module-design/METHOD.md) |
| A new UI question without a usable prototype | [Interface design](frontend-design/METHOD.md) |
| State, concurrency, retries, transactions, or recovery requiring a model | [State modeling](statechart/METHOD.md) |
| Multi-step work or execution allocation | [Task planning](task-planning/METHOD.md) |
| Wrong behavior, exceptions, or performance regression | [Defect diagnosis](debugging/METHOD.md) |
| Defined rules, cheap defect reproduction, or an explicit TDD request | [Conditional TDD](tdd/METHOD.md) |
| New abstractions, forwarding, or patch branches need simplification | [Code simplification](code-simplification/METHOD.md) |
| Reporting or acting on speed or resource measurements | [Performance measurement](benchmark/METHOD.md) |
| Independent review of a complete candidate | [Code review](code-review/METHOD.md) |
| Acceptance in an actual CLI, browser, service, or native app | [Runtime verification](actual-verification/METHOD.md) |
| Existing UI interaction, presentation, accessibility, or boundary review | [Interface review](interface-review/METHOD.md) |
| Skills, project agent rules, or other agent-readable documents | [Writing for agents](agent-writing/METHOD.md) |
| Writing, rewriting, proofreading, or reviewing Chinese technical content | [Chinese technical writing](chinese-writing/METHOD.md) |
| Explain implementation or draft delivery text | [Delivery writing](delivery-writing/METHOD.md) |
| Milestones or recurring defects need improvement | [Periodic review method](periodic-review/METHOD.md) |

## Explicitly requested functions

Run the following only when the user prompt explicitly requests the function. Relevance, a reference, or upstream advice is not activation. Natural language is sufficient; no special command is required. Current-task reading, necessary clarification, and normal acceptance still follow the standard. This is a bundle instruction, not a claim of host-enforced execution control.

| Example request | Method |
| --- | --- |
| Interview me about this requirement, at most three rounds | [Decision interview](requirements/METHOD.md#explicit-request-decision-interview) |
| Recover this project's previous-session context | [Context recovery](context-recovery/METHOD.md) |
| Deepen this task and rewrite the prompt | [Task refinement](task-refinement/METHOD.md) |
| Create or maintain repeatable project verification | [Verification authoring](actual-verification/references/maintenance.md) |
| Configure project check hooks or document human authorization steps | [Project tooling](project-tooling/METHOD.md) |
| Triage this specified repository's issue/PR batch | [Feedback triage](feedback-triage/METHOD.md) |
| Manually check/manage sources or analyze new capabilities | [Source maintenance](source-maintenance/METHOD.md) |
