import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('package', Path(__file__).resolve().parents[1] / 'scripts/package.py')
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / 'checkout'
        registry = package.load(package.ROOT, '.devnorm-files.json')
        for name in [r['path'] for r in registry['files']] + ['.devnorm-files.json']:
            p = self.root / name
            p.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(package.ROOT / name, p)

    def tearDown(self):
        self.temp.cleanup()

    def test_delivery_and_exact_release_round_trip(self):
        artifact, release, skills = package.verify(self.root)
        result = package.restore_release(self.root, self.base / 'release')
        restored = Path(result['source'])
        self.assertEqual(package.load(restored, 'artifact.json'), release)
        self.assertEqual(package.identity(release), artifact['artifactHash'])
        self.assertEqual(len(skills), 9)
        for row in release['files']:
            self.assertEqual(package.file_entry(restored, row['path']), row)

    def test_corrupt_resource_fails(self):
        (self.root / 'skills/devnorm/SKILL.md').write_text('changed')
        with self.assertRaisesRegex(ValueError, 'bytes or mode'):
            package.verify(self.root)

    def test_executable_bit_change_fails(self):
        p = self.root / 'skills/devnorm/SKILL.md'
        p.chmod(0o755)
        with self.assertRaisesRegex(ValueError, 'bytes or mode'):
            package.verify(self.root)

    def test_extra_runtime_file_fails(self):
        (self.root / 'skills/devnorm/unknown.txt').write_text('extra')
        with self.assertRaisesRegex(ValueError, 'unregistered runtime'):
            package.verify(self.root)

    def test_repository_maintenance_files_are_preserved(self):
        p = self.root / 'CONTRIBUTING.md'
        p.write_text('repository documentation')
        package.verify(self.root)
        self.assertEqual(p.read_text(), 'repository documentation')

    def test_symlink_resource_fails(self):
        p = self.root / 'skills/devnorm/SKILL.md'
        p.unlink()
        p.symlink_to(package.ROOT / 'skills/devnorm/SKILL.md')
        with self.assertRaisesRegex(ValueError, 'symlink'):
            package.verify(self.root)

    def test_restore_never_overwrites_destination(self):
        destination = self.base / 'existing'
        destination.mkdir()
        (destination / 'user.txt').write_text('preserve')
        with self.assertRaisesRegex(ValueError, 'already exists'):
            package.restore_release(self.root, destination)
        self.assertEqual((destination / 'user.txt').read_text(), 'preserve')

    def test_unsafe_and_duplicate_paths_fail(self):
        row = {'path': '../outside', 'mode': '0644', 'hash': 'a' * 64}
        with self.assertRaisesRegex(ValueError, 'unsafe'):
            package.entries([row])
        row['path'] = 'same'
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            package.entries([row, row])


if __name__ == '__main__':
    unittest.main()
