#!/usr/bin/env python3
"""Generate the report from the frozen local statistics and audited sources."""
import collections
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = json.loads((root / 'findings.json').read_text())
sample = json.loads((root / 'source-sample.json').read_text())
out = []
def add(text=''):
    out.append(text)

add('''# OEIS hard activity in 2026: composition, contributors and AI

Snapshot: 12 November 2026; events through 11 November. The unit is an event in the supplied Git-diff extraction, not a paper, person, independent discovery, or necessarily a new mathematical result. These are 1,312 distinct sequences, 654 new-file events and 905 data-extension events; 98 sequences have both kinds. November is incomplete. The historical 2024–25 rates in the question were not independently reproduced.

## Executive findings

* The shared feature is **computational scarcity**: these records often ask for exact counts, smallest witnesses, or primality under constrained conditions, where checking the next value can be costly. A `hard` tag is not proof of a particular algorithm or complexity class. Broad number theory and discrete enumeration dominate the name-based classification.
* Acceleration is both concentrated and wider than a single person. Extensions rise from 65 in June to 189 in October; new files rise from 72 to 90. Two extenders account for 74 of 145 September extensions. In October at least 23 extensions concern polyforms and 13 mention sigma/psi and phi. These overlapping name signals do not establish causal families.
* AI is unambiguously visible, but visibility is sparse and uneven. Four entries explicitly describe AI assistance or AI-generated proofs in their text, and an active extender's linked repository discloses AI-written search code. Direct mentions alone materially undercount the linked evidence. The available data cannot estimate the share of all AI-assisted work or establish AI as the cause of the overall rise.

## Scope and classification

The supplied extraction finds new sequences introduced with `hard`, and positive net `%S/%T/%U` term-count changes for sequences carrying `hard` at checkout HEAD. It does not count b-file-only expansions, every edit, withdrawn sequences or all hard sequences. Commit dates are file-change dates, not necessarily dates of computation. Two files were missing from the read-only checkout; their `%N` and `%A` were recovered from the supplied event diffs. The other 1,310 full files were scanned as of the local checkout. This makes full-entry descriptions a snapshot, not necessarily what was present at the event date.

The table uses reproducible **first-match, mutually exclusive name regexes** in the order in `scripts/analyze.py`, not a trained classifier or ground truth. For example, a graph about primes is classified as graphs; a design with neither “design” nor “code” in its title may land elsewhere. The 195 unclassified cases include diverse mathematics. Of 1,312 records, 714 have at least one of their up-to-three supplied cross-reference lines pointing to another sampled sequence; these links support related-family inspection, but are not treated as proof of shared subject or counted as independent clusters. Labels are indicative, not estimates of precise disciplinary proportions.

| Subject by name | Distinct sequences | New | Extended |
|---|---:|---:|---:|''')
for label, c in sorted(data['clusters'].items(), key=lambda item: -item[1]['sequences']):
    add(f"| {label} | {c['sequences']} | {c.get('new', 0)} | {c.get('extension', 0)} |")
add('''
New and extended columns overlap for sequences with both kinds. Illustrations: prime-constrained searches in [A165234](https://oeis.org/A165234), polyforms in [A365362](https://oeis.org/A365362), graph Ramsey enumeration in [A000789](https://oeis.org/A000789), and a reciprocal-sum extremal problem in [A390394](https://oeis.org/A390394). Cross-references corroborate related pairs [A119751](https://oeis.org/A119751)–[A119752](https://oeis.org/A119752), [A257466](https://oeis.org/A257466)–[A257467](https://oeis.org/A257467), and the arithmetic-function pair [A393230](https://oeis.org/A393230)–[A393425](https://oeis.org/A393425). Family observations use names and cross-references, not numerical proximity of sequence identifiers.

## Contributors

For new events, credit each underscore-delimited name in the current `%A` (or missing-file event `%A`). For extensions, credit each distinct underscore-delimited name on a `%E` line added in that event which itself contains `2026`. An added `%E` is not necessarily the person who made every newly added term; old lines may be reinserted, several people can share credit, and submitter/editor is not necessarily researcher. Attribution is available for 879 of 905 extension events. Names are not identity-resolved beyond whitespace; author names may have changed since the event. Counts are event-person associations, not necessarily distinct people or disjoint contributions.

| Rank | New-sequence author | New events | Extender | Extension events |
|---:|---|---:|---|---:|''')
for index in range(15):
    author, acount = data['top_authors'][index]
    extender, ecount = data['top_extenders'][index]
    add(f'| {index+1} | {author} | {acount} | {extender} | {ecount} |')
add('''
Taking the **union of events** associated with the top contributors, the top 5 and 10 authors cover 173/654 (26.5%) and 239/654 (36.5%) new events; the top 5 and 10 extenders cover 321/905 (35.5%) and 445/905 (49.2%) extension events. These use all events as denominator, including unattributed ones, and avoid double-counting joint credits. Ties follow file iteration order.

| 2026 | New | Extension | Extensions with attributed `%E` | Leading new authors (events) | Leading extenders (events) |
|---|---:|---:|---:|---|---|''')
for key in ['2026-06', '2026-07', '2026-08', '2026-09', '2026-10']:
    month = data['monthly'][key]
    def leaders(field):
        return ', '.join(f'{name} {count}' for name, count in sorted(month[field].items(), key=lambda item: -item[1])[:3])
    add(f"| {key} | {month['new']} | {month['extension']} | {month['ext_attributed']} | {leaders('authors')} | {leaders('extenders')} |")
