# Runtime verification

When explicitly asked to create or maintain project verification tooling, read [verification maintenance](references/maintenance.md). Normal acceptance does not automatically create tools.

## Scope and inputs

Use to verify completion, repairs, or delivery. Fix the exact candidate, target host, acceptance criteria, real-data/model authorization, cost, and stop budget. Prefer isolated projects, fictional data, and reversible operations.

## Select the actual entry

| Product | Action and observation |
| --- | --- |
| CLI | Run the real entry. Check help, valid/invalid inputs, exit, stdout/stderr, and file/service side effects. |
| Browser | Click, type, and navigate in the target browser/engine. Inspect actual visibility, layout, keyboard focus, and requests. |
| Service | Start the actual service and request public APIs. Check responses, persistence, side effects, retries, and recovery. |
| Native app | Use the actual build and platform features. Check windows, storage, credential/permission behavior, and accessibility. |

Record static, headless, browser, and native results separately. Another engine's pass does not prove the target engine.

## Procedure

1. Derive the minimum action sequence and expected results from visible acceptance criteria. Map project checks, substitutes, runtime, and model properties to their actual proof scope.
2. Check tool/version, directory, process, and service ownership. Use only task-owned resources. Accounts, sends, install, and release retain authorization. Missing permission blocks only that action.
3. Start the exact version and save build/start/action logs. An existing process or window does not prove this feature ran. Confirm the entry loads the candidate.
4. Test normal, failure, and recovery paths. Wait for a public completion signal, such as terminal status or `aria-busy` changing from `true` to `false`. Arbitrary sleeps and command returns do not establish async completion.
5. Inspect actual visibility, styles, bytes, or service state. Apply the [UI checklist](../../standard/5-ui-acceptance.md) to first use, empty/error/loading, narrow width, dark mode, keyboard, accessibility, AI output, layout, and screenshots.
6. For critical protection or a false-green risk, verify effective defect detection using the original failure or a runnable incorrect version. Reuse exact-input evidence where valid; do not invent a defect for a new feature or repeat the same proof for every role. Independent review still personally runs critical paths. Repair a broken/unmounted probe or tool without mislabeling it a product failure or pass.
7. Save exact inputs, host, commands, tool versions, raw output, results, unrun reasons, and reproduction. Stop only owned processes and clean up under project rules.

## Completion and stopping

Required behavior runs in the target environment and meets expectations, with explicit scope and limits. Missing tools, login, environment, or approval remain `not_run` and block affected delivery. Return product errors to implementation and changed semantics to design. Verification does not authorize commit, external sends, or release.

## Source and adaptation

Combines pinned Cursor Team Kit control-cli, control-ui, and verify-this. Keeps real entry and public-result verification, organized by product type. Removes fixed environment, automatic commit, and implicit release assumptions.
