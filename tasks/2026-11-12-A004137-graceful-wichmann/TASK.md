# Task: status and proof attempt for the conjecture in OEIS A004137

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued 2026-11-12
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Candidate 35 (list B2, the next-ranked conjecture leads after list B) from our screen of conjectures in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS A004137: Maximal number of edges in a graceful graph on n nodes.

Terms: 0,1,3,6,9,13,17,23,29,36,43,50,58,68,79,90,101,112,123,138,153,168,

Conjecture stated in the entry:
> If the conjecture is true that an optimal ruler with more than 12 segments is a Wichmann ruler then the sequence continues 232, 251, 270, 289, 308, 327, ... - _Peter Luschny_, Oct 09 2011 [updated to take the verifications of Robison into account, Oct 01 2015]

Sources: the live entry https://oeis.org/A004137 (all comments, formulas, links); our snapshot [context/A004137.seq](context/A004137.seq)
(raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A004137-graceful-wichmann/context/A004137.seq).

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
