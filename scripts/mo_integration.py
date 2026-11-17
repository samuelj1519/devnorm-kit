#!/usr/bin/env python3
"""Check or apply the hash-bound, local mo multi-skill compatibility patch."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import secrets
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(backend, destination):
    identities = json.loads((ROOT / 'integrations/mo/patch-identity.json').read_text())
    current = {name: digest(backend / name) for name in identities}
    if all(current[name] == row['after'] for name, row in identities.items()):
        return False
    if not all(current[name] == row['before'] for name, row in identities.items()):
        raise ValueError('mo backend differs from the reviewed baseline; review before applying')
    for name in identities:
        if (backend / name).is_symlink():
            raise ValueError('symlink backend is unsupported')
        shutil.copy2(backend / name, destination / name)
    subprocess.run(['patch', '--batch', '-p1', '-i', str(ROOT / 'integrations/mo/multi-skill.patch')],
                   cwd=destination, check=True)
    for name, row in identities.items():
        if digest(destination / name) != row['after']:
            raise ValueError('patched backend identity mismatch: ' + name)
        compile((destination / name).read_text(), name, 'exec')
    return True


def _ensure_private_dir(path):
    if path.exists():
        if not path.is_dir():
            raise FileExistsError(path)
        return
    if path.parent != path:
        _ensure_private_dir(path.parent)
    path.mkdir(mode=0o700)
    path.chmod(0o700)


def _backup_stamp():
    return datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')


def backup_directory(root):
    """Create a private directory for the three original backend files.

    The system temporary directory is removed on a schedule, so the originals
    stay under a persistent parent until local acceptance finishes. The
    maintainer deletes that directory. This script does not delete it.
    """
    root = Path(root).expanduser().resolve()
    _ensure_private_dir(root)
    for _ in range(8):
        stamp = _backup_stamp()
        path = root / f'devnorm-mo-patch-{stamp}-{secrets.token_hex(4)}'
        try:
            path.mkdir(mode=0o700)
        except FileExistsError:
            continue
        path.chmod(0o700)
        return path
    raise FileExistsError('could not allocate a new backup directory under ' + str(root))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('backend', type=Path)
    parser.add_argument('--apply', action='store_true', help='replace only the three reviewed backend files')
    parser.add_argument('--backup-root', type=Path, help='parent directory for the original-file backup')
    args = parser.parse_args()
    backend = args.backend.resolve()
    with tempfile.TemporaryDirectory(prefix='devnorm-mo-patch-') as tmp:
        stage = Path(tmp)
        needed = prepare(backend, stage)
        if needed and args.apply:
            identities = json.loads((ROOT / 'integrations/mo/patch-identity.json').read_text())
            for name, row in identities.items():
                if digest(backend / name) != row['before']:
                    raise ValueError('backend changed after preparation: ' + name)
            root = args.backup_root if args.backup_root is not None else Path.home() / '.agents' / 'backups'
            backup = backup_directory(root)
            replaced = []
            try:
                for name in identities:
                    shutil.copy2(backend / name, backup / name)
                for name in identities:
                    target = backend / name
                    with tempfile.NamedTemporaryFile(dir=backend, prefix='.devnorm-mo-', delete=False) as f:
                        temporary = Path(f.name)
                    try:
                        shutil.copy2(stage / name, temporary)
                        temporary.replace(target)
                    finally:
                        temporary.unlink(missing_ok=True)
                    replaced.append(name)
            except BaseException:
                for name in reversed(replaced):
                    if digest(backend / name) == identities[name]['after']:
                        shutil.copy2(backup / name, backend / name)
                raise
            print('backup=' + str(backup))
        print('status=' + ('applied' if needed and args.apply else 'ready' if needed else 'up-to-date'))


if __name__ == '__main__':
    main()
