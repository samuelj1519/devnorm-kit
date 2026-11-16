# Install DevNorm

The [README installation section](README.md#install) provides commands for the published `v1.5.0` tag, with the installer pinned to `skills@1.8.1`. Pick one manager for each skill/client/scope.

## Choose a delivery mode

| Target | Method | Scope |
| --- | --- | --- |
| Codex and Cursor | Skills CLI, `--agent codex --agent cursor --copy` | Project by default; add `--global` for user scope |
| Claude Code | Native `devnorm@devnorm-local` plugin | Explicit `--scope user` in the examples |
| Other compatible agents | Pinned skills CLI with the client's supported agent name | Select the intended scope |
| Maintainer's managed Mac | Registered accepted release through `mo` | Existing managed Agent/Cursor copies and Claude profiles |
| Isolated inspection | Local checkout with a temporary `--plugin-dir` session | That session only |

The native plugin includes all nine entries. The skills CLI selects all with `--skill '*'`, the main workflow with `--skill devnorm`, or one helper by its exact name. Each selected skill includes its own references, scripts, licenses, and provenance. Preserve complete directories rather than copying only `SKILL.md`.

For a Claude profile, choose either the native plugin or standalone skill copies. Profile settings, user/project scope, and a plugin cache's existence are separate from discovery in a running session.

## Verify the checkout

Python 3.11 or newer is sufficient for package verification:

```sh
python3 -B scripts/package.py verify
```

For repository tooling and failure-path checks, run `make check`. Generated file bytes, executable modes, provenance, and checksum coverage must match. Root README/INSTALL are independently maintained; their accepted release originals are hash-verified in `docs/generated/`. Those archives retain their original plugin-root relative links and serve reconstruction rather than user navigation.

The accepted runtime package is version `1.5.0`. Candidate: `a22bf22eb0c8d21a31a449d6a48c3675819f20b1bd2fa16decd664186da8b127`. Release identity: `a09cc096df2c4b0e207c4150821ddcb690d14f0f3a6eec71d960b52ed923d41b`. The original [source record and notices](skills/devnorm/THIRD_PARTY_NOTICES.md) remain unchanged.

## Verify discovery

1. Inspect the selected manager's installation list at the intended scope.
2. Open a fresh client session.
3. Select `devnorm` or a helper. In the native Claude plugin, invoke `/devnorm:devnorm`.
4. Ask it to identify the loaded entry and one linked method before using it on a task.

Installer success and static checks do not prove model behavior. Record actual CLI and IDE acceptance separately. See [delivery evidence](docs/DELIVERY.md) for what has been exercised.

## Conditional runtime tools

Ordinary methods use the client's existing tools. Source generation uses Bun; installing and reading the skills does not require it. State modeling requires existing Java, a TLC JAR, and Node with native TypeScript support or Bun. Selected Chinese-writing helpers use Python. The methods check prerequisites before use and do not install these tools automatically.

## Managed updates and recovery

On the maintainer's Mac, use `mo skills upgrade devnorm`, `mo skills check devnorm`, and `mo skills ls devnorm --details`. The current adapter manages all nine Agent/Cursor entries and the complete native Claude plugin. Source registration pins the accepted release hash; it does not adopt third-party updates. See [maintenance](docs/MAINTENANCE.md) for setup, backups, and exact release reconstruction.

For other installations, follow [update and removal instructions](README.md#update-or-uninstall) using the original manager and scope. Preserve user edits, target-project records, unrelated skills, real data, and active cache leases. A temporary plugin session needs no persistent uninstall.
