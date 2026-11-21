# 4. Periodic review

Review accumulated problems and automate detection of recurring errors. Repairs still follow the [development workflow](3-development-workflow.md).

## 4.1 Scheduled checks

At each milestone or agreed interval, the assigned owner checks dependency violations, test strength, duplication, complexity, stale documentation, and quality data against the [milestone requirements](1-principles.md#18-milestone-checks). Define 3–5 architecture health checks and baselines per project. Aggregate rework, review findings, regressions, and waiting from the same authoritative task records and original logs, without parallel statistics forms for ordinary work; mark unknown data. Select appropriate tools. An unrun check is not a pass. Manual confirmation cannot replace missing required automation.

**Periodic · Long-term**: Compare mutation survival rates against the threshold agreed at adoption and handle findings under the [milestone requirements](1-principles.md#18-milestone-checks).

Repair and recheck ordinary low-risk findings directly. Apply section 3.8 for an actual merge. For changes to rules, protection, dependencies, architecture, or recurring systemic issues, create a task. Reconfirm requirements at section 3.2 and estimate work, relationships, total cost, and risk at section 3.3. Return to this review after repair. Creating a task is not a repair. Unresolved blockers prevent completion. Assign other improvements an owner and follow-up date.

On return from the main workflow, verify completed scope, exact version, and evidence, then replay the original issue. Blocked, abandoned, or partial work does not count as a repair. If a review blocker remains, preserve state and the next owner and report BLOCKED at the stop condition.

Preserve failures and pending work when tools are missing, decisions conflict, ownership is absent, or waiting expires. Notify the coordinator. Requirements-owner approval is needed for architecture, dependency, permission, or protection changes and relaxed limits. If reduced checking causes regression, propose restoring or strengthening checks. Do not hide the failure or lower the standard unilaterally.

## 4.2 Prevention and automated checks

At the first review, acceptance, or periodic-review discovery, register the defect class, source, count, and owner. Create an automation task where detection is possible. Prefer existing rules, then diff scans, dependency rules, or architecture tests. If automation is unsuitable, state the specific reason, manual procedure, and review date per [measure before judging](1-principles.md#133-root-causes-and-related-defects).

By the second reviewer discovery of the same class, a corresponding task or specific automation limitation must already exist. The coordinator fills a missing record before completion. New checks follow the standard workflow. Prove rejection of the original defect and acceptance of normal behavior, then preserve independent-review evidence. A task does not mean the check is enabled. Repair the original check for a recurrence and record regression. Reducing protection still needs approval. Register systemic findings even when discovered during direct work.

## 4.3 Long-term requirements and temporary measures

Retain approval of goals and key design, independent review in the standard workflow, actual verification, architecture rules, and test protection. Remove a tool adapter only when equivalent native behavior is available and verified.

A temporary measure may be removed only after native equivalent behavior meets the project's predetermined criteria in repeated live checks and the requirements owner explicitly approves. Removal must preserve long-term protection.

| Temporary measure | Removal conditions |
| --- | --- |
| Waiting for trust prompts and detecting session readiness | The tool explicitly reports state, session, and receipt. Repeated live checks lose no tasks and preserve the user's trust decision. |
| Input mutual exclusion and no resend for unknown results | Native behavior covers every collaboration entry and session restart, queries the original operation, prevents duplicate side effects, and stops input on failure. |
| Check, approval, and notification adapters | Native behavior provides equivalent blocking, feedback, stable identity, deduplication, and recovery. Notifications do not grant authorization. |

## 4.4 Improving and maintaining the standard

At task or phase completion, record new issues, root causes, protection, sources, and unverified items in existing task records. State when nothing new was found. Avoid duplicate documents. Unverified proposals are not active rules.

For a material agent-skill or workflow change, compare representative tasks on a limited scope. Use identical goals, inputs, and acceptance criteria for old and new methods. Record tool, model, and environment differences. Blind reviewers to candidate names where practical. Compare delivery quality, elapsed time, total tokens, integration effort, and rework cost. Judge effectiveness by data per [measure before judging](1-principles.md#133-root-causes-and-related-defects); self-reported compliance and document completeness do not prove it. Also observe unnecessary changes from false findings, duplicate records/handovers, whether users can find results/risks/actions, and every agent's input, cached input, output, and cost. Also check repeated reading, rewritten briefs, unchanged reruns, fragmented approvals, and report-driven exhaustive work against existing simplification requirements; remove unnecessary increments without reducing protection. Attribute time from existing logs, distinguishing end-to-end wall time, actual processes, and gaps between processes. Model/tool timing fields may overlap: do not add them or interpret API fields as pure network latency, and do not attribute unclassified waiting to the model. Use available data and mark gaps unknown, without a new timing ledger or telemetry system for every task. Keep underfunded, unbilled, or uncertain comparisons unverified; fewer files or shorter replies do not establish efficiency.

Before a trial, agree on goals, measurement rules, scope, stop conditions, and authorization. Do not expand adoption after regression, insufficient benefit, or incomparable conditions. Retain the current method, preserve reasons, and decide whether to gather evidence or end the trial. Trial authorization does not relax existing protection.

To turn project experience into a general rule, obtain independent evidence from at least two different projects per [measure before judging](1-principles.md#133-root-causes-and-related-defects). Repeated incidents in one project are not two projects. First extract the principle that can catch this class of failure again, then rewrite the existing chapters and smooth the full text so the new understanding and the old provisions become one set of wording. Where an automatic check can be created, follow section 4.2; do not add another rule that people must remember. Mention examples in the original sentence; do not open a new appendix or append parallel clauses. State applicability, cost, and risk. Complete the scoped trial, independent review, and requirements-owner approval before adoption into the formal standard. Do not promote a practice still in trial into a general rule. Approve the scope of a check-reduction trial in advance. Stop the trial immediately if protection fails, and recheck under the original requirements.

A release records exact content, approval scope, results, and activation. Projects explicitly choose a version. The latest document does not apply automatically. Remove superseded active instructions and broken links while retaining evidence that supports current conclusions. Avoid conflicting execution instructions.
