# Task: status and proof attempt for the conjecture in OEIS A340726

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 2026-11-12
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Item 26 of our list of conjecture candidates in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS A340726: Maximum power V_s*A_s consumed by an electrical network with n unit resistors and input voltage V_s and current A_s constrained to be exact integers which are coprime, and such that all currents between nodes are integers.

Terms: 1,2,6,15,42,143,399,1190,4209,13130,41591,118590,404471,1158696,

Conjecture stated in the entry:
> Take the set SetA337517(n) of resistances, counted by A337517. For each resistance R multiply numerator and denominator. Conjecture: a(n) is the maximum of all these products. The reason is that common factors of V_s and A_s are quite rare (see the beautiful exceptional example with 21 resistors).

Sources: the live entry https://oeis.org/A340726 (all comments, formulas, links); our snapshot [context/A340726.seq](context/A340726.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A340726-resistor-power/context/A340726.seq).

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
