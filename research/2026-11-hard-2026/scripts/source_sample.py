#!/usr/bin/env python3
"""Fetch a bounded, documented sample of event-linked GitHub READMEs."""
import concurrent.futures
import json
import re
import urllib.request
from pathlib import Path

root = Path(__file__).resolve().parent.parent
repos = [
    ('Jacob H. Glickman', 'jhg023/first-knowns'),
    ('S. I. Dimitrov event-linked', 'Stoyan16/Numbers-k-such-that-psi-k-phi-k-omega-k-9'),
    ('Vladeta Jovovic event-linked, not necessarily authored by him', 'aeporreca/funkdigen2'),
    ('Max Alekseyev event-linked, not necessarily authored by him', 'qorud02/erdos-295-k18'),
    ('Andrei Zabolotskii event-linked, not necessarily authored by him', 'olligobber/LocalNonogram'),
    ('James Guillochon', 'guillochon/oeis-results'),
    ('Event-linked', 'jeff87654/Lifting'),
    ('Igor Blokhin', 'IgorBlokhin/Graceful_Prufer_codes'),
    ('Igor Blokhin', 'IgorBlokhin/Graph-Theory'),
    ('Event-linked', 'YuryBelousov/meander_factorization'),
    ('Event-linked', 'jaapspies/permanents-determinant'),
    ('Event-linked', 'techno-optimist/erdos-frontier-atlas'),
    ('Event-linked', 'Gwynerva/line-pencils'),
    ('Event-linked', 'michaelmross/Gilbreath'),
    ('Event-linked', 'pexley-math/oeis-A395422'),
]
pattern = re.compile(r'\b(?:AI|LLMs?|GPT|ChatGPT|Claude|Gemini|DeepMind|AlphaEvolve|FunSearch|Copilot|neural|machine learning|artificial intelligence)\b', re.I)
def fetch(item):
    label, repo = item
    url = f'https://raw.githubusercontent.com/{repo}/HEAD/README.md'
    result = {'label': label, 'repository': 'https://github.com/' + repo, 'url': url}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'OEIS-hard-research/1.0'})
        with urllib.request.urlopen(req, timeout=20) as response:
            text = response.read(500000).decode('utf-8', 'replace')
        result.update(status='ok', matches=[line.strip() for line in text.splitlines() if pattern.search(line)][:30])
    except Exception as error:
        result.update(status='error', error=str(error))
    return result
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    rows = list(executor.map(fetch, repos))
(root / 'source-sample.json').write_text(json.dumps(rows, indent=2, ensure_ascii=False))
for row in rows:
    print(row['label'], row['repository'], row['status'], len(row.get('matches', [])))
    for line in row.get('matches', [])[:2]:
        print(' ', line[:450])
