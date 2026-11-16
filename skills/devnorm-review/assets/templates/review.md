# Independent review template (1.0 draft)

Use under the [workflow](../../references/standard/3-development-workflow.md).

## <Task ID> independent review

## Conclusion and scope

<PASS / FAIL / incomplete, exact passed scope, P0/P1/P2 counts and applicable criteria. List artifacts/platforms and blockers for required unrun, failed, or unknown checks.>

## Fixed inputs and independence

| Field | Value |
| --- | --- |
| Task and standard/project rules | <exact paths, approved versions, commits> |
| Current plan/prototype/design | <version, commit, approval, task consistency> |
| Base, candidate, complete task diff | <full SHA or file manifest hashes> |
| Independent copy, branch, tested tree, dependencies | <actual origin and identities> |
| Author and reviewer sessions | <different IDs; reviewer did not implement target changes> |
| Time zone and actual executor | <values; label reused author evidence separately> |
| Scope and reduction approval | <full or approved incremental; no unapproved reduction> |

## Principles and merge conditions

Apply all 12 [review items](../../references/standard/1-principles.md#17-manual-review-checklist) and automated evidence. Confirm trusted full checks for the exact version before merge, including tests, dependencies, security, and coverage. Verify approval of check/limit changes.

## State-model review

<Section 3.2.1 applicability or N/A. Confirm pre-implementation TLC and chart review, complete required properties, and resolved blockers. Trace normal/failure/retry/timeout/cancellation/recovery, exits, and ownership. For implementation, check code/model correspondence, executable counterexamples, and actual replay. Re-review state-contract changes.>

## Actual checks

| Acceptance item | Command/action and expected/actual | Exit/status | Raw evidence and executor |
| --- | --- | --- | --- |
| <static/affected/full> | <exact command> | <value> | <reviewer or original author> |
| <public behavior/fault/actual environment> | <action and result> | <PASS/FAIL/not_run/N/A> | <path> |

## Required runtime checks and test changes

<Run applicable public entries for CLI/UI, authorization/external input, concurrency/persistence/recovery, delivered artifacts, and runtime integration. Separate storage, process, browser, and isolated-app results. Missing authority/tools remain not_run and prevent acceptance. Explain N/A for content with no runtime path.>

<Review every old test/assertion change and author explanation. Keep protection. Check current decisions, architecture, 3–5 architecture checks, and milestone security scan. Separate formal states from code replay.>

## Prove detection

<Independent original reproduction, physically isolated compilable incorrect version or removed protection, same failing assertion before repair and passing afterward, actual source/executable hashes. Explain N/A. Separate model counterexamples and implementation replay; unreplayed findings remain risks or contract gaps.>

## Findings

| ID/severity | Location and reproduction | Actual/expected and impact | Repair and recheck | Evidence |
| --- | --- | --- | --- | --- |
| <ID/P0/P1> | <file:line/command> | <behavior> | <root cause> | <raw log> |

Fail design/standard review for logic that causes incorrect or impossible execution. Style and optional suggestions do not block. Applicable behavior failures cannot be dismissed because labeled P2. Follow task/project acceptance rules. Existing checker failures remain blocking rather than subjective feedback.

## Itemized checks and unverified scope

<Each task criterion: pass/fail/not_run/N/A, reason, impact, next owner.>

## Re-review after repair

<Fresh non-author review under section 3.6, before/after versions, original finding resolution, new changes/impact, original-failure replay/evidence, expanded scope, and remaining unverified work. Keep the original report and failures.>

## Follow-up

<Next owner, pending decisions, approval, and temporary-resource retention/cleanup.>

- New-check registration: <class/count/source, task or specific automation limit; mandatory by the second similar reviewer finding; original error fails, normal passes, independent review, evidence>
