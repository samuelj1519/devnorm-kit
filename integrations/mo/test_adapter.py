"""Run with MO_BACKEND pointing at a patched mo backend containing its test fixtures."""
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

backend = Path(os.environ['MO_BACKEND']).resolve()
sys.path[:0] = [str(backend), str(backend / 'tests')]
from test_release_plugin_assets import ReleaseInstallTests
import release_plugin_assets as release
import agent_sources


class MultiSkillTests(ReleaseInstallTests):
    def setUp(self):
        super().setUp()
        helper = self.source / 'plugin/skills/devnorm-review'
        helper.mkdir()
        (helper / 'SKILL.md').write_text('---\nname: devnorm-review\ndescription: Review\n---\n# Review\n')
        (helper / 'resource.txt').write_text('complete helper resource')
        artifact = release.read(self.source / 'artifact.json')
        artifact['files'] = [{'path': p, 'hash': v[0], 'mode': v[1]} for p, v in sorted(release.signature(self.source).items()) if p not in {'artifact.json', 'SHA256SUMS'}]
        self.write(self.source / 'artifact.json', artifact)
        self.spec['revision'] = release.digest_json(artifact)
        self.spec['copy_skills'] = ['devnorm', 'devnorm-review']
        (self.source / 'SHA256SUMS').write_text(''.join(v[0] + '  ' + p + '\n' for p, v in sorted(release.signature(self.source).items()) if p != 'SHA256SUMS'))

    def test_all_members_installed_and_verified(self):
        self.assertTrue(self.install())
        self.assertTrue(release.inspect('devnorm', self.spec, self.api))
        for base in [self.api.STORE, self.home / '.cursor/skills']:
            self.assertEqual((base / 'devnorm-review/resource.txt').read_text(), 'complete helper resource')
        for profile in ['glm', 'zen']:
            self.assertFalse((self.home / release.PROFILES[profile] / 'skills/devnorm-review').exists())
            self.assertTrue((release.cache(self.home / release.PROFILES[profile], 'devnorm', 'devnorm-local') / 'skills/devnorm-review/resource.txt').is_file())
        a = release.resolve(self.spec, self.api)
        work = self.work / 'second'; work.mkdir()
        prepared = release.prepare('devnorm', self.spec, a, work, self.api)
        self.assertFalse(prepared['needed'])
        self.assertFalse(release.sync('devnorm', self.spec, a, prepared, 'NOOP', self.api))

    def test_unknown_helper_edits_are_preserved(self):
        p = self.api.STORE / 'devnorm-review/SKILL.md'
        p.parent.mkdir(parents=True); p.write_text('user helper')
        with self.assertRaisesRegex(ValueError, 'unmanaged'):
            self.prepared()
        self.assertEqual(p.read_text(), 'user helper')
        self.assertEqual(self.calls, [])

    def test_helper_tampering_is_detected(self):
        self.install()
        (self.home / '.cursor/skills/devnorm-review/resource.txt').write_text('tampered')
        with self.assertRaisesRegex(ValueError, 'unmanaged'):
            release.inspect('devnorm', self.spec, self.api)

    def test_helper_parent_alias_is_rejected(self):
        outside = self.work / 'outside-helper'; outside.mkdir()
        self.api.STORE.mkdir(parents=True)
        (self.api.STORE / 'devnorm-review').symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'symlink'):
            self.prepared()
        self.assertEqual(list(outside.iterdir()), [])

    def test_claude_helper_conflict_stops_before_install(self):
        p = self.home / '.claude-glm/skills/devnorm-review/SKILL.md'
        p.parent.mkdir(parents=True); p.write_text('standalone')
        with self.assertRaisesRegex(ValueError, 'standalone skill conflicts'):
            self.prepared()
        self.assertEqual(self.calls, [])

    def test_failed_native_step_restores_every_helper(self):
        def fail(cfg, cache):
            if cfg.name == '.claude-zen':
                raise RuntimeError('injected helper failure')
        self.fault = fail
        before = self.snapshot()
        with self.assertRaisesRegex(RuntimeError, 'injected helper failure'):
            self.install()
        self.assertEqual(self.snapshot(), before)

    def test_missing_or_duplicate_member_rejected(self):
        self.spec['copy_skills'].append('devnorm-review')
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            self.prepared()
        self.spec['copy_skills'] = ['devnorm', 'missing']
        with self.assertRaisesRegex(ValueError, 'skill missing'):
            self.prepared()


class MultiSkillOwnershipTests(unittest.TestCase):
    def test_inventory_and_claude_link_exclusions(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            for n in ['devnorm', 'devnorm-review']:
                p = home / '.agents/skills' / n; p.mkdir(parents=True)
                (p / 'SKILL.md').write_text('---\nname: ' + n + '\n---\n')
            declaration = {'assets': {'devnorm': {'kind': 'local-release-plugin', 'copy_skills': ['devnorm', 'devnorm-review'], 'claude_profiles': ['glm']}}}
            inventory = agent_sources.discover(home, home / 'settings', declaration)
            self.assertNotIn('local', inventory['assets'])
            clients = inventory['assets']['devnorm']['_runtime']['clients']
            self.assertEqual({c['client'] for c in clients}, {'codex', 'cursor', 'codex/devnorm-review', 'cursor/devnorm-review'})
            loader = importlib.machinery.SourceFileLoader('tested_skillctl', str(backend / 'skillctl'))
            spec = importlib.util.spec_from_loader(loader.name, loader)
            module = importlib.util.module_from_spec(spec)
            loader.exec_module(module)
            module.managed_specs = lambda: declaration['assets']
            self.assertEqual(module.native_release_skills('glm'), {'devnorm', 'devnorm-review'})
            self.assertEqual(module.native_release_skills('default'), set())


if __name__ == '__main__':
    unittest.main()
