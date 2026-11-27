# DevNorm Kit

[![Validate delivery](https://github.com/samuelj1519/devnorm-kit/actions/workflows/validate.yml/badge.svg)](https://github.com/samuelj1519/devnorm-kit/actions/workflows/validate.yml)
[![Tagged release](https://img.shields.io/badge/tagged%20release-v2.0.0-blue)](https://github.com/samuelj1519/devnorm-kit/tree/v2.0.0)
[![MIT license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

DevNorm gives coding agents a workflow for deciding when a change needs design, review, or further testing. It also includes standalone skills for debugging, design, review, and verification.

**Package version in this checkout: `2.0.0`.** After installation, open `INSTALL.md` in the installed skill directory to see its version.

## Install

In your project, use the Skills CLI for Cursor, Codex, or another supported client.

```sh
npx skills add samuelj1519/devnorm-kit@v2.0.0
```

Choose your client, skills, and installation scope when prompted. For Claude Code, add the marketplace and install its native plugin.

```sh
claude plugin marketplace add "samuelj1519/devnorm-kit#v2.0.0"
claude plugin install devnorm@devnorm
```

See the installation guide for [Cursor](INSTALL.md#cursor), [Codex and other Agent Skills clients](INSTALL.md#codex-and-other-agent-skills-clients), or [Claude Code](INSTALL.md#claude-code).

## Use

Start a new session in your project and ask the agent to use a skill.

```text
Use devnorm to implement this change and verify the result.
```

Use `devnorm` to choose the workflow for the change. Select a helper when you want to work on one part of a task. Each helper includes its own reference files.

| Skill | Use it to |
| --- | --- |
| [devnorm](skills/devnorm/SKILL.md) | Choose the workflow and checks for a change |
| [devnorm-design](skills/devnorm-design/SKILL.md) | Design interfaces, domain concepts, and shared state |
| [devnorm-debug](skills/devnorm-debug/SKILL.md) | Reproduce a defect and verify the repair |
| [devnorm-review](skills/devnorm-review/SKILL.md) | Independently review a fixed candidate against its requirements |
| [devnorm-verify](skills/devnorm-verify/SKILL.md) | Verify actual behavior in a CLI, service, browser, or native app |
| [devnorm-tdd](skills/devnorm-tdd/SKILL.md) | Develop suitable logic and defect fixes test-first |
| [devnorm-interview](skills/devnorm-interview/SKILL.md) | Clarify requirements through an explicitly requested interview |
| [devnorm-recall](skills/devnorm-recall/SKILL.md) | Recover project history when requested |
| [devnorm-sources](skills/devnorm-sources/SKILL.md) | Inspect upstream sources and capabilities when requested |

Your project rules govern which actions the agent can take and how the project adopts a DevNorm version.

## Verify and contribute

Use the [artifact manifest](artifact.json) to identify this checkout. See the [delivery record](docs/DELIVERY.md) for the checks run on the published version and the [installation guide](INSTALL.md#verify-installation) to confirm that a client loads the skill.

This repository distributes DevNorm. Work on the standard and skill content in the [source repository](https://github.com/samuelj1519/devnorm). For changes to this distribution, read [Contributing](CONTRIBUTING.md).

DevNorm content uses the [MIT license](LICENSE). Bundled materials retain their [licenses and notices](skills/devnorm/THIRD_PARTY_NOTICES.md). The [provenance record](skills/devnorm/provenance.json) identifies their sources and adaptations.
