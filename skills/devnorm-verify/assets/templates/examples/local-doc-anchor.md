# Repair a local documentation anchor

Teaching scenario. File names and outcomes illustrate the decision.

## When a direct fix is appropriate

The project's `README.md` links to `docs/setup.md#first-run`. The section was renamed, and its current anchor is `#current-onboarding`. The project authorizes this edit. Searching for the old anchor finds only this reference. The project confirms there is no external compatibility commitment and the link can be checked independently.

Handle it as a simple task. Update only that link, run the existing link check, and open the document to verify that the link reaches setup. Record the change and observed result in the original request. If integration is requested, separately verify the current exact combination.

## Pause affected writes when impact is unknown

If records indicate that an external installer might use the historical anchor and supported versions and callers are unknown, investigate references, compatibility commitments and ownership through authorized read-only actions. Leave the link and anchor unchanged while investigating. If a critical compatibility commitment still applies and the fix would change it, switch to the formal route and complete applicable design and test design review first. If the impact remains unknown, record the unresolved scope and conditions for resuming.

Editing the link before investigating, or reporting completion while ignoring unknown consumers, fails acceptance.
