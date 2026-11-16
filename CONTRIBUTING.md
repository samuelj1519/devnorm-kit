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

Create a focused branch from the current `main`. Keep unrelated work out of the change. Use descriptive commits such as `chore(repo): add delivery validation`. Run `make check`, inspect `git diff` and `git diff --cached`, and commit the exact checked files. Push the task branch and open a pull request describing the behavior, validation, and remaining limits. Use an independent reviewer for a complete candidate. Repository owners may bootstrap an empty repository directly on `main` after the same checks.

Generated files are listed in `.devnorm-files.json`. Do not edit them or regenerate hashes to bless manual changes. Each helper deliberately carries its own complete resources so a single selected skill can be installed independently.

## Refresh a generated release

Generate and accept the new version in the source project. Export it to a new empty temporary directory, verify it, then compare its generated registry with this checkout's registry. Replace only the previously registered generated files, removing retired generated files and preserving repository maintenance files. Review and validate the complete resulting tree before committing. The source exporter currently refuses destinations containing extra maintenance files; export to an empty staging directory rather than directly over this repository.

See [repository layout and installation](docs/MAINTENANCE.md) and [the installation guide](INSTALL.md). Source changes, publication, and local installation are separate operations.
