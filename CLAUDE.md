# Notes for Claude Code (and other agents)

This file is loaded automatically by Claude Code at the start of a session. It
captures the conventions, architecture decisions, and gotchas of this project
so a fresh agent can pick up context without re-deriving it from the code.

## What this project does

A Python pipeline that:

1. Fetches the Hacker News Best feed from `hnrss.org/best` every hour
2. For each new article: downloads the linked page, extracts the main text
   (`trafilatura`), and fetches the HN discussion via the Algolia HN API
3. Calls an OpenRouter LLM (Claude Haiku 4.5 by default, with two free-tier
   fallbacks) to produce: a rewritten factual title, a summary of the article,
   and a pro/con synthesis of the HN discussion
4. Publishes the result as a static RSS 2.0 feed at
   `https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml`,
   consumed by the user in Feedly. The `.fr.` suffix leaves room for a
   parallel `feed.en.xml` if English summaries are added later.

The orchestration is a single GitHub Actions workflow (`cycle.yml`) that runs
hourly on a public repo, so minutes are free.

## Conventions

- **Language**: all repo artifacts (commit messages, README, code comments,
  PR text, CLAUDE.md, docs) must be in **English**. The conversation with the
  user happens in French, don't conflate the two. User-facing content inside
  the feed (summary text, feed title, section headings like "Résumé de
  l'article", "Confirmations", "Réfutations") stays in **French** because
  that's the user's target reading language.
- **No comments unless a reader would be surprised**. No "this line does X"
  comments. Add a comment only when there's a non-obvious invariant, a
  workaround, or a subtle constraint.
- **No speculative code**. No feature flags, no hypothetical extension
  points, no abstractions for one call site.

## Architecture at a glance

- **No database**. One Markdown file per article, frontmatter for metadata,
  body for the LLM output. Files partitioned
  `artefacts/articles/YYYY/MM/DD/` by the article's HN submission date.
  Filename is a 8-char SHA-256 short hash of the `guid` for deterministic
  idempotent naming.
- **No backend**. The whole pipeline runs inside a single Actions job that
  reads/writes the repo and pushes back. The `artefacts/` folder is
  uploaded by a dedicated Actions workflow and served statically by Pages.
  Its contents are exposed at the site root, so the feed URL is
  `https://.../feed.fr.xml` (no `/artefacts/` in the path).
- **No queue, no retry service**. The pipeline keeps state via a `status`
  field in each article's frontmatter (`pending` → `article_fetched` →
  `discussion_fetched` → `summarized`, or `failed`). Each step iterates files
  of the matching status. Crash-resumable for free.
- **Raw HTML / discussion text is never committed**. Article content is kept
  in sidecar files (`artefacts/articles/.../<hash>.raw.article.txt`,
  `<hash>.raw.discussion.txt`) which are gitignored, used during the cycle,
  and cleared once the summary succeeds. Only the summary itself ends up in
  git. Driven by copyright and repo-size concerns.

## Key files

- `src/app/pipeline.py`, orchestration of the five steps and the retry
  bookkeeping (`_record_attempt`).
- `src/app/storage.py`, filesystem layout. `iter_summarized()` walks the
  date tree newest-first and sorts by `hn_item_id` desc within each day, so
  publish can break as soon as it has 200 items without scanning old files.
- `src/app/rss_in.py`, parses the hnrss feed and detects Ask HN / Show HN
  (when `entry.link == entry.comments`).
- `src/app/fetch_article.py`, HTTP + trafilatura, falls back to the feed's
  own summary if extraction fails or the URL isn't HTML.
- `src/app/fetch_discussion.py`, Algolia API + comment selection: recursive
  degressive comment budget (default 500), plus pinning of the HN submitter's
  own comments and their full ancestor chain.
- `src/app/llm.py`, OpenRouter client with model cascade on 429 / 5xx /
  empty body. Logs token usage per call.
- `src/app/summarize.py`, two prompts (article + title rewrite in one call,
  and discussion synthesis). French output, strict `## Titre` / `## Résumé`
  format that we parse back.
- `src/app/publish.py`, builds `feed.fr.xml` with `feedgen`. Items ordered by
  `hn_item_id` desc. `<link>` = article URL (or HN URL for Ask/Show HN),
  `<comments>` = HN URL. Description is markdown rendered with
  `markdown-it-py` (CommonMark-compliant, unlike the older `markdown`
  library which broke bullet lists).

## Gotchas worth knowing

- **OpenRouter 200 with error body**: some failures come back as HTTP 200
  with `{"error": {...}}` in the JSON. `llm._call` treats "no choices" as a
  `_Retryable` and falls through to the next model. The cascade design is
  load-bearing, don't bypass it.
- **hnrss "best" is not "newest"**: articles in `/best` rotate based on
  score decay, typically 1 to 4 days old. Sort by `hn_item_id` desc reflects
  submission order because HN IDs are strictly monotonic.
- **Python-Markdown is not CommonMark**: don't switch back. Bullets directly
  under a non-blank line rendered as flat text. `markdown-it-py` handles it.
- **Feed dedup is by `<guid>`**: we expose `short_hash` there, not the
  raw HN URL. Changing that field makes every reader treat every item as
  new, so avoid unless you mean it.
- **Cron is best-effort**: GitHub schedules run 5 to 15 min late under load.
  Not an issue at our cadence.

## Commands

```bash
uv sync                             # install deps
uv run pytest                       # full test suite (65 tests today)
uv run ruff check src/ tests/       # lint
uv run app cycle                    # run the whole pipeline once
uv run app fetch-feed               # step 1 only (no LLM)
uv run app publish                  # step 5 only (regenerate feed.fr.xml)
```

`OPENROUTER_API_KEY` must be set in `.env` locally, or as a GitHub Secret
for the workflow.

## Testing philosophy

We test **rules that can regress**, not plumbing. Good coverage on: comment
selection (budget, pinning, degressive split), LLM cascade, feed structure,
storage invariants, retry state machine. Skipped: CLI wiring (trivial),
logging setup (no logic), full mocked `run_cycle()`. Real Actions runs catch
integration bugs (like the two we already hit: wrong sort key, broken
markdown rendering) better than mocks ever would.

Don't chase 100% coverage. A test that is hard to write is often a test of
plumbing.
