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

Edit root `README.md`, root `INSTALL.md`, and other repository-owned documentation in this repository. The exporter owns every path in `.devnorm-files.json`, including the accepted documentation copies in `docs/generated/`. Regenerate those files from an accepted source release. Each helper includes the resources needed for independent installation.

## Refresh a generated release

Generate and accept the new version in the source project. Run `bun run build --export ../devnorm-kit` from that source checkout. It verifies and replaces generated content while preserving root documentation, CI, ordinary docs, and other repository-owned files. Generated archives in `docs/generated/` retain the exact accepted README/INSTALL bytes. Review the registry diff and run `make check` on the exact Kit combination before merging directly into `main`. Generator code changes still require the source prepare/check/review/accept cycle before full runtime regeneration. See [export ownership](docs/HASH-SCOPE.md) for the generated paths and recovery behavior.

For a release, create matching annotated `vX.Y.Z` tags in both repositories. Tag the verified source commit containing the accepted record and evidence archive, and the checked Kit commit. Confirm each tagged commit is reachable from its repository’s `main`. Push `main` and the matching tag as authorized, then verify the remote refs. Check authorization separately for GitHub Releases, installation and source changes. See [repository layout and installation](docs/MAINTENANCE.md) and [the installation guide](INSTALL.md).
