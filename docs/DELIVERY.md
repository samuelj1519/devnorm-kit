# Delivery evidence

Date: 2026-11-16. Package version: `1.5.0`.

Accepted candidate: `a22bf22eb0c8d21a31a449d6a48c3675819f20b1bd2fa16decd664186da8b127`.
Accepted release identity: `a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b`.
Accepted source record: `d03ba09e7b2c69af6356a7dfecfa040839a02f5b048bd650e6b4d4745838e8be`.

The initial staged whitespace check found final blank lines in 18 generated notice/index files. Two narrowly scoped Git attributes preserve those accepted bytes while retaining other whitespace checks.

The generated payload is preserved exactly. Repository governance, validation, CI, and local mo compatibility are maintained separately.

## Local checks

- `make check`: PASS; complete generated file identities, all nine entrypoints, release reconstruction, and eight failure/round-trip tests at the time of this record (the suite has 11 tests as of 2026-11-17; see the follow-up below).
- Original mo release-adapter suite against the patched backend: PASS, 33 tests.
- `MO_BACKEND=<patched-backend> python3 -B integrations/mo/test_adapter.py`: PASS, 74 tests including the inherited legacy cases and multi-skill cases.
- Existing source-management suite against the patched backend: PASS, 39 tests. Its first flat temporary layout failed three fixture path lookups; rerunning with the actual `settings/scripts/macos-rebuild` layout passed.
- Existing skillctl suite against the patched backend: PASS, 10 tests.
- Reconstructed release resolved by mo: PASS; exact accepted release hash, all nine skills, and accepted source record.

## Publication and local acceptance

