#!/usr/bin/env python3
"""Make a self-contained agent task for a conjecture in an OEIS entry (list B of our hard-sequence ranking).

usage: python3 tasks/make_task.py A-NUMBER RANK SLUG REGEX [OEISDATA]
REGEX selects the conjecture line in the entry. OEISDATA defaults to ~/research_scratch/oeisdata.
"""
import re, shutil, subprocess, sys
from datetime import date
from pathlib import Path

a, rank, slug, pat = sys.argv[1:5]
data = Path(sys.argv[5] if len(sys.argv) > 5 else Path.home() / 'research_scratch/oeisdata')
src = data / 'seq' / a[:4] / f'{a}.seq'
head = subprocess.run(['git', '-C', str(data), 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
text = src.read_text()
name = re.search(r'^%N ' + a + r' (.*)$', text, re.M).group(1)
terms = re.search(r'^%S ' + a + r' (.*)$', text, re.M).group(1)
conj = re.sub(r'^%[A-Za-z] ' + a + ' ', '', [l for l in text.splitlines() if re.search(pat, l)][0])
today = date.today().isoformat()
d = Path(__file__).resolve().parent / f'{today}-{a}-{slug}'
(d / 'context').mkdir(parents=True, exist_ok=True); (d / 'answers').mkdir(exist_ok=True)
shutil.copy(src, d / 'context' / f'{a}.seq')
(d / 'context' / 'README.md').write_text(
    f"# Context snapshot\n\n`{a}.seq` is a verbatim copy of OEIS {a} in the internal format, from https://github.com/oeis/oeisdata at commit\n"
    f"`{head}`. Licence: CC BY-SA 4.0 (https://oeis.org/LICENSE), credit to The OEIS Foundation and the contributors\n"
    f"named in the entry. The live entry https://oeis.org/{a} may be newer.\n")
rel = d.relative_to(Path(__file__).resolve().parent.parent)
raw = f'https://raw.githubusercontent.com/iwasborninbali/athanor-oeis/main/{rel}/context/{a}.seq'
(d / 'TASK.md').write_text(f'''# Task: status and proof attempt for the conjecture in OEIS {a}

Lab: Athanor (https://athanor.foundation), OEIS notebook https://github.com/iwasborninbali/athanor-oeis. Issued {today}
by the lab's guide (Claude Code) for Aleksei Kudriashov. Assignee: an AI agent with web access and a code sandbox.
Answer in English. This file is self-contained.

## Why
Item {rank} of our list of conjecture candidates in OEIS sequences with the keyword `hard`
(https://github.com/iwasborninbali/athanor-oeis/blob/main/research/2026-11-hard-ranking/README.md#b-conjecture-candidates).
The list comes from an automatic screen and can be wrong (one item was already proved in its own entry; another had
been proved in a preprint three days earlier). Our aim is to turn true conjectures into theorems, or refute them, with
every step checkable.

## The object
OEIS {a}: {name}

Terms: {terms}

Conjecture stated in the entry:
> {conj}

Sources: the live entry https://oeis.org/{a} (all comments, formulas, links); our snapshot [context/{a}.seq](context/{a}.seq)
(raw: {raw}).

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
''')
row = f'| [{d.name}]({d.name}/TASK.md) | Candidate {rank}, {a}: {conj[:90]}… ; issued |'
readme = Path(__file__).resolve().parent / 'README.md'
readme.write_text(readme.read_text().rstrip('\n') + '\n' + row + '\n')
print(d.name)
