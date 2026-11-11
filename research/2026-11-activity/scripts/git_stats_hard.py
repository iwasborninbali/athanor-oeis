"""Monthly OEIS activity restricted to sequences with keyword 'hard'.
New: added .seq files whose %K line contains 'hard'. Edits: modified .seq files of sequences tagged 'hard' at HEAD
(keyword at time of edit approximated by HEAD), plus data-extension events (term count grew) and terms added."""
import subprocess, re, collections, json, sys, os, glob
repo, since, out = sys.argv[1:4]
hard = set()
for p in glob.glob(os.path.join(repo, 'seq', 'A*', 'A*.seq')):
    with open(p, errors='replace') as f:
        for line in f:
            if line.startswith('%K') and re.search(r'[ ,]hard(,|$|\s)', line): hard.add('seq/' + os.path.relpath(p, os.path.join(repo, 'seq'))); break
print('hard at HEAD', len(hard), flush=True)
P = subprocess.Popen(['git', '-C', repo, 'log', '--since', since, '--date=short', '--format=@@C %ad', '-p', '-U0', '--no-renames', '--', 'seq/'],
                     stdout=subprocess.PIPE, text=True, errors='replace')
M = collections.defaultdict(collections.Counter); distinct = collections.defaultdict(set)
month = None; cur = None; new = False; deleted = False; minus = plus = 0; khard = False
def terms(line):
    b = line[1:].split(' ', 2); return len([t for t in b[2].strip().split(',') if t.strip()]) if len(b) > 2 else 0
def flush():
    global cur
    if cur is None: return
    if new:
        if khard: M[month]['new_hard_sequences'] += 1
    elif not deleted and cur in hard:
        M[month]['hard_edit_events'] += 1; distinct[month].add(cur)
        if plus > minus: M[month]['hard_data_extension_events'] += 1; M[month]['hard_terms_added'] += plus - minus
    cur = None
for line in P.stdout:
    if line.startswith('@@C '): flush(); month = line[4:11]; continue
    if line.startswith('diff --git '):
        flush(); path = line.split(' b/', 1)[1].strip()
        cur = path if re.match(r'seq/A\d+/A\d+\.seq$', path) else None
        new = deleted = khard = False; minus = plus = 0; continue
    if cur is None: continue
    if line.startswith('new file mode'): new = True
    elif line.startswith('deleted file mode'): deleted = True
    elif line.startswith('+%K') and re.search(r'[ ,]hard(,|$|\s)', line): khard = True
    elif not new:
        if line[:3] in ('-%S', '-%T', '-%U'): minus += terms(line)
        elif line[:3] in ('+%S', '+%T', '+%U'): plus += terms(line)
flush()
res = {m: dict(M[m], hard_distinct_edited=len(distinct[m])) for m in sorted(M)}
json.dump(res, open(out, 'w'), indent=1)
for m in sorted(res): print(m, res[m])
