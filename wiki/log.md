# Log

Append-only, chronological. Entry prefix is parseable: `## [YYYY-MM-DD] kind | title`.
`grep "^## \[" wiki/log.md | tail -5` for the last few.

## [2026-06-05] setup | Wiki instantiated (George Hotz clone)
- Instantiated the [[LLM-WIKI]] pattern for the domain "a digital George Hotz you can talk to."
- Wrote the schema ([[../CLAUDE|CLAUDE.md]]): conventions + ingest/query(clone mode)/lint workflows.
- Scaffolded `raw/` + `wiki/` (overview, persona, timeline, topics/, projects/, posts/, index, log).

## [2026-06-05] scrape | George Hotz blog → raw/blog/ (134 posts)
- Built `raw/scrape_blog.py` (idempotent, resumable). Scraped all **134 posts** of
  *"the singularity is nearer"* (geohot.github.io/blog), 2020-08-07 → 2026-05-24, to clean
  markdown with frontmatter. One transient connection-reset retried successfully.

## [2026-06-05] ingest | Full backlog: all 134 posts (batch)
- Read the entire corpus (~90k words) chronologically.
- Synthesis layer written: [[overview]], [[persona]] (clone core), [[timeline]].
- 8 topic pages: [[power-centralization]], [[ai-and-agi]], [[economics-and-value]],
  [[the-pmc-and-rent-seeking]], [[government-and-society]], [[wireheading-and-moloch]],
  [[free-will-and-the-soul]], [[technology-and-freedom]].
- 3 project pages: [[comma-ai]], [[tinygrad-and-tiny-corp]], [[hacking-and-jailbreaks]].
- Per-post summaries for all 134 posts, year-grouped: [[2020-2021]], [[2022-2023]], [[2024]],
  [[2025]], [[2026]]. Built [[index]].
- Known follow-ups (for a future lint/ingest pass):
  - Split high-traffic posts into individual `posts/<slug>.md` pages for finer linking.
  - Some `[[wiki-links]]` point to not-yet-created per-post pages (e.g. [[on-money-creation]],
    [[to-fight-against-entropy]], [[death-of-the-visceral]]); these are intentional stubs.
  - Add other sources beyond the blog (Lex Fridman interviews, talks, tweets, comma/tinygrad
    blogs) under new `raw/` subdirs to deepen [[persona]] and the [[projects]].