add('''
In September Sponaugle and Jovovic account for 45 and 29 events; in October Sponaugle, Jovovic and Alekseyev have 32, 24 and 23. The top five for October together have 104 person-event credits, not necessarily 104 different events. October's 23 polyform-name matches include the [A365355](https://oeis.org/A365355), [A365358](https://oeis.org/A365358), [A365362](https://oeis.org/A365362) and [A365365](https://oeis.org/A365365) variants, and 13 sigma/psi–phi-name matches are another recurring family. These patterns and the concurrent rise across other contributors favor a mixture of focused campaigns and broader activity, not one single-family explanation. Price's new sequences repeatedly vary prime expressions; Dimitrov's repeatedly vary arithmetic-function identities. These are observations about names, not claims about intent.

## Methods and why these sequences are hard

Literal mention counts below count sequences in the full local text, not event-specific methods, not unique computations, and not all instances of a method. They overlap. Negative results mean only that these literal patterns were absent; code and b-files may be linked or described without the words used here.

| Method / indicator | Sequences with literal match |
|---|---:|''')
for label, item in data['methods'].items():
    add(f"| {label} | {item['sequence_count']} |")
add('''
The b-file count is only explicit `b-file` or `/bNNNNNN.txt` references; other OEIS “Table of n, a(n)” link formats are missed. The 0 LODA result is **not** evidence that no mined programs exist. `%o` labels in the prepared records show PARI 287, Python 209, C++ 30, Magma 14, SageMath 11 and C 11 sequences; these are not mutually exclusive and do not say what was used for the 2026 extension. SAT, ILP, GPU, distributed or exhaustive-search mentions can describe earlier work. [A000789](https://oeis.org/A000789) provides a concrete exhaustive graph-search and integer-programming context; [A390394](https://oeis.org/A390394) describes ILP and exact checking. A program in a record is not by itself evidence that it produced the new terms.

## AI: direct entry evidence

The whole available local entries were screened for AI/LLM/GPT/Claude/Gemini/DeepMind/AlphaEvolve/AlphaProof/FunSearch/agents/neural and related terms. This yields 30 exact matching lines across 15 sequences, including obvious false positives; the complete verbatim hit list follows in the appendix. The two missing full files were screened only through their provided event additions. This is a lexical audit, not proof that every possible AI paraphrase was found.

Four sequences explicitly state AI use or AI proofs: [A006455](https://oeis.org/A006455) credits a program explored with an LLM for independent computations including a(17)–a(18); [A390394](https://oeis.org/A390394) credits AI assistance for a(39)–a(60); [A248802](https://oeis.org/A248802) and [A358684](https://oeis.org/A358684) report AI proofs. Proofs are not necessarily new sequence terms. A248802's AI text and references are snapshot evidence, not necessarily present at its July extension; similarly A358684's comment is not independently dated. A101877's `claude/` branch is a textual match, **not by itself a disclosure**. Person-name Claude, mathematical variables `ai`, an unrelated multi-agent system, an AI journal or a ChatGPT-hosted domain are not evidence of AI authorship.

## AI: linked arXiv metadata

Extracting links and `arXiv:` identifiers from the provided full `%H` fields yields 268 distinct IDs, including older-style IDs. Batched arXiv Atom queries returned 268/268 metadata records; requests were separated by at least 3.2 seconds. Title, abstract and comments were screened; this is not a full-paper search. The six matches are listed below; matches are leads, not automatically evidence that a term was produced by AI. `arxiv-papers.json` includes all returned abstracts, and `findings.json` includes the complete flags and associated sequences.

| arXiv ID | First posted | Title | Why flagged / interpretation | Sampled entries |
|---|---|---|---|---|''')
why = {
 '2606.15159': 'Explicit human–AI collaboration; Claude used in formalisation, experiments and writing; claims Lean checking.',
 '2605.22763': 'AI/LLM-driven formal proof search; authors report 44 of 492 OEIS conjectures proved.',
 '2608.11941': 'Language-model benchmark of OEIS conjectures; author reports 147 resolved at stated budget.',
 '2508.20825': 'Survey includes machine learning among graph methods; not a claim all its results use ML.',
 '1907.05974': 'Mentions possible ML application, not AI-generated results.',
 '2312.06581': 'Studies neural-network interpretability, not evidence of AI-assisted OEIS extension.',
}
for paper in sorted(data['flagged_arxiv_papers'], key=lambda item: item['published'], reverse=True):
    add(f"| [{paper['id']}](https://arxiv.org/abs/{paper['id']}) | {paper['published'][:10]} | {paper['title'].replace('|', '/')} | {why.get(paper['id'], ', '.join(paper['why']))} | {', '.join(paper['sequences'])} |")
