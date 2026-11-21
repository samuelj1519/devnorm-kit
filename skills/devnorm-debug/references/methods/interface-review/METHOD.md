# Interface review

Read [motion/states](references/motion.md), [responsive adaptation](references/responsive.md), [components/tokens](references/tokens.md), [typography](references/typography.md), or [color](references/color.md) only for the current concern.

## Scope and inputs

Review the exact existing UI version, platform, viewport, input methods, user task, and authorized scope. Separate read-only findings from approved repairs.

## Procedure

1. Perform the main task in the actual host, recording page, state, viewport, and actions. Map the [UI checklist](../../standard/5-interaction-and-interface/5.8-ui-acceptance.md) to evidence; product requirements are in [sections 5.1 through 5.7 of the interaction and interface standard](../../standard/5-interaction-and-interface.md).
2. Select one primary angle per issue: task/hierarchy in [experience review](references/critique.md), semantics/keyboard/contrast/theme/performance in [Web audit](references/audit.md), states and boundaries in [robustness](references/harden.md), labels in [UI copy](references/clarify.md), and presentation in [visual/interaction checks](references/craft-floor.md). Read only applicable references.
3. Check information order, discovery, feedback, recovery, and consistency. Review typography, line length, grouping, color roles, and small-size clarity. Remove decoration that does not aid understanding or operation.
4. Check keyboard, focus, assistive technology, reduced motion, narrow width, dark mode, and errors. Verify platform-specific behavior in the actual native app. This package has no complete iOS/Android audit resources.
5. Use project severity. Otherwise distinguish blocked use, serious task impairment, ordinary defects, and optional improvements. Include location, trigger, user impact, reproduction, and specific repair.
6. After an authorized repair, rerun the original action and affected states. A review-only task writes only reports/evidence. Record host, actual results, and unrun scope with [runtime verification](../actual-verification/METHOD.md).

## Completion and stopping

Applicable checks are covered, original findings reproduce, and repairs can be verified. Missing host access limits conclusions and remains not_run. Unresolved high-priority findings block affected acceptance. Aesthetic preference does not override approved brand or accessibility.

## Source and adaptation

Adapted from pinned Impeccable critique, audit, harden, clarify, and craft-floor. Retains Apache-2.0, NOTICE, and per-file changes. Covers delivered Web/common cross-platform material without implying absent native resources.
