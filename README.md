# Hacker News Best with summaries

[![CI](https://img.shields.io/github/actions/workflow/status/YoannAubineau/HackerNewsBestWithSummary/ci.yml?label=CI)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/ci.yml)
[![Last feed refresh](https://img.shields.io/endpoint?url=https://yoannaubineau.github.io/HackerNewsBestWithSummary/last-refresh.json)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/cycle.yml)
[![Total LLM cost](https://img.shields.io/endpoint?url=https://yoannaubineau.github.io/HackerNewsBestWithSummary/llm-cost.json)](#llm-cost-supported-by-the-author)
[![Sponsors](https://img.shields.io/github/sponsors/YoannAubineau?label=Sponsors&color=blueviolet)](https://github.com/sponsors/YoannAubineau)

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with LLM-generated content:

- a rewritten, factual title (clickbait headlines are replaced by what the article actually says)
- a summary of the linked article, or of the linked video's transcript when the URL points to YouTube
- a synthesis of the main pro / con arguments from the Hacker News discussion

The generated feed is a static RSS 2.0 file, updated hourly by GitHub Actions and served through GitHub Pages.

## Usage

Paste the URL below into your RSS reader to subscribe:

<https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml>

Opening the feed URL in a browser renders a styled page via an embedded
XSLT stylesheet. RSS readers receive the same file as plain RSS 2.0.

Older articles that have rotated out of the feed's 100-item window are
still reachable on the
[archive page](https://yoannaubineau.github.io/HackerNewsBestWithSummary/archive.html),
which is sortable by HN submission date, first appearance in `/best`, or
entry into this feed.

For the moment, this feed is only available in French.
[Open an issue](https://github.com/YoannAubineau/HackerNewsBestWithSummary/issues)
if you'd like to see another language supported.

## LLM Cost Supported by the Author

Daily spend on OpenRouter over the last 30 days. Refreshed each hour by the cycle workflow.

![Daily OpenRouter spend over the last 30 days](https://yoannaubineau.github.io/HackerNewsBestWithSummary/usage-chart.svg)

These costs cover the LLM calls used to rephrase titles, summarize articles,
and analyze Hacker News discussions.

If the feed is useful to you, you can chip in via
[GitHub Sponsors](https://github.com/sponsors/YoannAubineau).
Every contribution keeps the LLM bills covered.

## Set up your own instance using Github Pages

The project is MIT-licensed. Feel free to fork it and run a copy under your
own Pages URL if you want summaries in a different language, or from a
different Hacker News feed (`newest`, `show`, `ask`, a tag-specific one,
etc.). Step-by-step instructions, including how to swap the source feed
or translate the output, are in
[docs/SELF_HOSTING.md](docs/SELF_HOSTING.md).

## Development

Running the pipeline locally, testing without spending LLM credits, and
the full list of environment variables are in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md).

## Architecture

A five-stage hourly pipeline writes one Markdown file per article under
`artefacts/articles/YYYY/MM/DD/` and regenerates `feed.fr.xml`. No
database, no backend. Git is the data layer, GitHub Pages is the CDN.
Full breakdown of the pipeline stages, storage layout, dependencies,
and external services in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## License

MIT, see [LICENSE](LICENSE).
