# athanor-oeis

Working notebook of the Athanor lab for the OEIS (The On-Line Encyclopedia of Integer Sequences): our directions, research on
OEIS activity, candidate lists, and the status of our own contributions. Everything is kept here so it does not get lost.

Author: Aleksei Kudriashov (ORCID 0009-0006-8885-5338), with AI assistance (Claude Code as the lab's guide; OpenAI Codex cores and ChatGPT agents).
The OEIS policy on AI use (https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions) applies to everything we submit: a human
author is responsible for correctness, programs are understood and published, and nothing is bulk-submitted.

Archived snapshots: v0.5 (12 Nov 2026, 84 checks across lists B, B2, B3), Zenodo DOI pending;
v0.4 (12 Nov 2026, 79 checks across lists B, B2, B3), Zenodo [10.5281/zenodo.24160259](https://doi.org/10.5281/zenodo.24160259);
v0.3 (12 Nov 2026, all 30 list-B candidates), Zenodo [10.5281/zenodo.24155164](https://doi.org/10.5281/zenodo.24155164);
v0.2 (12 Nov 2026, first agent tasks), Zenodo [10.5281/zenodo.24153457](https://doi.org/10.5281/zenodo.24153457);
v0.1, Zenodo [10.5281/zenodo.24145040](https://doi.org/10.5281/zenodo.24145040). Concept DOI (always the latest): 10.5281/zenodo.24145039.

## Directions

Our focus is sequences with the keyword `hard`: easier problems will be solved by others when they need them.

1. **New hard sequences**: define and compute new sequences whose terms are genuinely hard to obtain.
2. **Extending hard sequences**: new terms with certificates, including better software for the computation.
3. **Conjectures in hard sequences**: proofs (or counterexamples) of conjectures stated in hard entries, preferably machine-checked (Lean).

See [directions.md](directions.md) for the reasoning, the competitive landscape and next steps.

## Contents

| Path | What |
|---|---|
| [directions.md](directions.md) | The three directions, strategy, landscape (AI labs, benchmarks), ideas queue |
| [contributions/](contributions/README.md) | Our OEIS sequences and pending edits, with links to certificates |
| [research/2026-11-activity/](research/2026-11-activity/summary.md) | Monthly OEIS activity 2024-2026, overall and for `hard` |
| [research/2026-11-hard-2026/](research/2026-11-hard-2026/report.md) | Who and what is behind the 2026 rise in `hard` activity; where AI is visible |
| [research/2026-11-hard-ranking/](research/2026-11-hard-ranking/README.md) | Interest and opportunity metrics for all 10,080 `hard` sequences; three candidate lists |
| [tasks/](tasks/README.md) | Self-contained tasks for AI agents, one link each, with reviewed answers |

## Reproducing

The scripts read a local clone of the official OEIS data repository (`git clone https://github.com/oeis/oeisdata ~/oeisdata`,
about 3.3 GB). OEIS content is licensed CC BY-SA 4.0; files here that quote or derive from OEIS entries (findings.json,
hard_metrics.csv) carry that licence. Our own code is MIT and our own text and data CC BY 4.0 (see LICENSE.md).
