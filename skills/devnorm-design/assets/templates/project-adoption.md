# Project adoption

Record the adopted version, project differences, and actual check commands under [project setup](../../references/standard/2-project-setup.md).

## AGENTS.md or equivalent entry

Replace placeholders with approved project versions and paths.

```markdown
This project adopts DevNorm version <version>.
Standard: <standard repository>/standard/README.md
Exact standard commit: <approved complete 40-character SHA>
Adoption approval: <source, date, exact scope>
Project differences: <path and version>

At task start, read this entry, the task, and relevant plan/progress records.
On adoption or version change, check the standard entry and project differences.
Follow workflow sections 3.1 through 3.8. Read UI acceptance for UI work.
Recheck working location on session start or change. Read section 3.4 before input or approval.
Use periodic review for scheduled checks and improvements.
Project rules add or strengthen requirements. Exceptions need exact requirements-owner approval.
```

## Roles and existing interfaces

<Requirements owner, delegated approvers, coordinator, implementer, independent reviewer, and permissions. Preserve existing tool commands, environment variables, and arguments. Record adapter mappings.>

## Required project information

| Item | Project value |
| --- | --- |
| Product/plan authority | <goal documents, module versions, historical boundary> |
| Prohibitions and authorization | <real data, credentials, network, install, Git operations, exact approvals; no expansion> |
| Roles and skills | <implementation/review/coordination, disabled executors, actual models, quota checks> |
| UI applicability | <map [5.1 through 5.11](../../references/standard/5-ui-acceptance.md) to project requirements and evidence. Use defaults for gaps. List old/new, risks, replacement protection, and approval before reducing requirements> |
| Verification commands | <static, affected, full, public behavior, native apps, real services, actual capabilities> |
| State-model review | <section 3.2.1 applicability, statechart/TLC entry, plan/model records, chart-review owner, implementation counterexamples> |
| Risk mapping | <small/large criteria and section 3.3 arrangement; unapproved reductions retain original checks> |
| Writers | <single owners of shared interfaces, generated content, locks, aggregate state> |
| Git/checkouts | <under the [collaboration standard](../../references/standard/6-version-control.md): remotes/main branch, branches/writers, commit format/language, merge method, quick/full checks and trusted execution, actual approval accounts, tag/evidence retention, cleanup and history exceptions; state platform gaps and replacement safeguards> |
| Input mutual exclusion | <acquire/hold/release owners, target, launch batch/time, stop on failure; equivalent replacement needs evidence and exact approval> |
| Isolation | <fictional samples, separate source/test/build directories, real app identity, CUA limits or N/A> |
| Evidence/status | <task/report/log paths, first failures, unrun definitions, private-data boundary> |
| Alignment | <approved standard version, next reviewer, conflicts/exceptions> |

## Architecture and periodic review

- <Responsibilities, dependency rules, invariants, and current approved decisions>
- <Dependency guard, actionable errors, 3–5 architecture checks with baselines/limits, milestone security scan, tool choice without forced installation>
- <Milestone/interval, review owner, findings, task creation, main-workflow repair, return and recheck>
- <Four task metrics and new-check tasks/limitations, mandatory registration by a second similar reviewer finding>
- <Long-term and temporary requirements, native-equivalent/repeated-live/approval removal conditions>

## Exceptions

| Rule ID | Project condition and reason | Exact difference, risk, replacement protection | Approval, expiry, revocation | Status |
| --- | --- | --- | --- | --- |
| <ID or none> | <reason> | <content> | <source; pending conflicts remain unresolved> | <pending / active / revoked> |

During adoption, test normal tasks and deliberately incorrect versions or out-of-scope tasks. Confirm acceptance and rejection separately.
