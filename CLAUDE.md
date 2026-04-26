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
  l'article", "Avis positifs", "Avis négatifs", "Commentaires les plus
  plébiscités") stays in **French** because that's the user's target
  reading language.
- **No comments unless a reader would be surprised**. No "this line does X"
  comments. Add a comment only when there's a non-obvious invariant, a
  workaround, or a subtle constraint.
- **No speculative code**. No feature flags, no hypothetical extension
  points, no abstractions for one call site.

## Architecture at a glance

- **No database**. One Markdown file per article, frontmatter for metadata,
  body for the LLM output. Files partitioned
  `artefacts/articles/YYYY/MM/DD/` by `our_published_at` (the date the
  article first appeared in our feed, captured from hnrss's
  `lastBuildDate`), not by its HN submission date. Filename is a 8-char
  SHA-256 short hash of the `guid` for deterministic idempotent naming.
- **No backend**. The whole pipeline runs inside a single Actions job that
  reads/writes the repo and pushes back. The `artefacts/` folder is
  uploaded by a dedicated Actions workflow and served statically by Pages.
  Its contents are exposed at the site root, so the feed URL is
  `https://.../feed.fr.xml` (no `/artefacts/` in the path).
- **No queue, no retry service**. The pipeline keeps state via a `status`
  field in each article's frontmatter (`pending` → `discussion_fetched` →
  `article_fetched` → `summarized`, or `failed`). Discussion runs before
  article fetch so the canonical article URL Algolia returns can replace
  the (sometimes stale) hnrss `<link>` before we hit the publisher, and
  so the dupe-pointer check in the first comment can either drop the
  entry or rewrite it to the canonical HN item before any LLM call.
  Each step iterates files of the matching status. Crash-resumable for
  free.
- **Raw HTML / discussion text is never committed**. Article content is kept
  in sidecar files (`artefacts/articles/.../<hash>.raw.article.txt`,
  `<hash>.raw.discussion.txt`, `<hash>.raw.top_comments.txt`) which are
  gitignored, used during the cycle, and cleared once the summary
  succeeds. Only the summary itself ends up in git. Driven by copyright
  and repo-size concerns.
- **Weekly LLM version check**. A separate workflow
  (`.github/workflows/check-llm-versions.yml`) runs `uv run app
  check-llm-versions` every Monday, queries OpenRouter's `/models`
  endpoint, and opens a GitHub issue when a newer generation of the
  configured `openrouter_model` family is published. The bump itself is
  manual (edit `openrouter_model` in `src/app/config.py`).

## Key files

- `src/app/pipeline.py`, orchestration of the five steps and the retry
  bookkeeping (`_record_attempt`). `step_fetch_discussions` also runs
  the dupe-pointer check after `fetch_discussion()`: when the returned
  `Discussion.canonical_dupe_id` is set, it either deletes the dupe
  article (if `find_existing(canonical_guid)` already has the canonical)
  or rewrites the article's identity fields in place (`hn_item_id`,
  `guid`, `hn_url`, `title`, `source_published_at`), moves the file to
  the new `short_hash`-derived path, and continues with the canonical's
  discussion. `our_published_at` is preserved so the partition does not
  move.
- `src/app/storage.py`, filesystem layout. `iter_summarized()` walks the
  date tree newest-first and sorts by `our_published_at` desc within each
  day, so publish can break as soon as it has 100 items without scanning
  old files. `find_existing(guid)` is a hash-based lookup used by
  `step_fetch_feed` to detect already-seen entries — needed because the
  partition is now based on a timestamp we cannot recompute from a fresh
  feed poll.
- `src/app/rss_in.py`, parses the hnrss feed and detects Ask HN / Show HN
  (when `entry.link == entry.comments`).
- `src/app/fetch_article.py`, HTTP + trafilatura, falls back to the feed's
  own summary if extraction fails or the URL isn't HTML. Also detects
  JavaScript-required SPA pages by fuzzy-matching trafilatura's output
  against the raw HTML's `<noscript>` block (ratio ≥ 0.9 via
  `difflib.SequenceMatcher`), in which case it returns
  `ContentSource.JS_REQUIRED` with empty text. YouTube URLs
  (`youtube.com/watch`, `youtu.be`, `shorts`, `embed`, `v`) short-circuit
  the HTML path: the video transcript is pulled via
  `youtube-transcript-api` (`fr` then `en`, auto-generated accepted) and
  returned as `ContentSource.VIDEO_TRANSCRIPT`. `img.youtube.com`
  thumbnail is always used as `image_url`, even when the transcript
  fetch fails.
