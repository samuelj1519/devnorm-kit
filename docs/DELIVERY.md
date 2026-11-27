# Delivery evidence

## Public delivery 1.13.0

DevNorm now requires documentation closeout for simple and formal tasks. Update current guidance to match the delivered result, remove obsolete and duplicate material, and check instructions from the entry point readers use. Preserve historical evidence and finish any updates that depend on the published tag within the same delivery.

Source implementation commit `bcf3a1de9b51dafc5e01ed3d4f15436a8c1bf3ad`. Candidate `78d61926a070b515c2465737688daced928245fbda283f74e3d1a15005288489`. Acceptance record `36c937ba02ba1c0816f0ca9e124dd4ae3cd7c5f6e8e440ca178c02b775049ff5`. Release artifact `f67731d8e8b465ffaa128682e7768b63fa0a3afbf1a3a1ee204eb795e5ac308b`.

The frozen candidate passed all six checks and 299 tests. The independent review covered 18 targeted model outcomes and four isolated Codex CLI scenarios. The documentation fixture verified its tag, corrected stale examples and commands, removed repeated instructions, and preserved the historical record. The export updated 46 generated paths, including the registry, and preserved 1732 registry entries. The Kit homepage and installation guide point to `v1.13.0`. Persistent client installation and loading were outside the verification scope.

## Delivery 1.12.1 on `main`

The workflow now selects preflight checks by impact. Task-branch commits use quick checks on the exact staged version. Review, acceptance, and integration refer to the same still-valid trusted full-check result for the exact integration combination.

Source implementation commit `8a3c149656a577a410dde3dde85e369f23fdf36a`. Candidate `4ebb51b2d536e742e2ee5029c2a66488b61975c33d852c78695699d68febedfc`. Acceptance record `2f90f6317d313f99ad705cbc118f31e79129d7779f71fc4661061c2ff686c7b2`. Release artifact `51d271fd9861a9c2101322d157a4d18ed4f7af1416db6abb540b84927a549d9c`.

The frozen candidate passed six required checks and 299 tests. Independent review covered 18 targeted model cases and three isolated Codex CLI sessions. The delivery fixture exercised two separate staged quick checks and one trusted full check before a synthetic push and SHA readback. The model runner rejected the first output path. It completed on replay in an allowed directory. The export updated 46 generated paths, including the registry, and preserved 1732 registry entries. This delivery uses the `main` branch. Persistent client installation and loading were outside the verification scope.

## Public delivery 1.12.0

The source implementation is commit `7b58a66ca61c9fc61ae6650a381ac376b00678f2`. The public candidate is `ef269d25ef59d66f3a1993d4fe5ccf2d0746519ff45535e68de17a04f6824301`, the source acceptance record is `cf2476dd556f3d844067c18028664c06073d34669a5fe61fc9de0fc4ba10d83b`, and the release artifact is `77ef11be3517434c8e521b4421f354a97812224a09064ec87d4573694775e473`.

The workflow now tells agents when to commit each verified increment, how to complete authorized remote delivery, and when a change needs a separate version tag. The adoption template records who can push and to which repository and branch.

The public candidate passed all six required checks, including 299 tests. Independent review verified eight required proofs from 16 targeted model cases and five isolated Codex sessions. The sessions covered separate commits, push and remote SHA readback, refusal of an out-of-scope push, discovery of an external compatibility obligation, and a formal review held pending until verification. The first model launch could not open a local Java port under the sandbox. The same inputs passed on replay with local port access. Persistent installation and other clients were outside this verification.

The Kit passed all 17 repository tests. Independent restoration matched all 3,541 accepted payload files by SHA-256 and mode. Export changed 100 generated files, including the registry, and preserved 1,678. See [Install DevNorm](../INSTALL.md).

## Historical evidence

### Public delivery 1.11.0

