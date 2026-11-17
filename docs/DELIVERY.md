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
