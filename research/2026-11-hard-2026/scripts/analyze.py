#!/usr/bin/env python3
"""Reproduce local corpus statistics; does not modify the OEIS checkout."""
import collections
import datetime
import html
import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
records = [json.loads(line) for line in open('hard2026_records.jsonl')]
events = json.load(open('events2026.json'))
for record in records:
    if not record['name'] or not record['author']:
        added = [line for event in events if event['anum'] == record['anum'] for line in event['added']]
        for field, tag in [('name', '%N '), ('author', '%A ')]:
            if not record[field]:
                matching = [line.split(' ', 2)[2] for line in added if line.startswith(tag) and len(line.split(' ', 2)) == 3]
                if matching:
                    record[field] = matching[0]
by_id = {record['anum']: record for record in records}
full = {}
for record in records:
    anum = record['anum']
    path = Path.home() / 'oeisdata/seq' / anum[:4] / (anum + '.seq')
    full[anum] = path.read_text(errors='replace').splitlines() if path.exists() else [line for event in events if event['anum'] == anum for line in event['added']]

# First-match classes are deliberately mutually exclusive; xrefs are used below
# for family evidence, not propagated as presumed subject labels.
rules = [
    ('Graphs and networks', r'\b(graph|graphs|digraph|digraphs|vertex|vertices|edges|chromatic|ramsey|clique|hamiltonian|planar map|tournament|trees|treewidth)\b'),
    ('Geometry, packing and grids', r'\b(packings?|tilings?|polyomino|polyominoes|polyform|polyhedron|polyhedra|lattice points?|grid|sphere|circle|squares? in (?:a|an|the)|no.three.in.line|collinear|geometr|polygons?|triangulations?)\b'),
    ('Designs and codes', r'\b(codes?|coding|error.correct|hamming|designs?|hadamard|latin squares?|orthogonal arrays?|covering arrays?|block design|steiner system)\b'),
    ('Games and puzzles', r'\b(game|games|chess|queens?|knights?|rooks?|sudoku|puzzle|nim|checkers|reversi|golomb ruler)\b'),
    ('Primes and divisibility', r'\b(prime|primes|primality|pseudoprime|semiprime|divisors?|divisible|factorizations?|factorisation|factoring|composite|multiples?|coprime|totient|abundant|perfect numbers?|smooth numbers?|mersenne)\b'),
    ('Other number theory', r'\b(diophantine|integer solutions?|representations? of|sums? of|powers? of|digits?|decimal|base [0-9]|modulo|modular|congruence|residue|quadratic|cubes?|squares?|factorial|partition into|consecutive integers?|palindrom|repunit)\b'),
    ('Combinatorics and enumeration', r'\b(number of|counting|counts?|permutations?|partitions?|compositions?|subsets?|subsequences?|words?|strings?|sequences? of length|arrangements?|enumerat|tableaux|matrices|matrix|binary sequences?|necklaces?|polynomials?|sets? of)\b'),
]
def category(record):
    name = record['name'].lower()
    return next((label for label, expression in rules if re.search(expression, name)), 'Other / unclassified')

def names(text):
    return [re.sub(r'\s+', ' ', value.strip()) for value in re.findall(r'_([^_]+)_', text)]

def extenders(event):
    people = set()
    for line in event['added']:
        if line.startswith('%E ') and re.search(r'\b2026\b', line):
            people.update(names(line))
    return sorted(people)

clusters = collections.defaultdict(collections.Counter)
for record in records:
    bucket = clusters[category(record)]
    bucket['sequences'] += 1
    for kind in record['kinds']:
        bucket[kind] += 1

authors = collections.Counter()
ext_counts = collections.Counter()
monthly = collections.defaultdict(lambda: {'new': 0, 'extension': 0, 'authors': collections.Counter(), 'extenders': collections.Counter(), 'clusters_new': collections.Counter(), 'clusters_extension': collections.Counter(), 'ext_attributed': 0})
for event in events:
    record = by_id[event['anum']]
    month = monthly[event['date'][:7]]
    kind = event['kind']
    month[kind] += 1
    month['clusters_' + kind][category(record)] += 1
    people = names(record['author']) if kind == 'new' else extenders(event)
    if kind == 'extension' and people:
        month['ext_attributed'] += 1
    for person in set(people):
        (authors if kind == 'new' else ext_counts)[person] += 1
        month['authors' if kind == 'new' else 'extenders'][person] += 1

