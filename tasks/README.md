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
