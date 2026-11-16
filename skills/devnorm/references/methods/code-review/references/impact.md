# Verify change impact

For cross-boundary changes or small diffs with broad consequences, trace actual callers, protocols, configuration, persistence, and host behavior beyond the diff. Identify the few facts the safety conclusion depends on, such as whether old callers remain or failures leave state behind.

Choose an execution that can disprove each material fact: actual caller/search coverage for migrations, representative round trips for serialization, and repeated public commands or failure injection for recovery/idempotence. Exercise relevant unchanged paths. Use isolated mutations where needed to prove protection detects the mistake.

Report actual scope, commands, and limits. Unconfirmed concerns remain risks to investigate, not verified defects. Neither a claim of controlled impact nor a large checklist replaces execution. Do not default to competing implementations or model fan-out.

Source: adapted from pinned pstack blast-radius.