ai_re = re.compile(r'\b(?:AI|LLMs?|GPT(?:-?\d[\w.-]*)?|ChatGPT|Claude|Gemini|DeepMind|AlphaEvolve|AlphaProof|FunSearch|neural(?:\s+networks?)?|machine learning|deep learning|artificial intelligence|agents?|automated discovery|large language models?|reinforcement learning|AlphaGeometry|Copilot|Chat-GPT|OpenAI)\b', re.I)
mentions = []
for anum, lines in full.items():
    for line in lines:
        if line.startswith(('%N ', '%C ', '%H ', '%E ', '%F ', '%o ', '%p ', '%t ', '%A ')) and ai_re.search(line):
            mentions.append({'anum': anum, 'line': line})

methods = {
    'exhaustive/brute-force search': r'\b(?:exhaustive(?:ly)?|brute[ -]force|complete search)\b',
    'SAT / satisfiability': r'\b(?:SAT|satisfiability|satisfiable|unsatisfiability|unsatisfiable|SAT.solver)\b',
    'integer / linear programming': r'\b(?:integer programming|integer linear programming|mixed.integer|ILP|MILP|linear programming)\b',
    'GPU': r'\b(?:GPU|CUDA|OpenCL)\b',
    'distributed / parallel': r'\b(?:distributed computing|distributed search|parallel computing|parallel search|multi.threaded|multithreaded|CPU.hours|CPU.days)\b',
    'LODA': r'\bLODA\b',
    'primality / prime testing': r'\b(?:primality|prime test|probable prime|primality test|primality testing)\b',
    'b-file links': r'(?:b.file|/b\d+\.txt)',
}
method_counts = {}
for label, expr in methods.items():
    pattern = re.compile(expr, re.I)
    ids = [anum for anum, lines in full.items() if any(pattern.search(line) for line in lines)]
    method_counts[label] = {'sequence_count': len(ids), 'examples': ids[:8]}
languages = collections.Counter(language for record in records for language in record['program_langs'])

# Extract modern and historical arXiv identifiers only from H links.
arxiv = collections.defaultdict(set)
for record in records:
    for link in record['links']:
        ids = re.findall(r'(?:arxiv\.org/(?:abs|pdf)/|arxiv\s*:\s*)((?:\d{4}\.\d{4,5}|[a-z][a-z.-]+/\d{7})(?:v\d+)?)', link, re.I)
        for paper_id in ids:
            arxiv[re.sub(r'v\d+$', '', paper_id)].add(record['anum'])
links = collections.Counter()
for event in events:
    for line in event['added']:
        if line.startswith('%H '):
            for url in re.findall(r'https?://[^"\s<>]+', html.unescape(line)):
                if re.search(r'github\.com|gitlab\.com|personal|~', url, re.I):
                    links[url] += 1

crossrefs = {record['anum']: sorted(set(re.findall(r'A\d{6}', ' '.join(record['xref']))) & by_id.keys() - {record['anum']}) for record in records}
result = {'metadata': {'records': len(records), 'events': len(events), 'event_kinds': dict(collections.Counter(e['kind'] for e in events)), 'date_min': min(e['date'] for e in events), 'date_max': max(e['date'] for e in events), 'full_files_read': sum((Path.home() / 'oeisdata/seq' / a[:4] / (a + '.seq')).exists() for a in full), 'records_with_in_corpus_xrefs': sum(bool(v) for v in crossrefs.values()), 'classification': 'First matching regex in ordered names; not an ontology, do not sum new + extension as they overlap.'}, 'clusters': dict(clusters), 'subject_assignments': {record['anum']: category(record) for record in records}, 'crossrefs_in_corpus': crossrefs, 'top_authors': authors.most_common(), 'top_extenders': ext_counts.most_common(), 'monthly': dict(monthly), 'ai_mentions': mentions, 'methods': method_counts, 'program_languages': languages.most_common(), 'arxiv_ids': {k: sorted(v) for k, v in sorted(arxiv.items())}, 'event_links': links.most_common()}
with open('findings.json', 'w') as handle:
    json.dump(result, handle, indent=2, ensure_ascii=False)
print('metadata', result['metadata'])
print('clusters', dict(clusters))
print('authors', authors.most_common(15))
print('extenders', ext_counts.most_common(20))
print('attribution', sum(m['ext_attributed'] for m in monthly.values()), 'of', sum(e['kind']=='extension' for e in events))
print('methods', method_counts)
print('languages', languages.most_common(12))
print('AI lines', len(mentions), 'sequences', len({v['anum'] for v in mentions}), 'arxiv', len(arxiv), 'event links', len(links))
for month in ['2026-06','2026-07','2026-08','2026-09','2026-10']:
    m = monthly[month]
    print(month, m['new'], m['extension'], 'ext attributed', m['ext_attributed'], 'authors', m['authors'].most_common(5), 'extenders', m['extenders'].most_common(5), 'classes', m['clusters_extension'].most_common(3))
