# Install DevNorm 1.10.1

This package provides the `devnorm` workflow skill and independently invocable helpers with the development standard, task-specific methods, runtime resources, and licenses. Ordinary method reading needs the agent's existing tools, not the source repository's Bun build environment.

## Verify the package

Candidate: `7cf1e582e18570f6a43c86b02f6113f8ea0eb9fb8610f232af99b79f41d0836e`. Check `artifact.json` and every entry in `SHA256SUMS` before loading. The skill's `provenance.json` and `THIRD_PARTY_NOTICES.md` identify original commits, adaptations, and licenses.

| Location | Generated release | Delivery repository |
| --- | --- | --- |
| Native plugin root | `plugin/` | Repository root |
| Standalone skill | `agent-skills/devnorm/` | `skills/devnorm/` |
| Claude marketplace | Root `.claude-plugin/marketplace.json` points to `./plugin` | Root marketplace points to `./` |

Keep one effective installation per skill in each host. The two exported skill trees are identical in content and modes.

## Unified local installation with mo

On the maintainer's managed Mac, use the registered DevNorm source through `mo skills upgrade devnorm`, then `mo skills check devnorm` and `mo skills ls devnorm --details`. The source registration must identify the accepted release and content hash. A missing registration is a setup condition, not permission to update unrelated sources.

mo owns local installation, scope, backups, and checks. Source generation remains DevNorm's responsibility. Installation does not publish this repository or make every target project adopt the standard. Existing project rules remain authoritative.

## Install the skill with npx

From the target project, use the complete delivery repository as a local source:

```sh
npx --yes skills@1.8.1 add /path/to/devnorm-kit --skill devnorm --agent codex --agent cursor --copy
```

Use `--agent claude-code` for the standalone Claude skill alternative. Choose either this alternative or the native Claude plugin for that host. `--copy` produces independent complete copies. Without `-g`, installation is project-scoped. Select global scope explicitly when intended.

For a published delivery version, replace the local path with `samuelj1519/devnorm-kit@<release-tag-or-full-commit>`. This remote form requires the content to have been committed and pushed. This package does not claim a tag exists merely because it was generated.

Use the same pinned CLI's `list`, `check`, and `update` commands for published Git versions. Reinstall a local source to refresh it. To remove this one skill from every project-level consumer and its shared canonical directory, run `npx --yes skills@1.8.1 remove devnorm --yes`. Per-agent removal may retain shared content used by other compatible agents. An installer success does not prove model behavior. Verify the entry and method resources in a fresh client session. Reference: [skills CLI 1.8.1](https://github.com/vercel-labs/skills/blob/v1.8.1/docs/commands.md).

## Cursor

pstack's official Cursor entry is `/add-plugin pstack` because it is listed in Cursor's marketplace. DevNorm is not listed there. Use the verified standard-skill installation above or mo's configured Cursor consumer for local delivery. Do not assume `/add-plugin devnorm` works before listing or marketplace registration.

For an isolated native plugin session, run:

```sh
cursor-agent --workspace /isolated/project --plugin-dir /path/to/plugin-root
```

Use the generated `plugin/` directory or the delivery repository root. In a new session, select `/devnorm` from the supported skill UI before the task when available. Confirm the loaded entry and packaged method. CLI and IDE acceptance are separate. Native marketplace registration in the CLI uses `cursor-agent plugin marketplace add <git-url>` and requires a published accessible Git source. It is separate from plugin selection/activation.

Keep the full skill directory for Cursor copies. Its local and Cloud Agents discovery behavior must be verified separately; a plugin cache alone does not prove either is loaded. Reference: [Cursor plugins](https://cursor.com/docs/plugins), [pstack installation](https://github.com/cursor/plugins/tree/main/pstack#install).

## Claude Code

Temporary loading uses `claude --plugin-dir /path/to/plugin-root`. Invoke `/devnorm:devnorm` in a fresh session. Existing compatible wrappers, such as a user-configured `claude-glm`, may pass the same plugin arguments. Record the actual model/provider separately.

For persistent native installation, add the root marketplace and install the plugin:

```sh
claude plugin marketplace add /path/to/release-or-delivery-repository
claude plugin install devnorm@devnorm-local --scope user
claude plugin list --json
```

Use the intended `CLAUDE_CONFIG_DIR` for a named profile. Keep installation changes within the selected scope. A new session must discover `/devnorm:devnorm`. Native plugin installation and standalone `.claude/skills/devnorm/` installation are alternatives. Reference: [Claude plugin installation](https://code.claude.com/docs/en/plugins/install).

## Runtime requirements

Ordinary methods read documents. Methods that need tools check actual availability and authorization first. State modeling requires existing Java, a TLC jar, and Node with native TypeScript support or Bun. Set `JAVA` and `TLA2TOOLS` and use the packaged controlled entry; it does not install tools. Python is needed only for selected Chinese-writing helpers. Pele rendering is optional. Keep Mermaid and explicit limitations if unavailable.

## Update or remove

Choose a fixed new version, preserve target-project content, and replace the complete owned installation through its manager. Do not mix files from versions. mo updates accepted DevNorm releases, not unreviewed third-party upstream content.

For npx installation, remove only the selected `devnorm` skill with the pinned CLI. For Claude native installation, use `claude plugin uninstall devnorm@devnorm-local --scope user`, then remove the local marketplace if no longer needed. A temporary plugin-dir session does not create a persistent installation. Verify absence in a fresh session. Preserve project records, real data, and other skills.

## Acceptance scope

File checks, schemas, tests, models, installation, client discovery, and real model tasks prove different things. Read the current source-repository acceptance report for the exact tested version. Unrun items remain `not_run`. No commit, push, public listing, or unrelated installation follows automatically from these instructions.

## Select skills

Read the generated README skill list. Native plugins contain all entries. With skills CLI, choose `--skill devnorm` for the main workflow, `--skill devnorm-review` for one complete helper, or `--skill '*'` for every entry. Each copied skill is self-contained. Do not mix versions. Explicit helper entries carry Claude/Cursor invocation metadata and Codex policy metadata; actual host behavior still needs verification.

The current local mo integration manages the main skill for Codex/Cursor copies. Do not claim helper copies are installed merely because a new bundle was generated; native plugin and skills-CLI selection have separate acceptance.
