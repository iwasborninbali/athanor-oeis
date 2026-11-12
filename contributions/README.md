# Our OEIS contributions and pending edits

| Sequence | What | Keywords | Status |
|---|---|---|---|
| [A399138](https://oeis.org/A399138) | Maximum number of points in an n X n X n grid with no three collinear: 1, 8, 16, 28, 40, 64 | nonn, more, hard, nice | Created Aug 19 2026. Witnesses: repo `a399138-witnesses`. |
| [A398172](https://oeis.org/A398172) | Number of subsets of the n X n grid with no three collinear points | nonn, more | Created Sep 03 2026. a(9) = 167892639418 and a(10) = 7287023194031 approved Nov 12 2026 (#36); data in [no3-results](https://github.com/iwasborninbali/no3-results/tree/main/oeis/counting). |
| [A398184](https://oeis.org/A398184) | Number of maximal no-three-in-line subsets of the n X n grid | nonn, more | Created Sep 03 2026. a(9) = 1861878186 and a(10) = 56412888628 approved Nov 12 2026 (#66); supporting file by size to n = 10 proposed. |
| [A398580](https://oeis.org/A398580) | Triangle: k-element no-three-in-line subsets of the n X n grid | nonn, tabf | Created Sep 10 2026. b-file rows 1..10 (terms 1..120) proposed Nov 12 2026. |
| [A097160](https://oeis.org/A097160) | Greatest prime with exactly n consecutive quadratic residues | nonn, hard | Edit prepared: a(7)-a(12) = 4481, 9857, 25793, 60961, 132113, 324673, replacing two wrong old values; certificates in [oeis-A097160](https://github.com/iwasborninbali/oeis-A097160) (archived in Zenodo 10.5281/zenodo.24163515). a(12) confirmed by a second full scan (Nov 12 2026). Proposed Nov 12 2026, citing Buell-Hudson (1984), whose Weil bound K(9) = 414463 and search to 420000 very likely covered a(7) (their 1986 paper says P0 = 1 mod 4 for m <= 8). |

Submissions go through `oeisb` (the OEIS local bridge, ~/projects/oeis-bridge) in Alex's signed-in browser, one reviewed
edit at a time; the site allows at most three open drafts per contributor. Comment text (%C) must be the human author's
own words (OEIS AI policy); data, links and %E credit lines are prepared by the guide.
