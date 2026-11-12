# Task: status and proof attempt for the conjecture in OEIS A051783

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 12 November
2026 by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Item 15 of our list of conjecture candidates in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong: item 8 turned out to be proved in its own entry. Our aim is to turn
true conjectures into theorems (or refute them), with every step checkable.

## The object
OEIS A051783: Numbers k such that 3^k + 2 is prime.

Terms: 0,1,2,3,4,8,10,14,15,24,26,36,63,98,110,123,126,139,235,243,315,363,

Conjecture stated in the entry:
> Conjecture: The number n = 3^k + 2 is prime if and only if 2^((n-1)/2) == -1 (mod n). - _Maheswara Rao Valluri_, Jun 01 2020. [Note that this is an if and only if assertion, so it does not follow from Fermat's Little Theorem. - _N. J. A. Sloane_, Sep 07 2020]

Sources: the live entry https://oeis.org/A051783 (all comments, formulas, links); our snapshot [context/A051783.seq](context/A051783.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A051783-valluri-criterion/context/A051783.seq).

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
