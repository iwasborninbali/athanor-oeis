# Tasks for agents

Each folder is one self-contained task, so that an agent can be given a single link and nothing else.

| Path | What |
|---|---|
| `TASK.md` | The task: why it exists, the object, sources, steps, rules, what to return |
| `context/` | Snapshots the task relies on (e.g. the OEIS entry at a fixed commit), with source and licence |
| `answers/` | Agents' answers, committed by the lab's guide after an independent review, named `<date>-<agent>.md` |

Conventions: a task states the answer language (English unless the task says otherwise); the guide does not run code
returned by an agent, it re-implements the check.

| Task | Status |
|---|---|
| [2026-11-12-A111441-mod12](2026-11-12-A111441-mod12/TASK.md) | Status check of the mod-12 conjecture in A111441 (conjecture candidate 8). Answered by ChatGPT in 205 s, reviewed: [already resolved in the entry](2026-11-12-A111441-mod12/answers/2026-11-12-chatgpt.md) |
| [2026-11-12-A007850-giuga-derivative](2026-11-12-A007850-giuga-derivative/TASK.md) | Candidate 6, A007850: Conjecture: Giuga numbers are the solution of the differential equation n' = n + 1, where … ; issued |
| [2026-11-12-A002827-unitary-perfect-zumkeller](2026-11-12-A002827-unitary-perfect-zumkeller/TASK.md) | Candidate 5, A002827: Conjecture: Subsequence of A083207 (Zumkeller numbers). Verified for all present terms. - … ; issued |
| [2026-11-12-A092506-totient-equation](2026-11-12-A092506-totient-equation/TASK.md) | Candidate 14, A092506: Conjecture: these are the only solutions to the equation A000010(x)+A000010(x-1)=floor((3x… ; issued |
| [2026-11-12-A051783-valluri-criterion](2026-11-12-A051783-valluri-criterion/TASK.md) | Candidate 15, A051783: Conjecture: The number n = 3^k + 2 is prime if and only if 2^((n-1)/2) == -1 (mod n). - _M… ; issued |
| [2026-11-12-A075245-egyptian-floor-formula](2026-11-12-A075245-egyptian-floor-formula/TASK.md) | Candidate 18, A075245: Conjecture: a(n) = floor(n/4) + d, with d = 1 except for some n = 8k+1 (k = 6, 9, 11, 14, … ; issued |
