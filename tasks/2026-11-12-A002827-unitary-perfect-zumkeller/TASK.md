# Task: status and proof attempt for the conjecture in OEIS A002827

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 12 November
2026 by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Item 5 of our list of conjecture candidates in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong: item 8 turned out to be proved in its own entry. Our aim is to turn
true conjectures into theorems (or refute them), with every step checkable.

## The object
OEIS A002827: Unitary perfect numbers: numbers k such that usigma(k) - k = k.

Terms: 6,60,90,87360,146361946186458562560000

Conjecture stated in the entry:
> Conjecture: Subsequence of A083207 (Zumkeller numbers). Verified for all present terms. - _Ivan N. Ianakiev_, Jan 20 2020

Sources: the live entry https://oeis.org/A002827 (all comments, formulas, links); our snapshot [context/A002827.seq](context/A002827.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A002827-unitary-perfect-zumkeller/context/A002827.seq).

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