The [published `v1.11.0` tag](https://github.com/samuelj1519/devnorm-kit/tree/v1.11.0) points to Kit commit `c4a8504891b19a6b69f3852191e1b99bc9d5518d`. The local source commit used for this release is `b3c8f367672bb6548cb56f244e200203009c1c99`. The frozen candidate is `779989403604f555d82f511e4a0c2f3afeb7749002e7b422f9085c26532cf12b`, the source acceptance record is `733f3a313710409512bfc1fe5ee128dadb55a86679b26320c48bc3158db8820f`, and the release artifact is `2b0fc6fc4e92f0dcf030993db0e4a19841115e7886e255eae5812aee6fee04bb`.

The standard routes tasks by evidence requirements and gives independent skills direct links to relevant package resources. The design skill includes its own path to state modeling. The source program invalidates a previous pass before freezing a candidate again.

The public candidate passed all six checks with 299 tests passing. The independent reviewer verified 16 model cases and three isolated Codex sessions for direct routing, unresolved compatibility, and independent review. The Kit passed all 17 repository tests and reconstructed the accepted release. For current install commands, see [Install DevNorm](../INSTALL.md).

### Initial delivery 1.5.0, 2026-11-16

Accepted candidate: `a22bf22eb0c8d21a31a449d6a48c3675819f20b1bd2fa16decd664186da8b127`.
Accepted release identity: `a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b`.
Accepted source record: `d03ba09e7b2c69af6356a7dfecfa040839a02f5b048bd650e6b4d4745838e8be`.

The initial staged whitespace check found final blank lines in 18 generated notice/index files. Two narrowly scoped Git attributes preserve those accepted bytes while retaining other whitespace checks.

The generated payload is preserved exactly. Repository governance, validation, CI, and local mo compatibility are maintained separately.

### Local checks

- `make check`: PASS; complete generated file identities, all nine entrypoints, release reconstruction, and eight failure/round-trip tests at the time of this record (the suite has 11 tests as of 2026-11-17; see the follow-up below).
- Original mo release-adapter suite against the patched backend: PASS, 33 tests.
- `MO_BACKEND=<patched-backend> python3 -B integrations/mo/test_adapter.py`: PASS, 74 tests including the inherited legacy cases and multi-skill cases.
- Existing source-management suite against the patched backend: PASS, 39 tests. Its first flat temporary layout failed three fixture path lookups; rerunning with the actual `settings/scripts/macos-rebuild` layout passed.
- Existing skillctl suite against the patched backend: PASS, 10 tests.
- Reconstructed release resolved by mo: PASS; exact accepted release hash, all nine skills, and accepted source record.

### Publication and local acceptance

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

The 1.5.0 delivery recorded runtime model behavior, fresh-session discovery, Cursor IDE acceptance, and adoption by target projects as `not_run`.

### Repository documentation follow-up, 2026-11-17

The root README and INSTALL now have repository ownership. Their accepted originals moved unchanged to `docs/generated/`; skills, native manifests, licenses, notices, source records, and runtime checks remain protected. The source exporter preserves ordinary repository files instead of requiring the whole directory to equal its generated registry.

Source validation: `bun run verify` PASS (174 tests plus dependencies, types, formatting, and standard checks). This repository: `make check` PASS (11 tests). The model and actual filesystem failure probes, including the three independent cleanup findings and their repairs, are recorded in [export verification](../verification/export/README.md). The final generated files match an actual source-export conversion of the existing accepted artifact, independently verified byte-for-byte and by mode.

The installed runtime remains `1.5.0`, with its original release identity and accepted source record. Full runtime regeneration with the edited source program was correctly blocked by `toolchain-changed`; no new acceptance, installation, or uninstall occurred. The source code is a separately reviewed local change pending its next source release cycle. The homepage's pinned installation/removal examples were also exercised with the cached `skills@1.8.1` in an isolated temporary project/home; all nine entries installed and removal preserved an unrelated fictional skill.

### Private local validation follow-up, 2026-11-20

The current generated working tree is accepted private version `1.7.0`, source candidate `027b27e2725285611a8736d07ca86fa1c4a88a141d208679152b051137f188d2`, accepted source record `44c9efe8e830349d0b1ff429ee76248c691f2154541887dc605f145d6cb0e61f`, and source release identity `5228652e81ece0bbb68fc277df7ea66775de3ccf2b97f07a76fbb24be5e9f787`. The [source-release metadata](../release-artifact.json) preserves the accepted identity. This is not a published release. The earlier dated evidence above remains historical rather than being transferred to this version.

The authorized source task quality-lite-v3 completed exact candidate checks (291 tests, zero failures) and non-author implementation review with Cursor CLI / Grok 4.7 High. The review retained one independent key-test timeout and its successful isolated replay. Actual temporary Cursor CLI main, review-only continuation, and native-plugin sessions read the exact copied entries while source and known personal DevNorm skill paths were denied. Three initial client processes timed out; later explicitly bounded original-session completions preserve those failures and cumulative usage. Standalone statechart probes ran with existing Bun 1.3.11/Java/TLC under the same read boundary: normal model exit 0, wrong invariant exit 1, missing tools exit 2. Preview and accepted content match in all 3289 other files; only the top-level record identity and its checksum changed at acceptance.

A prospectively fixed fictional Python trial completed ordinary local/cross-module work and a direct documentation correction without applying an unapproved guard-bypass proposal or stopping unrelated work. A distinct fresh reviewer personally replayed the original five assertion mismatches, verified the guard's negative witness, and passed all seven frozen tests. The two trial processes took 393.60 seconds. Quality checks passed, but one authoritative task record still expanded from seven to 112 lines. No old-workflow paired control or two-real-project evidence exists; billing and lead-agent total usage are unknown. The adoption decision is **evidence insufficient: keep limited private/isolated validation**, not general promotion or a savings claim.

The exporter preserved all 144 observed repository-owned/Git file identities before these three intentional manual-document updates. The original workspace-bound export attempt reported `lock-held`; the queried lock was absent and the destination unchanged. An approved exact cross-workspace retry completed with the normal transaction and ownership protections; no lock was removed or taken over.

No persistent installation, push, public tag, or project-wide automatic adoption was performed by this task. The published examples remain pinned to `v1.5.0`. The current installed/loaded versions and Cursor IDE, Claude Code, and Codex behavior are not established by this local CLI validation. The follow-up package check result is recorded with the source task's final evidence rather than inferred from export success.

### Local formal delivery 1.7.1, 2026-11-20

The user explicitly selected local formal delivery only. The current generated payload is accepted private `1.7.1`, candidate `13c40b6c980df4f50566dbb93d772eb0ebcf12866e993e092a133b3488219378`, accepted source record `6cecee2b046d529f02df626d7aacb460130e7a3efe637b73a7825fd483ae133e`, and source release identity `dd305ae5babcf0c62200ad6bd0ece95f52158ca54120904e7fd5019d59a28e9a`. The prior dated 1.7.0 entry remains historical. Published installation examples remain pinned to `v1.5.0`; this task performs no push, public tag, upload, persistent installation, or automatic project adoption.

This version includes the reviewed eight Chinese/English standard, method, and template corrections from source commit `ed541a3`: reuse the existing brief and validated evidence, retain required reviewer-owned critical checks, stop for new failures, return confirmed blockers promptly, respect authorization and cumulative budgets, and report only meaningful increments. Runtime programs, existing tests and time limits, source pins, and protection rules are unchanged.

The first candidate full-test process exceeded the unchanged 120-second deadline before a complete native summary. Its failed receipt and original logs were retained. One controlled identical-input replay passed all six required checks; native tests reported 291 pass / 0 fail in 108.07s. The original nonauthor Grok High reviewer resumed for exact candidate binding and actually read the new temporary plugin review entry; its own report states personally executed versus reused evidence and unverified limits. Existing runtime/host evidence is reused only for unchanged scope, not as fresh Cursor IDE or other-client acceptance or proof of lower costs. Adoption remains limited private/isolated use with efficiency benefit unproven.

The exporter preserved the immediately recorded repository-owned/Git identities before these three deliberate manual-document updates. Preview and accepted build differ only in the top-level accepted-record identity and its checksum; runtime/resource bytes and modes match. The final source evidence records the actual post-export package and make-check outcomes rather than inferring them from export success. Installed and loaded versions remain unestablished by this operation.

### Local delivery 1.8.0, 2026-11-21

The generated payload is accepted `1.8.0`, candidate `0ad897952e24a7007c99e2e7ad3a93c860e937ed02be3201e9e3749bfb22a9bb`, accepted source record `4d91e30a4c2769858aecadb295d697d3aa03f851a28bdbf5fd50c5e528bcd2b3`, and artifact identity `9d70d500a236b326c8d48c7ba3debe25279aaaea9fc310f3d564fc101df5cb3c`. The prior dated entries remain historical. The [release metadata](../release-artifact.json) keeps purpose `private` from the accepted candidate; the push scope below was authorized separately.

This version delivers the interaction and interface product standard (source commits `fb54db6` and `432708d`): chapter 5 is rebuilt as an index plus sections 5.1–5.9, the eleven UI acceptance checks are renumbered 5.8.1–5.8.11 with all protected defaults unchanged, the interface design and interface review methods now route to sections 5.1–5.7, and English projections are synchronized. It also raises the candidate `tests` check timeout from 120s to 180s (source commit `78b34a3`, requirements-owner approval recorded in that commit); the other five checks keep 120s.

Candidate checks passed on the first run (291 tests, 0 failures, 123.33s). An earlier candidate of the same content under the previous 120s limit recorded one tests timeout (exit 124/SIGTERM) and one controlled identical-input replay that passed; that candidate was superseded by the approved timeout change rather than accepted. An independent non-author reviewer in a fresh session verified the candidate identity and input freeze, recomputed all six spec and log hashes, personally reran the standard check, the dependencies check, and the full suite (first run 289 pass / 2 load-related failures, one controlled replay to 291 pass / 0 fail), and spot-checked the eleven checks, protected literals, the English section tree, and the timeout scope; its report is `evidence/review.md` inside the accepted source candidate.

Authorization scope is `public-release` limited to pushing this repository's `release/v1.8.0` branch (user instruction, 2026-11-21). This entry records that push as performed; no public tag, `main` advance, install-command change, persistent installation, or automatic adoption by other projects occurred. After export, `make check` passed: package verify, 17 tests, and `git diff --check`. Installed and loaded versions remain unestablished by this operation.

### Publication v1.8.0, 2026-11-21

Following the user's same-day authorization, the 1.8.0 payload was published: `main` fast-forwarded to the payload commit plus this documentation update, annotated tag `v1.8.0` created at the publication commit, and the root README/INSTALL installation commands and version badge repointed from `v1.5.0` to `v1.8.0`. The publication commit passed `make check` before tagging. Installation and fresh-session verification results follow below.

### Installation evidence 1.8.0, 2026-11-21

The `main` advance was blocked by the repository rule "changes must be made through a pull request", and the active fine-grained token lacks pull-request write access, so `main` remains at its previous head pending that merge; the annotated tag `v1.8.0` and the `release/v1.8.0` branch (including this documentation) are pushed and carry the same content.

Local installation was performed through the documented maintainer path: `scripts/package.py restore-release` reconstructed the accepted release to `~/.local/share/devnorm/releases/1.8.0` and to the revision-named cache directory (revision `9d70d500…`), the `devnorm-local` marketplace source was repointed, and `claude plugin update devnorm@devnorm-local` upgraded the plugin from `1.5.0` to `1.8.0` in the `default`, `mi`, `kimi`, `glm`, and `zen` profiles (`plugin list --json` shows version `1.8.0` in each). The installed skill tree contains `references/standard/5-interaction-and-interface/` with all nine sections.

A fresh `claude -p` session in the `glm` profile listed the `devnorm:` plugin commands and successfully read `references/standard/5-interaction-and-interface/5.8-ui-acceptance.md`, confirming items 5.8.1 through 5.8.11. The session's proxy rejected further tool actions after those reads (environment-specific auto-mode check); the two requested answers were returned before the exit.

Not exercised in this round: the public `npx skills add samuelj1519/devnorm-kit@v1.8.0` channel (command attempts were declined locally), Codex/Cursor copies previously managed by `mo`, and `mo skills upgrade` itself — `mo 0.2.1` currently reports ambiguous source selection and unbound plugin recipes for this asset, a macops-side registration state outside this repository. The `managed-agent-assets.json` registrations were updated to the 1.8.0 release path and revision for when that flow is rebound.

### Local delivery and installation 1.9.0, 2026-11-23

Source commit `8f5e7c1917c3758a1e69f6f8fba13e84eb06415f` delivers simple and formal task routes, combined design and test review, evidence-based candidate approval, and production verification and recovery. This private delivery binds source candidate `d7cf81a2b7ea87f5109bb5c0e103c2226ec184527177f26321fa7b3b8aaba189`, acceptance record `81a5628e206890b1c1679d93f9b70d597e0d59ba67cc36e889cb18391f0166a5`, and artifact identity `12f4516f802e69a4b4b507bb7f304f4f8289f8771077a1f1ab42e9f4f16ab113`.

A clean source worktree excluded ignored historical logs from the accepted candidate. All six frozen-candidate checks passed on an unchanged-input replay following one test timeout, with 291 passed and zero failed. Independent review is included in the source acceptance record. The exported package passed `make check`, including 17 tests.

The existing local release adapter installed nine skills each for Codex and Cursor, and upgraded the five configured Claude Code profiles. File content and executable modes match the release. All five native Claude registrations list version `1.9.0` and are enabled. Running-session load status was not tested. The persistent release is `~/.local/share/devnorm/releases/1.9.0`.

### Release branch 1.10.0, 2026-11-25

The approved version is `1.10.0`. The frozen candidate is `f07e2ff3ca460a24797f705585909164ed86f15a07ff0d09ec078ec987e31d68`, the accepted source record is `723adbe9f8bc8a5cc45b05833e4cbe36f9944deb2ad1c1cea1eed09f872fe32e`, and the artifact identity is `c7b8c7d30a7db0698ae8304a9e64f749313546e9a4a1ddfc65627126beb614b3`.

This version introduces versioned mandatory conditions and shorter default reading paths. The source and exact candidate each passed the required checks, including 298 project tests. Independent review and the seven required condition proofs passed. Seventeen TLC results matched their expected outcomes. Two isolated read-only Codex sessions verified simple-task completion and escalation, and independent review before and after required evidence.

`make check` passed all 17 Kit tests. A separate restoration rebuilt nine skills and matched all 3,507 release files by path, SHA-256, and mode.

The approved destination is `release/v1.10.0`. The two client samples support the observed routing and review behavior. A paired Token comparison and persistent installation were outside this verification.

### Release branch 1.10.1, 2026-11-25

The accepted version is `1.10.1`. The frozen candidate is `7cf1e582e18570f6a43c86b02f6113f8ea0eb9fb8610f232af99b79f41d0836e`, the accepted source record is `270055b6cd72d1113a3084cf1ef87c8569e95b0bda5dc5da1551cdb8555cec86`, and the artifact identity is `cbec014542768aa1fe98b06606a842acef75b80dfb12beffccd0c1c7f595f0c8`.

This revision adds guidance for checking all affected uses of changed behavior and for preventing confirmed defects from recurring. The source and isolated candidate each passed the required checks, including 298 project tests. The independent review accepted seven condition proofs. Three model proofs had matching scopes and were reused. Seven targeted TLC cases matched their expected outcomes. Two authorized read-only Codex sessions observed the direct route and escalation, and independent review before and after required evidence.

`make check` passed all 17 Kit tests. A separate restoration rebuilt nine skills and matched 3,507 release files by path, SHA-256, and mode.

The approved delivery destination is `release/v1.10.1`. The runtime results apply to the two isolated fixtures. Persistent installation and a paired Token comparison remain separate.
