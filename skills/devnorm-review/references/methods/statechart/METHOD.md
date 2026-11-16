# State modeling

After implementation or state-contract changes, apply [model maintenance](references/maintenance.md) to correspondence, properties, and counterexamples.

## Scope and inputs

Use for state transitions, concurrency, retries, transactions, recovery, or other modeling required by the standard. Express requirements as decidable invariants. Identify actors, shared objects, commit points, failures, and interruption scope. Resolve critical semantics in design first.

## Environment and limits

Set existing `JAVA` and `TLA2TOOLS` paths, then run the [controlled entry](scripts/statechart) with `--check-environment`. Keep those variables for the packaged fixed tool. Missing/invalid tools stop execution before upstream automatic downloads. Existing Node or Bun runs TypeScript. Follow the [rendering guide](references/render.md) with authorized installed tools. Without Pele, retain Mermaid text rather than install dependencies.

## Procedure

1. Write TLA+, configuration, and view in an authorized isolated directory. Define finite constants, state boundaries, invariants, and applicable temporal properties. List concrete actions in `Next`. Use terminal-only self-loops for valid termination without masking nonterminal deadlock.
2. Define reader-facing states with `state(vars)` and actions with `step(action, from, to)`. Arrays represent parent states and objects represent parallel regions. Names describe domain behavior and mapping functions use only their arguments.
3. Run the controlled entry. The fixed [main script](../../upstream/cursor-plugins/statechart/scripts/statechart), [dynamic worker](../../upstream/cursor-plugins/statechart/scripts/worker.ts), and dependencies form the packaged runtime. Replace example paths with actual ones:

```sh
JAVA=/existing/java TLA2TOOLS=/existing/tla2tools.jar sh /copied/devnorm/references/methods/statechart/scripts/statechart SPEC.tla --config SPEC.cfg --view view.mjs --out /isolated/new-result
```

4. Read raw TLC output and reports. Distinguish property violation, deadlock, state limits, unchecked properties, and tool failure. State bounds, constraints, VIEW, and SYMMETRY affect coverage. Explain merged/omitted states and steps.
5. Keep charts readable while preserving every counterexample path and distinct failed property. A merged state with only some failing underlying states may fail; hidden paths are not proven safe.
6. Replay each counterexample's actions in the real implementation or an independent test. Inspect mapping when implementation does not reproduce it. Repair plan or code and rerun original properties and necessary normal cases. Keep the original failure.
7. Deliver model, config, view, chart, logs, commands, and input hashes. Record every property, result, unrun reason, and excluded scope. The behavior owner reviews the chart.

## Completion and stopping

Applicable properties ran, counterexamples are addressed, chart/implementation mapping exists, and reproduction is complete. Missing tools, permission, or required properties leave the task in design. Model success does not replace file-transaction, process, native-platform, or product acceptance. Manual confirmation cannot replace required checks.

## Source and adaptation

Uses pinned pstack statechart scripts and reporting, including all non-test runtime dependencies and the dynamic worker. DevNorm adds environment validation to avoid automatic installation. Workflow and completion follow the standard without fixed host models or delegate counts.
