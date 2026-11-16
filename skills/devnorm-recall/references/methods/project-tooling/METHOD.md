# Project tooling and human-only steps

**Run only when the prompt explicitly requests check/hook/Git protection configuration or a guide for actions a human must perform.** Ordinary development reuses available tools.

Ordinary Git operations follow the [collaboration standard](../../standard/6-version-control.md). This method's explicit-request restriction applies to tooling setup, not normal Git checks during an authorized task.

## Checks and hooks

Inspect the actual package manager, lockfile, checks, CI, and host support before proposing the smallest concrete patch. Separate quick commit checks from full merge checks. Do not mandate Husky, npm, or one lockfile format. Verify authorization before configuration and installation; never automatically stage or commit for setup. Test allowed and denied command forms and explain alias, shell, and host limits. String matching is not Git semantic parsing and cannot replace authorization.

## Human-only steps

Keep only login, authorization, or dashboard actions the agent cannot perform. Verify official pages, destination, and permissions, then provide reviewable concise steps. Write a wizard only when repetition warrants a script; do not copy unreviewed templates. Use the appropriate credential process without printing secrets, reading .env by default, writing through symlinks, or changing unrelated settings. Verify scripts and actual dashboard steps separately; mark unexecuted paths unverified.

Complete when configuration/steps match the project and applicable checks pass. Missing authority or tools block the affected action. A generated patch is not an installed, enabled, or published feature.

Source: adapted from pinned Matt Pocock wizard for human-only guidance. Hook and Git protection design follows local project rules without copying other installed skills' automatic setup/commit scripts.
