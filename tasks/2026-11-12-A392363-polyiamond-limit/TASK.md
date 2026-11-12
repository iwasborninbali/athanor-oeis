# Task: status and proof attempt for the conjecture in OEIS A392363

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 2026-11-12
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Candidate 81 (list B3, explicit "Conjecture:" lines from the same screen) from our screen of conjectures in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS A392363: Smallest connected polyiamond containing all free n-iamonds under rigid motions of the triangular lattice.

Terms: 1,2,3,5,7,10,13,16,19,24,27,32,37,42

Conjecture stated in the entry:
> Conjecture: lim_{n -> infinity} a(n)/n^2 = 1/5. The ratio a(n)/n^2 decreases from 0.240 at n=10 to 0.214 at n=14 (monotonic in this range). For all n <= 14, a(n) <= ceiling((n^2+2n)/5), with equality for n <= 8 and n=10, and a(n) is 1-3 less for n=9,11,12,13,14.

Sources: the live entry https://oeis.org/A392363 (all comments, formulas, links); our snapshot [context/A392363.seq](context/A392363.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A392363-polyiamond-limit/context/A392363.seq).

## What to do
1. **Status.** Is the statement open, proved, refuted, equivalent to a known open problem, or ill-posed? Search the
   entry, its links and related entries, the OEIS wiki, arXiv, Zenodo, MathSciNet/zbMATH-indexed literature and the
   web, **including preprints from the last four weeks** (search Zenodo and arXiv by keywords and by A-number). Cite
   exactly (author, year, place) and quote the decisive sentence. If it is known, stop after step 4 with the citation.
2. **Proof or counterexample.** If open: prove it, refute it, reduce it to a named open problem, or prove the strongest
   partial result you can. Make the statement precise first. Every step must be checkable. Lean 4 / Mathlib welcome.
3. **Check.** Write a short program that tests the statement (and any lemma you rely on) as far as is cheap, run it,
   and report the exact output and range.
4. **Verdict.** One paragraph: status, what is new (if anything) and how sure you are; what an OEIS comment would say.
   Be strict: never present known material as new; if you did not search a source, say so.

## Rules
- Keep each claim's status explicit: proved, computed (with range), conjectured, or known (with citation).
- No submissions or edits to the OEIS: this task only produces a report.
  OEIS AI policy: https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions

## What to return
One Markdown answer with sections 1–4. The lab's guide reviews it independently (re-implementing every computation)
and commits it under [answers/](answers/).
