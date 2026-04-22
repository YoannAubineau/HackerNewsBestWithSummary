# Hacker News Best — with summaries

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with:

- a rewritten, factual title (clickbait headlines are replaced by what the article actually says)
- a summary of the linked article
- a synthesis of the main pro / con arguments from the Hacker News discussion

The generated feed is a static RSS 2.0 file, updated hourly by GitHub Actions and served through GitHub Pages.

## Preview

Opening the feed URL in a browser renders a styled page via an embedded
XSLT stylesheet; RSS readers receive the same file as plain RSS 2.0.

![Screenshot of the XSLT-rendered feed](docs/feed-preview.png)

## Subscribe

Feed URL (French summaries):

<https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml>

## Run locally

```bash
uv sync
cp .env.example .env                    # then set OPENROUTER_API_KEY
uv run app cycle
xmllint --noout artefacts/feed.fr.xml   # validation
```

Individual steps for debugging: `app fetch-feed`, `app fetch-articles`, `app fetch-discussions`, `app summarize`, `app publish`.

## Architecture

- Input: `https://hnrss.org/best`
- Storage: one Markdown file per article in `artefacts/articles/YYYY/MM/DD/{short_hash}.md`
- LLM: OpenRouter with cascading fallback (Claude Haiku 4.5 primary, then free-tier models)
- HN discussion: Algolia HN API `https://hn.algolia.com/api/v1/items/{id}`
- Output: `artefacts/feed.fr.xml` — `<link>` points at the original article, `<comments>` at the HN discussion. The `artefacts/` folder is served at the site root by GitHub Pages, so the feed's public URL is `.../feed.fr.xml`. The language suffix leaves room for a future `feed.en.xml`.

Raw article HTML is never committed (copyright and repo size). Only the two summaries and metadata are.

Title rewriting and article summarization share a single LLM call — no extra cost.

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
| `FEED_TITLE` | `Hacker News: Best, with Summary` | Channel `<title>`. |
| `FEED_DESCRIPTION` | (see `config.py`) | Channel `<description>`. |
| `DISCUSSION_BUDGET` | `500` | Max number of HN comments sent to the LLM. Split recursively across root threads, decreasing by rank. |
| `LLM_SLEEP_SECONDS` | `3.0` | Pause between two LLM calls to stay under rate limits. |
| `HTTP_TIMEOUT` | `20.0` | Timeout in seconds for outbound HTTP calls. |
| `MAX_ATTEMPTS` | `3` | How many cycles an article may fail in a row before being moved to `_failed/`. |
| `USER_AGENT` | `hn-best-summary/0.1 (+...)` | Sent with every outbound HTTP request. |
| `ARTICLES_DIR` | `artefacts/articles` | Root of the partitioned article store. |
| `FAILED_DIR` | `artefacts/articles/_failed` | Where articles that exceeded `MAX_ATTEMPTS` move. |
| `FEED_OUTPUT_PATH` | `artefacts/feed.fr.xml` | Output path for the generated feed. |
| `LOG_LEVEL` | `INFO` | One of `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`. |

## Set up your own instance

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
5. **Trigger the cycle workflow once** (*Actions → cycle → Run workflow*)
   so the initial feed is built and deployed. The hourly cron takes over
   after that.

Estimated runtime cost at the default configuration: roughly **US$10–15 per
month** in OpenRouter credits (Claude Haiku 4.5 at ~10 new HN Best articles
per day). Free-tier fallback models remain available at zero cost if
OpenRouter rate-limits the primary.

## Toolchain

### Language and packaging

| Tool | Role |
|---|---|
| **Python 3.12+** | Runtime for the pipeline. |
| **uv** (Astral) | Single binary that handles virtual environments, dependency resolution, Python installation, and script execution. Replaces `pip`, `venv`, and `pyenv`. |
| **pyproject.toml** | Project metadata, runtime and dev dependencies, and configuration for ruff and pytest. |
| **uv.lock** | Deterministic lockfile pinning every transitive dependency. |

### Code quality and tests

| Tool | Role |
|---|---|
| **ruff** (Astral) | Linter and formatter. Replaces flake8, black, isort. |
| **pytest** | Test runner. |
| **pytest-httpx** | Mocks HTTP calls in tests without touching the network. |

### Source control

| Tool | Role |
|---|---|
| **git** | Local version control, history, branching, reverts. |
| **GitHub** | Remote repository, collaboration, releases. |
| **gh** CLI | Scripted access to the GitHub API: workflow runs, PR merges, repo settings. |

