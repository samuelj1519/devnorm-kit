# Defect diagnosis

## Scope and inputs

Use for wrong output, exceptions, failing tests, hangs, or performance regression. Fix the version, minimal failing input, expected/actual behavior, allowed files, and cumulative budget.

## Procedure

1. Replay the symptom independently and record command, environment, input, exit, and raw output. Distinguish product, test/probe, dependency, and permission failures. Gather missing reproduction conditions first.
2. Trace actual data and state to the first contract deviation. Test hypotheses with callers, logs, minimal input, and boundary observations. Prefer reversible experiments that separate explanations.
3. State the current explanation, evidence, and possible refutation. Change only what tests it. After two substantive repairs on the same premise fail, test that premise directly before choosing another design.
4. Repair the cause at the earliest responsible boundary. Add a guard only for a legitimate state. Do not hide failures by swallowing errors, relaxing limits, or skipping behavior.
5. Choose the cheapest behavior check that prevents recurrence. A cheap local target may start with a failing test. Integration/native defects rely on actual replay. Prove critical checks fail against runnable old logic or removed protection in an isolated copy.
6. Replay the original input, then check actual impact. Use [performance measurement](../benchmark/METHOD.md) for performance and [runtime verification](../actual-verification/METHOD.md) for async/UI completion signals.

## Completion and stopping

The original defect is reproduced and repaired on the exact version, regression protection detects incorrect behavior, and applicable paths pass. Preserve original failure and real repair counts. Return at exhausted budget, changed critical assumptions, or unapproved files. New tasks, executors, and rollback do not reset budget.

## Source and adaptation

Adapted from pinned Matt Pocock diagnosing-bugs. Retains replayable hypothesis testing, root-cause repairs, and behavior verification. Adds the standard premise check, cumulative budget, and stops, without fixed delegation.
