# Delivery evidence

Date: 2026-11-16. Package version: `1.5.0`.

Accepted candidate: `a22bf22eb0c8d21a31a449d6a48c3675819f20b1bd2fa16decd664186da8b127`.
Accepted release identity: `a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b`.
Accepted source record: `d03ba09e7b2c69af6356a7dfecfa040839a02f5b048bd650e6b4d4745838e8be`.

The initial staged whitespace check found final blank lines in 18 generated notice/index files. Two narrowly scoped Git attributes preserve those accepted bytes while retaining other whitespace checks.

The generated payload is preserved exactly. Repository governance, validation, CI, and local mo compatibility are maintained separately.

## Local checks

- `make check`: PASS; complete generated file identities, all nine entrypoints, release reconstruction, and eight failure/round-trip tests.
- Original mo release-adapter suite against the patched backend: PASS, 33 tests.
- `MO_BACKEND=<patched-backend> python3 -B integrations/mo/test_adapter.py`: PASS, 74 tests including the inherited legacy cases and multi-skill cases.
- Existing source-management suite against the patched backend: PASS, 39 tests. Its first flat temporary layout failed three fixture path lookups; rerunning with the actual `settings/scripts/macos-rebuild` layout passed.
- Existing skillctl suite against the patched backend: PASS, 10 tests.
- Reconstructed release resolved by mo: PASS; exact accepted release hash, all nine skills, and accepted source record.

## Publication and local acceptance

Publication and actual installation results are recorded after those operations complete. Runtime model behavior, Cursor IDE discovery, and adoption by target projects remain `not_run`; file or inventory checks do not establish them.
