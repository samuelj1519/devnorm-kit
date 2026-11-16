# Local mo compatibility

The maintainer's mo `local-release-plugin` adapter originally copies only the primary skill to Agent/Cursor. `multi-skill.patch` adds an optional `copy_skills` list, keeping the existing default unchanged. Each declared skill receives the existing preflight, backup, drift detection, rollback, final verification, and recorded ownership. Claude retains a single native plugin; its standalone link planner excludes every declared member. Inventory lists every Agent/Cursor member under the package owner.

This integration is specific to the backend identified by `patch-identity.json`. It changes only `release_plugin_assets.py`, `agent_sources.py`, and `skillctl`. It never updates other mo sources. A different baseline requires a new review.

Check and apply from the delivery checkout:

```sh
python3 -B scripts/mo_integration.py /path/to/settings/scripts/macos-rebuild
python3 -B scripts/mo_integration.py /path/to/settings/scripts/macos-rebuild --apply
MO_BACKEND=/path/to/settings/scripts/macos-rebuild python3 -B integrations/mo/test_adapter.py
```

Before application, test against a temporary copy of the backend with this patch applied. The fixture tests exercise installation, drift, no-op repetition, helper conflicts, symlink boundaries, complete rollback, inventory ownership, and Claude link exclusions. They use fictional profiles and files, without network or model calls. The script prints the original-file backup directory when applied. To revert, first confirm no other backend changes have occurred and restore only those three originals; retain the backup until local acceptance finishes.

Configure the `devnorm` asset with the accepted release source/revision and its complete `copy_skills` list, then use the normal `mo skills upgrade devnorm` lifecycle. This patch does not change source-generation acceptance or prove runtime model behavior.
