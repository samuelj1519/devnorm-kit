# Development workflow overview

Classify the task under [section 3.1](3-workflow/3.1-task-classification.md#31-task-classification). Other work follows sections 3.2 through 3.8, with full checks before merge. Detailed collaboration, methods, transitions, and periodic-review branches are in the [statecharts](../provenance.md).

```mermaid
---
title: Task execution
---
stateDiagram-v2
  s0: 3.1 Classify task
  s1: Abandon and notify
  s2: Block and notify
  s3: Standard workflow
  s4: 3.1 Direct low-risk work
  s5: Complete
  s6: 3.8 Full checks before merge
  [*] --> s0
  s0 --> s1: Decide not to proceed
  s0 --> s2: Preserve state and notify
  s0 --> s3: Prepare required plan
  s0 --> s4: No mandatory plan brief or separate review
  s3 --> s2: Preserve state and notify
  s4 --> s0: Risk requires standard workflow
  s4 --> s2: Preserve state and notify
  s4 --> s5: Necessary checks and local closeout
  s4 --> s6: Actual merge required
  s6 --> s2: Preserve state and notify
  s6 --> s5: Complete remaining work
  s3 --> s6: Verification complete
  s3 --> s0: Continue workflow
```

For Git operations at any node, read the [Git and GitHub collaboration standard](6-version-control.md) on demand. Verify applicable [Git closeout](3-workflow/3.8-integration-and-completion.md#git-closeout) before reporting completion. This adds no workflow stage.

In this chart, merge covers every project-designated integration-target update, including direct commits or pushes. Ordinary task-branch commits still use quick checks. The chart shows integration routes, without requiring every workspace task to update a target.

Run [periodic review](4-periodic-review.md) at each milestone or agreed interval. Return to the same review after repairs to verify the original findings.

Within implementation and self-check, select small TDD cycles under section 3.5.2; this adds no universal unit-test-first stage.
