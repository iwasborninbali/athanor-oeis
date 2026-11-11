"""Monthly OEIS activity from the official oeis/oeisdata git history (daily exports).
Per month: new sequences (seq/*.seq added), modified sequences (events and distinct), data extensions
(modified .seq whose %S/%T/%U term count increased; terms added), new %E lines, b-files added/modified."""
import subprocess, re, collections, json, sys
repo = sys.argv[1]; since = sys.argv[2]
P = subprocess.Popen(['git', '-C', repo, 'log', '--since', since, '--date=short', '--format=@@C %ad',
                      '-p', '-U0', '--no-renames', '--', 'seq/', 'files/'], stdout=subprocess.PIPE, text=True, errors='replace')
M = collections.defaultdict(lambda: collections.Counter()); distinct = collections.defaultdict(set)
month = None; cur = None; new = False; deleted = False; minus = 0; plus = 0; E_plus = 0
def terms(line):
    body = line[1:].split(' ', 2)
    return len([t for t in body[2].strip().split(',') if t.strip()]) if len(body) > 2 else 0
def flush():
    global cur
    if cur is None: return
    kind, name = cur
    if kind == 'seq':
        if new: M[month]['new_sequences'] += 1
        elif not deleted:
            M[month]['modified_seq_events'] += 1; distinct[month].add(name)
            if plus > minus: M[month]['data_extension_events'] += 1; M[month]['terms_added_in_data'] += plus - minus
            if E_plus: M[month]['new_E_lines'] += E_plus
    elif kind == 'bfile':
        M[month]['bfiles_added' if new else 'bfiles_modified'] += 1
    cur = None
for line in P.stdout:
    if line.startswith('@@C '):
        flush(); month = line[4:11]; continue
    if line.startswith('diff --git '):
        flush(); path = line.split(' b/', 1)[1].strip()
        if re.match(r'seq/A\d+/A\d+\.seq$', path): cur = ('seq', path)
        elif re.match(r'files/A\d+/b\d+\.txt$', path): cur = ('bfile', path)
        else: cur = ('other', path)
        new = deleted = False; minus = plus = 0; E_plus = 0; continue
    if cur is None: continue
    if line.startswith('new file mode'): new = True
    elif line.startswith('deleted file mode'): deleted = True
    elif cur[0] == 'seq' and not new:
        if line.startswith('-%S') or line.startswith('-%T') or line.startswith('-%U'): minus += terms(line)
        elif line.startswith('+%S') or line.startswith('+%T') or line.startswith('+%U'): plus += terms(line)
        elif line.startswith('+%E'): E_plus += 1
flush()
out = {m: dict(M[m], distinct_modified_sequences=len(distinct[m])) for m in sorted(M)}
json.dump(out, open(sys.argv[3], 'w'), indent=1)
for m in sorted(out): print(m, out[m])
