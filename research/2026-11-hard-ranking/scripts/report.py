import csv,collections,json,subprocess,re,textwrap
from pathlib import Path
P=Path('ranking'); R=list(csv.DictReader((P/'hard_metrics.csv').open())); by={r['id']:r for r in R}; num=lambda r,k:int(r[k] or 0); score=lambda r:float(r['watch_score']); keys=lambda r:set(r['keywords'].split(',')); ordered=lambda rs:sorted(rs,key=lambda r:(-score(r),r['id']))
# The sentence descriptions identify the specific candidate, not every conjecture in its record.
choices={
'A000043':'A modular characterization involving Mersenne and Fermat numbers',
'A000668':'Uniqueness of 31 in a stated divisor-sum condition',
'A007097':'Asymptotic product of logarithms of the terms',
'A000170':'Strong asymptotic estimate for the terms; the weak exponential rate is established in the entry',
'A002827':'Whether the sequence lies within the Zumkeller numbers',
'A007850':'Arithmetic-derivative characterization of Giuga numbers',
'A111441':'Absence of terms congruent to 3 or 9 modulo 12',
'A007540':'A prime power-sum characterization',
'A003459':'Eventual equality with a shifted sequence',
'A011541':'Growth of the number of distinct prime factors',
'A006794':'A bound for the prime preceding a prime p# − 1',
'A005234':'A bound for the prime following a prime p# + 1',
'A048211':'Conjectured limiting ratio around 2.54',
'A092506':'Completeness of listed solutions to a totient equation',
'A051783':'Primality characterization for 3^k + 2',
'A191363':'Whether 3 is the only odd term',
'A072567':'A symmetric-matrix comparison for the maximum number of ones',
'A075245':'A proposed formula with specified exceptional indices',
'A064591':'A characterization using reciprocal sums over divisors',
'A058129':'An asymptotic relation to A027851',
'A059442':'The fence conjecture for the stated Ramsey bound',
'A347391':'Whether the sequence is finite',
'A051602':'An asymptotic density conjecture for maximal grid arrangements',
'A345370':'A proposed value for a(12)',
'A038552':'An open largest-discriminant conjecture; the formal file also marks a different statement solved',
'A119591':'Whether a(n) exists for every n ≥ 2',
'A229232':'Whether a(n) is positive for n > 5 except n = 13',
'A334916':'Whether a base other than 6 or 10 has a unique baseless number',
'A340726':'Maximum numerator–denominator product for resistor networks',
'A358684':'Conjecture II, a(n) ~ 2^n; the entry reports Conjecture I solved',
}
assert len(choices)==30
extension=ordered([r for r in R if not num(r,'commits_2026') and not ({'fini','full'}&keys(r)) and ('more' in keys(r) or (r['last_growth'] and r['last_growth'][:4]<='2022' and r['last_stu_change'][:4]<='2022')) and (num(r,'incoming_all')>=5 or num(r,'wikipedia_all_pages') or num(r,'references_D')+num(r,'links_H')>=3)])[:30]
conjs=ordered([by[a] for a in choices]); watch=ordered(R)[:30]
print('eligible extension',len(extension),'conjectures',len(conjs),'watch',len(watch))
lines=[]
def add(s=''):lines.append(s)
def label(r):return f"[{r['id']}](https://oeis.org/{r['id']})"
def title(r):return textwrap.shorten(re.sub(r'\s+',' ',r['name']).rstrip('.'), width=115, placeholder='…')
def sourcehash(repo):return subprocess.check_output(['git','-C',str(P/'sources'/repo),'rev-parse','HEAD'],text=True).strip()
add('# OEIS hard: interest and opportunity ranking')
add('\nSnapshot: local OEIS HEAD `57bbd254e161585873f56950ff19ba6dc4aeb66c`, 11 November 2026; 401,255 local sequence files, 10,080 tagged `hard`. The rankings are screening tools, not estimates of page views or peer-reviewed assessments of difficulty. The OEIS record is the starting point for checking the exact target. All references below are to that snapshot unless otherwise stated.')
add('\n## A. Extension candidates')
add('\nFilter: no Git commit touching the sequence file in 2026; neither `fini` nor `full`; either `more`, or both last observed growth and last data-line change no later than 2022; and at least five incoming references, one Wikipedia page, or three D/H lines. Sort by the watch score below, then A-number. This conservative activity filter excludes even harmless 2026 edits. A blank growth date means no observed growth since the 2023 import, not a known date of the last extension. Dates and sizes cover only inline terms, never b-files. Verify the linked b-file and recent OEIS state before computing.')
add()
for i,r in enumerate(extension,1):
 year=r['last_growth'][:4] if r['last_growth'] else 'unknown'; flags='more' if 'more' in keys(r) else 'stalled'; add(f"{i}. {label(r)} — {title(r)}; {flags}; {num(r,'incoming_all')} incoming, {num(r,'wikipedia_all_pages')} Wikipedia pages; last inline term {r['last_term_digits'] or '?'} digits; last observed growth {year}.")
