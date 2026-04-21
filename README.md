# Hacker News Best — with summaries

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with:

- a rewritten, factual title (clickbait headlines are replaced by what the article actually says)
- a summary of the linked article
- a synthesis of the main pro / con arguments from the Hacker News discussion

The generated feed is a static RSS 2.0 file, updated hourly by GitHub Actions and served through GitHub Pages.

## Run locally

```bash
uv sync
cp .env.example .env                    # then set OPENROUTER_API_KEY
uv run app cycle
xmllint --noout artefacts/feed.xml      # validation
```

Individual steps for debugging: `app fetch-feed`, `app fetch-articles`, `app fetch-discussions`, `app summarize`, `app publish`.

## Architecture

- Input: `https://hnrss.org/best`
- Storage: one Markdown file per article in `artefacts/articles/YYYY/MM/DD/{short_hash}.md`
- LLM: OpenRouter with cascading fallback (Claude Haiku 4.5 primary, then free-tier models)
- HN discussion: Algolia HN API `https://hn.algolia.com/api/v1/items/{id}`
- Output: `artefacts/feed.xml` — `<link>` points at the original article, `<comments>` at the HN discussion. The `artefacts/` folder is what GitHub Pages actually serves, so the feed's public URL is just `.../feed.xml`.

Raw article HTML is never committed (copyright and repo size). Only the two summaries and metadata are.

Title rewriting and article summarization share a single LLM call — no extra cost.