### Runtime Python dependencies

| Library | Role |
|---|---|
| **httpx** | HTTP client used for every external call (source feed, articles, Algolia, OpenRouter). |
| **feedparser** | Parses the upstream RSS feed. |
| **trafilatura** | Extracts the main text content from article HTML. |
| **feedgen** | Builds the output RSS XML. |
| **markdown-it-py** | CommonMark renderer converting Markdown bodies to HTML for the feed description. Configured with `html=False` to escape raw HTML in model output. |
| **pydantic** + **pydantic-settings** | Typed data models (`Article`, `AlgoliaItem`) and environment-driven configuration. |
| **typer** | CLI framework backing the `app` command. |
| **tenacity** | Declarative retry with backoff for flaky network calls. |
| **structlog** | Structured logging with key/value pairs surfaced in workflow logs. |
| **python-frontmatter** | Reads and writes Markdown files with YAML frontmatter. |

### External services

| Service | Endpoint | Role |
|---|---|---|
| **hnrss.org** | `https://hnrss.org/best` | Upstream RSS source. |
| **Algolia HN Search API** | `https://hn.algolia.com/api/v1/items/{id}` | Public API returning the full comment tree for an HN item. |
| **OpenRouter** | `https://openrouter.ai/api/v1/chat/completions` | Gateway routing to the configured LLM with cascading fallback between providers. |
| **Anthropic Claude Haiku 4.5** | via OpenRouter | Default LLM used for title rewriting and both summaries. |
| Article publishers | per-article URL | Fetched to extract the article text. |

### Storage

| Choice | Rationale |
|---|---|
| **Filesystem + git** | Articles are Markdown files under `artefacts/articles/YYYY/MM/DD/{short_hash}.md`. Git provides history, idempotency (deterministic filename), and deployment in one. |
| **No database** | Unwarranted at this scale; the repository itself is the data layer. |
| **Gitignored sidecar files** | `.raw.article.txt` and `.raw.discussion.txt` cache raw content between pipeline stages and are never committed. |

### CI/CD

| Component | Role |
|---|---|
| **`.github/workflows/cycle.yml`** | Hourly cron plus manual `workflow_dispatch`. Runs the pipeline end-to-end and deploys to Pages. |
| **`.github/workflows/ci.yml`** | Runs ruff and pytest on every push to `main` and every pull request (skipped for commits that only touch `artefacts/`). |
| **Dependabot** | Weekly batched PRs for Python deps (via `uv`) and GitHub Actions versions; real-time PRs for security advisories. |

### Actions used in the workflows

| Action | Role |
|---|---|
| **`actions/checkout`** | Clones the repository into the runner. |
| **`astral-sh/setup-uv`** | Installs uv and caches its download directory across runs. |
| **`actions/configure-pages`** | Sets up the Pages environment and OIDC token for deployment. |
| **`actions/upload-pages-artifact`** | Packages the `artefacts/` folder as a Pages artifact. |
| **`actions/deploy-pages`** | Publishes the artifact to the Pages CDN. |

### Hosting and delivery

| Component | Role |
|---|---|
| **GitHub Pages** | Static hosting. Serves the contents of `artefacts/` at the site root. |
| **Fastly** | CDN underneath Pages. Handles edge caching and TLS. |

### Browser-side rendering

| Component | Role |
|---|---|
| **`artefacts/feed.xsl`** | XSLT 1.0 stylesheet applied by the browser when the feed URL is opened directly. Transforms the RSS into a styled HTML page. |
| **Browser-native XSLT engine** | Chrome, Firefox, and Safari all implement XSLT 1.0 client-side — no extra runtime required. |
| **Inline CSS** (in the stylesheet) | Light/dark theme via `prefers-color-scheme`, responsive single-column layout. |
| **Inline JavaScript** (in the stylesheet) | Appends the HN item ID to each article footer at render time, without touching the stored body. |

### Secrets

| Secret | Location |
|---|---|
| **`OPENROUTER_API_KEY`** (local) | `.env` at repo root (gitignored). Loaded by `pydantic-settings`. |
| **`OPENROUTER_API_KEY`** (production) | GitHub Secret injected into the cycle workflow as an environment variable. |
| **`GITHUB_TOKEN`** | Provided automatically by GitHub Actions, scoped to `contents: write`, `pages: write`, `id-token: write`. |

## License

MIT — see [LICENSE](LICENSE).
