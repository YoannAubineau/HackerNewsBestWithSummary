# Hacker News Best with summaries

[![CI](https://img.shields.io/github/actions/workflow/status/YoannAubineau/HackerNewsBestWithSummary/ci.yml?label=CI)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/ci.yml)
[![Last feed refresh](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/YoannAubineau/HackerNewsBestWithSummary/main/docs/last-refresh.json)](https://github.com/YoannAubineau/HackerNewsBestWithSummary/actions/workflows/cycle.yml)
[![License: MIT](https://img.shields.io/github/license/YoannAubineau/HackerNewsBestWithSummary)](LICENSE)

Republishes the [Hacker News Best](https://hnrss.org/best) feed, enriched with LLM-generated content:

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

Daily spend on OpenRouter over the last 30 days. Refreshed each hour by the cycle workflow.

These costs cover the LLM calls used to rephrase titles, summarize articles,
and analyze Hacker News discussions.

![Daily OpenRouter spend over the last 30 days](docs/usage-chart.svg)

## Set up your own instance using Github Pages

The project is MIT-licensed; feel free to fork it and run a copy under your
own Pages URL — useful if you want summaries in a different language or
from a different Hacker News feed (`newest`, `show`, `ask`, a tag-specific
one, etc.).

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

### Overriding configuration in the workflow

Most of the settings listed in
[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md#configuration) can be overridden
without touching the code, by adding lines to the `env:` block of the
`Run cycle` step in `.github/workflows/cycle.yml`:

```yaml
      - name: Run cycle
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          SOURCE_FEED_URL: https://hnrss.org/newest
          CHANNEL_SITE_URL: https://news.ycombinator.com/newest
```

### Use a different Hacker News feed

Set `SOURCE_FEED_URL` to any feed served by [hnrss.org](https://hnrss.org),
for example `https://hnrss.org/newest`, `/ask`, `/show`, `/frontpage`, or
a tag/keyword query like `https://hnrss.org/newest?q=rust`.

You should also update `CHANNEL_SITE_URL` to the matching HN page (e.g.
`https://news.ycombinator.com/newest`): it is emitted as the channel's
`<link>`, and RSS readers fetch that page to extract its favicon as the
feed's icon.

### Translate the output into a different language

The summaries are in French because the prompts are. Switching language
requires two small code edits:

1. In `src/app/summarize.py`, rewrite `_ARTICLE_SYSTEM` and
   `_DISCUSSION_SYSTEM` to instruct the model in your target language,
   and update the section headings (`## Titre`, `## Résumé`,
   `Confirmations`, `Réfutations`) to match.
2. In `src/app/publish.py`, replace `fg.language("fr")` with your
   [RFC 5646](https://www.rfc-editor.org/rfc/rfc5646) language tag
   (`"en"`, `"es"`, `"de"`, …).

You will probably also want to override `FEED_TITLE`, `FEED_DESCRIPTION`,
and `FEED_SELF_URL` (the default filename is `feed.fr.xml`) so the feed's
metadata matches the new language.

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
