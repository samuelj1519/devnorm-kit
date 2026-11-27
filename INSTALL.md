# Install DevNorm

Choose the guide for your client. The commands install the published [`v2.0.0` tag](https://github.com/samuelj1519/devnorm-kit/tree/v2.0.0). Use one installation route per client and scope.

## Cursor

From the project where you want to use DevNorm, run the Skills CLI.

```sh
npx skills add samuelj1519/devnorm-kit@v2.0.0
```

Choose Cursor when prompted. Select `devnorm` for the development workflow, or include the helpers you want. Choose project scope to keep the installation in this project.

Start a new Cursor session in the project and ask it to use `devnorm`.

## Codex and other Agent Skills clients

Run this command from your project.

```sh
npx skills add samuelj1519/devnorm-kit@v2.0.0
```

Choose Codex or another supported client when prompted. Select `devnorm` and any helpers you want. Start a new session in the project and select `devnorm` or mention it in your request.

The Skills CLI uses Git and Node.js with `npx`. For command options and supported clients, see the [Skills CLI documentation](https://github.com/vercel-labs/skills).

## Claude Code

Add the marketplace to Claude Code, then install the native plugin.

```sh
claude plugin marketplace add "samuelj1519/devnorm-kit#v2.0.0"
claude plugin install devnorm@devnorm
```

The plugin installs at user scope by default and includes all nine skills. Start a new Claude Code session and invoke `/devnorm:devnorm`. If you need a different scope, see the [Claude Code installation guide](https://code.claude.com/docs/en/plugins/install#choose-an-install-scope).

### Replace the former DevNorm marketplace

Keep your existing Claude configuration and installation scope. The examples below use user scope. Add the new marketplace using the install command above, then switch the plugin.

```sh
claude plugin disable devnorm@devnorm-local --scope user
claude plugin install devnorm@devnorm --scope user
claude plugin list
```

After the new ID and version are confirmed, remove the old plugin with its data retained. Remove the old marketplace only after checking that it has no remaining installations.

```sh
claude plugin uninstall devnorm@devnorm-local --scope user --keep-data
claude plugin marketplace remove devnorm-local --scope user
```

If the new installation fails or the version does not match, inspect `claude plugin list`. If the new ID is active, disable it in the same scope with `claude plugin disable devnorm@devnorm --scope user` before restoring the old ID with `claude plugin enable devnorm@devnorm-local --scope user`. [Claude Code marketplace management](https://code.claude.com/docs/en/plugins/install#manage-marketplaces)

## Verify installation

- For the Skills CLI, run `npx skills list` from the project. Add `--global` if you chose user scope.
- For Claude Code, run `claude plugin list` and check for `devnorm@devnorm` at version `2.0.0`.
- In a fresh session, select `devnorm` and ask the agent to identify the skill and a linked method. An installation listing confirms registration. This session check confirms discovery.

If you see duplicate skills, check whether the client has both a native plugin and a standalone installation. Keep the route you want to manage.

## Update or uninstall

For the Skills CLI, rerun the install command with the new [published tag](https://github.com/samuelj1519/devnorm-kit/tags). Choose the original clients and scope. To remove DevNorm skills, run `npx skills remove` and select the entries you installed. Add `--global` if you chose user scope.

For Claude Code, check the marketplace's tag before updating. For removal, use the **Installed** tab in `/plugin` and select the scope where you installed DevNorm. [Claude Code plugin management](https://code.claude.com/docs/en/plugins/install#manage-installed-plugins)

The individual skill lists any tools it needs. State modeling, for example, uses Java, a TLC JAR, and Bun or a compatible Node.js runtime.
