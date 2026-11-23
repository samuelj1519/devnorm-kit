# Task brief template (1.0 draft)

Use under the [development workflow](../../references/standard/3-development-workflow.md). Formal tasks prefer the [short brief](task-short.md) and use applicable sections here when more detail is needed. Simple tasks need no brief. Expand fields by applicable risk within the existing authoritative task record, without duplicating the six-field brief or development/acceptance/review records. Replace placeholders and save in the project's task directory, satisfying its checker fields.

## <Task ID>: <observable outcome>

- Status: <pending / active / independent review / recheck / approval / completed scope>
- Standard: DevNorm <approved version> at <package artifactHash or full source commit>; project rules: <path/version>
- Task type: <design / prototype / implementation / review / recheck / integration>
- Change impact  <changed contracts or critical guarantees, evidence of recoverability and checks, applicable prior review, and classifier. Investigate unknown impact first>
- Checks: <full / affected checks then pre-merge full / identical-input reuse then isolated combination and milestone full checks before actual merge>; authority: <section 3.3, stricter project rules, separate exception approvals>
- Milestone: <name/boundary or N/A>
- Implementer: <one role/session>; primary reviewer: <non-author ID; fresh first review, then continuation; or pending assignment>
- Working location: <absolute path, branch, writer, reason>
- Semantic review unit: <complete behavior, related invariants, tests, and docs; separate from subtasks/commits; final combination verified separately>
- Fixed task base: <full 40-character SHA>; review candidate: <full SHA or file manifest/hashes if uncommitted>
- Plan module: <exact path/version>; consistency check: <match/conflict>
- Prototype/design: <existing artifact version and approval; no extra prototype without UI or where a prototype exists; explain N/A>
- Preconditions: <interfaces/tasks/fixed versions or none>
- Skills/tools: <allowed capabilities, actual tool/model, limits/remaining quota or unknown>
- Git authorization: <draft edits / commit / named push or PR / named integration; apply existing authorization separately, without inferring it from implementation>
- Git execution: <inherited project policy; remote/source commit/target ref, ownership of existing staged and working-tree changes, tested/intended commit versions, necessary policy differences; follow the [collaboration standard](../../references/standard/6-version-control.md)>
- Architecture/current decisions: <paths, hashes, approval scope>
- Plan state review: <section 3.2.1 applicability, plan/model versions, TLC and chart review; complete applicable checks before implementation dispatch>
- Rework/wait limits: <agree rounds, runtime, and resources beforehand; failures/timeouts/recovery/replacements accumulate; no copied model-example budgets>
- Architecture/security: <milestone 3–5 health checks, commands, owner; identify missing configuration>
- Test changes: <none or location/reason/original protection; preserve protection and review separately>

## Goal and scope

<Goal, failures, unknown results, recovery, observable acceptance, exclusions.>

## Integration contracts

The coordinator defines:

- <signature, inputs/outputs/errors, state owner, version, callers>
- <one integration owner for shared files, locks, and generated output; stop point for missing preconditions>

## Allowed files

- <path>
- <path>

