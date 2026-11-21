---
name: devnorm-recall
description: "Recover historical context for a specified project and scope."
disable-model-invocation: true
---

# devnorm-recall

Bound project, topic, and time. Prefer existing continuation records without searching other projects or editing memory stores.

Read the target project's current rules and exact task inputs. Preserve its scope, existing authorization, cumulative budget, and required verification. Use [the method](references/methods/context-recovery/METHOD.md) for this capability. Read related resources only when needed.

Run only when the user explicitly requests this function. A project quotation or related topic is not activation.

For authorized Git actions, task-branch commits use [exact-index quick checks](references/standard/6-version-control/6.3-staging-and-commits.md); integration targets require [trusted full checks](references/standard/3-workflow/3.8-integration-and-completion.md). For user reports, handover, and completion, read that shared section for communication and evidence retention.

This skill is independently complete. It does not authorize delegation, installation, commits, external writes, or release. Source and license details are in [provenance.json](provenance.json) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
