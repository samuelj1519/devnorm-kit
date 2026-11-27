#!/usr/bin/env python3
"""Verify a delivery checkout and restore its exact accepted mo release layout."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_DOCUMENTS = ('README.md', 'INSTALL.md')


def require(condition, message):
    if not condition:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True,
                       separators=(',', ':')) + '\n').encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def identity(value):
    return sha(canonical({'schemaVersion': 1, 'value': value}))


def load(root, name):
    return json.loads((root / name).read_text())


def entries(rows):
    result = {}
    for row in rows:
        name = row['path']
        p = PurePosixPath(name)
        require(isinstance(name, str) and name and not p.is_absolute()
                and p.as_posix() == name and '..' not in p.parts
                and '\\' not in name and name not in result,
                f'unsafe or duplicate path: {name}')
        require(row['mode'] in {'0644', '0755'}
                and re.fullmatch('[a-f0-9]{64}', row['hash']),
                f'invalid file identity: {name}')
        result[name] = row
    return result


def file_entry(root, name):
    p = root / name
    for parent in (p, *p.parents):
        if parent == root.parent:
            break
        require(not parent.is_symlink(), f'symlink: {name}')
    require(p.is_file(), f'missing file: {name}')
    return {'path': name, 'hash': sha(p.read_bytes()),
            'mode': '0755' if p.stat().st_mode & 0o111 else '0644'}


def document_paths(payload):
    paths = {}
    for name in REPOSITORY_DOCUMENTS:
        archive = 'docs/generated/' + name
        require(not (archive in payload and name in payload), f'generated document has multiple owners: {name}')
        paths[name] = archive if archive in payload else name
    return paths


def release_source(name, documents):
    if name == 'plugin/README.md':
        return documents['README.md']
    if name.startswith('plugin/'):
        return name[len('plugin/'):]
    if name.startswith('agent-skills/'):
        return 'skills/' + name[len('agent-skills/'):]
    if name == 'INSTALL.md':
        return documents['INSTALL.md']
    raise ValueError(f'unsupported accepted release file: {name}')


def verify(root):
    root = root.resolve()
    artifact = load(root, 'artifact.json')
    release = load(root, 'release-artifact.json')
    registry = load(root, '.devnorm-files.json')
    require(artifact['schemaVersion'] == release['schemaVersion'] == registry['schemaVersion'] == 1,
            'unsupported schema version')
    require(artifact['name'] == release['name'] == 'devnorm', 'package identity mismatch')
    require(artifact['version'] == release['version'], 'version mismatch')
    require(identity(release) == artifact['artifactHash'] == registry['artifactHash'],
            'accepted release identity mismatch')
    payload = entries(artifact['files'])
    documents = document_paths(payload)
    registered = entries(registry['files'])
    require(set(registered) == set(payload) | {'artifact.json', 'SHA256SUMS'},
            'registry coverage mismatch')
    for name, row in registered.items():
        require(file_entry(root, name) == row, f'bytes or mode changed: {name}')
    require(all(registered[name] == row for name, row in payload.items()),
            'payload and registry differ')
    sums = ''.join(f"{row['hash']}  {name}\n" for name, row in sorted(registered.items())
                   if name != 'SHA256SUMS')
    require((root / 'SHA256SUMS').read_text() == sums, 'checksum coverage mismatch')
    # Extra repository maintenance files are permitted; extra runtime files are not.
    for folder in ('skills', '.claude-plugin', '.cursor-plugin', 'docs/generated'):
        for p in (root / folder).rglob('*'):
            name = p.relative_to(root).as_posix()
            require(not p.is_symlink(), f'symlink: {name}')
            require(p.is_dir() or name in payload, f'unregistered runtime file: {name}')
    for name in ('plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json'):
        manifest = load(root, name)
        require(manifest['name'] == 'devnorm' and manifest['version'] == release['version'],
                f'plugin identity mismatch: {name}')
    marketplace = load(root, '.claude-plugin/marketplace.json')
    major_version = int(release['version'].split('.', 1)[0])
    market_name = 'devnorm-local' if major_version < 2 else 'devnorm'
    plugins = marketplace['plugins']
    require(marketplace['name'] == market_name and len(plugins) == 1
            and plugins[0]['name'] == release['name']
            and plugins[0]['version'] == release['version']
            and plugins[0]['source'] == './', 'marketplace identity mismatch')
    skills = sorted(p.parent.name for p in (root / 'skills').glob('*/SKILL.md'))
    require('devnorm' in skills and len(skills) == len(list((root / 'skills').iterdir())),
            'missing skill entry')
    explicit = {'devnorm-interview', 'devnorm-recall', 'devnorm-sources'}
    for name in skills:
        folder = root / 'skills' / name
        text = (folder / 'SKILL.md').read_text()
        require(text.startswith('---\n') and '\n---\n' in text[4:], f'frontmatter: {name}')
        front, body = text[4:].split('\n---\n', 1)
        require(re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', name) and len(name) <= 64,
                f'invalid skill name: {name}')
        require(f'name: {name}' in front.splitlines(), f'skill name mismatch: {name}')
        description = re.search(r'^description: (.+)$', front, re.M)
        require(description and 0 < len(description[1].strip('"')) <= 1024,
                f'invalid description: {name}')
        require(len(body.splitlines()) < 500, f'entry needs progressive disclosure: {name}')
        if name in explicit:
            require('disable-model-invocation: true' in front,
                    f'explicit invocation missing: {name}')
            require('allow_implicit_invocation: false' in (folder / 'agents/openai.yaml').read_text(),
                    f'Codex invocation policy missing: {name}')
        provenance = load(folder, 'provenance.json')
        require(provenance['candidateHash'] == release['candidateHash'], f'provenance: {name}')
        require((folder / 'THIRD_PARTY_NOTICES.md').is_file() and (folder / 'licenses').is_dir(),
                f'license resources missing: {name}')
        # Resolve entrypoint links without loading every conditional reference.
        for link in re.findall(r'\]\(([^)]+)\)', body):
            if '://' not in link and not link.startswith('#'):
                target = (folder / link.split('#')[0]).resolve()
                require(target.is_relative_to(folder) and target.exists(), f'broken entry link: {name}: {link}')
    release_files = entries(release['files'])
    for name, row in release_files.items():
        if name == '.claude-plugin/marketplace.json':
            original = json.loads(json.dumps(marketplace))
            original['plugins'][0]['source'] = './plugin'
            require(sha(canonical(original)) == row['hash'] and row['mode'] == '0644',
                    'original marketplace cannot be reconstructed')
            continue
        mapped = release_source(name, documents)
        require(file_entry(root, mapped)['hash'] == row['hash']
                and file_entry(root, mapped)['mode'] == row['mode'],
                f'accepted release mapping mismatch: {name}')
    return artifact, release, skills


def restore_release(root, destination):
    artifact, release, skills = verify(root)
    documents = document_paths(entries(artifact['files']))
    destination = destination.absolute()
    require(not destination.exists() and not destination.is_symlink(), 'destination already exists')
    require(not destination.is_relative_to(root.resolve()), 'release destination must be outside checkout')
    require(destination.parent.is_dir() and destination.parent.resolve() == destination.parent,
            'destination parent must be an existing non-symlink directory')
    with tempfile.TemporaryDirectory(prefix='.devnorm-release-', dir=destination.parent) as tmp:
        stage = Path(tmp) / 'release'
        stage.mkdir()
        for name, row in entries(release['files']).items():
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if name == '.claude-plugin/marketplace.json':
                data = load(root, name)
                data['plugins'][0]['source'] = './plugin'
                target.write_bytes(canonical(data))
            else:
                mapped = release_source(name, documents)
                shutil.copyfile(root / mapped, target)
            target.chmod(int(row['mode'], 8))
            require(file_entry(stage, name) == row, f'restored identity mismatch: {name}')
        (stage / 'artifact.json').write_bytes(canonical(release))
        rows = {**entries(release['files']), 'artifact.json': file_entry(stage, 'artifact.json')}
        (stage / 'SHA256SUMS').write_text(''.join(f"{row['hash']}  {name}\n" for name, row in sorted(rows.items())))
        stage.rename(destination)
    return {'source': str(destination), 'revision': artifact['artifactHash'],
            'version': artifact['version'], 'skills': skills}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('verify')
    restore = sub.add_parser('restore-release')
    restore.add_argument('destination', type=Path)
    args = parser.parse_args()
    try:
        if args.command == 'verify':
            artifact, _, skills = verify(args.root)
            print(json.dumps({'result': 'PASS', 'version': artifact['version'],
                              'release': artifact['artifactHash'], 'skills': skills}))
        else:
            print(json.dumps(restore_release(args.root.resolve(), args.destination)))
    except (ValueError, KeyError, OSError) as error:
        print(f'FAIL: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
