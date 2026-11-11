# OEIS activity, January 2024 to October 2026

Source: git history of the official OEIS data repository (daily robot exports), counted with `scripts/git_stats.py` and
`scripts/git_stats_hard.py`; raw monthly counts in the two JSON files. Edits on `hard` sequences are attributed by the keyword at the
current HEAD, which slightly misattributes sequences whose keyword changed.

Typical month in 2026 (all sequences): about 900 new sequences, about 700 data-extension events adding about 3,500 terms, about
870 new b-files, 7-10 thousand sequences edited.

`hard` sequences (10,080 of 401,255 at HEAD), monthly means over complete months. Two bulk months are excluded from the
"new" means (Nov 2024: 4,907 new hard files; Oct 2025: 407), which look like bulk imports or renumbering rather than new work:

| | 2024 | 2025 | 2026 |
|---|---|---|---|
| New hard sequences | 31 | 33 | 61 (Sep 83, Oct 90) |
| Data-extension events | 51 | 44 | 84 (Aug 111, Sep 145, Oct 189) |
| Terms added | ~150 | ~150 | ~305 (Oct 697) |
| Distinct hard sequences edited (all months) | ~270 | ~530 | ~470 |

Medians are lower but show the same shift (extension events 45 / 48 / 62.5; terms added 140 / 137 / 282).
