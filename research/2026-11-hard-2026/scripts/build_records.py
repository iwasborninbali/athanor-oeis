import json, os, re, collections, sys
repo = os.path.expanduser('~/oeisdata')
ev = json.load(open('events2026.json'))
by = collections.defaultdict(list)
for e in ev: by[e['anum']].append(e)
out = open('hard2026_records.jsonl', 'w')
for a, es in sorted(by.items()):
    p = os.path.join(repo, 'seq', a[:4], a + '.seq')
    rec = dict(anum=a, kinds=sorted({e['kind'] for e in es}), dates=sorted({e['date'] for e in es}),
               terms_added_2026=sum(e.get('terms_added', 0) for e in es))
    lines = collections.defaultdict(list)
    if os.path.exists(p):
        for l in open(p, errors='replace'):
            l = l.rstrip('\n')
            if len(l) > 3 and l[0] == '%':
                lines[l[1]].append(l[3:].split(' ', 1)[1] if ' ' in l[3:] else '')
    rec['name'] = (lines['N'] or [''])[0]
    rec['keywords'] = (lines['K'] or [''])[0]
    rec['author'] = (lines['A'] or [''])[0]
    rec['data_head'] = ''.join(lines['S'] + lines['T'] + lines['U'])[:160]
    rec['comments'] = [c[:300] for c in lines['C']][:8]
    rec['links'] = lines['H']
    rec['extensions'] = lines['E']
    rec['program_langs'] = sorted({m.group(1) for c in lines['o'] for m in [re.match(r'\(([^)]+)\)', c)] if m})
    rec['xref'] = (lines['Y'] or [''])[:3]
    rec['added_lines_2026'] = sorted({l for e in es for l in e.get('added', []) if l[:2] in ('%E', '%H', '%C')})[:30]
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
out.close()