- Four check triggers: <pre/post-write, commit, pre-merge, milestone; actual project commands under the [principles](../../references/standard/1-principles.md#15-automated-check-schedule)>
- Check/limit changes: <none or proposed reduction, reason, replacement protection, requirements-owner approval; no author self-approval>
- Existing assertions: <necessary spec change, approval, assigned test owner; preserve until approved>
- Combination/merge: <only an isolated combination before full checks; trusted full checks for the exact version before actual merge>

## Verification plan

Reference relevant commitments in product behavior, architecture and module organization, and core algorithms and code logic. At design review, record applicable unit, integration, and acceptance scenarios, what to observe, expected results, and environment. Cite actual evidence for the exact candidate in the same record after implementation.

Use applicable [task-specific methods](../../references/standard/3-workflow/3.5-implementation.md#351-task-specific-methods). Record a refactor behavior baseline, batch sample, or performance comparison only when applicable. For observable uncertainty, record a minimal experiment's input, expectation, and observation.

| Required behavior/risk | Method | Exact command/action and expectation | Owner/log |
| --- | --- | --- | --- |
| <scope/version/permission/sample> | Constraint | <command/exit> | <role/path> |
| <normal/boundary/failure/recovery> | Empirical | <public result, sample, actual side effects> | <role/path> |
| <old defect/protection> | Empirical | <runnable incorrect version fails, repair passes, or N/A reason> | <independent source/build directories> |
| <plan state/implementation mapping> | Formal and empirical | <review, properties, mapping, executable counterexamples/replay, or N/A> | <owner/path> |
| <project full checks/isolated recheck> | Project checks | <command, TASK_CARD/fixed BASE, exact tested tree> | <role/path> |
| <UI/real host/actual artifact> | Empirical | <pointer/keyboard/focus/scroll, platform/prototype comparison, or N/A> | <role/path> |

For UI, record applicability, requirement, result, evidence, and repair task for [5.8.1 through 5.8.11](../../references/standard/5-interaction-and-interface/5.8-ui-acceptance.md). Use defaults for missing project requirements, explain N/A, and mark unrun checks `not_run`.

Choose scope before work under [section 3.3](../../references/standard/3-workflow/3.3-task-planning.md#33-task-brief-and-work-allocation). Obtain approval for additional reductions. For real models or real data, record authorization, counts, input/output limits, timeout, and failure-counting rules. Otherwise use fictional samples or test substitutes.

## Independent review and acceptance

- <One non-author primary reviewer, fresh first review then continuation; applicable rules, complete semantic unit, personally run critical behavior; attributed conclusions/evidence allowlist in original record; replace after implementation edits>
- <PASS criteria, required-unrun stop point, applicable P0/P1/behavior blockers; exact approval for any review waiver>
- <Recheck owner, exact combined tree, local integration scope, recheck after source/environment change or conflict>
- <Separate delivered artifact, native app, real backend, and model checks; keep missing execution not_run>

## Isolation, authorization, and stopping

- Test data: <fictional generation or temporary read-only copy; original protection>
- Temporary resources: <exact roots, owner/process/source/target, later consumers, cleanup authority, retained evidence>
- Collaboration input: <[section 3.4](../../references/standard/3-workflow/3.4-execution-environment.md#34-execution-environment) acquire/hold/release owner and target, launch batch/time; approved equivalent evidence or stop if absent>
- Restricted actions: <approved or unapproved dependencies, permissions, installation, real reads/writes, deletion, sends, push>
- Stop conditions: <scope/version conflict, missing dependency, uncertain identity, unknown side effect, failed checks or isolation>
- GUI authorization: <project per-action CUA scope or N/A; no automatic renewal>

## Periodic review and metrics

- Origin: <ordinary work or review finding ID; reclassify review repairs>
- Rework/review findings: <actual counts or unknown>
- Post-merge regressions/observation: <count or unknown, linked repair tasks; do not rewrite old PASS>
- Duplicate-code growth: <baseline, current value, tool, or unknown>
- Dependency/architecture rejection: <edge, check, repair, original failure/recheck>
- Temporary-measure removal proposal: <native equivalent, predetermined repeated-live criteria/evidence, exact approval; retain incomplete requirements>

## Acceptance result

- Candidate/base/input hashes, executor/session, start/end/time zone: <values or unknown>
- Commands/actions, exit codes, original failures, reruns, raw logs: <links>
- Independent review/recheck: <reports, tested-tree/artifact relation; state incompleteness>
- Unrun/unknown/N/A: <item, reason, effect, next owner>
- Outcome/next step: <verified scope, pending approval/integration/delivery>
- Temporary resources: <actual cleanup, retained items, owners>
- Lessons: <symptom, cause, protection, source, applicability, pending verification; or no new findings>
- New-check registration: <class/count/source, automation task or specific limitation; required by the second similar reviewer finding; old error rejected, normal accepted, independent review, evidence>

Update owner and progress when executors change. Link original logs.

## Return conditions for delegated work

Complete this section only after delegation is justified.

1. Return conditions: <same defect after the agreed substantive-repair count; unapproved files/interfaces/permissions; ambiguous requirements or preconditions. Agree counts beforehand. Separate reruns, environment failures, and expected negative probes.>
2. Stop and record: <stop writing; record exact version, directory, original error/log, attempted repairs, affected files, decisions needed. Query the original operation for unknown outcomes.>
3. Resolution and follow-up: <coordinator distinguishes plan, code, environment, and permissions, assigns repairs, and obtains out-of-scope approval. Review total cost, usage, and quality at the observation point agreed before adoption. Keep unknowns unknown.>

After a plan changes implementation, acceptance, or permissions, record the new version and recheck affected areas. Repeated returns require a different split or one executor. Budgets accumulate continuously. Planning reads implementation without editing it, but may write plans. A session that edited implementation cannot independently review the same task.

## Applicable pre-implementation review

When section 3.2 requires prior review of the current increment, record the exact design, architecture and test design inputs, reviewer, conclusion, blockers and actual review evidence before substantive implementation. Check data ownership, async changes, validation at final commit, and the initial, failure and retry paths. Record expected results, observable side effects and evidence for affected guarantees. Implementation review cannot retroactively satisfy this step. Direct low-risk tasks need no brief.
