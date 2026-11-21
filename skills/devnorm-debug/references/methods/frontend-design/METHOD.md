# Interface design

For specific presentation concerns, reuse [interface methods](../interface-review/METHOD.md) on demand without duplicating design systems or prototypes.

## Scope and inputs

Build a prototype only for a new UI question without a usable existing reference. Handle small existing-UI fixes at their applicable scope. No UI means no prototype. Establish user tasks, content, platform, design system, and acceptance; product requirements follow [sections 5.1 through 5.7 of the interaction and interface standard](../../standard/5-interaction-and-interface.md).

## Procedure

1. Inspect real content and primary operations. Define reading order, hierarchy, interactions, and states. Reuse project components, type, palette, and layout conventions.
2. Choose a visual direction that fits the product. Use typography for reading/hierarchy, color for roles/states, and spacing for grouping. Explain how choices support the task. Avoid unrelated marketing templates and decoration.
3. For consequential interactions without precedent, compare a few different sketches or runnable prototypes against the same task. Check clarity, readability, and recoverability. Build the comparable core first.
4. Implement the main flow and default, hover, focus, active, disabled, loading, error, empty, and success states. Motion explains feedback and relationships and respects reduced motion.
5. Adapt to real viewports and inputs. Check touch targets, keyboard order, focus, semantics, and contrast. Rearrange responsive content for the task rather than scaling the desktop.
6. Use [interface review](../interface-review/METHOD.md) and [runtime verification](../actual-verification/METHOD.md) on the exact implementation. Screenshots, prototypes, and static code do not replace real interaction.

## Completion and stopping

Main actions, hierarchy, states, and adaptations run. Choices have specific reasons and acceptance mapping. Unsettled form/scope remains in design. Use authorized resources and fonts. Product release and asset sharing retain task authorization.

## Source and adaptation

Adapted from pinned Anthropic frontend-design, preserving intentional type, color, space, and interaction. Adds prototype conditions, UI checklist, and real acceptance. Apache-2.0, copyright, and notices remain; no upstream endorsement.
