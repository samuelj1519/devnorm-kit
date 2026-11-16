#!/usr/bin/env python3
"""Check or apply the hash-bound, local mo multi-skill compatibility patch."""
import argparse
import hashlib
import json
from pathlib import Path
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('backend', type=Path)
    parser.add_argument('--apply', action='store_true', help='replace only the three reviewed backend files')
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
            # Preserve originals beside the patch evidence; live installation is done by mo.
            backup = Path(tempfile.mkdtemp(prefix='devnorm-mo-backup-'))
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
