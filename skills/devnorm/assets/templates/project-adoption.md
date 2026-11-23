# Project adoption

Record the adopted version, project differences, and actual check commands under [project setup](../../references/standard/2-project-setup.md).

## AGENTS.md or equivalent entry

Replace placeholders with approved project versions and paths.

```markdown
This project adopts DevNorm version <version>.
Actual standard location: <installed package standard entry or an accessible project path>
Adoption identity: <approved release artifactHash; exact complete commit when adopting source>
Adoption approval: <source, date, exact scope>
Project differences: <path and version>
Execution contract: <table below or existing project rules: resources, checks, trusted origins, isolation, evidence>
If required resources, command mappings, or authorization are missing, stop dependent actions and report the gaps.

At task start, read this entry, the task, and relevant plan/progress records.
On adoption or version change, check the standard entry and project differences.
Follow workflow sections 3.1 through 3.8. Read interaction and interface for UI work.
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
| UI applicability | <map [5.8.1 through 5.8.11](../../references/standard/5-interaction-and-interface/5.8-ui-acceptance.md) to project requirements and evidence. Use defaults for gaps. List old/new, risks, replacement protection, and approval before reducing requirements> |
| Standard and method resources | <accessible main entry and every standalone skill, adopted identities, dependencies, and licenses; no sibling skill or maintainer-local path dependency> |
| Verification commands | <actual quick, affected, and full commands and scope; test-diff protection, static/public/native/real-service behavior; trusted toolchain and comparison-baseline origins; gaps are not run, never an empty successful check> |
| State-model review | <section 3.2.1 applicability, statechart/TLC entry, plan/model records, chart-review owner, implementation counterexamples> |
| Continuous production deployment, where applicable | <existing release procedure and owner; exact artifact and authorization; exposure, observation window, signals and thresholds; pause, containment or recovery rehearsal, and evidence of restored behavior and affected data; see [verification and acceptance](../../references/standard/3-workflow/3.7-verification-and-acceptance.md)> |
| Task classification and checks | <criteria for handling simple tasks directly, one formal-task record and non-author primary reviewer, applicable prior review, models and actual acceptance, and approved project trials> |
| Writers | <single owners of shared interfaces, generated content, locks, aggregate state> |
| Git/checkouts | <under the [collaboration standard](../../references/standard/6-version-control.md): remotes/main branch, branches/writers, commit format/language, merge method, quick/full checks and trusted execution, actual approval accounts, tag/evidence retention, cleanup and history exceptions; state platform gaps and replacement safeguards> |
| Input mutual exclusion | <acquire/hold/release owners, target, launch batch/time, stop on failure; equivalent replacement needs evidence and exact approval> |
| Isolation | <clean input copy/worktree, fictional samples, test-data/runtime-output directories, trusted execution entry, real app identity, CUA limits; missing environment means not run, not inapplicable> |
| Evidence/status | <existing authoritative task record, accessible original logs and access controls, failure/unrun terms, retention-policy reference; protect active/open/referenced evidence and exclude private material from packages> |
| Temporary resources | <owners and previous values for creating/verifying/releasing processes, locks, worktrees, temporary permissions and configuration; query unknown outcomes, preserve restoration failures, and leave others' or investigated material intact> |
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
