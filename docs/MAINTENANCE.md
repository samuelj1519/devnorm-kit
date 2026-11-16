# Delivery maintenance

## Ownership and layout

| Location | Owner and purpose |
| --- | --- |
| `skills/` | Generated, self-contained skill entries and resources |
| `plugin.json`, `.claude-plugin/`, `.cursor-plugin/` | Generated native plugin discovery metadata |
| `artifact.json`, `release-artifact.json`, `SHA256SUMS`, `.devnorm-files.json` | Generated delivery, accepted release, and ownership identities |
| `README.md`, `INSTALL.md`, `LICENSE` | Generated user documentation and original-content license |
| `scripts/`, `tests/`, `Makefile` | Repository validation and exact accepted-release reconstruction |
| `.github/` | Pull request checks, issue intake, and dependency update configuration |
| `integrations/mo/` | Maintainer-specific mo compatibility patch and its exact baseline identities |

Generated payloads remain unchanged when repository maintenance files change. Git records both layers. Each skill retains independent resources; sharing them with symlinks would break independent copies.

## Maintainer installation with mo

The existing local mo release adapter expects a release layout with `plugin/` and `agent-skills/`. This repository uses the native plugin as its root. Reconstruct the exact accepted release without changing its identity:

```sh
python3 -B scripts/package.py verify
mkdir -p /path/to/persistent/releases
python3 -B scripts/package.py restore-release /path/to/persistent/releases/1.5.0
```

The destination must not exist. Reconstruction checks every output against `release-artifact.json`; it does not create a new release or accept unreviewed content.

The maintainer's mo backend needs the [multi-skill adapter](../integrations/mo/README.md) to copy all nine entries. Register only the `devnorm` asset in `manifests/managed-agent-assets.json` using the printed absolute `source`, full `revision`, marketplace `devnorm-local`, the existing Claude profiles, and the printed skill names as `copy_skills`. Other source registrations stay unchanged. Then run:

```sh
mo skills upgrade devnorm --dry-run
mo skills upgrade devnorm
mo skills check devnorm
mo skills ls devnorm --details
```

mo owns backup, immutable local source, installation records, and consumer verification. Agent/Codex reads `~/.agents/skills/`; Cursor receives complete copies in `~/.cursor/skills/`; Claude uses its native plugin CLI across the already registered profiles. Standalone Claude copies would duplicate the native plugin. The compatibility patch excludes all declared entries from those links.

Keep the persistent release and pinned revision until a new accepted version replaces them. Use mo for later upgrades. Backup paths and operation IDs are printed by mo. For failure recovery, preserve the reported backup and inspect the failed operation before retrying; do not erase active cache leases or unrelated settings.

## Evidence and limits

`make check` validates the delivered files and tooling. `mo skills check devnorm` validates installed payloads and registrations. A fresh client session must separately demonstrate discovery and actual behavior; inventory reports `loaded=unknown` until then. CLI and IDE results are separate. See [delivery evidence](DELIVERY.md) for this delivery's results.

## Reference basis

- [GitHub repository practices](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [GitHub Actions security](https://docs.github.com/en/actions/reference/security/secure-use): read-only token, pinned action, no persisted checkout credentials.
- [Agent Skills specification](https://agentskills.io/specification) and [authoring practices](https://agentskills.io/skill-creation/best-practices): descriptive entrypoints, progressive disclosure, complete referenced resources.
- [Claude plugin manifest](https://code.claude.com/docs/en/plugins-reference) and [Cursor plugin reference](https://cursor.com/docs/reference/plugins).

Reference pages were consulted on 2026-11-16. Native client behavior remains subject to actual verification.
