# Task: status and proof attempt for the conjecture in OEIS A005115

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 2026-11-12
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Candidate 45 (list B2, the next-ranked conjecture leads after list B) from our screen of conjectures in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS A005115: Let i, i+d, i+2d, ..., i+(n-1)d be an n-term arithmetic progression of primes; choose the one which minimizes the last term; then a(n) = last term i+(n-1)d.

Terms: 2,3,7,23,29,157,907,1669,1879,2089,249037,262897,725663,36850999,

Conjecture stated in the entry:
> Green & Tao prove that this sequence is infinite, and further a(n) < 2^2^2^2^2^2^2^2^O(n). Granville conjectures that a(n) <= n! + 1 for n >= 3 and give a heuristic suggesting a(n) is around (exp(1-gamma) n/2)^(n/2). - _Charles R Greathouse IV_, Feb 26 2013

Sources: the live entry https://oeis.org/A005115 (all comments, formulas, links); our snapshot [context/A005115.seq](context/A005115.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A005115-granville-ap-primes/context/A005115.seq).

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
