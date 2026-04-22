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

These costs cover the LLM calls used to rephrase each title, summarize the
article, and analyze the Hacker News discussion.

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

## Development

Running the pipeline locally, testing without spending LLM credits, and
the full list of environment variables are in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Architecture and toolchain

A five-stage hourly pipeline writes one Markdown file per article under
`artefacts/articles/YYYY/MM/DD/` and regenerates `feed.fr.xml`. No
database, no backend — git is the data layer, GitHub Pages is the CDN.
Full breakdown of the pipeline stages, storage layout, dependencies,
and external services in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## License

MIT — see [LICENSE](LICENSE).
