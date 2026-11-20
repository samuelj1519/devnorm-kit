---
name: devnorm-verify
description: "Verify actual CLI, service, browser, and native behavior."
---

# devnorm-verify

Reuse existing controls for normal acceptance. Create or maintain verification tooling only when explicitly requested; missing tools are not a pass.

Read the target project's current rules and exact task inputs. Preserve its scope, existing authorization, cumulative budget, and required verification. Use [the method](references/methods/actual-verification/METHOD.md) for this capability. Read related resources only when needed.

For authorized Git actions, task-branch commits use [exact-index quick checks](references/standard/6-version-control/6.3-staging-and-commits.md); integration targets require [trusted full checks](references/standard/3-workflow/3.8-integration-and-completion.md). For user reports, handover, and completion, read that shared section for communication and evidence retention.

This skill is independently complete. It does not authorize delegation, installation, commits, external writes, or release. Source and license details are in [provenance.json](provenance.json) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
