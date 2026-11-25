# 2. Project setup

Check this chapter when first adopting the standard, changing its version, or changing tool capabilities. Read relevant material on demand during routine work.

## 2.1 Standard version and project rules

The common standard defines collaboration, authorization, verification, and delivery. Project rules define product facts, commands, role limits, runtime, and cleanup. Task briefs fix the task's exact input, files, people or agents, checks, and authorization.

Project rules record the outcome users or callers need, the hard constraints and acceptance criteria, and applicable default methods. Formal tasks apply those rules and add the current goal, trade-offs and verification approach to the existing task record. When goals conflict, compare options under chapter 1. The authorized owner decides whether to change a hard constraint already promised.

Project rules may add or strengthen requirements. For an exception, record the conflicting clause, reason, exact scope, risks, replacement checks, expiry, and revocation. Obtain requirements-owner approval. One project's permission does not authorize another project. Apply existing exact approvals within their original scope.

Reference the [standard](README.md) from `AGENTS.md` or an equivalent entry. Record the adopted standard version, exact commit, product-plan version, and task input version separately.

## 2.2 Plans and architecture decisions

The current plan fully describes goals, scope, interfaces, states, failures, and recovery. Implementers must not reconstruct it from successive amendments. When a prototype or detailed design changes requirements, write the confirmed decisions into the plan first, state their scope, and update the task, implementation, and tests.

Record key architecture choices in a [decision record](../../assets/templates/architecture-decision.md) approved by the requirements owner. Provide only current decisions relevant to the task. For a missing version, obsolete goal, or conflicting decision, stop the affected action. The coordinator presents the differences to the authorized decision-maker. Continue other authorized work.

## 2.3 Tooling and environment

Use the [project adoption template](../../assets/templates/project-adoption.md) to confirm actual commands, capabilities, role limits, input mutual exclusion, independent checkouts, and isolation from real environments. Record missing dependencies or permissions and resolve them within authorization.

Before work, check repository path, branch, existing changes, and actual writers. Use independent copies for long implementation, parallel work, and incorrect-version probes. Candidate and incorrect-version source, test data, and build outputs must be physically isolated. They must not share outputs, alias each other, be ancestor directories, or hard-link test artifacts. Verify the actual compiled source and executable.

Follow the [Git collaboration standard](6-version-control.md) for Git operations. At adoption, define remotes and the main branch, commit format, merge method, actual checks and approvals, retention, and cleanup. Tasks inherit these policies and record only their objects, authorization, and differences.

## 2.4 Task records and evidence

Read the task brief, project prohibitions, and one or two related records. Avoid repeatedly loading unchanged standards or shared material. Read full plans and full approval requests rather than summaries alone. Save long output within task scope. Report conclusions, commands, exit codes, blockers, and evidence paths in conversation.

Evidence identifies input versions and hashes, working directory, actual executor, session, time, commands, tool versions, samples, expected and actual behavior, exit codes, and raw logs. Preserve first failures and reruns. Distinguish author evidence from independent execution. Explain the relationship between the tested version and delivered artifact, unrun or inapplicable checks, and the next owner.

Use fictional data or approved read-only copies. Do not read credentials. Logs, screenshots, and samples must not contain secrets or unauthorized real data. On a change of executor, update progress, remaining work, evidence, and next owner.

Before reusing evidence, confirm identical source, dependencies, rules, samples, tools, environment, security data, and coverage baseline. Original logs must remain accessible and free of concurrent contamination. State the original executor, time, and reuse. Verify the original session and artifact after a tool notification, then act within existing authorization.
