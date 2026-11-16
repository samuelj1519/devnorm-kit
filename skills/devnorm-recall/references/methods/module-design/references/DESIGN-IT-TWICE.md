<!-- DevNorm adaptation of Matt Pocock codebase-design/DESIGN-IT-TWICE.md. MIT; source and copyright retained. Removes fixed agent counts and personal terminology. -->

# Compare designs

For a new interface or responsibility without precedent and with important downstream effects, compare a few different shapes against the same problem. Reuse a stable precedent for low-risk work.

1. Fix external behavior, constraints, callers, dependencies, and recovery. Use one normal and one failing caller example without predetermining the interface.
2. Propose alternatives with different goals, such as fewer caller steps, serving the main caller, hiding a remote boundary, or reducing shared state. Specify types, parameters, outputs, legal states, order, errors, and recovery.
3. Run the same examples through each design. Compare caller burden, change locality, boundaries, testing, migration, and legacy removal.
4. Recommend a design and explain retained trade-offs. Recheck complete calls when combining alternatives to avoid duplicate responsibilities.

Compare sequentially or delegate independent designs only when authorization and total cost justify it. Include briefing, receipt, integration, and rework. Do not prescribe roles, headcount, or models. The appropriate owner decides critical trade-offs.