add('''
These are authors' claims, not independently checked proofs. In particular, the arXiv abstract's machine-checked claim is subject to its stated trusted base. AI-proof benchmarks and direct term generation are distinct.

## AI: bounded public-source check

We ranked the top 15 people by the **sum** of new-author and extension-person counts; this is a sampling convenience, not a unique-event total. For each, we inspected event-linked GitHub URLs and corpus disclosures; a focused public-web search was made for several, not an exhaustive search for all 15. Fifteen event-linked repository READMEs were fetched at HEAD (`source-sample.json`); 14 loaded, one failed. Some repositories are linked from an event but were not authored by the credited contributor, so no AI use is imputed to that contributor. HEAD can postdate an event; no historical README revision was checked.

* **Jacob H. Glickman:** [first-knowns README](https://github.com/jhg023/first-knowns) explicitly describes Claude and ChatGPT/Codex roles and AI-written search code. Seventeen events in this corpus carry both a Glickman 2026 `%E` credit and a link to that repository, including [A070737](https://oeis.org/A070737) and [A165234](https://oeis.org/A165234). This establishes a specific disclosed AI-assisted workflow and link to those events; it does not establish that every Glickman event, every term, or earlier repository state used the same workflow.
* **Petra Radko's** event-linked [line-pencils README](https://github.com/Gwynerva/line-pencils) explicitly attributes work on theorems, proofs, code and computations to Claude Code under human direction. This is a project self-report, not an independent verification or attribution to another person in the event.
* The event-linked [Erdős 295 repository](https://github.com/qorud02/erdos-295-k18) describes a previous Claude-associated witness. A link appearing in a Max Alekseyev event does **not** imply that Alekseyev used AI.
* Ten of the 14 fetched READMEs had no AI-keyword hit; the four with hits are the three above and the AI-focused [Erdős frontier atlas](https://github.com/techno-optimist/erdos-frontier-atlas). No hit is not evidence of no AI. The A101877 linked path with `claude/` in its branch name was separately inspected, but that string alone establishes no AI use.
* The top-15 sample includes Jeff Sponaugle, Vladeta Jovovic, Max Alekseyev, S. I. Dimitrov, Robert Price, Michael S. Branicky, Pontus von Brömssen, Eric W. Weisstein, Martin Fuller, Chai Wah Wu, Hugo Pfoertner, Andrei Zabolotskii, Firdous Ahmad Mala, Amiram Eldar and Jacob H. Glickman. Only a subset had event-linked GitHub READMEs in this bounded sample; absence of a found disclosure cannot be read as non-use. Search results involving similarly named people and generic GitHub UI text were not attributed to a contributor.

## External context

The current [OEIS AI submission policy](https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions) requires a human author responsible for correctness, forbids AI as author, full AI-generated comments, and uncomprehended AI programs, and prohibits automated bulk submissions without prior permission. It applies to updates as well as new sequences. This policy is not evidence that disclosed cases violate it.

[DeepMind's 2026 formal-proof paper](https://arxiv.org/abs/2605.22763) reports 44/492 OEIS conjectures formally proved using an AI agent, and [OEIS Open](https://arxiv.org/abs/2608.11941) reports a separate benchmark. These concern conjectures, not necessarily new terms. For actual term work, the directly attributed A390394 entry and the Glickman repository above are verifiable 2026 examples. [AlphaEvolve's 2025 paper](https://arxiv.org/abs/2511.02864) reports AI-guided mathematical constructions, but no corpus-specific OEIS term attribution is inferred from that paper alone.

## Limits

No causal identification, general population of all OEIS submissions, historical baseline re-extraction, identity resolution, project-by-project proof audit, or systematic full-text paper search was performed. Names and keywords are imperfect classifiers. The prepared `added_lines_2026` field was truncated; contributor counts and event-linked URLs instead use the full supplied event diffs. `%H` links and full-entry lines reflect the checkout snapshot and may have been added after the event. No non-disclosure is evidence of non-use. Automated-paper matches can be irrelevant; missing AI mentions are not negative ground truth. All GitHub and arXiv sources were accessed on 12 November 2026.

Reproduction: run `python3 scripts/analyze.py`, then `python3 scripts/arxiv_metadata.py`, `python3 scripts/source_sample.py`, and `python3 scripts/write_report.py` from this directory. The cached Atom responses avoid repeated arXiv requests. The analysis script needs the read-only OEIS clone at `~/oeisdata`.

## Appendix: exact lexical AI matches in available entry lines

All matching lines are reproduced without modification from the provided local OEIS data; this includes false positives and non-2026 context. Their presence is not itself a claim of AI use. Links in these lines are OEIS internal HTML.''')
grouped = collections.defaultdict(list)
for item in data['ai_mentions']:
    grouped[item['anum']].append(item['line'])
for anum, lines in sorted(grouped.items()):
    add(f'\n### {anum} — https://oeis.org/{anum}\n')
    for line in lines:
        add('```text\n' + line + '\n```')
(root / 'report.md').write_text('\n'.join(out) + '\n')
print('wrote report.md', len(out), 'blocks;', len(grouped), 'AI-hit sequences')
