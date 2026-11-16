# Periodic review and improvement

Apply [periodic review](../../standard/4-periodic-review.md) at agreed intervals, milestones, or recurring defects. Do not repeat a full retrospective for every small edit.

1. Read actual check commands, CI, hooks, and failures. Distinguish disconnected or broken protection from missing protection; repair existing checks first.
2. Separate mechanically decidable errors from judgment. Prefer structure, types, existing lint, or tests for the former; use concise conditional guidance for the latter. More documentation does not repair a broken check.
3. Trace repeated defects to the first wrong state and inspect architecture, dependencies, and test strength. After two repairs sharing one failed premise, test the premise directly. Keep improvements within project scope and authorization.
4. Prove new protection rejects an original error or runnable mutation and accepts valid behavior. Verify recovery, installation, and service behavior through actual entries. Probe failure is not defect detection.
5. Record cost, result, limits, and review conditions in existing records. Unimplemented changes remain proposals. Do not automatically edit global rules, memories, thresholds, or releases.

Close issues only after the required repair and verification. A follow-up task does not replace current obligations. Return product issues to implementation, systemic design issues to design, and protection changes through the standard.

Source: adapted from pinned Matt Pocock retro and pstack correct, integrated with DevNorm section 4. Authors still follow standards and reviewers still inspect requirements and actual implementation.
