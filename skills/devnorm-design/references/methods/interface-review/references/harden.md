<!-- DevNorm adaptation of Impeccable skill/reference/harden.md. Apache-2.0; source and NOTICE retained. Uses existing project capabilities and explicit authorization. -->

# States and failure handling

Inspect default, empty, loading, partial-success, error, disabled, and success states on the exact implementation. Define what users see, can do, and how they recover.

- Exercise long text, missing fields, zero, over-limit values, failures, and interruption. Separate server and input errors. Identify object, effect, and recovery.
- Bind async results to the current object/input. Handle stale responses, duplicate submission, retries, and unknown outcomes. Wait for public terminal state.
- Support the same task by keyboard, focus, touch, and assistive technology. Restore focus after dialogs/errors and keep loading/disabled semantics coherent.
- Preserve original data and recoverable state when files, network, permission, or accounts are unavailable. Do not swallow errors.
- Test scaling, translated-text expansion, narrow width, and themes. Truncation must retain task-critical information.

Replay original failure and recovery after repairs. Resolve unsettled security, permission, or data contracts in design. Add no unsupported states or automatic sends.