- `src/app/fetch_discussion.py`, Algolia API + comment selection: walks the
  full tree depth-first and yields every comment with text, in HN's natural
  reply order, so all comments reach the LLM. The Algolia root payload also
  carries the canonical article URL (HN's source of truth, which can drift
  from the hnrss `<link>` after a moderator edit). The pipeline uses it to
  overwrite `article.url` before `step_fetch_articles` runs. A `null` URL
  (Ask/Show HN, polls) keeps the feed URL untouched. Before any of that,
  `find_dupe_canonical_id` inspects the first child comment for an HN
  moderator dupe pointer (`dupe:` keyword + `news.ycombinator.com/item?id=NNN`
  link, with `html.unescape` because Algolia entity-encodes the slashes
  as `&#x2F;`). When found, `fetch_discussion` short-circuits and returns
  a `Discussion` with empty text and `canonical_dupe_id=NNN`, plus the
  payload's `title` and `created_at` so the caller can substitute the
  article identity without a second Algolia call. Also produces the
  "Commentaires les plus plébiscités" block rendered at the end of the
  discussion section. Per-comment scores are not exposed by any HN API
  (Algolia returns `points: null` on every child, Firebase doesn't carry
  it either), and Algolia's `/items/{id}` returns children
  chronologically by ID, which mostly surfaces the earliest posted
  comments rather than HN's best picks. So `_fetch_hn_display_order`
  scrapes `news.ycombinator.com/item?id=<id>` and extracts the top-level
  comment rows (`<tr class="athing comtr">` with `indent="0"`) in their
  rendered order, which is HN's own internal best-ranking. The IDs are
  mapped onto the Algolia tree by `_select_top_comments` to pull each
  comment's text and author, the text is HTML-stripped and whitespace-
  collapsed, truncated to 300 chars with U+2026 on overflow, and the
  first three valid entries are returned. An HTTP or parse failure
  degrades silently to an empty section rather than crashing the cycle.
  The rendered markdown travels between `step_fetch_discussions` and
  `step_summarize` via the gitignored `<hash>.raw.top_comments.txt`
  sidecar, which `clear_sidecars` cleans up after summarization
  alongside its siblings.
- `src/app/llm.py`, OpenRouter client with model cascade on 429 / 5xx /
  empty body. Logs token usage per call.
- `src/app/check_models.py`, queries OpenRouter's `/models` endpoint and
  prints a report (exit 2) when a newer version of the configured
  `openrouter_model` family is available. Invoked weekly by its own
  workflow. HTTP errors propagate so a transient network failure surfaces
  as a red workflow run rather than being silently swallowed.
- `src/app/summarize.py`, three prompts (article + title rewrite in one
  call, discussion synthesis, and a cheap title-only translation used when
  the article is `js_required`). French output, strict `## Titre` /
  `## Résumé` format that we parse back.
- `src/app/publish.py`, builds `feed.fr.xml` with `feedgen`. Items ordered
  by `our_published_at` desc (date of entry in our feed), so the XSLT
  preview shows the most recently ingested articles on top. Per-item
  `<pubDate>` stays at `source_published_at` (HN submission date) on
  purpose. `<link>` = article URL (or HN URL for Ask/Show HN),
  `<comments>` = HN URL. Description is markdown rendered with
  `markdown-it-py` (CommonMark-compliant, unlike the older `markdown`
  library which broke bullet lists).

## Gotchas worth knowing

- **OpenRouter 200 with error body**: some failures come back as HTTP 200
  with `{"error": {...}}` in the JSON. `llm._call` treats "no choices" as a
  `_Retryable` and falls through to the next model. The cascade design is
  load-bearing, don't bypass it.
- **hnrss "best" is not "newest"**: articles in `/best` rotate based on
  score decay, typically 1 to 4 days old. That is why the feed is
  ordered by `our_published_at` (when the item first hit our ingest)
  rather than by `hn_item_id` — HN IDs are strictly monotonic in
  submission time, not in when the article became interesting to us.
- **Python-Markdown is not CommonMark**: don't switch back. Bullets directly
  under a non-blank line rendered as flat text. `markdown-it-py` handles it.
- **Feed dedup is by `<guid>`**: we expose `short_hash` there, not the
  raw HN URL. Changing that field makes every reader treat every item as
  new, so avoid unless you mean it.
- **Cron is best-effort**: GitHub schedules run 5 to 15 min late under load.
  Not an issue at our cadence.
