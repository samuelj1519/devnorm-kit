# Persist before acknowledging a message

Teaching scenario. Obtain evidence for the actual version by running its model and public entry points against the intended outcomes below.

## Key commitments

The consumer handles each event under a stable message ID. It acknowledges the message, or sends an ACK, after transaction commit. If the commit outcome is unknown, query by the original ID first. For the business record in this example, redelivery leaves one record and one effective write. Confirm the real consumer and database boundaries in the plan.

The supported old release in this example reads the current compatible format. Keep writes in that format during mixed deployment. If the old release cannot read a new format, stop increasing exposure and verify a compatibility change or authorized containment before acting.

## Evidence before implementation

Use the [state-modeling method](../../../references/methods/statechart/METHOD.md) to check that an ACK requires persistence and a message ID takes effect at most once. Check successful completion, an unknown commit outcome, redelivery after a lost ACK and safe termination. An ACK before persistence should violate the invariant if the write fails. The non-author reviewer checks the exact plan, model, counterexamples and compatibility assumptions. Record actual required-property results, plus the models and scenarios to rerun and replay after implementation.

## Evidence after implementation

Send a message through the actual consumer entry in an isolated environment. Let the first commit succeed and lose its ACK. Redeliver the message under the same ID. Check persisted record count, effective write count and the observed ACK, then read back supported old data. Verify that the same fixture fails with an ACK-before-write or duplicate-write implementation. Rerun relevant models under section 3.7. Link versions, environment, original results, independent conclusions and unverified scope in the original task record. Verify the current exact combination before integration.