- Published to [samuelj1519/devnorm-kit](https://github.com/samuelj1519/devnorm-kit): initial generated import `0a17541`; repository/tooling commit `2726608`.
- [Validate delivery on the pushed tooling commit](https://github.com/samuelj1519/devnorm-kit/actions/runs/43896929258): PASS (`push`, exact commit `2726608007206949f43b2ed5bce62b25ee9bc48c`).
- Independent non-author review: standards PASS, specification PASS. The reviewer independently ran package and mo tests, demonstrated failure on the original adapter, and checked patch application, no-op repetition, drift rejection, mode preservation, and migration from an old single-skill installation record. The two scoped EOF attributes also received an independent failure probe; trailing spaces and unrelated EOF violations still fail.
- The patch uses zero-context diffs to avoid whitespace warnings caused by blank patch context lines. Before/after full-file hashes and resulting code remain unchanged from the reviewed candidate.
- GitHub description/topic update: PASS after the user updated token permissions. The initial attempt returned `HTTP 403: Resource not accessible by personal access token`; the retry saved the description and all five topics (`agent-skills`, `claude-code`, `codex`, `cursor`, `development-workflow`), confirmed by an API read-back.
- Persistent accepted source: `~/.local/share/devnorm/releases/1.5.0`.
- Actual mo operation: `SKILLS-20261116-233038-f2479d5e`, `batch=passed assets=1 changed=1`.
- `mo skills check devnorm`: PASS. Independent file/mode comparison also found exactly nine complete Agent skill copies and nine complete Cursor copies.
- Claude native registration/cache: version `1.5.0`, nine skills each in `default`, `mi`, `kimi`, `glm`, and `zen`; no standalone copies of these entries in those profiles. mo used the native CLI and verified its returned plugin identity and payload.
- Source registration changed only the DevNorm entry. Existing local settings changes remain uncommitted and preserved.
- Registration and original backend backup: `~/.agents/backups/devnorm-registration-20261116-ehmhsb3p/`; installation backups use the mo operation ID above.

Runtime model behavior, fresh-session discovery, Cursor IDE acceptance, and adoption by target projects remain `not_run`; file or inventory checks do not establish them. Reload the relevant clients before using the new entries. Normal maintenance uses `mo skills upgrade devnorm` and `mo skills check devnorm`.

## Repository documentation follow-up, 2026-11-17

The root README and INSTALL now have repository ownership. Their accepted originals moved unchanged to `docs/generated/`; skills, native manifests, licenses, notices, source records, and runtime checks remain protected. The source exporter preserves ordinary repository files instead of requiring the whole directory to equal its generated registry.

Source validation: `bun run verify` PASS (174 tests plus dependencies, types, formatting, and standard checks). This repository: `make check` PASS (11 tests). The model and actual filesystem failure probes, including the three independent cleanup findings and their repairs, are recorded in [export verification](../verification/export/README.md). The final generated files match an actual source-export conversion of the existing accepted artifact, independently verified byte-for-byte and by mode.

The installed runtime remains `1.5.0`, with its original release identity and accepted source record. Full runtime regeneration with the edited source program was correctly blocked by `toolchain-changed`; no new acceptance, installation, or uninstall occurred. The source code is a separately reviewed local change pending its next source release cycle. The homepage's pinned installation/removal examples were also exercised with the cached `skills@1.8.1` in an isolated temporary project/home; all nine entries installed and removal preserved an unrelated fictional skill.

## Private local validation follow-up, 2026-11-20

The current generated working tree is accepted private version `1.7.0`, source candidate `027b27e2725285611a8736d07ca86fa1c4a88a141d208679152b051137f188d2`, accepted source record `44c9efe8e830349d0b1ff429ee76248c691f2154541887dc605f145d6cb0e61f`, and source release identity `5228652e81ece0bbb68fc277df7ea66775de3ccf2b97f07a76fbb24be5e9f787`. The [source-release metadata](../release-artifact.json) preserves the accepted identity. This is not a published release. The earlier dated evidence above remains historical rather than being transferred to this version.

The authorized source task quality-lite-v3 completed exact candidate checks (291 tests, zero failures) and non-author implementation review with Cursor CLI / Grok 4.7 High. The review retained one independent key-test timeout and its successful isolated replay. Actual temporary Cursor CLI main, review-only continuation, and native-plugin sessions read the exact copied entries while source and known personal DevNorm skill paths were denied. Three initial client processes timed out; later explicitly bounded original-session completions preserve those failures and cumulative usage. Standalone statechart probes ran with existing Bun 1.3.11/Java/TLC under the same read boundary: normal model exit 0, wrong invariant exit 1, missing tools exit 2. Preview and accepted content match in all 3289 other files; only the top-level record identity and its checksum changed at acceptance.

A prospectively fixed fictional Python trial completed ordinary local/cross-module work and a direct documentation correction without applying an unapproved guard-bypass proposal or stopping unrelated work. A distinct fresh reviewer personally replayed the original five assertion mismatches, verified the guard's negative witness, and passed all seven frozen tests. The two trial processes took 393.60 seconds. Quality checks passed, but one authoritative task record still expanded from seven to 112 lines. No old-workflow paired control or two-real-project evidence exists; billing and lead-agent total usage are unknown. The adoption decision is **evidence insufficient: keep limited private/isolated validation**, not general promotion or a savings claim.

The exporter preserved all 144 observed repository-owned/Git file identities before these three intentional manual-document updates. The original workspace-bound export attempt reported `lock-held`; the queried lock was absent and the destination unchanged. An approved exact cross-workspace retry completed with the normal transaction and ownership protections; no lock was removed or taken over.

No persistent installation, push, public tag, or project-wide automatic adoption was performed by this task. The published examples remain pinned to `v1.5.0`. The current installed/loaded versions and Cursor IDE, Claude Code, and Codex behavior are not established by this local CLI validation. The follow-up package check result is recorded with the source task's final evidence rather than inferred from export success.

## Local formal delivery 1.7.1, 2026-11-20

The user explicitly selected local formal delivery only. The current generated payload is accepted private `1.7.1`, candidate `13c40b6c980df4f50566dbb93d772eb0ebcf12866e993e092a133b3488219378`, accepted source record `6cecee2b046d529f02df626d7aacb460130e7a3efe637b73a7825fd483ae133e`, and source release identity `dd305ae5babcf0c62200ad6bd0ece95f52158ca54120904e7fd5019d59a28e9a`. The prior dated 1.7.0 entry remains historical. Published installation examples remain pinned to `v1.5.0`; this task performs no push, public tag, upload, persistent installation, or automatic project adoption.

This version includes the reviewed eight Chinese/English standard, method, and template corrections from source commit `ed541a3`: reuse the existing brief and validated evidence, retain required reviewer-owned critical checks, stop for new failures, return confirmed blockers promptly, respect authorization and cumulative budgets, and report only meaningful increments. Runtime programs, existing tests and time limits, source pins, and protection rules are unchanged.

The first candidate full-test process exceeded the unchanged 120-second deadline before a complete native summary. Its failed receipt and original logs were retained. One controlled identical-input replay passed all six required checks; native tests reported 291 pass / 0 fail in 108.07s. The original nonauthor Grok High reviewer resumed for exact candidate binding and actually read the new temporary plugin review entry; its own report states personally executed versus reused evidence and unverified limits. Existing runtime/host evidence is reused only for unchanged scope, not as fresh Cursor IDE or other-client acceptance or proof of lower costs. Adoption remains limited private/isolated use with efficiency benefit unproven.

The exporter preserved the immediately recorded repository-owned/Git identities before these three deliberate manual-document updates. Preview and accepted build differ only in the top-level accepted-record identity and its checksum; runtime/resource bytes and modes match. The final source evidence records the actual post-export package and make-check outcomes rather than inferring them from export success. Installed and loaded versions remain unestablished by this operation.
