# OEIS hard activity in 2026: composition, contributors and AI

Snapshot: 12 November 2026; events through 11 November. The unit is an event in the supplied Git-diff extraction, not a paper, person, independent discovery, or necessarily a new mathematical result. These are 1,312 distinct sequences, 654 new-file events and 905 data-extension events; 98 sequences have both kinds. November is incomplete. The historical 2024–25 rates in the question were not independently reproduced.

## Executive findings

* The shared feature is **computational scarcity**: these records often ask for exact counts, smallest witnesses, or primality under constrained conditions, where checking the next value can be costly. A `hard` tag is not proof of a particular algorithm or complexity class. Broad number theory and discrete enumeration dominate the name-based classification.
* Acceleration is both concentrated and wider than a single person. Extensions rise from 65 in June to 189 in October; new files rise from 72 to 90. Two extenders account for 74 of 145 September extensions. In October at least 23 extensions concern polyforms and 13 mention sigma/psi and phi. These overlapping name signals do not establish causal families.
* AI is unambiguously visible, but visibility is sparse and uneven. Four entries explicitly describe AI assistance or AI-generated proofs in their text, and an active extender's linked repository discloses AI-written search code. Direct mentions alone materially undercount the linked evidence. The available data cannot estimate the share of all AI-assisted work or establish AI as the cause of the overall rise.

## Scope and classification

The supplied extraction finds new sequences introduced with `hard`, and positive net `%S/%T/%U` term-count changes for sequences carrying `hard` at checkout HEAD. It does not count b-file-only expansions, every edit, withdrawn sequences or all hard sequences. Commit dates are file-change dates, not necessarily dates of computation. Two files were missing from the read-only checkout; their `%N` and `%A` were recovered from the supplied event diffs. The other 1,310 full files were scanned as of the local checkout. This makes full-entry descriptions a snapshot, not necessarily what was present at the event date.

The table uses reproducible **first-match, mutually exclusive name regexes** in the order in `scripts/analyze.py`, not a trained classifier or ground truth. For example, a graph about primes is classified as graphs; a design with neither “design” nor “code” in its title may land elsewhere. The 195 unclassified cases include diverse mathematics. Of 1,312 records, 714 have at least one of their up-to-three supplied cross-reference lines pointing to another sampled sequence; these links support related-family inspection, but are not treated as proof of shared subject or counted as independent clusters. Labels are indicative, not estimates of precise disciplinary proportions.

| Subject by name | Distinct sequences | New | Extended |
|---|---:|---:|---:|
| Primes and divisibility | 431 | 197 | 257 |
| Combinatorics and enumeration | 345 | 163 | 217 |
| Other / unclassified | 195 | 124 | 92 |
| Graphs and networks | 159 | 90 | 79 |
| Other number theory | 110 | 43 | 73 |
| Geometry, packing and grids | 48 | 30 | 20 |
| Games and puzzles | 19 | 5 | 15 |
| Designs and codes | 5 | 2 | 3 |

