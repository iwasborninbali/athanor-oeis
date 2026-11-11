# Directions, strategy and landscape

## The owner's framing (verbatim, 12 Nov 2026)

> Короче, по оеис в целом я вижу такие направления:
> 1. Поиск новых последовательностей с тегом Хард;
> 2. Дополнение Хард последовательностей; (сюда же входит вектор по улучшению софта для вычислений);
> 3. Доказательство оеис гипотез, где есть тег Хард;
>
> Почему я так зациклен на Хард: как раз из-за уровня сложности задачи. Задачи полегче - решат другие, если им это понадобится;

> ... мы пытались взять задачи тысячелетия- результаты есть но скромные; много долбились в доказательство ГК - также результаты есть
> но скромные. А вот на уровень пониже у нас классно все получается - обычно мы можем вносить ощутимый вклад в продвижение задачи;
> так что я бы пока потоптался бы на этом месте

## What `hard` means and what it does not

`hard` is assigned by OEIS editors: further terms are hard to compute. It is a good filter for "others will not do it casually",
but not a measure of importance. Hence the second filter: interest (incoming references, Wikipedia links, literature, `nice`/`core`,
`more`), see [research/2026-11-hard-ranking](research/2026-11-hard-ranking/README.md).
`core` is a fixed list of 183 fundamental sequences (primes, Fibonacci, ...); only 12 of them are also `hard`
(A000001, A000043, A000105, A000109, A000112, A000609, A000798, A002106, A003094, A005470, A006966, A055512), all heavily worked.
`core` is therefore not a usable target filter; `nice` and incoming references are better signals.

## Landscape as of November 2026

- Activity on `hard` sequences roughly doubled in 2026 and accelerated from August (extension events per month: 2024 ~51,
  2025 ~44, 2026 ~84; Oct 2026: 189). Partly a few very active people, partly broad growth.
- AI is visible but rarely declared: A006455 (LLM-derived program), A390394 (a(39)-a(60), "AI-assisted (Claude Fable 5)"),
  A248802 and A358684 (AlphaProof proofs in Lean), a disclosed Claude/Codex search-code workflow in one contributor's repository.
- Google DeepMind (AlphaProof Nexus; Tsoukalas et al., arXiv:2605.22763) formalised 492 OEIS conjectures in Lean and proved 44
  at a few hundred dollars per problem. Epoch AI turned those 492 into the open benchmark OEIS Open (arXiv:2608.11941): generic
  language models with minimal tools resolved 147 (30%) at $50 per attempt; extra literature access and fancier agent loops did not help.
  These conjectures are now contested by every lab; conjectures outside these sets are not.

## Our edge

Exact computation with certificates: a proved cutoff that makes a finite search complete (A097160 via the Weil bound), independent
re-implementation of every search, published programs and witnesses, and honest records of what is and is not proved.

## Ideas queue

- Direction 2: pick from list A of the ranking (stalled, `more`, real interest, not active in 2026); prefer problems where a
  mathematical cutoff or a symmetry reduction turns the search into a certificate (as in A097160), over pure PRP races dominated by
  GPU farms (the many "k such that (b^k - c^k)/d is prime" entries).
- Direction 3: conjectures in hard entries that are not in OEIS Open / formal-conjectures (list B, "not found in either set");
  formalise in Lean locally; attempt proofs with our cores; submit with Lean files.
- Direction 1: hard sequences that arise from our own work (A399138, no three in line in the n X n X n grid, got `hard` and `nice`
  from the editors; the A398172/A398184/A398580 family).
- Software: speed-ups of standard tools (as with eclib saturation, Sage integral_points) when a hard computation depends on them.
