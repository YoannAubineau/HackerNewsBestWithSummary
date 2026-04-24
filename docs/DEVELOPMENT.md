# Development

How to run the pipeline locally and which environment variables steer it.

## Run locally

### Prerequisites

- **uv** (Astral), one-shot install: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`). Handles Python install, virtualenv, and deps.
- **xmllint**, ships with macOS. On Debian/Ubuntu `apt install libxml2-utils`. Only needed for the optional validation step below.
- An **OpenRouter API key**. Create a free account at <https://openrouter.ai>, generate a key (format `sk-or-v1-…`), and add a few dollars of credit if you want to use the paid primary model. Purely free-tier usage is possible by setting `OPENROUTER_MODEL` to one of the fallbacks (e.g. `meta-llama/llama-3.3-70b-instruct:free`).

### Setup

```bash
uv sync                      # install runtime + dev deps, matches uv.lock
cp .env.example .env         # then edit: OPENROUTER_API_KEY=sk-or-v1-...
```

### Run the full pipeline

```bash
uv run app cycle
```

Fetches new HN Best articles, extracts their content, pulls the HN
discussion, summarizes both via the LLM, regenerates
`artefacts/feed.fr.xml`. First run ingests ~30 articles at once, which
costs roughly **US$1–2** on Claude Haiku 4.5. Each later run only
processes genuinely new entries (typically 0–2 per hour).

### Inspect the generated feed in a browser

`file://` URLs don't apply the XSLT stylesheet reliably, so serve the
folder over HTTP:

```bash
python -m http.server --directory artefacts 8000
# then open http://localhost:8000/feed.fr.xml
```

Validate the XML separately with `xmllint --noout artefacts/feed.fr.xml`.

### Work without spending LLM credits

Every pipeline step except `summarize` is free to call. Use a dummy
key to explore intermediate state:

```bash
OPENROUTER_API_KEY=dummy uv run app fetch-feed         # step 1: RSS → pending files
OPENROUTER_API_KEY=dummy uv run app fetch-articles     # step 2: HTTP + trafilatura
OPENROUTER_API_KEY=dummy uv run app fetch-discussions  # step 3: Algolia HN API
# step 4 (summarize) needs a real key
OPENROUTER_API_KEY=dummy uv run app publish            # step 5: regenerate feed.fr.xml
```

### Keep the primary LLM current

`OPENROUTER_MODEL` points at a floating alias (no date suffix), so
point-releases of the same version line roll in automatically. Newer
generations (e.g. Haiku 5, Sonnet 5) do not, because the family version
is part of the slug. Run:

```bash
uv run app check-llm-versions
```

The command queries OpenRouter's `/models` endpoint and exits 2 when a
newer version of the configured family is published, printing the
candidate slugs. Exit 0 means the current model is still the newest in
its family. Any other exit code means the check itself failed (typically
an HTTP error against OpenRouter). In CI,
`.github/workflows/check-llm-versions.yml` runs it every Monday, opens a
tracking issue labelled `llm-model-update` when a bump is available, and
opens a separate issue labelled `check-llm-versions-failure` when the
workflow itself fails. The code change to bump the model stays manual
(edit `openrouter_model` in `src/app/config.py` after sanity-checking
the output quality).

### Tests and lint

```bash
uv run pytest                          # full suite (~125 tests)
uv run ruff check src/ tests/          # lint
uv run ruff format src/ tests/         # auto-format
```

### Git hygiene after a local run

`uv run app cycle` writes new files under `artefacts/` that show up in
`git status`. On a fork you probably don't want to commit those. They
are produced again on every GitHub Actions cycle. If you're just
experimenting, either reset with `git checkout artefacts/` or ignore
the folder locally.

## Configuration

All settings are read from environment variables (locally from `.env`, in CI
from GitHub Secrets / workflow `env:`). Every value has a sensible default
except `OPENROUTER_API_KEY`.

