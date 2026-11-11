#!/usr/bin/env python3
"""Fetch cached arXiv Atom metadata in batches, respecting its request limit."""
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / 'findings.json').read_text())
ids = sorted(data['arxiv_ids'])
cache = root / 'arxiv-cache'
cache.mkdir(exist_ok=True)
for start in range(0, len(ids), 40):
    batch = ids[start:start + 40]
    path = cache / f'batch-{start:04d}.xml'
    if path.exists():
        continue
    params = urllib.parse.urlencode({'id_list': ','.join(batch), 'max_results': len(batch)})
    url = 'https://export.arxiv.org/api/query?' + params
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={'User-Agent': 'OEIS-hard-research/1.0 (academic metadata analysis)'})
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = response.read()
            ET.fromstring(payload)
            path.write_bytes(payload)
            print('batch', start, 'received', len(payload), flush=True)
            break
        except Exception as error:
            print('batch', start, 'attempt', attempt + 1, type(error).__name__, str(error)[:150], flush=True)
            time.sleep(5 * (attempt + 1))
    time.sleep(3.2)

ns = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
pattern = re.compile(r'\b(?:AI|artificial intelligence|machine learning|deep learning|neural networks?|(?:large )?language models?|LLMs?|AI[ -](?:based|driven|assisted|generated|powered|aided)|GPT(?:-\d+)?|ChatGPT|Claude|Gemini|DeepMind|AlphaEvolve|AlphaProof|FunSearch|reinforcement learning|automated (?:discovery|theorem proving)|agents?|generative AI)\b', re.I)
papers = []
for path in sorted(cache.glob('batch-*.xml')):
    for entry in ET.parse(path).getroot().findall('a:entry', ns):
        def text(tag):
            return ' '.join((entry.findtext(tag, default='', namespaces=ns)).split())
        paper_id = re.sub(r'v\d+$', '', text('a:id').split('/abs/')[-1])
        title, abstract, comments = text('a:title'), text('a:summary'), text('x:comment')
        hits = sorted({m.group() for m in pattern.finditer(' '.join([title, abstract, comments]))}, key=str.lower)
        papers.append({'id': paper_id, 'title': title, 'published': text('a:published'), 'updated': text('a:updated'), 'abstract': abstract, 'comments': comments, 'why': hits, 'sequences': data['arxiv_ids'].get(paper_id, [])})
data['arxiv_metadata'] = {'requested': len(ids), 'retrieved': len(papers), 'missing': sorted(set(ids) - {p['id'] for p in papers})}
data['flagged_arxiv_papers'] = [p for p in papers if p['why']]
(root / 'arxiv-papers.json').write_text(json.dumps(papers, indent=2, ensure_ascii=False))
(root / 'findings.json').write_text(json.dumps(data, indent=2, ensure_ascii=False))
print('retrieved', len(papers), 'flagged', len(data['flagged_arxiv_papers']), 'missing', len(data['arxiv_metadata']['missing']))
for paper in data['flagged_arxiv_papers']:
    print(paper['id'], paper['published'][:10], paper['why'], paper['title'][:130], paper['sequences'])