New and extended columns overlap for sequences with both kinds. Illustrations: prime-constrained searches in [A165234](https://oeis.org/A165234), polyforms in [A365362](https://oeis.org/A365362), graph Ramsey enumeration in [A000789](https://oeis.org/A000789), and a reciprocal-sum extremal problem in [A390394](https://oeis.org/A390394). Cross-references corroborate related pairs [A119751](https://oeis.org/A119751)–[A119752](https://oeis.org/A119752), [A257466](https://oeis.org/A257466)–[A257467](https://oeis.org/A257467), and the arithmetic-function pair [A393230](https://oeis.org/A393230)–[A393425](https://oeis.org/A393425). Family observations use names and cross-references, not numerical proximity of sequence identifiers.

## Contributors

For new events, credit each underscore-delimited name in the current `%A` (or missing-file event `%A`). For extensions, credit each distinct underscore-delimited name on a `%E` line added in that event which itself contains `2026`. An added `%E` is not necessarily the person who made every newly added term; old lines may be reinserted, several people can share credit, and submitter/editor is not necessarily researcher. Attribution is available for 879 of 905 extension events. Names are not identity-resolved beyond whitespace; author names may have changed since the event. Counts are event-person associations, not necessarily distinct people or disjoint contributions.

| Rank | New-sequence author | New events | Extender | Extension events |
|---:|---|---:|---|---:|
| 1 | S. I. Dimitrov | 59 | Jeff Sponaugle | 98 |
| 2 | Robert Price | 58 | Max Alekseyev | 75 |
| 3 | Vladeta Jovovic | 20 | Vladeta Jovovic | 64 |
| 4 | Firdous Ahmad Mala | 20 | Michael S. Branicky | 48 |
| 5 | Igor Blokhin | 16 | Martin Fuller | 36 |
| 6 | Brendan McKay | 15 | Pontus von Brömssen | 35 |
| 7 | Paolo Xausa | 14 | Eric W. Weisstein | 26 |
| 8 | Stefano Spezia | 14 | Chai Wah Wu | 23 |
| 9 | M. F. Hasler | 12 | Andrei Zabolotskii | 22 |
| 10 | Hugo Pfoertner | 11 | Jacob H. Glickman | 19 |
| 11 | Tyler Satchel Orden | 11 | Amiram Eldar | 16 |
| 12 | Paolo P. Lava | 11 | Lyle Blosser | 15 |
| 13 | Haoyang Xu | 11 | James Guillochon | 14 |
| 14 | Charles L. Hohn | 11 | Bert Dobbelaere | 14 |
| 15 | Eric W. Weisstein | 10 | Hugo Pfoertner | 13 |

Taking the **union of events** associated with the top contributors, the top 5 and 10 authors cover 173/654 (26.5%) and 239/654 (36.5%) new events; the top 5 and 10 extenders cover 321/905 (35.5%) and 445/905 (49.2%) extension events. These use all events as denominator, including unattributed ones, and avoid double-counting joint credits. Ties follow file iteration order.

| 2026 | New | Extension | Extensions with attributed `%E` | Leading new authors (events) | Leading extenders (events) |
|---|---:|---:|---:|---|---|
| 2026-06 | 72 | 65 | 60 | S. I. Dimitrov 9, Firdous Ahmad Mala 8, Charles L. Hohn 6 | Max Alekseyev 9, Benjamin Chaffin 9, Michael S. Branicky 5 |
| 2026-07 | 53 | 60 | 58 | Robert Price 9, Haoyang Xu 5, S. I. Dimitrov 4 | Max Alekseyev 17, Lyle Blosser 7, Keisuke Hidaka 2 |
| 2026-08 | 58 | 111 | 111 | Robert Price 6, Vladeta Jovovic 5, Brendan McKay 3 | Jeff Sponaugle 19, Michael S. Branicky 13, Leo Y. Zhang 11 |
| 2026-09 | 83 | 145 | 140 | Vladeta Jovovic 13, Robert Price 9, Ed Pegg Jr 5 | Jeff Sponaugle 45, Vladeta Jovovic 29, Jacob H. Glickman 9 |
| 2026-10 | 90 | 189 | 186 | Robert Price 10, Tyler Satchel Orden 7, S. I. Dimitrov 4 | Jeff Sponaugle 32, Vladeta Jovovic 24, Max Alekseyev 23 |

In September Sponaugle and Jovovic account for 45 and 29 events; in October Sponaugle, Jovovic and Alekseyev have 32, 24 and 23. The top five for October together have 104 person-event credits, not necessarily 104 different events. October's 23 polyform-name matches include the [A365355](https://oeis.org/A365355), [A365358](https://oeis.org/A365358), [A365362](https://oeis.org/A365362) and [A365365](https://oeis.org/A365365) variants, and 13 sigma/psi–phi-name matches are another recurring family. These patterns and the concurrent rise across other contributors favor a mixture of focused campaigns and broader activity, not one single-family explanation. Price's new sequences repeatedly vary prime expressions; Dimitrov's repeatedly vary arithmetic-function identities. These are observations about names, not claims about intent.

## Methods and why these sequences are hard

Literal mention counts below count sequences in the full local text, not event-specific methods, not unique computations, and not all instances of a method. They overlap. Negative results mean only that these literal patterns were absent; code and b-files may be linked or described without the words used here.

| Method / indicator | Sequences with literal match |
|---|---:|
| exhaustive/brute-force search | 79 |
| SAT / satisfiability | 23 |
| integer / linear programming | 7 |
| GPU | 7 |
| distributed / parallel | 6 |
| LODA | 0 |
| primality / prime testing | 10 |
| b-file links | 112 |

The b-file count is only explicit `b-file` or `/bNNNNNN.txt` references; other OEIS “Table of n, a(n)” link formats are missed. The 0 LODA result is **not** evidence that no mined programs exist. `%o` labels in the prepared records show PARI 287, Python 209, C++ 30, Magma 14, SageMath 11 and C 11 sequences; these are not mutually exclusive and do not say what was used for the 2026 extension. SAT, ILP, GPU, distributed or exhaustive-search mentions can describe earlier work. [A000789](https://oeis.org/A000789) provides a concrete exhaustive graph-search and integer-programming context; [A390394](https://oeis.org/A390394) describes ILP and exact checking. A program in a record is not by itself evidence that it produced the new terms.

## AI: direct entry evidence

The whole available local entries were screened for AI/LLM/GPT/Claude/Gemini/DeepMind/AlphaEvolve/AlphaProof/FunSearch/agents/neural and related terms. This yields 30 exact matching lines across 15 sequences, including obvious false positives; the complete verbatim hit list follows in the appendix. The two missing full files were screened only through their provided event additions. This is a lexical audit, not proof that every possible AI paraphrase was found.

Four sequences explicitly state AI use or AI proofs: [A006455](https://oeis.org/A006455) credits a program explored with an LLM for independent computations including a(17)–a(18); [A390394](https://oeis.org/A390394) credits AI assistance for a(39)–a(60); [A248802](https://oeis.org/A248802) and [A358684](https://oeis.org/A358684) report AI proofs. Proofs are not necessarily new sequence terms. A248802's AI text and references are snapshot evidence, not necessarily present at its July extension; similarly A358684's comment is not independently dated. A101877's `claude/` branch is a textual match, **not by itself a disclosure**. Person-name Claude, mathematical variables `ai`, an unrelated multi-agent system, an AI journal or a ChatGPT-hosted domain are not evidence of AI authorship.

## AI: linked arXiv metadata

Extracting links and `arXiv:` identifiers from the provided full `%H` fields yields 268 distinct IDs, including older-style IDs. Batched arXiv Atom queries returned 268/268 metadata records; requests were separated by at least 3.2 seconds. Title, abstract and comments were screened; this is not a full-paper search. The six matches are listed below; matches are leads, not automatically evidence that a term was produced by AI. `arxiv-papers.json` includes all returned abstracts, and `findings.json` includes the complete flags and associated sequences.

| arXiv ID | First posted | Title | Why flagged / interpretation | Sampled entries |
|---|---|---|---|---|
| [2608.11941](https://arxiv.org/abs/2608.11941) | 2026-08-12 | OEIS Open: How many conjectures can language models turn into theorems? | Language-model benchmark of OEIS conjectures; author reports 147 resolved at stated budget. | A248802 |
| [2606.15159](https://arxiv.org/abs/2606.15159) | 2026-06-13 | Every natural number is a sum of distinct semiprime unit fractions | Explicit human–AI collaboration; Claude used in formalisation, experiments and writing; claims Lean checking. | A397192 |
| [2605.22763](https://arxiv.org/abs/2605.22763) | 2026-05-21 | Advancing Mathematics Research with AI-Driven Formal Proof Search | AI/LLM-driven formal proof search; authors report 44 of 492 OEIS conjectures proved. | A248802 |
| [2508.20825](https://arxiv.org/abs/2508.20825) | 2025-08-28 | Computer-assisted graph theory: a survey | Survey includes machine learning among graph methods; not a claim all its results use ML. | A000109, A000944 |
| [2312.06581](https://arxiv.org/abs/2312.06581) | 2023-12-11 | Grokking Group Multiplication with Cosets | Studies neural-network interpretability, not evidence of AI-assisted OEIS extension. | A000638 |
| [1907.05974](https://arxiv.org/abs/1907.05974) | 2019-07-12 | Resolvability of Hamming Graphs | Mentions possible ML application, not AI-generated results. | A303735 |

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

All matching lines are reproduced without modification from the provided local OEIS data; this includes false positives and non-2026 context. Their presence is not itself a claim of AI use. Links in these lines are OEIS internal HTML.

### A000112 — https://oeis.org/A000112

```text
%H A000112 Claude Chaunier, <a href="/A000112/a000112.pdf">Letter to N. J. A. Sloane, Jun 22 1993, with several attachments</a>.
```
```text
%H A000112 Claude Chaunier and Nik Lygerōs, <a href="https://web.archive.org/web/20171110173858/http://www.lygeros.org/0052-fr.html">The Number of Orders with Thirteen Elements</a>, Order 9(2) (1992), 203-204. [See Chaunier letter]
```
```text
%H A000112 Claude Chaunier and Nik Lygerōs, <a href="https://doi.org/10.1016/0304-3975(94)90070-1">Le nombre de posets à isomorphie près ayant 12 éléments</a>, Theoret. Comp. Sci. (1994) Vol. 123, 89-94.
```
```text
%H A000112 Claude Chaunier and Nik Lygerōs, <a href="https://lygeros.org/wp-content/uploads/root/49.pdf">Progrès dans l'énumération des posets</a>, C. R. Acad. Sci. Paris 314 série I (1992) 691-694. [See Chaunier letter]
```

### A000170 — https://oeis.org/A000170

```text
%H A000170 J. Freeman, <a href="https://library.wolfram.com/infocenter/Articles/1910/">A neural network solution to the n-queens problem</a>, The Mathematica J., 3 (No. 3, 1993), 52-56.
```
```text
%H A000170 Ian P. Gent, Christopher Jefferson and Peter Nightingale, <a href="https://doi.org/10.1613/jair.5512">Complexity of n-Queens Completion</a>, Journal of Artificial Intelligence Research 59 (2017), see p 816.
```
```text
%H A000170 Eric Grigoryan, <a href="https://doi.org/10.13187/mai.2018.1.3">Investigation of the Regularities in the Formation of Solutions n-Queens Problem</a>, Modeling of Artificial Intelligence, 2018, 5(1), 3-21.
```
```text
%H A000170 E. Grigoryan, <a href="https://arxiv.org/abs/1912.05935">Linear algorithm for solution n-Queens Completion problem</a>, arXiv:1912.05935 [cs.AI], 2019.
```

### A006455 — https://oeis.org/A006455

```text
%C A006455 a(13)-a(18) computed independently by Gi-Sang Cheon, Samuele Giraudo, and Alejandro H. Morales with a program obtained via exploration with an LLM, of which a(17)-a(18) were computed in a cluster of the Digital Research Alliance of Canada in Sep 2026. Also, a(13)-a(15) were independently computed by Ian Wanless with code written by himself July 20 2026. - _Alejandro H. Morales_, Oct 26 2026
```

### A093483 — https://oeis.org/A093483

```text
%H A093483 Carlos Rivera, <a href="http://primepuzzles.net/puzzles/puzz_037.htm">Puzzle 37. Set of even numbers { ai } such that every ai + aj + 1 is prime ( i & j are different )</a>, The Prime Puzzles and Problems Connection.
```

### A101877 — https://oeis.org/A101877

```text
%H A101877 Tatsuru Watanabe, <a href="https://github.com/tat67/Egyptian-Fraction/blob/claude/gracious-wright-3cqw57/a101877/README.md">A101877: the least largest denominator of a sum of distinct unit fractions equal to n</a>, GitHub, 2026.
```

### A124059 — https://oeis.org/A124059

```text
%H A124059 Myung-Gon Yoon, Peter Rowlinson, Dragos Cvetkovic, and Zoran Stanic, <a href="https://doi.org/10.1002/asjc.793">Controllability of multi-agent dynamical systems with a broadcasting control signal</a>, Asian J. Control 16 (4) (2014) 1066-1072, Table 1
```

### A175531 — https://oeis.org/A175531

```text
%H A175531 Claude Goutier, <a href="http://www-labs.iro.umontreal.ca/~goutier/OEIS/A055553/">Compressed text file carm10e22.gz containing all the Carmichael numbers up to 10^22</a>.
```

### A248802 — https://oeis.org/A248802

```text
%C A248802 Conjectures 1 and 4 were proved by an autonomous AI agent, see the Tsoukalas paper and the Lean files. The first proof uses modular arithmetic in Z_d, reducing the term to 4 * 16^(1024^n) mod d. It tracks the finite orbit of 16 under x => x^1024, verifying by computation over d=2..66 that 4x+3 is not congruent 0, while 67 always divides. The second proof uses Fermat's little theorem to make 2^(2^k+2)+3 mod p periodic in k, then verifies via fast modular squaring that no prime p<1399 (excluding special cases 67, 271, 523) divides it, while 1399 always does (Summaries by Opus 4.7). - _Ralf Stephan_, May 26 2026
```
```text
%H A248802 Tom Adamczewski, <a href="https://arxiv.org/abs/2608.11941">OEIS Open: How many conjectures can language models turn into theorems?</a>, arXiv:2608.11941 [cs.AI], 2026. See pp. 14, 22 (proof, Appendix A).
```
```text
%H A248802 Google Deepmind, <a href="https://github.com/google-deepmind/alphaproof-nexus-results/blob/main/APNOutputs/OEIS/oeis_248802_conjecture_0.lean">AlphaProof Nexus: A244802 Lean file 1</a>.
```
```text
%H A248802 Google Deepmind, <a href="https://github.com/google-deepmind/alphaproof-nexus-results/blob/main/APNOutputs/OEIS/oeis_248802_conjecture_4.lean">AlphaProof Nexus: A244802 Lean file 2</a>.
```
```text
%H A248802 George Tsoukalas et al., <a href="https://arxiv.org/abs/2605.22763">Advancing Mathematics Research with AI-Driven Formal Proof Search</a>, arXiv:2605.22763 [cs.AI], 2026.
```

### A299710 — https://oeis.org/A299710

```text
%H A299710 Claude Goutier, <a href="http://www-labs.iro.umontreal.ca/~goutier/OEIS/A055553/">Text file readme.text summarizing enumeration of Carmichael numbers up to 10^22</a>.
```
```text
%H A299710 Claude Goutier, <a href="/A055553/a055553.txt">Text file readme.text summarizing enumeration of Carmichael numbers up to 10^22</a>. [Local copy, with permission]
```

### A299711 — https://oeis.org/A299711

```text
%H A299711 Claude Goutier, <a href="http://www-labs.iro.umontreal.ca/~goutier/OEIS/A055553/">Text file readme.text summarizing enumeration of Carmichael numbers up to 10^22</a>.
```
```text
%H A299711 Claude Goutier, <a href="/A055553/a055553.txt">Text file readme.text summarizing enumeration of Carmichael numbers up to 10^22</a>. [Local copy, with permission]
```

### A323658 — https://oeis.org/A323658

```text
%C A323658 If G is an oriented graph with vertex set {1,...,n}, then the associated bipartite graph is a bipartite graph B(G) with parts {a1,...,an} and {b1,...,bn} such that ai ~ bj if (i,j) is an edge in G.
```

### A358684 — https://oeis.org/A358684

```text
%C A358684 _Moritz Firsching_ (personal communication) reports that AlphaProof solved Conjecture I by applying the formula below and the fact that A007814(k-1) <= floor(log_2(k)) for every integer k >= 2. See links for formal proof by AlphaProof.
```
```text
%H A358684 Google DeepMind, <a href="https://github.com/google-deepmind/formal-conjectures/blob/ff51e6a91df774fd96674189bd7696f26a043a74/FormalConjectures/OEIS/358684.lean#L74">Lean proof of Firsching's formula below</a>.
```
```text
%H A358684 Google DeepMind, <a href="https://github.com/google-deepmind/formal-conjectures/blob/ff51e6a91df774fd96674189bd7696f26a043a74/FormalConjectures/OEIS/358684.lean#L141">Lean proof of Conjecture I</a>.
```

### A390394 — https://oeis.org/A390394

```text
%C A390394 Terms a(39)-a(60) were computed by integer linear programming over lazily generated forbidden-set constraints with a complete separation oracle, using exact integer arithmetic (reciprocals scaled by lcm(1..60)); values were cross-checked against complete constraint enumeration plus exact minimum hitting set for all n <= 44, and all optimal witness sets re-verified against the definition. The computation was AI-assisted (Claude Fable 5). - _William Alexander Carney_, Aug 02 2026
```

### A398723 — https://oeis.org/A398723

```text
%H A398723 G. Chu and P. J. Stuckey, <a href="https://doi.org/10.1016/j.artint.2012.02.001">A complete solution to the Maximum Density Still Life Problem</a>, Artificial Intelligence, 184-185 (2012), 1-16.
```
```text
%H A398723 Conference For AI Scientists (CAISc) 2026, <a href="https://caisc2026.github.io/verifiable-problems/?problem=connected-still-life">Connected Still Life, Verifiable Problems Track</a>.
```

### A401295 — https://oeis.org/A401295

```text
%H A401295 Elisha Goldman, <a href="https://irreducible-posets.ponensmoder.chatgpt.site/?n=5&amp;k=5&amp;p=1">Join-irreducible counts in posets</a> (see main diagonal)
```
