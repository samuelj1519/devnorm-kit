# Contributing

This repository distributes accepted DevNorm releases. Workflow and skill source belongs in [samuelj1519/devnorm](https://github.com/samuelj1519/devnorm). The generated package remains English; its Chinese writing resources retain their original language.

## Check a checkout

Use Git, Make, and Python 3.11 or newer. No Python dependencies or package installation are required.

```sh
git clone https://github.com/samuelj1519/devnorm-kit.git
cd devnorm-kit
make check
```

The verifier checks bytes, executable modes, checksum coverage, accepted release identity, skill names, entry links, invocation policies, and plugin versions. Tests exercise corruption, extra runtime files, unsafe paths, symlinks, and exact release reconstruction. These checks do not prove that a running client has loaded a skill.

## Change and review

Keep `main` as the only long-lived branch. Work from current `main` in a temporary branch or isolated checkout. Keep changes focused and use descriptive commits such as `chore(repo): add delivery validation`. Run `make check` on the exact combination and inspect `git diff` and `git diff --cached` before committing. Formal tasks require independent review of the complete candidate. Merge completed work directly into `main` without a pull request, following the configured remote rules. When authorized to clean up, remove only merged, unreferenced branches. Keep branches with unique commits or records. Check authorization separately for local commits, merges and pushes.

Generated files are listed in `.devnorm-files.json`. Root `README.md` and `INSTALL.md` are independently maintained here; their accepted release originals remain in `docs/generated/` for integrity verification and exact reconstruction. Do not edit them or regenerate hashes to bless manual changes. Each helper deliberately carries its own complete resources so a single selected skill can be installed independently.

## Refresh a generated release

Generate and accept the new version in the source project. Run `bun run build --export ../devnorm-kit` from that source checkout using the exporter with repository ownership support. It verifies and replaces generated content while preserving root documentation, CI, ordinary docs, and other repository-owned files. Generated archives in `docs/generated/` retain the exact accepted README/INSTALL bytes. Review the registry diff and run `make check` on the exact Kit combination before merging directly into `main`. A legacy exporter that rejects extra repository files must be upgraded before synchronizing this layout. Generator code changes still require the source prepare/check/review/accept cycle before full runtime regeneration. The existing-artifact-only documentation conversion and its exact inputs are recorded in [export verification](verification/export/README.md).

For a release, create matching annotated `vX.Y.Z` tags in both repositories. Tag the verified source commit containing the accepted record and evidence archive, and the checked Kit commit. Confirm each tagged commit is reachable from its repository’s `main`. Push `main` and the matching tag as authorized, then verify the remote refs. Check authorization separately for GitHub Releases, installation and source changes. See [repository layout and installation](docs/MAINTENANCE.md) and [the installation guide](INSTALL.md).
