# Hacker News Best with summaries

[![CI](https://img.shields.io/github/actions/workflow/status/YoannAubineau/HackerNewsBestWithSummary/ci.yml?label=CI)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/ci.yml)
[![Feed Refresh](https://img.shields.io/github/actions/workflow/status/YoannAubineau/HackerNewsBestWithSummary/cycle.yml?label=Feed%20Refresh)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/cycle.yml)
[![License: MIT](https://img.shields.io/github/license/YoannAubineau/HackerNewsBestWithSummary)](LICENSE)

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with:

- a rewritten, factual title (clickbait headlines are replaced by what the article actually says)
- a summary of the linked article
- a synthesis of the main pro / con arguments from the Hacker News discussion

The generated feed is a static RSS 2.0 file, updated hourly by GitHub Actions and served through GitHub Pages.

## Subscribe

Feed URL (French summaries):

<https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml>

## Preview

Opening the feed URL in a browser renders a styled page via an embedded
XSLT stylesheet; RSS readers receive the same file as plain RSS 2.0.

![Screenshot of the XSLT-rendered feed](docs/feed-preview.png)

## LLM Cost Supported by the Author

![Daily OpenRouter spend over the last 30 days](docs/usage-chart.svg)

Daily spend on OpenRouter over the last 30 days. Refreshed each hour by the cycle workflow.

## Set up your own instance using Github Pages

The project is MIT-licensed; feel free to fork it and run a copy under your
own Pages URL.

1. **Fork the repository** on GitHub.
2. **Create an OpenRouter account** at <https://openrouter.ai> and generate
   an API key. Add a few dollars of credit (or restrict yourself to the
   free-tier fallback models by setting `OPENROUTER_MODEL` to one of them).
3. **Add the API key as a GitHub Secret** named `OPENROUTER_API_KEY`
   under *Settings → Secrets and variables → Actions → New repository secret*.
4. **Switch GitHub Pages to workflow deployment**: *Settings → Pages →
   Build and deployment → Source: **GitHub Actions***.
5. **Trigger the Feed Refresh workflow once** (*Actions → Feed Refresh → Run workflow*)
   so the initial feed is built and deployed. The hourly cron takes over
   after that.

Estimated runtime cost at the default configuration: roughly **US$10–15 per
month** in OpenRouter credits (Claude Haiku 4.5 at ~10 new HN Best articles
per day). Free-tier fallback models remain available at zero cost if
OpenRouter rate-limits the primary.

## Run locally

### Prerequisites

- **uv** (Astral) — one-shot install: `curl -LsSf https://astral.sh/uv/install.sh | sh` (or `brew install uv`). Handles Python install, virtualenv, and deps.
- **xmllint** — ships with macOS; on Debian/Ubuntu `apt install libxml2-utils`. Only needed for the optional validation step below.
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

`file://` URLs don't apply the XSLT stylesheet reliably — serve the
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

### Tests and lint

```bash
uv run pytest                          # full suite (~90 tests)
uv run ruff check src/ tests/          # lint
uv run ruff format src/ tests/         # auto-format
```

### Git hygiene after a local run

`uv run app cycle` writes new files under `artefacts/` that show up in
`git status`. On a fork you probably don't want to commit those — they
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
| `FEED_ITEMS_LIMIT` | `200` | Maximum items kept in the output feed. |
| `FEED_TTL_MINUTES` | `15` | `<ttl>` advertised to polite readers — minimum polling interval in minutes. |
| `FEED_TITLE` | `Hacker News: Best, with Summary` | Channel `<title>`. |
| `FEED_DESCRIPTION` | (see `config.py`) | Channel `<description>`. |
| `CHANNEL_SITE_URL` | `https://news.ycombinator.com/best` | URL used for the channel's plain `<link>`. Readers resolve the feed's icon from this page's favicon. |
| `DISCUSSION_BUDGET` | `500` | Max number of HN comments sent to the LLM. Split recursively across root threads, decreasing by rank. |
| `LLM_SLEEP_SECONDS` | `3.0` | Pause between two LLM calls to stay under rate limits. |
| `HTTP_TIMEOUT` | `20.0` | Timeout in seconds for outbound HTTP calls. |
| `MAX_ATTEMPTS` | `3` | How many cycles an article may fail in a row before being moved to `_failed/`. |
| `USER_AGENT` | `hn-best-summary/0.1 (+...)` | Sent with every outbound HTTP request. |
| `ARTEFACTS_DIR` | `artefacts` | Root of all generated output. Article store, failed-article subfolder, and the feed file are all derived from this path. |
| `LOG_LEVEL` | `INFO` | One of `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |

## Architecture and toolchain

A five-stage hourly pipeline writes one Markdown file per article under
`artefacts/articles/YYYY/MM/DD/` and regenerates `feed.fr.xml`. No
database, no backend — git is the data layer, GitHub Pages is the CDN.
Full breakdown of the pipeline stages, storage layout, dependencies,
and external services in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## License

MIT — see [LICENSE](LICENSE).
