# OEIS submission queue (as of 12 Nov 2026, 23:40 WITA)

At most three open drafts at a time (OEIS limit). Submitted through `oeisb` one at a time, in this order.
Comment text (%C) only in Alex's own words; otherwise link-only edits (OEIS AI policy).

## 1. Certified data (our computations)

| # | Entry | What | State |
|---|---|---|---|
| 1 | A097160 | a(7)-a(12) = 4481 … 324673 (Weil cutoff + two full scans) | proposed Nov 12 (Buell-Hudson 1984 cited; a(7)-a(8) reinstated, a(9)-a(12) new); editors' notes answered by fixing the entry (links in alphabetical order, Zenodo duplicate removed), resubmitted |
| 2 | A398172 | a(9), a(10) | **approved Nov 12** |
| 3 | A398184 | a(9), a(10) | **approved Nov 12** |
| 4 | A398580 | rows n = 9, 10 (b-file, terms 1..120; row 8 credit to Sean A. Irvine kept) | proposed Nov 12 (Michel Marcus split an example line) |
| 5 | A398184 | supporting file "maximal subsets by size" n = 1..7 -> 1..10 | proposed Nov 12 (a398184_1.txt replaces the n = 1..7 link) |

| 5a | A398172 | replace the no3-results link by [oeis-A398172](https://github.com/iwasborninbali/oeis-A398172) | next free slot |
| 5b | A399138 | link [oeis-A399138](https://github.com/iwasborninbali/oeis-A399138) instead of saturation; upload the witness file for n = 1..11 (bounds a(9) >= 116, a(10) >= 138, a(11) >= 164, checked by the guide's own code) replacing the file labelled "a(8) >= 93" | queued |
| 5c | A399138 | **our own comment is false** ("Every optimum found has the same layer profile ... two outer layers cannot both carry 2n points at any total"): a nonuniform 40-point optimum for n = 5 exists (checked by the guide) and two opposite faces with 10 points each are trivially possible. Fix: delete the comment and link the witness; any replacement text must be Alex's own words | queued, needs Alex's decision on wording |
| 5d | A280537 | link [oeis-A280537](https://github.com/iwasborninbali/oeis-A280537); new lower bounds a(21) >= 47, a(22) >= 49, a(27) >= 56 (improvements over the 2017 comment and the 2016 contest per our note; witnesses checked by the guide) via the link title or an uploaded file | queued |
| 5e | A000755 | link [oeis-A000755](https://github.com/iwasborninbali/oeis-A000755) (orbit-sum check of a(20)) | queued |

Rule (Alex, 13 Nov 2026): one sequence, one public repository `oeis-ANNNNNN`; the entry links only that repository.
Repositories exist for all seven entries we authored or extended: A097160, A398172, A398184, A398580, A399138, A280537, A000755.
A097160, A398184 and A398580 drafts were switched to their own repositories before approval.

## 2. New results (each gets its own repository `oeis-ANNNNNN` with the proof; link-only unless Alex writes a comment)

| # | Entry | What |
|---|---|---|
| 6 | A332101 | formula a(n) = A078607(n) + 2 fails at n = 777451915729368 (certified twice) |
| 7 | A078607 | pointer to #6 (Hasler's "it appears" comment) |
| 8 | A092506 | Cloitre's conjecture proved (iff x = 2 or a Fermat prime) |
| 9 | A328151 | Schoenfield's identities proved (D(2m^2) = D(m^2)) |
| 10 | A167809 | a(n) >= Catalan(n) proved (Dyck-path injection) |
| 11 | A075245 | conjectured formula fails at n = 409 (10 failures to 2000) |
| 12 | A007097 | conjecture of Mar 26 2015 false; corrected asymptotic, C ~ 0.238 |
| 13 | A059442 | Fence conjecture fails at m = n = 74 (Erdős 1947) |
| 14 | A004137 | hypothesis of Oct 09 2011 false as worded (example in A193802) |
| 15 | A064591 | Lagneau's conjecture equivalent to Ligh-Wall + no odd perfect numbers |

## 3. Corrections to existing text

| # | Entry | What |
|---|---|---|
| 16 | A081978 | third form should be (p^r+1)/2 |
| 17 | A011541 | remark on Pavlov's conjecture vs the bound 101^3*a(6) |
| 18 | A000170 | constants 0.944 / 2.570, not 0.90 / 2.54 (Simkin) |
| 19 | A023194 | the "Proof" assumes the Goormaghtigh conjecture (check Grantham 2024 first) |

## 4. Missing references to published results (read each source before adding)

| # | Entry | Reference |
|---|---|---|
| 20 | A001419 | Madras, Ann. Comb. 3 (1999) |
| 21 | A005432 | Roney-Dougal and Tracey, arXiv:2503.05416 |
| 22 | A046747 | Hu, Song and Wu, arXiv:2609.39463 (preprint) |
| 23 | A387098 | Minevich et al., arXiv:2411.02251 |
| 24 | A007540 | Lerch 1905 / Sondow 2014 (via A197632) |
| 25 | A262181 | Poonen and Rubinstein 1998, Lemma 2 |
| 26 | A333650 | cross-reference to Luschny's comment in A339494 |

Nothing to submit: entries already settled in their own text (A060843, A111441, A337856, A346509, A346952, A347255,
A242533, A003192, A129924, A002106, A002966, A194091), A002827 (Mella's result, his to add), A186783 (agent's citation was
wrong), and the open conjectures (partial results only).

## 5. Candidate new sequences found by the September-November archaeology (need definition, novelty search, review)

- Maximal no-three-in-line subsets of the n X n grid by size, as a triangle M(n,k) (rows through n = 10 exact; data in oeis-A398184).
- No-three-in-line subsets (all, and maximal) counted modulo the symmetries of the square (fixed-set profiles exist for n = 8, 9).
- Bipancyclic graphs: minimum number of edges for even N = 4..64 (4, 7, 9, 12, 14, ...) and the excess over N (0, 1, 1, 2, 2, 2, 3, ...); no OEIS match found by prefix search.
- Costas arrays: maximum number D(n) of pairwise disjoint order-n Costas arrays; D(13) = 11 (independently checked); initial terms to assemble.
Not sequences as they stand: the q-covering bound C_2(6,3,2) <= 104 (interval 99..104) and the Hai-Walsh classification.
