# Rules for our OEIS work

Set by Aleksei Kudriashov on 13 November 2026; kept by the lab's guide. They bind every agent that works on OEIS material for the lab.
The OEIS policy on AI use (https://oeis.org/wiki/Use_of_AI_for_OEIS_Submissions) stands above them.

## 1. What we are here for

1. **We work with the OEIS, and our job is to maintain it.** The OEIS is the source of truth about what is recorded and how.
   We do not keep a parallel database; our repositories exist to back what goes into the OEIS.
2. **A result that is known but missing from the OEIS is ours to add.** It does not matter who found it. The repository
   names the work in which it was found (ours or someone else's) and credits its authors; the entry cites that work in the
   form the editors accept (a published paper or preprint; not an agent platform or a chat log).
3. **We verify everything ourselves.** A value taken from a paper, a table, another agent or our own earlier run is a report
   until we have checked it independently.
4. **No verification certificate, nothing goes to the OEIS.** No term, bound, correction, link or reference is submitted
   unless its repository holds a certificate that meets section 4 and the registry records it.

## 2. One sequence, one public repository

Everything behind our contribution to one OEIS entry lives in one public repository under `github.com/iwasborninbali`, and the
entry links only that repository. A result that concerns two entries lives in the repository of the entry it is about; the other
entry gets a pointer.

The repository name shows whether anything has been submitted:

| State | Name | Example |
|---|---|---|
| New sequence, not submitted (no A-number yet) | `oeis-A______-<slug>` (six underscores in place of the number) | `oeis-A______-bipancyclic-min-edges` |
| Edit to an existing entry, not submitted | `oeis-ANNNNNN-unsubmitted` | `oeis-A272651-unsubmitted` |
| Something from the repository is proposed or approved | `oeis-ANNNNNN` | `oeis-A097160` |

- The exact name `oeis-ANNNNNN` is used only when at least one contribution from the repository is proposed, under review or approved.
- When a new sequence is submitted, the OEIS allocates its A-number; the repository is renamed to `oeis-ANNNNNN` on the same day
  (`registry.py promote`), the README title and status block get the number, and the registry is updated. When an edit to an
  existing entry is submitted, the suffix `-unsubmitted` is dropped the same way.
- Rename before the link is put into the entry. A name that is linked from the OEIS is never changed again.
- Every README carries a status block between `<!-- oeis-status:begin -->` and `<!-- oeis-status:end -->`. It is written by
  `registry.py render`, never by hand.

Layout of a repository: `README.md` (definition, terms or the exact change, method, verification, prior art, how to reproduce,
provenance), `CERTIFICATE.md`, `PRIOR-ART.md`, `LICENSE.md`, `data/`, `programs/`, `verification/` (with logs). Repositories
created before these rules keep their folders and gain the three documents.

## 3. The registry

`registry/registry.json` is the single list of everything we have for the OEIS: approved contributions, open drafts, queued
edits, candidates for new sequences, and findings that are not OEIS items. `REGISTRY.md` is generated from it. One record per
contribution; several records may share a repository.

States: `idea` → `candidate` (repository exists) → `verified` (certificate complete, guide's own check done) → `queued`
(approved for submission, waiting for a slot) → `proposed` → `reviewed` → `approved`; and `rejected`, `withdrawn`,
`superseded`, `not-for-oeis`.

**The agent keeps the registry current.** The guide (or any agent acting for the lab) updates the registry, regenerates
`REGISTRY.md` and the status blocks, runs `registry.py check`, commits and pushes:

- on every event from the OEIS watcher (a draft approved, reviewed, edited by an editor, a note in the discussion, a rejection);
- right after every submission (state, draft or A-number, date; rename the repository when the rule above requires it);
- when a new result or candidate is found (a record and a repository before anything else is done with it);
- when a certificate changes, a prior-art finding changes the claim, or a repository is created, renamed or archived;
- at the start of every OEIS working session: compare the registry with the live drafts (`oeisb drafts`) and with the entries.

Every record names its next action and who owns it (guide, Alex, editors). Nothing found is dropped: a result that turns out
not to be an OEIS item stays in the registry as `not-for-oeis` with the reason.

## 4. The verification certificate

`CERTIFICATE.md` in the repository states:

- **Claim**: the exact statement, one line per term, bound, correction or reference.
- **Evidence**: the producer and an **independent check**: a second program written separately (different method where
  possible), or a checker for an explicit witness, or for a proof the complete written argument plus programs for every
  computational step. Who wrote each, what it covers, whether it shares code or data with the producer.
- **Replay**: the commands actually run, where, when, with outputs or logs and file hashes.
- **Not covered**: every gap and every part that rests on a report. A reported value is never written as verified.
- **Guide's independent check**: what the guide checked with his own code or by his own reading, and the result.
- **Verdict**: `complete`, `partial` or `none`.

A record may be `verified` only with verdict `complete` and the guide's check filled in. For exact terms the independent
check must cover the full claim, not a sample. For a lower bound an explicit witness and a checker suffice. For a proof the
certificate says plainly that it is a human-checkable proof unless it is machine-checked. For a reference the source itself
must have been read, and the certificate quotes the place.

## 4a. Independent recounts by ChatGPT agents

Added by Aleksei Kudriashov on 13 November 2026. To check a count independently we use ChatGPT agents through the lab's
Chrome bridge (`cgpt`, see the `chatgpt-bridge` skill). Each agent has its own container (about 4 cores and 8 GB of RAM)
and can run the computation there.

1. **The task goes as an archive.** In the candidate's repository the guide writes
   `verification/chatgpt/<date>-<slug>/TASK.md` (English, self-contained): the definition, the exact claim to check, what
   to compute, limits, and the report to return. The archive is `git archive` of that commit (tracked files only), sent with
   `cgpt thread verify-<slug> "<one-line request>" --attach <archive>.zip`. One thread per check, named `verify-<slug>`.
2. **Independence.** For an independent recount the archive holds the definition and, where needed, the witnesses or
   certificates to be checked, but not our producing program; the agent writes its own program from the definition. A replay
   of our program is allowed only as an additional check and is recorded as such.
3. **Long computations.** The agent writes progress and checkpoints to files and makes the run resumable. We ask it
   to keep the computation running in the background and to set itself a reminder, a scheduled task or cron to report
   progress. Observed on 13 Nov 2026: the agents say a process in their container does not outlive the reply, and their
   containers have 5 logical CPUs with a 4-CPU quota and a 4 GB memory limit. So in practice the run is split into pieces:
   each reply computes as much as fits (about 10-20 minutes), saves a checkpoint, and reports what fraction is done; the
   guide continues it with `cgpt thread verify-<slug> "continue from the checkpoint"` until it is finished. If the checkpoint
   is lost (container reset), the agent says so and restarts from the last state it reported.
4. **What comes back.** The agent's program, the exact commands, the output, the container's cores and memory, run times,
   and SHA-256 of every result file. Text artefacts come back in chunks with per-chunk hashes (see the bridge skill).
   Everything is saved next to the task (`answer.md`, `program/`, `logs/`).
5. **Before it counts.** The guide reads the agent's program, checks that it computes the stated definition, reruns it locally
   on the small cases (and on a large one if the machine allows), and only then records the recount in `CERTIFICATE.md`
   as an independent check, naming the agent, the thread and the date. An agent's report that was not reviewed this way is a report.

## 5. Prior art

`PRIOR-ART.md` records, with dates and exact queries: OEIS searches for the terms (also shifted and re-indexed) and for key
words; the literature and public tables found, including preprints and archives of the last months; who established what first.
The search is repeated just before submission. If someone else got there first, the entry credits them and our repository says
which part is ours: an independent verification, an extension, or nothing new. Third-party data and papers are not copied into
our repositories: a fetch script with the URL and checksum instead.

## 6. Submitting

- From Aleksei Kudriashov's OEIS account, through `oeisb`, one edit at a time; at most three open drafts (OEIS limit).
- Order when a slot is free: (1) corrections of our own errors in the OEIS; (2) editors' notes on our open drafts, answered by
  fixing the entry; (3) data and links for entries we already contributed to; (4) results on other entries; (5) new sequences,
  one at a time, never in bulk or in series.
- Human gates: the name and definition (%N) of a new sequence, any comment text (%C) and any reply to editors are the author's
  own words. Agents prepare data, links, references, programs and %E credit lines, and never write the rest.
- Before submitting: certificate complete, prior art re-checked, live entry re-read (someone may have edited it), registry updated.
- After approval: registry updated, repository tagged and archived at Zenodo (the DOI goes into the registry and the README,
  not into the OEIS entry, which links the repository only).

## 7. Housekeeping

- Results are public; tools and infrastructure are private.
- Nothing over 5 MB in git; large artefacts are described by size, hash and archive location.
- Commit only our own files; no `sources/` folders; no secrets.
