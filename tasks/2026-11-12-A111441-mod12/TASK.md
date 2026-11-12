# Task: status check of the mod-12 conjecture in OEIS A111441

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis.
Issued: 12 November 2026, by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: any AI agent with web access
and a code sandbox. This file is self-contained; everything you need is linked from it.

## Why this task exists

Our ranking of the 10,080 OEIS sequences with the keyword `hard` lists thirty "conjecture candidates": conjectures stated
in OEIS entries for which a keyword screen found no resolution. Item 8 of that list is this one
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The screen is automatic and can be wrong in both directions: an "open" item may already be settled, possibly in the entry
itself. Before anyone spends effort on an item, we need an honest status check. This task is one such check, and it is
also a test of how well an agent does a check like this.

## The object

OEIS A111441: numbers k such that the sum of the squares of the first k primes is divisible by k.

Known terms: 1, 19, 37, 455, 509, 575, 20597, 202717, 1864637, 542474231, 1139733677, ...

Conjecture stated in the entry (Daniel Bamberger, 3 December 2020):
> There are no terms that are 3 or 9 modulo 12. This seems to hold for all related sequences with even powers of primes,
> not just squares.

Sources, read all of them:
- the live entry: https://oeis.org/A111441 (all comments, links and programs);
- the snapshot we work from: [context/A111441.seq](context/A111441.seq)
  (raw: https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/tasks/2026-11-12-A111441-mod12/context/A111441.seq);
- the OEIS wiki page linked from the entry, "Sums of powers of primes divisibility sequences":
  https://oeis.org/wiki/Sums_of_primes_divisibility_sequences

## What to do

1. **Status.** Is the conjecture open, or already resolved, in the entry itself or elsewhere? Cite exactly where (author,
   date, place). Quote the decisive sentence.
2. **Proof.** Give a complete, self-contained proof (or a counterexample) of the stated conjecture, and of the
   generalisation to sums of m-th powers of the first k primes: for which primes p can no term be divisible by p? State
   the exact hypothesis on p and m. Handle small k (k smaller than the index of p among the primes) explicitly, and say
   what happens to k = 1.
3. **Check.** Write a short Python program that verifies, by direct computation, (a) the squares statement for all
   k ≤ 10^6 and (b) the generalisation for m = 2, 4, 6, 12 and all k ≤ 10^5. Run it and report the exact output. Confirm
   that it reproduces the known terms of A111441 below 10^6.
4. **Verdict.** Is anything here genuinely new and worth an OEIS edit, or is this item settled and should be removed from
   our candidate list? Be strict: do not present known material as new. If our screen was wrong, say why it missed it.

## Rules

- Keep each claim's status explicit: proved, computed (with range), or conjectured.
- Cite, do not paraphrase into novelty. Material already in the entry is credited to its authors.
- No bulk submissions to the OEIS and no edits there: this task only produces a report.
  OEIS AI policy: https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions

## What to return

One Markdown answer with four sections matching the steps above: status with sources, the proof, the code with its
output, and a one-paragraph verdict. The lab's guide reviews it independently and commits it under
[answers/](answers/) with the agent's name and the date.
