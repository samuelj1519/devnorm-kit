---
name: devnorm
description: Route development under this project standard.
---

# DevNorm

Read project rules and inputs. Protect existing work. Stay authorized. Check affected project paths and callers for project facts, follow the current stage's bundled links for DevNorm rules, and broaden the search for a local docs edit only if evidence is missing.

<!-- devnorm:condition:simple-route:start -->
Use two task types: simple and formal. Handle a simple task directly when the goal, scope and authorization are clear, the impact is known, bounded and recoverable, the existing contract and critical guarantees stay intact, and an effective check can be performed independently. Text edits and bounded logic or settings repairs within an existing contract can qualify. Classify by actual impact, using the technology and file scope to investigate affected behavior.

Use the formal route for tasks that do not qualify as simple. Only formal tasks follow the standard workflow. Derive the necessary design, prior review, models, checks and actual acceptance from the change. One non-author primary reviewer checks the exact candidate.

For a simple task, run the necessary checks, complete applicable [Git closeout](references/standard/3-workflow/3.8-integration-and-completion.md#git-closeout), and report the result and unverified limits. Skip the full workflow, capability index and task brief. If simple-task conditions cease to hold, stop affected writes, switch to the formal workflow and invalidate affected evidence. Investigate unknown impact and stop actions lacking necessary authorization. Stricter project rules and trusted full checks before integration still apply.
Regressions or repeated failure require the standard workflow and inclusion in quality statistics.
<!-- devnorm:condition:simple-route:end -->

## Current action

For formal work, read [planning](references/standard/3-workflow/3.3-task-planning.md) and complete applicable [prior review](references/standard/3-workflow/3.2-requirements-and-design.md#design-and-test-design-review). Read only the current stage: [implement](references/standard/3-workflow/3.5-implementation.md), [review](references/standard/3-workflow/3.6-independent-review.md), or [verify](references/standard/3-workflow/3.7-verification-and-acceptance.md).

Choose one [method](references/methods/README.md) if needed. Helpers work independently.

After each independently verifiable increment passes, [commit it and confirm its SHA](references/standard/6-version-control/6.3-staging-and-commits.md) within existing authorization. A single small task can use one commit after acceptance. Use quick checks on task branches and [trusted full checks](references/standard/3-workflow/integration.md) for integration targets.

Before reporting completion, follow [Git closeout](references/standard/3-workflow/3.8-integration-and-completion.md#git-closeout). Finish pending commits and any required, authorized integration and push, then read back the remote SHA. Handle tags only for an authorized version release. Keep installation separately authorized. Report any blocked step.

Hold actions lacking tools, permission or evidence. Query unknown outcomes before retry. For formal evidence or handoff, see [records](references/standard/3-workflow/evidence-retention.md) and [reporting](references/standard/3-workflow/reporting.md) when needed. [Provenance](provenance.json).