| Variable | Default | Purpose |
|---|---|---|
| `OPENROUTER_API_KEY` | *required* | Auth token for OpenRouter. |
| `OPENROUTER_MODEL` | `anthropic/claude-haiku-4.5` | Primary LLM called for each summary. |
| `OPENROUTER_FALLBACK_MODELS` | `nvidia/nemotron-3-super-120b-a12b:free, meta-llama/llama-3.3-70b-instruct:free` | Comma-separated list of free fallbacks tried in order when the primary 429/5xx/empties. |
| `SOURCE_FEED_URL` | `https://hnrss.org/best` | Upstream RSS feed polled each cycle. |
| `FEED_SELF_URL` | `http://localhost/feed.fr.xml` | URL used for `<atom:link rel="self">`. Set to the public Pages URL in CI. |
| `FEED_ITEMS_LIMIT` | `100` | Maximum items kept in the output feed. |
| `FEED_TTL_MINUTES` | `15` | `<ttl>` advertised to polite readers. Minimum polling interval in minutes. |
| `FEED_TITLE` | `Hacker News: Best, with Summary` | Channel `<title>`. |
| `FEED_DESCRIPTION` | (see `config.py`) | Channel `<description>`. |
| `CHANNEL_SITE_URL` | `https://news.ycombinator.com/best` | URL used for the channel's plain `<link>`. Readers resolve the feed's icon from this page's favicon. |
| `DISCUSSION_BUDGET` | `500` | Max number of HN comments sent to the LLM. Split recursively across root threads, decreasing by rank. |
| `LLM_SLEEP_SECONDS` | `3.0` | Pause between two LLM calls to stay under rate limits. |
| `HTTP_TIMEOUT` | `20.0` | Timeout in seconds for outbound HTTP calls. |
| `MAX_ATTEMPTS` | `3` | How many cycles an article may fail in a row before being moved to `_failed/`. |
| `DAILY_COST_LIMIT_USD` | `2.0` | Circuit breaker. When today's OpenRouter spend exceeds this value, `step_summarize` skips for the rest of the cycle. Set to `0` to disable. |
| `USER_AGENT` | `hn-best-summary/0.1 (+...)` | Sent with every outbound HTTP request. |
| `ARTEFACTS_DIR` | `artefacts` | Root of all generated output. Article store, failed-article subfolder, and the feed file are all derived from this path. |
| `WEBSHARE_PROXY_USERNAME` | *unset* | Optional. Proxy Username from <https://dashboard.webshare.io/proxy/settings> (Residential plan only). When set together with `WEBSHARE_PROXY_PASSWORD`, YouTube transcript requests tunnel through Webshare's rotating residential pool. Required from GitHub Actions, whose datacenter IPs YouTube blocks. Ignored locally unless your own IP is blocked. |
| `WEBSHARE_PROXY_PASSWORD` | *unset* | Optional. Proxy Password paired with `WEBSHARE_PROXY_USERNAME`. Both must be set for the proxy to be used. |
| `LOG_LEVEL` | `INFO` | One of `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |

## Comment selection budget

A popular HN thread has hundreds to thousands of comments, too many to
cram into a single LLM prompt, and most of them are short reactions that
add little to a synthesis. `fetch_discussion.py` therefore walks the tree
and picks a bounded subset before calling the model.

### Rules

1. **Leaves are dropped.** A comment with no reply is considered
   low-signal and is never included, unless it is pinned (see 3).
2. **Each included comment costs 1 unit of budget.** The starting budget
   is `DISCUSSION_BUDGET` (default 500).
3. **Submitter comments are pinned.** Any comment whose author matches
   the story submitter is always included, along with every ancestor up
   to the root. Pinned comments don't consume the budget, since they are
   kept for their clarifying value and would otherwise be easy to miss.
4. **Remaining budget is split triangularly across children, by HN
   rank.** At any level, non-pinned "branch" children (those with at
   least one reply of their own) receive allocations weighted
   `n, n-1, …, 1`. The top-ranked thread gets the largest slice, the
   next a bit less, and so on. Children with no budget are skipped.
5. **Recursion.** Each included comment walks into its own children
   with `budget - 1`, applying the same triangular split one level
   deeper. The tree thins out naturally as depth increases.

Allocations are a **ceiling, not a target**. Unused budget from a
sub-thread that turns out to be shorter than expected is not
redistributed to its siblings. The real number of comments emitted can
therefore be less than `DISCUSSION_BUDGET`. Redistributing would take a
second pass over the tree for marginal gain. When the budget overflows
the tree, there was already enough room for every qualifying comment.

### Why these rules

- **Budget cap** keeps prompt size (and therefore latency and cost)
  predictable regardless of how viral a thread goes.
- **Triangular split** reflects HN's own ranking signal: top threads
  tend to carry the most informative exchanges, so they deserve a
  bigger share of the context window.
- **Leaf drop** filters out pure reactions and ack-only replies.
- **Submitter pinning** preserves the single most authoritative voice
  in the thread (the poster's own clarifications and rebuttals).

### Tuning

Raising `DISCUSSION_BUDGET` lets the model see more of the deep
sub-threads but inflates the prompt and the per-call cost. Lowering it
tightens the focus on the top-ranked exchanges. 500 was chosen so that
a typical front-page thread fits comfortably in a Haiku 4.5 context
window without dominating it.
