# Task: status and proof attempt for the conjecture in OEIS A075245

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 12 November
2026 by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Item 18 of our list of conjecture candidates in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong: item 8 turned out to be proved in its own entry. Our aim is to turn
true conjectures into theorems (or refute them), with every step checkable.

## The object
OEIS A075245: x-value of the solution (x,y,z) to 4/n = 1/x + 1/y + 1/z satisfying 0 < x < y < z and having the largest z-value. The y and z components are in A075246 and A075247.

Terms: 1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,

Conjecture stated in the entry:
> Conjecture: a(n) = floor(n/4) + d, with d = 1 except for some n = 8k+1 (k = 6, 9, 11, 14, 20, 21, 24, 29, 30, 35, 39, ...) where d = 2 . - _M. F. Hasler_, Jul 02 2022

Sources: the live entry https://oeis.org/A075245 (all comments, formulas, links); our snapshot [context/A075245.seq](context/A075245.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A075245-egyptian-floor-formula/context/A075245.seq).

## What to do
1. **Status.** Is the statement open, proved, refuted or ill-posed? Search the entry, its links, the OEIS wiki, arXiv,
   MathSciNet/zbMATH-indexed literature and the web. Cite exactly (author, year, place) and quote the decisive sentence.
   If it is known, stop after step 4 with a clear citation.
2. **Proof or counterexample.** If open: prove it, refute it, or prove the strongest partial result you can (one
   direction, a restricted range, a conditional result). Make the statement precise first. Every step must be
   checkable; no hand-waving. A Lean 4 / Mathlib formalisation is welcome but optional.
3. **Check.** Write a short program that tests the statement (and any lemma you rely on) as far as is cheap, run it,
   and report the exact output and range.
4. **Verdict.** One paragraph: status, what is new (if anything) and how sure you are; what would be needed for an OEIS
   comment or edit. Be strict: never present known material as new; if you did not search a source, say so.

## Rules
- Keep each claim's status explicit: proved, computed (with range), conjectured, or known (with citation).
- No submissions or edits to the OEIS: this task only produces a report.
  OEIS AI policy: https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions

## What to return
One Markdown answer with sections 1–4. The lab's guide reviews it independently (re-implementing every computation)
and commits it under [answers/](answers/).
