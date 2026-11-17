import hashlib
import importlib.util
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[1]
PATCH = REPO / 'integrations/mo/multi-skill.patch'


def load_module():
    spec = importlib.util.spec_from_file_location('mo_integration', REPO / 'scripts/mo_integration.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def patch_hunks():
    """Old lines the real patch matches, keyed by backend filename."""
    files = {}
    name = None
    lines = PATCH.read_text().splitlines()
    index = 0
    while index < len(lines):
        if lines[index].startswith('--- '):
            index += 1
            name = lines[index][4:]
            if name.startswith('b/'):
                name = name[2:]
            files[name] = []
            index += 1
            continue
        if lines[index].startswith('@@'):
            header = lines[index].split()[1][1:]
            start = int(header.split(',')[0])
            old = []
            index += 1
            while index < len(lines) and not lines[index].startswith(('@@', '--- ')):
                prefix, body = lines[index][:1], lines[index][1:]
                if prefix in ' -':
                    old.append(body)
                elif prefix not in '+\\':
                    break
                index += 1
            files[name].append((start, old))
            continue
        index += 1
    return files


def write_fixture(directory):
    """Write three files the shipped patch can apply, and return before/after hashes.

    Filler lines hold the hunk line numbers. They are not the mo backend, and
    prepare() would refuse to compile them. Callers replace compile for that check.
    """
    backend = directory / 'backend'
    backend.mkdir()
    for name, hunks in patch_hunks().items():
        last = 0
        for start, old in hunks:
            last = max(last, start + max(len(old), 1) - 1)
        content = ['x = 1'] * last
        for start, old in hunks:
            for offset, line in enumerate(old):
                content[start - 1 + offset] = line
        (backend / name).write_text('\n'.join(content) + '\n')
    stage = directory / 'stage'
    shutil.copytree(backend, stage)
    subprocess.run(['patch', '--batch', '-p1', '-i', str(PATCH)], cwd=stage, check=True, capture_output=True)
    identities = {}
    for name in patch_hunks():
        identities[name] = {
            'before': hashlib.sha256((backend / name).read_bytes()).hexdigest(),
            'after': hashlib.sha256((stage / name).read_bytes()).hexdigest(),
        }
    shutil.rmtree(stage)
    return backend, identities


class MoBackupTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hold = tempfile.TemporaryDirectory()
        cls.pristine, cls.identities = write_fixture(Path(cls.hold.name))
        cls.module = load_module()

    @classmethod
    def tearDownClass(cls):
        cls.hold.cleanup()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.backend = Path(self.temp.name) / 'backend'
        shutil.copytree(self.pristine, self.backend)
        self.sandbox = Path(__file__).resolve().parent / '.mo-backup-sandbox' / self.id().replace('.', '_')
        self.sandbox.mkdir(parents=True)
        self.home = self.sandbox / 'home'
        self.home.mkdir()

    def tearDown(self):
        self.temp.cleanup()
        shutil.rmtree(self.sandbox, ignore_errors=True)
        try:
            self.sandbox.parent.rmdir()
        except OSError:
            pass

    def hashes(self, directory):
        return {name: hashlib.sha256((directory / name).read_bytes()).hexdigest() for name in self.identities}

    def run_apply(self, extra, fault_on_replace=None):
        module = self.module
        real_loads = json.loads
        real_replace = os.replace
        argv = sys.argv
        home = os.environ.get('HOME')
        calls = {'n': 0}

        def loads(text):
            data = real_loads(text)
            row = data.get('release_plugin_assets.py') if isinstance(data, dict) else None
            if isinstance(row, dict) and 'before' in row and 'after' in row:
                return self.identities
            return data

        def replace(src, dst, *args, **kwargs):
            calls['n'] += 1
            if fault_on_replace is not None and calls['n'] == fault_on_replace:
                raise OSError('injected replace failure')
            return real_replace(src, dst, *args, **kwargs)

        os.environ['HOME'] = str(self.home)
        sys.argv = ['mo_integration.py', str(self.backend), *extra]
        module.json.loads = loads
        # The fixture carries patch context only. Production still compiles real backends.
        module.compile = lambda *args, **kwargs: None
        os.replace = replace
        buffer = io.StringIO()
        try:
            with redirect_stdout(buffer):
                module.main()
        finally:
            module.json.loads = real_loads
            del module.compile
            os.replace = real_replace
            sys.argv = argv
            if home is None:
                os.environ.pop('HOME', None)
            else:
                os.environ['HOME'] = home
        return buffer.getvalue()

    def backup_from(self, output):
        line = next(item for item in output.splitlines() if item.startswith('backup='))
        return Path(line.split('=', 1)[1])

    def assert_outside_system_temp(self, path):
        temp_root = Path(tempfile.gettempdir()).resolve()
        self.assertFalse(path.resolve().is_relative_to(temp_root))

    def test_apply_stores_originals_under_the_home_backup_root(self):
        output = self.run_apply(['--apply'])
        backup = self.backup_from(output)
        root = self.home / '.agents' / 'backups'
        self.assertEqual(backup.parent, root.resolve())
        self.assertRegex(backup.name, r'^devnorm-mo-patch-\d{8}T\d{6}Z-[0-9a-f]{8}$')
        self.assert_outside_system_temp(backup)
        self.assertEqual(stat.S_IMODE(backup.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(root.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE((self.home / '.agents').stat().st_mode), 0o700)
        self.assertEqual(self.hashes(backup), {name: row['before'] for name, row in self.identities.items()})
        self.assertEqual(self.hashes(self.backend), {name: row['after'] for name, row in self.identities.items()})
        self.assertIn('status=applied', output.splitlines())

    def test_backup_root_override_is_used_and_home_is_untouched(self):
        root = self.sandbox / 'chosen'
        output = self.run_apply(['--apply', '--backup-root', str(root)])
        backup = self.backup_from(output)
        self.assertEqual(backup.parent, root.resolve())
        self.assert_outside_system_temp(backup)
        self.assertFalse((self.home / '.agents').exists())
        self.assertEqual(stat.S_IMODE(backup.stat().st_mode), 0o700)
        self.assertEqual(self.hashes(backup), {name: row['before'] for name, row in self.identities.items()})

    def test_check_does_not_create_the_backup_directory(self):
        root = self.sandbox / 'unused'
        output = self.run_apply(['--backup-root', str(root)])
        self.assertIn('status=ready', output.splitlines())
        self.assertFalse(root.exists())
        self.assertEqual(self.hashes(self.backend), {name: row['before'] for name, row in self.identities.items()})

    def test_failed_replace_restores_originals_and_keeps_the_backup(self):
        root = self.sandbox / 'rollback'
        with self.assertRaisesRegex(OSError, 'injected replace failure'):
            self.run_apply(['--apply', '--backup-root', str(root)], fault_on_replace=2)
        self.assertEqual(self.hashes(self.backend), {name: row['before'] for name, row in self.identities.items()})
        created = list(root.iterdir())
        self.assertEqual(len(created), 1)
        self.assert_outside_system_temp(created[0])
        self.assertEqual(self.hashes(created[0]), {name: row['before'] for name, row in self.identities.items()})

    def test_existing_backup_directory_is_not_reused(self):
        root = self.sandbox / 'collide'
        root.mkdir()
        root.chmod(0o755)
        existing = root / 'devnorm-mo-patch-20261117T000000Z-aaaa'
        existing.mkdir()
        (existing / 'keep').write_text('keep')
        with mock.patch.object(self.module, '_backup_stamp', return_value='20261117T000000Z'), \
             mock.patch.object(self.module.secrets, 'token_hex', side_effect=['aaaa', 'bbbb']):
            created = self.module.backup_directory(root)
        self.assertEqual((existing / 'keep').read_text(), 'keep')
        self.assertEqual(created.name, 'devnorm-mo-patch-20261117T000000Z-bbbb')
        self.assertEqual(stat.S_IMODE(created.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(root.stat().st_mode), 0o755)

    def test_readme_records_the_persistent_backup_and_manual_deletion(self):
        text = (REPO / 'integrations/mo/README.md').read_text()
        self.assertIn('~/.agents/backups/', text)
        self.assertIn('devnorm-mo-patch-', text)
        self.assertIn('--backup-root', text)
        self.assertIn('does not delete', text)
        self.assertIn('manually', text)


if __name__ == '__main__':
    unittest.main()