add('\n## B. Conjecture candidates')
add('\nThirty selected leads, ranked by the same watch score. Twenty-four choices were selected from explicit conjectures without an identified resolution in the local lines; six further choices represent formalized problems or questions. “Open candidate” means a lead to check, not a verified current mathematical status: a proof or counterexample can appear elsewhere, and a statement may be trivial, false, or only partially formalized. Sequence-level membership does not prove that the specific statement listed is the one formalized. `OEIS Open` means benchmark membership; `formal-conjectures` means a file exists. A benchmark-accepted proof is attached to a sample, not automatically to every conjecture in that sequence. Inclusion in a repository signals exposure, not actual current competition by an AI lab; absence does not prove low competition.')
add()
for i,r in enumerate(conjs,1):
 tags=[]
 if num(r,'oeis_open_samples'):tags.append('OEIS Open')
 if num(r,'formal_conjectures_oeis'):tags.append('formal-conjectures')
 tag=' + '.join(tags) if tags else 'not found in either set'
 add(f"{i}. {label(r)} — {choices[r['id']]}; {tag}; {num(r,'incoming_all')} incoming references.")
add('\n## C. Most watched by a transparent composite')
add('\nFor R = distinct incoming sequence files, W = distinct Wikipedia pages summed across English, Russian and German, and L = D + H lines, the score is **3 log10(1 + R) + 2 log10(1 + W) + log10(1 + L) + 1[core] + 0.5[nice]**. Sorted by score, then A-number. Weights are judgment calls and this is an index of linked visibility, not audience, importance, or statistical probability. Git activity and AI membership are deliberately excluded from the score.')
add()
for i,r in enumerate(watch,1):add(f"{i}. {label(r)} — {title(r)}; score {score(r):.3f}; {r['incoming_all']} incoming, {r['wikipedia_all_pages']} Wikipedia pages, {int(r['references_D'])+int(r['links_H'])} D/H lines"+('; core' if 'core' in keys(r) else '')+('; nice' if 'nice' in keys(r) else '')+'.')
add('\n## What can we infer?')
add('\nInterest can be estimated only indirectly. Many independent-looking incoming references and links from different Wikipedia pages are useful signals of visibility; specific literature and current evidence of independent work are stronger for research relevance when manually checked. None measures reading, use, correctness, difficulty, or demand. References favor older and central records, Wikipedia favors popular and English-language topics, and OEIS Open/formalization reflects a particular benchmark selection. A sequence with few links may still offer an excellent opportunity. `more` expresses an OEIS need, not proof the next term is feasible or useful.')
add('\n## CSV definitions and limitations')
add('''
* `id`, `name`, `keywords`: OEIS identifier, `%N`, and all `%K` tokens. Keywords such as `nice`, `core`, `more`, `unkn`, `fini`, `full`, `base`, `word`, and `obsc` are preserved in the comma-separated field. They have OEIS editorial meanings, can overlap, and are not independent votes.
* `incoming_all`: number of **other distinct source sequence files** in the full local corpus with an A-number token anywhere in the field content, including `%Y`; repeats within one source count once, self-mentions are excluded. `incoming_Y` is the analogous subset in `%Y`. This is textual linkage, not proof of substantive citation. References from related sequence families, programs and boilerplate can inflate it; older entries have had longer to accumulate links.
* `references_D`, `links_H`: counts of `%D` and `%H` lines; not unique publications, external links, citations, or independent researchers. `arxiv_link_lines`, `doi_link_lines`: `%H` lines mentioning arxiv.org / arXiv: or doi.org / DOI: respectively; multiple links on a line count once and alternate forms can be missed. `latest_literature_year` is the largest 1900–2026 four-digit year found in D/H line text, a crude proxy for most recent linked paper year; it may be an access date, unrelated number, book year, or missing, and must be checked.
* `term_count_inline`, `last_term_digits`: comma-delimited terms in `%S/%T/%U`, and decimal digit characters in the last inline item, ignoring sign. Empty is unknown. Expressions, truncated values, decimals, offsets, multi-dimensional encodings, and separate b-files limit interpretation; digit length is not computational cost.
* `commits`, `commits_since_2024`, `commits_2026`: number of Git commits touching the `.seq` file since the local history began, and subsets with commit date on or after 2024-01-01 and 2026-01-01. An export commit may touch thousands of files, collapse edits, or contain bot activity. The 2026 number is through snapshot date, not a full year.
* `last_growth`: latest commit date after file creation where the total count of comma-separated inline values added on changed S/T/U diff lines exceeds those removed. It is an observable net-growth proxy, not a semantic comparison, b-file extension, or date of the underlying computation. `last_stu_change` is the latest commit changing any S/T/U line after creation, including corrections and formatting. Empty means no observable event, not no historical event. Git starts with the 2023-02-19 import; dates before it are unavailable. File additions are deliberately not treated as extensions. Other files, full b-files and changes that remove and add the same number of terms are not counted as growth.
* `conjecture_lines`: number of `%C`/`%F` lines containing case-insensitive `conjecture`, including “conjectured”; a line may mention someone else's conjecture, multiple conjectures, or an already resolved claim. `conjecture_proof_marked_lines` counts these same lines containing a heuristic proof **or disproof/refutation** marker; `conjecture_unmarked_lines` is the remainder, not a count of open conjectures. `conjecture_example` is its first unmarked line. `conjecture_resolution_contexts` also checks an immediately following line that refers to the conjecture and adds “this is true” and “solved” markers; `conjecture_proved_contexts` counts those contexts containing the whole word proved or proven. This is an imprecise indication, cannot establish that a proof was later, can miss nearby or external resolutions, and can associate a marker with the wrong statement.
* `wikipedia_en_pages`, `wikipedia_ru_pages`, `wikipedia_de_pages`: distinct main-namespace page IDs whose external-link URL contains the A-number in the MediaWiki exturlusage bulk result for `oeis.org/A`, fetched with continuation and one request per second. `wikipedia_all_pages` is their sum, treating pages on different language editions as separate pages. It misses links by other OEIS URL forms, templates or redirects that the API does not expose as these external links, other languages, and pages with no link. Wikimedia links are not page views and tend toward famous topics.
* `oeis_open_samples`, `oeis_open_sample_ids`: number and exact benchmark IDs in the 492-item `samples.jsonl` associated with the A-number. `oeis_open_attempted_samples` counts IDs with any checked-in individual score in the inspected OEIS runs; `oeis_open_solved_samples` / `oeis_open_solved_ids` count IDs with at least one `proof_scorer.value = C`. This is an accepted checker result at the benchmark version, not independent validation of the formalization, novelty, or the entire OEIS entry. Absence of an accepted result is not proof of openness, and other unrecorded results can exist.
* `formal_conjectures_oeis`: a Lean file named for the sequence exists in the DeepMind OEIS folder. `formal_category_open`, `formal_category_solved`, `formal_category_test` count matching `@[category ...]` attributes in that file. Categories are the repository's labels, may mix different statements, and a `solved` category can still have `sorry`; it is not a machine-checked proof. The benchmark uses a pinned older formal-conjectures revision, so membership can differ. Zeros mean not found in the inspected snapshots, not proof of absence elsewhere.
* `erdosproblems_link`: case-insensitive literal `erdosproblems.com` anywhere in the current sequence file. It misses problems referred to by name or other URLs; it does not assert that the linked problem remains open.
* `watch_score`: the exact composite above, rounded to three decimals for the CSV and ranking. Ties use A-number.
''')
add('## Verification')
add('\nThe CSV has 10,080 unique hard IDs. All 756 HEAD-present sequences with a 2026 extension in the previous local event extraction also have a 2026 growth date and a 2026 file commit in this pass. This cross-check is not independent of the Git source and does not cover b-file-only work. Spot checks include A087725 (an explicitly refuted conjecture), A000105 (a conjecture marked true), and A248802 (three accepted benchmark sample IDs).')
add('\n## Provenance and reproducibility')
add(f"\n* [OEIS data repository](https://github.com/oeis/oeisdata), read-only local snapshot above; history is one `git log -p` stream. `history.py` counts file touches and inline data diffs; `build.py`, `enrich.py`, and `report.py` produce the outputs. Run them in that order after `wiki.py` for each language. Scripts run within this directory and read the local OEIS checkout.")
add(f"* [OEIS Open paper](https://arxiv.org/abs/2608.11941); [LeanOpenProblems](https://github.com/epoch-research/LeanOpenProblems) `{sourcehash('LeanOpenProblems')}`; [results](https://github.com/epoch-research/LeanOpenProblems-results) `{sourcehash('LeanOpenProblems-results')}`. All 3,468 individual OEIS run score files present at this results revision were inspected; {sum(num(r,'oeis_open_solved_samples') for r in R)} accepted benchmark samples belong to hard sequences. Individual score files are retained in the sparse, shallow source checkout.")
add(f"* [Formal Conjectures OEIS folder](https://github.com/google-deepmind/formal-conjectures/tree/main/FormalConjectures/OEIS) `{sourcehash('formal-conjectures')}`, sparse shallow checkout. The OEIS Open benchmark pins `{(P/'sources/LeanOpenProblems/apn/data/oeis/fc_commit').read_text().strip()}` instead.")
for lang in ('en','ru','de'):
 s=json.loads((P/f'wiki_{lang}_status.json').read_text());add(f"* [Wikipedia {lang} MediaWiki API](https://{lang}.wikipedia.org/w/api.php?action=query&list=exturlusage&euquery=oeis.org%2FA&eunamespace=0&eulimit=max&format=json): {s['requests']} requests, {s['rows']} returned link rows, continuation completed: {s['complete']}; raw JSONL and status retained. The query does not guarantee all possible URL variants.")
(P/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
