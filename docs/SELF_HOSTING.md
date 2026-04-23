# Set up your own instance using GitHub Pages

The project is MIT-licensed. Feel free to fork it and run a copy under your
own Pages URL if you want summaries in a different language, or from a
different Hacker News feed (`newest`, `show`, `ask`, a tag-specific one,
etc.).

1. **Fork the repository** on GitHub.
2. **Create an OpenRouter account** at <https://openrouter.ai> and generate
   an API key. Add a few dollars of credit (or restrict yourself to the
   free-tier fallback models by setting `OPENROUTER_MODEL` to one of them).
3. **Add the API key as a GitHub Secret** named `OPENROUTER_API_KEY`
   under *Settings → Secrets and variables → Actions → New repository secret*.
4. **(Optional) Add Webshare proxy secrets** `WEBSHARE_PROXY_USERNAME` and
   `WEBSHARE_PROXY_PASSWORD` if you want article summaries for YouTube
   videos. YouTube blocks datacenter IPs including GitHub Actions runners,
   so the transcript path needs a residential proxy to work from CI. See
   the [YouTube transcript support](#youtube-transcript-support) section
   below for the full picture. Without these secrets the pipeline still
   works, videos just fall back to the feed's own summary.
5. **Switch GitHub Pages to workflow deployment**: *Settings → Pages →
   Build and deployment → Source: **GitHub Actions***.
6. **Trigger the Feed Refresh workflow once** (*Actions → Feed Refresh → Run workflow*)
   so the initial feed is built and deployed. The hourly cron takes over
   after that.

Estimated runtime cost at the default configuration: roughly **US$10–15 per
month** in OpenRouter credits (Claude Haiku 4.5 at ~10 new HN Best articles
per day). Free-tier fallback models remain available at zero cost if
OpenRouter rate-limits the primary.

## Overriding configuration in the workflow

Most of the settings listed in
[DEVELOPMENT.md](DEVELOPMENT.md#configuration) can be overridden
without touching the code, by adding lines to the `env:` block of the
`Run cycle` step in `.github/workflows/cycle.yml`:

```yaml
      - name: Run cycle
        env:
          OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
          SOURCE_FEED_URL: https://hnrss.org/newest
          CHANNEL_SITE_URL: https://news.ycombinator.com/newest
```

## Use a different Hacker News feed

Set `SOURCE_FEED_URL` to any feed served by [hnrss.org](https://hnrss.org),
for example `https://hnrss.org/newest`, `/ask`, `/show`, `/frontpage`, or
a tag/keyword query like `https://hnrss.org/newest?q=rust`.

You should also update `CHANNEL_SITE_URL` to the matching HN page (e.g.
`https://news.ycombinator.com/newest`): it is emitted as the channel's
`<link>`, and RSS readers fetch that page to extract its favicon as the
feed's icon.

## Translate the output into a different language

The summaries are in French because the prompts are. Switching language
requires two small code edits:

1. In `src/app/summarize.py`, rewrite `_ARTICLE_SYSTEM`,
   `_DISCUSSION_SYSTEM`, and `_TITLE_TRANSLATION_SYSTEM` to instruct the
   model in your target language, and update the section headings
   (`## Titre`, `## Résumé`, `Avis positifs`, `Avis négatifs`) plus the
   `(no content)` placeholder in `src/app/pipeline.py` to match.
2. In `src/app/publish.py`, replace `fg.language("fr")` with your
   [RFC 5646](https://www.rfc-editor.org/rfc/rfc5646) language tag
   (`"en"`, `"es"`, `"de"`, …).

You will probably also want to override `FEED_TITLE`, `FEED_DESCRIPTION`,
and `FEED_SELF_URL` (the default filename is `feed.fr.xml`) so the feed's
metadata matches the new language.

## YouTube transcript support

When an HN story links to a YouTube video, the pipeline tries to pull
the video transcript via `youtube-transcript-api` and summarise that,
rather than falling back to the hnrss blurb. YouTube blocks requests
from cloud-provider IP ranges, which includes every GitHub Actions
runner, so this path only works from CI when routed through a
residential proxy.

The project is wired for [Webshare](https://www.webshare.io/) residential
proxies specifically. To enable it:

1. Create a Webshare account and purchase a **"Residential"** plan. Do
   **not** pick "Proxy Server" (datacenter) or "Static Residential", both
   are rejected by this endpoint.
2. Open <https://dashboard.webshare.io/proxy/settings> and copy the
   *Proxy Username* and *Proxy Password* (these are distinct from the
   account login).
3. Add them as GitHub Secrets named `WEBSHARE_PROXY_USERNAME` and
   `WEBSHARE_PROXY_PASSWORD` under *Settings → Secrets and variables →
   Actions*.

The cycle workflow forwards both values to `uv run app cycle` as
environment variables. When either is missing, the transcript request
goes out directly, which is fine from a home IP but guaranteed to fail
from a runner. A YouTube video that can't be transcribed still gets an
entry in the feed, just with the generic feed-summary text and the
YouTube thumbnail.
