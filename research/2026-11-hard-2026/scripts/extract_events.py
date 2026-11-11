"""Events of 2026 on sequences tagged 'hard' at HEAD (or added with 'hard'):
new sequences and data extensions, with the %E/%H/%C/%o/%A lines added in the same diff."""
import subprocess, re, json, sys, os, glob
repo, since, out = sys.argv[1:4]
HARD = re.compile(r'[ ,]hard(,|$|\s)')
hard = set()
for p in glob.glob(os.path.join(repo, 'seq', 'A*', 'A*.seq')):
    with open(p, errors='replace') as f:
        for line in f:
            if line.startswith('%K') and HARD.search(line):
                hard.add(os.path.basename(p)[:-4]); break
P = subprocess.Popen(['git', '-C', repo, 'log', '--since', since, '--date=short', '--format=@@C %ad %h', '-p', '-U0', '--no-renames', '--', 'seq/'],
                     stdout=subprocess.PIPE, text=True, errors='replace')
events = []; date = None; cur = None
def terms(line):
    b = line[1:].split(' ', 2); return len([t for t in b[2].strip().split(',') if t.strip()]) if len(b) > 2 else 0
def flush():
    global cur
    if cur is None: return
    a = cur
    if a['new'] and a['khard']:
        events.append(dict(anum=a['anum'], date=date, kind='new', added=a['added']))
    elif not a['new'] and not a['deleted'] and a['anum'] in hard and a['plus'] > a['minus']:
        events.append(dict(anum=a['anum'], date=date, kind='extension', terms_added=a['plus'] - a['minus'],
                           added=[l for l in a['added'] if l[:2] in ('%E', '%H', '%C', '%o', '%A', '%N', '%K')]))
    cur = None
for line in P.stdout:
    line = line.rstrip('\n')
    if line.startswith('@@C '):
        flush(); date = line.split()[1]; continue
    if line.startswith('diff --git '):
        flush(); path = line.split(' b/', 1)[1].strip()
        m = re.match(r'seq/A\d+/(A\d+)\.seq$', path)
        cur = dict(anum=m.group(1), new=False, deleted=False, khard=False, plus=0, minus=0, added=[]) if m else None
        continue
    if cur is None: continue
    if line.startswith('new file mode'): cur['new'] = True
    elif line.startswith('deleted file mode'): cur['deleted'] = True
    elif line.startswith('+%') :
        cur['added'].append(line[1:])
        if line.startswith('+%K') and HARD.search(line): cur['khard'] = True
        if line[:3] in ('+%S', '+%T', '+%U'): cur['plus'] += terms(line)
    elif line[:3] in ('-%S', '-%T', '-%U'): cur['minus'] += terms(line)
flush()
json.dump(events, open(out, 'w'))
import collections
c = collections.Counter((e['kind']) for e in events); print(c, len({e['anum'] for e in events}))
