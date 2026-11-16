# Export ownership verification

This directory records the repository-layout change for the existing accepted DevNorm `1.5.0` artifact. The root README/INSTALL become repository-owned; their original accepted bytes remain in `docs/generated/`. No runtime entry, method, source record, accepted artifact identity, or installed copy changes.

The input release identity is `a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b`.

## Model

Set `TLA2TOOLS` to the existing TLC JAR and optionally `JAVA` to the Java executable, then run:

```sh
python3 -B verification/export/check.py
```

The driver checks safety, deadlocks, termination under weak fairness, three reachability witnesses, and an unsafe rollback mutation. It writes the corresponding logs here. TLC may require permission for its local RMI socket. The model treats rollback atomically and does not model backup bytes, symlinks, or cleanup I/O; filesystem regressions cover those boundaries.

## Source implementation

The source repository's `tests/delivery/artifacts.test.ts` exercises preserved repository documents/CI, root-document seeding and legacy migration, unknown generated content, symlinks, every old/new unit transfer failure, source/lock drift, foreign installed/backup files and empty directories, late symlinks, and cleanup I/O failure. The final source `bun run verify` passed 174 tests plus dependency, type, formatting, and standard checks.

Independent review found three real cleanup failures during this work. Their original ordinary-file, empty-directory, and symlink probes were replayed after repair; each now preserves external content and the recovery journal. The temporary-tree fingerprint check covers observed operation boundaries, not arbitrary OS writes inside an individual native filesystem operation.

## Existing-artifact conversion

`bun run build --export` was attempted and correctly rejected with `toolchain-changed`: the edited generator is not the program identity in the old accepted snapshot. That operation did not render a release, change the accepted lock, or install anything. The source program changes remain subject to the source project's next prepare/check/review/accept cycle.

The exported `exportRepository` function has a narrower role: verify an already materialized immutable artifact and convert its repository layout. It does not render skills, accept a candidate, or change installation state. For this user-authorized documentation ownership migration, the implementation received independent review and complete source checks. The following invocation ran from the source checkout into a new temporary directory:

```sh
bun --no-install -e 'import { exportRepository } from "./src/delivery/artifacts.ts"; import { hashObject, readJson } from "./src/delivery/identity.ts"; const releaseRoot = "/path/to/devnorm/dist/1.5.0"; const expected = "a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b"; if (hashObject(readJson(releaseRoot + "/artifact.json")) !== expected) throw new Error("Accepted release identity differs"); const result = await exportRepository({ releaseRoot, destination: "/path/to/new-temporary-export" }); if (result.artifactHash !== expected) throw new Error("Export identity differs"); console.log(JSON.stringify(result));'
```

The [actual conversion result](conversion.log) identifies the local input/output operation. All registered output files, modes, and control files match this repository. `release-artifact.json` remains byte-identical to the accepted input `artifact.json`. Only the root documentation ownership and its archived paths change.

The verifier supports both the original `v1.5.0` layout and this separated-document layout. `make check` here passed 11 tests, including exact reconstruction after root-document edits, archive tampering/unknown-file rejection, and legacy-layout reconstruction. A real isolated `skills@1.8.1` installation/removal probe installed all nine entries and removed them while preserving an unrelated fictional skill; no existing user installation was changed.
