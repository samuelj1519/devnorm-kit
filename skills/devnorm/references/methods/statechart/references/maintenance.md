# Maintain model-to-code correspondence

When verified state, concurrency, retry, parsing, or recovery behavior changes, identify the relevant implementation diff and original assumptions. Map code states, transitions, and properties before updating models, adapters, and counterexample tests.

Separate verification drift from product defects. Repair implementation that violates a still-valid property. If the specification truly changes, return to design and confirm semantics before changing properties. Never weaken properties merely to pass. Rerun applicable models, retain original counterexamples and successful results, and review key chart paths.

Report model results separately from actual CLI/app, persistence, and platform behavior. Identify unverified tools/properties; an old model pass is not current evidence. Maintaining an applicable model is normal design verification; creating project verification tooling still requires an explicit request.

Source: adapted from pinned pstack maintain-formal-verification-skill under standard sections 3.2.1 and 3.7.