- **Thin discussions are parked, not failed**: `step_fetch_discussions`
  leaves articles at their current status (`pending`, or `article_fetched`
  for legacy in-flight items) when their comment count is below
  `MIN_DISCUSSION_COMMENTS` (default 20). No `attempts` bump, no move to
  `_failed/`. Each later cycle picks them up again via the chained
  `iter_by_status(PENDING)` / `iter_by_status(ARTICLE_FETCHED)` source, so
  they graduate as soon as the discussion grows past the threshold. For a
  substituted dupe whose canonical comes back below threshold, the
  rewritten identity is saved at `pending` before parking so the new
  on-disk entry exists at the canonical guid for re-pickup; the old
  per-dupe path is already gone by then.
- **HN HTML is the only source for comment ranking**: per-comment scores
  are not exposed by Algolia or Firebase, and Algolia returns children
  in chronological (ID-ascending) order, not HN's best order. The
  "Commentaires les plus plébiscités" section therefore depends on a
  fetch of `news.ycombinator.com/item?id=<id>` per article. HTTP 429
  from HN happens often enough on shared GitHub Actions IPs to be a
  real concern, even on a single request. `_fetch_hn_html` is wrapped
  in a tenacity retry (3 attempts, 2-10 s exponential backoff on 429
  / `ConnectError` / `ReadTimeout`). If those retries are exhausted
  and `WEBSHARE_PROXY_USERNAME` / `WEBSHARE_PROXY_PASSWORD` are set,
  `_fetch_hn_display_order` falls back to a single attempt through
  `_fetch_hn_html_via_proxy`, which routes the same GET through the
  Webshare residential pool already used by the YouTube path — fresh
  IP per request, sidesteps HN's IP throttling. If everything fails,
  the section degrades to empty rather than crashing. If HN ever
  rewrites its comment-row markup, update `_COMMENT_ROW_RE` in
  `fetch_discussion.py`.
- **Dupe detection looks at the first comment only**: HN moderators
  (and occasionally regular users) flag a duplicate submission with a
  comment of the form `dupe: https://news.ycombinator.com/item?id=NNN`.
  We trigger on `payload.children[0]` because Algolia returns children
  in chronological order and the dupe pointer is almost always posted
  first. The `dupe` keyword is required in addition to the link, to
  avoid false positives on first comments that legitimately link to a
  related HN thread. Substitution is single-hop only. If the canonical
  is itself a dupe, the resulting `Discussion` will carry its own
  `canonical_dupe_id` and we ignore it. Multi-hop chains are rare
  enough not to justify the loop. The article filename changes when the
  guid is rewritten because `short_hash` is derived from the guid, so
  the dupe branch unlinks the old file and recomputes `path_for(...)`
  before saving. `our_published_at` stays put because the partition
  layout depends on it.
- **YouTube transcripts need a residential proxy in CI**: YouTube blocks
  cloud-provider IP ranges, so any direct transcript fetch from a GitHub
  Actions runner raises `RequestBlocked`. `_fetch_youtube_transcript`
  reads `WEBSHARE_PROXY_USERNAME` / `WEBSHARE_PROXY_PASSWORD` from
  settings and, when both are set, routes through Webshare's rotating
  residential pool. Locally (unblocked home IP) the variables can stay
  empty. The failure is logged as `youtube_transcript_failed` and falls
  through to `ContentSource.FEED_FALLBACK`, never crashes the pipeline.
  The proxy is a workaround for the GitHub Actions hosting, not a hard
  dependency of the pipeline. If the service ever moves to a VPS or a
  home server whose IP YouTube does not block, both variables can stay
  unset and the direct transcript fetch will work.

## Commands

```bash
uv sync                             # install deps
uv run pytest                       # full test suite (~125 tests today)
uv run ruff check src/ tests/       # lint
uv run app cycle                    # run the whole pipeline once
uv run app fetch-feed               # step 1 only (no LLM)
uv run app publish                  # step 5 only (regenerate feed.fr.xml)
```

`OPENROUTER_API_KEY` must be set in `.env` locally, or as a GitHub Secret
for the workflow.

## Testing philosophy

We test **rules that can regress**, not plumbing. Good coverage on: LLM
cascade, feed structure, storage invariants, retry state machine. Skipped:
CLI wiring (trivial),
logging setup (no logic), full mocked `run_cycle()`. Real Actions runs catch
integration bugs (like the two we already hit: wrong sort key, broken
markdown rendering) better than mocks ever would.

Don't chase 100% coverage. A test that is hard to write is often a test of
plumbing.
