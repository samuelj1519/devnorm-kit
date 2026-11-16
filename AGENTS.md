# DevNorm delivery repository

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing this package. `skills/` and the files in `.devnorm-files.json` are generated from accepted inputs in [devnorm](https://github.com/samuelj1519/devnorm); change their source and regenerate them together.

The root `README.md` and `INSTALL.md` are repository-maintained. The accepted release originals remain hash-verified in `docs/generated/`. Other repository maintenance lives in `.github/`, ordinary `docs/`, `scripts/`, `tests/`, and `integrations/`. Keep each skill self-contained and preserve third-party licenses, provenance, executable modes, and explicit invocation metadata.

Run `make check` before delivery. This checks package integrity and repository tooling; client discovery and model behavior require separate evidence. Use the current task's authorization for commits, pushes, and installation. Review complete candidates in a fresh non-author context before acceptance.
