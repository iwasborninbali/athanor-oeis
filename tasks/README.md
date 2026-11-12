# Tasks for agents

Each folder is one self-contained task, so that an agent can be given a single link and nothing else.

| Path | What |
|---|---|
| `TASK.md` | The task: why it exists, the object, sources, steps, rules, what to return |
| `context/` | Snapshots the task relies on (e.g. the OEIS entry at a fixed commit), with source and licence |
| `answers/` | Agents' answers, committed by the lab's guide after an independent review, named `<date>-<agent>.md` |

Conventions: a task states the answer language (English unless the task says otherwise); the guide does not run code
returned by an agent, it re-implements the check.
Priority checks must include Zenodo and arXiv for the last weeks: on 12 Nov 2026 an agent missed a three-day-old
Zenodo preprint that had already proved its target (A002827).

| Task | Status |
|---|---|
| [2026-11-12-A111441-mod12](2026-11-12-A111441-mod12/TASK.md) | Status check of the mod-12 conjecture in A111441 (conjecture candidate 8). Answered by ChatGPT in 205 s, reviewed: [already resolved in the entry](2026-11-12-A111441-mod12/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A007850-giuga-derivative](2026-11-12-A007850-giuga-derivative/TASK.md) | Candidate 6, A007850: Conjecture: Giuga numbers are the solution of the differential equation n' = n + 1, where … ; answered (ChatGPT), reviewed: [OPEN (literature status reported, nothing new claimed)](2026-11-12-A007850-giuga-derivative/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A002827-unitary-perfect-zumkeller](2026-11-12-A002827-unitary-perfect-zumkeller/TASK.md) | Candidate 5, A002827: Conjecture: Subsequence of A083207 (Zumkeller numbers). Verified for all present terms. - … ; answered (ChatGPT), reviewed: [PROVED, but NOT NEW: Mella (Zenodo, 9 Nov 2026) proved it first](2026-11-12-A002827-unitary-perfect-zumkeller/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A092506-totient-equation](2026-11-12-A092506-totient-equation/TASK.md) | Candidate 14, A092506: Conjecture: these are the only solutions to the equation A000010(x)+A000010(x-1)=floor((3x… ; answered (ChatGPT), reviewed: [PROVED (elementary); no earlier proof found](2026-11-12-A092506-totient-equation/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A051783-valluri-criterion](2026-11-12-A051783-valluri-criterion/TASK.md) | Candidate 15, A051783: Conjecture: The number n = 3^k + 2 is prime if and only if 2^((n-1)/2) == -1 (mod n). - _M… ; answered (ChatGPT), reviewed: [OPEN (necessity proved; sufficiency open)](2026-11-12-A051783-valluri-criterion/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A075245-egyptian-floor-formula](2026-11-12-A075245-egyptian-floor-formula/TASK.md) | Candidate 18, A075245: Conjecture: a(n) = floor(n/4) + d, with d = 1 except for some n = 8k+1 (k = 6, 9, 11, 14, … ; answered (ChatGPT), reviewed: [REFUTED (by the entry's own b-file)](2026-11-12-A075245-egyptian-floor-formula/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A007540-wilson-power-sum](2026-11-12-A007540-wilson-power-sum/TASK.md) | Candidate 9, A007540: Conjecture: Odd primes p such that 1^(p-1) + 2^(p-1) + ... + (p-1)^(p-1) == p-1 (mod p^2).… ; answered (ChatGPT), reviewed: [KNOWN THEOREM (Lerch 1905); the conjecture is true](2026-11-12-A007540-wilson-power-sum/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A000668-sigma-collision-31](2026-11-12-A000668-sigma-collision-31/TASK.md) | Candidate 2, A000668: Primes p of the form sigma(n) where n is even; subsequence of A023195. Primes p of the for… ; answered (ChatGPT), reviewed: [OPEN; equivalent to a prime-restricted Goormaghtigh case; an existing OEIS 'proof' is conditional](2026-11-12-A000668-sigma-collision-31/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A064591-nonunitary-perfect-inverses](2026-11-12-A064591-nonunitary-perfect-inverses/TASK.md) | Candidate 19, A064591: Conjecture: let s0 be the sum of the inverses of the even divisors of a number n and s1 th… ; answered (ChatGPT), reviewed: [OPEN, with an exact reduction (verified)](2026-11-12-A064591-nonunitary-perfect-inverses/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A000043-barina-congruence](2026-11-12-A000043-barina-congruence/TASK.md) | Candidate 1, A000043: Conjecture: for p prime, 2^p-1 is (a Mersenne) prime or p = 2^(2^m)+1 (is a Fermat number)… ; answered (ChatGPT), reviewed: [OPEN (forward direction proved; computation to p ≤ 5000)](2026-11-12-A000043-barina-congruence/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A072567-zarankiewicz-symmetric](2026-11-12-A072567-zarankiewicz-symmetric/TASK.md) | Candidate 17, A072567: Conjecture: the same number of 1s is achieved for symmetric n X n matrices (cf. A350189). … ; answered (ChatGPT), reviewed: [OPEN (special cases by projective-plane polarity; n ≤ 21 matched)](2026-11-12-A072567-zarankiewicz-symmetric/answers/2026-11-12-chatgpt.md) |
