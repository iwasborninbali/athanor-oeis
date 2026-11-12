# Task: status and proof attempt for the conjecture in OEIS A328151

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 2026-11-12
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Candidate 52 (list B3, explicit "Conjecture:" lines from the same screen) from our screen of conjectures in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS A328151: a(n) is the smallest nonnegative integer k where exactly n ordered pairs of positive integers (x, y) exist such that x^2 + y^2 = k.

Terms: 0,2,5,50,65,1250,325,31250,1105,8450,8125,19531250,5525,488281250,

Conjecture stated in the entry:
> Conjecture: a(2k) = A093195(k) for k >= 1, a(2k+1) = 2*A006339(k)^2 for k >= 0. - _Jon E. Schoenfield_, Jan 23 2022

Sources: the live entry https://oeis.org/A328151 (all comments, formulas, links); our snapshot [context/A328151.seq](context/A328151.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A328151-parity-formula/context/A328151.seq).

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
