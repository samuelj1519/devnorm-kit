# 5. UI acceptance

For UI tasks, record applicability, requirements, results, and evidence for items 5.1 through 5.11 in the [task brief](../../assets/templates/task.md). Use `N/A` with a reason for inapplicable items and `not_run` for missing execution. Repair failures and rerun. Script success does not replace actual interaction. Applicable required failures prevent completion. State when a task has no UI.

| ID | Required checks |
| --- | --- |
| 5.1 | First use: explain the product within seconds, explain permissions and allow deferral, provide one primary action, and show no fabricated reviews or data. |
| 5.2 | Empty state: explain why it is empty and the next action. Reserve accent color for that action. |
| 5.3 | Errors: explain the failure, effect, and recovery without blaming the user. Text contrast is at least 4.5:1 and icon contrast at least 3:1. |
| 5.4 | Loading: show progress and continued feedback after about 1 second. Allow cancellation for long work. Use honest step descriptions for AI work rather than unexplained endless activity. |
| 5.5 | Narrow windows: define the minimum usable width, allow sidebar collapse, prevent reading-area overflow, and use targets at least 24×24 px. |
| 5.6 | Dark mode: use semantic color variables rather than light-only hex values, measure contrast, and use opaque backgrounds when Reduce Transparency is enabled. |
| 5.7 | Keyboard and focus: align Tab and visual order, keep focus visible, close overlays with Esc, and document common shortcuts. |
| 5.8 | Accessibility: meet WCAG AA contrast, use more than color for important actions, test reduced motion, and provide accessible names with assistive technology. |
| 5.9 | AI output: label generated content, expose capabilities and limits, support at least two of edit/regenerate/discard, and preview plus confirmation or Undo before data changes or sends. Avoid fabricated accuracy percentages. Provide a non-AI path for high-risk work. |
| 5.10 | Layout: group every element, avoid isolated floating controls, and provide one primary action per screen. |
| 5.11 | Prototype and implementation screenshots: use the same fictional state and actual container width, preserve side-by-side evidence, and state acceptance boundaries per task. |

Specify project requirements and evidence for every applicable item. Use this checklist and its defaults where project UI guidance is absent or incomplete. Keep stricter project requirements.

Before deleting, reducing, or replacing a requirement, record its ID, old and new requirements, scope, reason, risk, replacement verification, recovery, and requirements-owner approval. Keep the original until approved. No UI or an existing prototype means no additional prototype is needed. Compare screenshots only when a prototype applies, and explain inapplicable items.
