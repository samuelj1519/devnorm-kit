#!/usr/bin/env python3
"""Check export safety/liveness and require reachable recovery/success witnesses."""
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parent
jar = Path(os.environ['TLA2TOOLS']).resolve()
java = os.environ.get('JAVA', 'java')
source = (root / 'RepositoryExport.tla').read_text()
config = (root / 'RepositoryExport.cfg').read_text()
constants = config.split('SPECIFICATION')[0]
cases = [('safety-liveness', source, config, 'Model checking completed. No error has been found.')]
for witness in ['NeverComplete', 'NeverRestoredAfterSeed', 'NeverBlockedAfterSeed']:
    cases.append((witness, source, constants + 'SPECIFICATION Spec\nINVARIANT ' + witness + '\n',
                  'Invariant ' + witness + ' is violated'))
old = 'phase = "recovering" /\\ SafeRecovery'
assert source.count(old) == 1
mutant = source.replace(old, 'phase = "recovering" /\\ lease')
cases.append(('unsafe-rollback', mutant, constants + 'SPECIFICATION Spec\nINVARIANT PreserveForeign\n',
              'Invariant PreserveForeign is violated'))
with tempfile.TemporaryDirectory(prefix='devnorm-export-model-') as temp:
    base = Path(temp).resolve()
    for name, model, cfg, expected in cases:
        work = base / name; work.mkdir()
        (work / 'RepositoryExport.tla').write_text(model)
        (work / 'RepositoryExport.cfg').write_text(cfg)
        result = subprocess.run([java, '-XX:+UseParallelGC', '-cp', str(jar), 'tlc2.TLC',
                                 '-workers', '1', '-metadir', str(work / 'states'),
                                 '-config', 'RepositoryExport.cfg', 'RepositoryExport.tla'],
                                cwd=work, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (root / (name + '.log')).write_text(result.stdout)
        if expected not in result.stdout or result.returncode != (0 if name == 'safety-liveness' else 12):
            raise SystemExit(f'{name}: unexpected TLC result {result.returncode}; see {name}.log')
        print(name + ': PASS')
