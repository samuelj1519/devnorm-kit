# DevNorm

[![Validate delivery](https://github.com/samuelj1519/devnorm-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/samuelj1519/devnorm-kit/actions/workflows/validate.yml)
[![Version](https://img.shields.io/badge/version-1.8.0-blue)](https://github.com/samuelj1519/devnorm-kit/tree/v1.8.0)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Development standards and task-specific methods for Codex, Claude Code, Cursor, and other Agent Skills-compatible tools. DevNorm routes a task through requirements, design, implementation, debugging, review, verification, and delivery. Each of its nine skills includes the resources needed for independent installation.

[Install](#install) · [Use](#use) · [Skills](#skills) · [Update or uninstall](#update-or-uninstall) · [Compatibility](#compatibility) · [Contribute](#verify-and-contribute)

## Current release

This working tree and the published `v1.8.0` tag contain accepted DevNorm `1.8.0` (publication authorized by the user on 2026-11-21). See [the delivery record](docs/DELIVERY.md#local-delivery-180-2026-11-21) for checks and limits. Installed and loaded versions must be checked separately.

## Install

Use one installation manager per skill in each client. If this machine already manages DevNorm with `mo`, use [the mo commands](#maintainer-managed-installation) instead of adding another copy.

### Codex and Cursor

Prerequisites: Git, Node.js **22.20.0 or newer**, npm with `npx`, and an installed client with Agent Skills support. The commands below pin the installer to `skills@1.8.1` and DevNorm to the published `v1.8.0` tag.

Run this command from the project where you want to use the skills:

```sh
npx --yes skills@1.8.1 add samuelj1519/devnorm-kit@v1.8.0 --skill '*' --agent codex --agent cursor --copy --yes
```

This installs all nine entries at project scope. `--copy` keeps each installation self-contained. To install for only one client, keep its `--agent` option. To use user scope across projects, add `--global`. To install only the main workflow, replace `--skill '*'` with `--skill devnorm`.

Inspect the selected scope after installation:

```sh
npx --yes skills@1.8.1 list
```

For user scope, add `--global` to the list command. Start a fresh client session and select `devnorm` from its skill menu. See the [pinned installer reference](https://github.com/vercel-labs/skills/blob/v1.8.1/docs/commands.md) for other supported agents.

### Claude Code

Install the complete native plugin at user scope:

```sh
claude plugin marketplace add samuelj1519/devnorm-kit#v1.8.0
claude plugin install devnorm@devnorm-local --scope user
claude plugin list --json
```

Confirm that `devnorm@devnorm-local` is listed at version `1.8.0`, then start a fresh session and invoke `/devnorm:devnorm`. The marketplace name is `devnorm-local` even when its source is GitHub. All nine skills are included.

For a standalone skill installation instead, use the skills CLI above with `--agent claude-code`. Choose either the native plugin or standalone copies for that Claude profile to keep a single effective installation. See [Claude's plugin installation guide](https://code.claude.com/docs/en/plugins/install).

### Local checkout and temporary loading

To inspect the pinned package or use an offline checkout:

```sh
git clone --branch v1.8.0 https://github.com/samuelj1519/devnorm-kit.git
cd devnorm-kit
python3 -B scripts/package.py verify
```

Package verification requires Python 3.11 or newer. To install this checkout, replace the GitHub source in the skills CLI command with its absolute directory path. Ordinary skill use requires the client's existing tools; Bun is only needed to develop the source project.

For a temporary Claude Code session, run `claude --plugin-dir /absolute/path/to/devnorm-kit`. A compatible Cursor CLI can load the same checkout with `cursor-agent --workspace /path/to/project --plugin-dir /absolute/path/to/devnorm-kit`. Temporary loading does not create a persistent installation.

### Maintainer-managed installation

On the maintainer's Mac, the accepted release and all nine skills are registered with `mo`:

```sh
mo skills upgrade devnorm --dry-run
mo skills upgrade devnorm
mo skills check devnorm
mo skills ls devnorm --details
```

`mo` is a maintainer-specific tool, not a prerequisite for other users. It maintains Agent/Codex copies, Cursor copies, and the native Claude plugin across the registered profiles. See [local setup and ownership](docs/MAINTENANCE.md).

## Use

Ask for the main workflow in your task, or select a helper when you want one capability:

```text
Use devnorm to implement this change. Read the project rules first and verify the resulting behavior.

Use devnorm-debug to reproduce this bug and verify its root cause and repair.

Use devnorm-interview to clarify the requirements, at most three rounds.
```

In Codex, explicitly select `$devnorm` or a helper such as `$devnorm-review`. In a native Claude plugin session, use `/devnorm:devnorm` or `/devnorm:devnorm-review`. In Cursor, select the entry through the available skill UI or name it in your request.

Project rules and your task's permissions remain authoritative. Installing DevNorm does not change a project's adopted standard or authorize commits, account changes, deployment, or installation of other tools.

## Skills

| Skill | Purpose | Selection |
| --- | --- | --- |
| [devnorm](skills/devnorm/SKILL.md) | Route development tasks through the project workflow | By task |
| [devnorm-design](skills/devnorm-design/SKILL.md) | Design module interfaces, domain concepts, and shared state | When applicable |
| [devnorm-debug](skills/devnorm-debug/SKILL.md) | Reproduce defects and verify repairs | When applicable |
| [devnorm-review](skills/devnorm-review/SKILL.md) | Independently review a fixed candidate against standards and requirements | When applicable |
| [devnorm-verify](skills/devnorm-verify/SKILL.md) | Verify actual CLI, service, browser, or native behavior | When applicable |
| [devnorm-interview](skills/devnorm-interview/SKILL.md) | Conduct a bounded requirements interview | Explicit request |
| [devnorm-recall](skills/devnorm-recall/SKILL.md) | Recover scoped project history | Explicit request |
| [devnorm-tdd](skills/devnorm-tdd/SKILL.md) | Apply test-first cycles to suitable logic and defects | When applicable |
| [devnorm-sources](skills/devnorm-sources/SKILL.md) | Manually inspect sources and new capabilities | Explicit request |

The [capability index](skills/devnorm/references/capabilities.json) maps each capability to its methods, prerequisites, and completion criteria. UI work, performance measurement, and state modeling apply when the task needs them.

## Update or uninstall

Keep the client and installation scope consistent with the original install. Preserve any local edits before replacing skill copies.

For the skills CLI, choose the next accepted tag or full commit and rerun the same `add` command for the selected DevNorm entries and agents. Reinstall local sources from their complete checkout. The CLI also provides `check` and `update`; use a fixed source ref when you want to remain on a reviewed release.

To remove the project-scoped main skill:

```sh
npx --yes skills@1.8.1 remove devnorm --yes
```

To remove all nine DevNorm entries while preserving unrelated skills:

```sh
npx --yes skills@1.8.1 remove devnorm devnorm-design devnorm-debug devnorm-review devnorm-verify devnorm-interview devnorm-recall devnorm-tdd devnorm-sources --yes
```

Replace `devnorm` in the single-skill command with another DevNorm skill name to remove that entry. Add `--global` for a user-scoped installation. To remove entries only from selected clients, include the original `--agent` selections. Omitting `--agent` removes the selected skills across agents at that scope. The installer may retain shared content used by another agent. Review the selected scope before removing every entry.

For a Claude native installation:

```sh
claude plugin uninstall devnorm@devnorm-local --scope user
```

When moving to another accepted tag, update the marketplace's pinned source, then reinstall or update the plugin through Claude's native manager. Remove the `devnorm-local` marketplace only when no longer needed. On the managed Mac, use `mo` for upgrades and its recorded ownership/backups for recovery.

## Compatibility

DevNorm bundles adapted development methods from several upstream projects. Similar standalone skills can remain useful outside the DevNorm workflow. When both are installed, choose one implementation for each capability within a task, particularly for TDD, review, requirements interviews, and UI design.

DevNorm does not require separate pstack, Matt Pocock, or interface-method bundles. Those bundles also contain capabilities DevNorm does not replace. Keep native plugins intact and manage them with their owner rather than deleting files from their caches.

## Troubleshooting

| Symptom | Check |
| --- | --- |
| A skill does not appear | Confirm the client and project/user scope, then open a fresh session |
| Claude lists the plugin but its command is absent | Check that it is enabled in the intended profile; use the `/devnorm:` namespace |
| A skill appears twice | Check for both native plugin and standalone copies, or installations from multiple managers |
| Cursor cannot find `/add-plugin devnorm` | Use the skills CLI or temporary local loading; this package does not claim a Cursor marketplace listing |
| A specialized method reports a missing tool | Follow that method's prerequisites; ordinary installation does not install its toolchain |
| Hash verification fails | Compare the complete accepted package and executable modes; preserve local edits before recovery |

State modeling needs existing Java, a TLC jar, and Node with native TypeScript support or Bun. Selected Chinese-writing helpers use Python. These are conditional requirements; see the [installation guide](INSTALL.md).

## Verify and contribute

```sh
make check
```

This checks generated identities, skill resources, and the package tools. Client discovery, actual model behavior, and native UI acceptance require separate evidence. See [delivery results and limits](docs/DELIVERY.md).

For changes, read [CONTRIBUTING.md](CONTRIBUTING.md). Runtime skill source and source adoption live in [samuelj1519/devnorm](https://github.com/samuelj1519/devnorm). Repository maintenance and this homepage live here. See [the ownership guide](docs/MAINTENANCE.md) and [security reporting](SECURITY.md).

## License and sources

Original DevNorm content uses the [MIT license](LICENSE). Third-party content retains its own licenses and notices. The [provenance](skills/devnorm/provenance.json) and [third-party notices](skills/devnorm/THIRD_PARTY_NOTICES.md) identify fixed source commits, adaptations, and bundled licenses.

The generated skill package is English. Chinese writing guidance and examples remain Chinese. This distribution does not automatically adopt unreviewed upstream changes.
