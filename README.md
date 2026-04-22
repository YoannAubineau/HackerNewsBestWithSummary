# Hacker News Best with summaries

[![CI](https://img.shields.io/github/actions/workflow/status/YoannAubineau/HackerNewsBestWithSummary/ci.yml?label=CI)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/ci.yml)
[![Last feed refresh](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YoannAubineau/HackerNewsBestWithSummary/main/docs/last-refresh.json)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/cycle.yml)
[![Total LLM cost](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YoannAubineau/HackerNewsBestWithSummary/main/docs/llm-cost.json)](#llm-cost-supported-by-the-author)

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with LLM-generated content:

- a rewritten, factual title (clickbait headlines are replaced by what the article actually says)
- a summary of the linked article
- a synthesis of the main pro / con arguments from the Hacker News discussion

The generated feed is a static RSS 2.0 file, updated hourly by GitHub Actions and served through GitHub Pages.

## Subscribe

Feed URL (French summaries):

<https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml>

Opening the feed URL in a browser renders a styled page via an embedded
XSLT stylesheet; RSS readers receive the same file as plain RSS 2.0.

## LLM Cost Supported by the Author

Daily spend on OpenRouter over the last 30 days. Refreshed each hour by the cycle workflow.

These costs cover the LLM calls used to rephrase titles, summarize articles,
and analyze Hacker News discussions.

![Daily OpenRouter spend over the last 30 days](docs/usage-chart.svg)

If the feed is useful to you, you can chip in via
[Buy Me a Coffee](https://buymeacoffee.com/yoannaubineau) — every cup
keeps the LLM bills covered.

## Set up your own instance using Github Pages

The project is MIT-licensed; feel free to fork it and run a copy under your
own Pages URL — useful if you want summaries in a different language or
from a different Hacker News feed (`newest`, `show`, `ask`, a tag-specific
one, etc.). Step-by-step instructions, including how to swap the source
feed or translate the output, are in
[docs/SELF_HOSTING.md](docs/SELF_HOSTING.md).

## Development

Running the pipeline locally, testing without spending LLM credits, and
the full list of environment variables are in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Architecture

A five-stage hourly pipeline writes one Markdown file per article under
`artefacts/articles/YYYY/MM/DD/` and regenerates `feed.fr.xml`. No
database, no backend — git is the data layer, GitHub Pages is the CDN.
Full breakdown of the pipeline stages, storage layout, dependencies,
and external services in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## License

MIT — see [LICENSE](LICENSE).
