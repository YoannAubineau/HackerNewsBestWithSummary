# Discussion refresh against Feedly

How the pipeline keeps the HN discussion synthesis fresh until Feedly
crawls the article, and how to keep the Feedly developer token alive.

## What it does

Once an article is `SUMMARIZED`, its body is normally frozen for the
rest of its life in the feed. But a HN discussion keeps growing for
hours after submission, and Feedly typically does not crawl our feed
for 15 minutes to 1 hour after we publish (median lag observed via
`feedly-lag` is around 25 minutes, max around 1 hour for the current
Feedly tier).

`step_refresh_discussions` exploits that window. On every cycle, it
asks Feedly which articles it already has in its store, and for each
locally `SUMMARIZED` article that Feedly has not yet ingested, it
re-fetches the HN discussion and re-runs the discussion-only LLM call
to refresh:

- the "Avis positifs" / "Avis négatifs" synthesis,
- the "Top commentaires" block (top 3 by HN's own ranking),
- the comment count in the section heading.

The article summary itself (the `## Résumé de l'article` section) is
left untouched. The new discussion section is spliced into the
existing body via a regex anchored on the structure produced by
`compose_body`.

## Where it runs

### In the cycle

`run_cycle()` calls the step between `step_summarize` and `step_publish`:

```text
fetch_feed -> fetch_discussions -> fetch_articles -> summarize
            -> refresh_discussions -> publish
```

A `cycle_started_at` timestamp is captured at the start of the cycle
and passed to the step, so articles summarized in the current cycle
(which have not yet been through `publish`, and which Feedly therefore
cannot have seen) are skipped. This gate is duration-free, so it
remains correct if the cron cadence ever changes from hourly to 15 min
or anything else.

### As a one-off command

```bash
uv run app refresh-discussions
```

The CLI command calls `step_refresh_discussions(now)` with the current
time, which trivially passes the same-cycle gate (no article was
summarized in the future), so all `SUMMARIZED` articles within the
24 h window are candidates.

## Gates and short-circuits

The step is conservative on purpose. It returns 0 (no work done)
when any of these conditions hit:

| Condition | Behavior |
|-----------|----------|
| `FEEDLY_DEV_TOKEN` env var is empty | Whole step skipped, log `refresh_discussions_skipped_no_token` |
| `today_spend() >= daily_cost_limit_usd` | Whole step skipped, log `refresh_discussions_cost_breaker` |
| `fetch_feedly_origin_ids()` returns `None` (auth or HTTP failure) | Whole step skipped, log `refresh_discussions_skipped_feedly_unavailable`. Treating an unknown Feedly state as "missing from Feedly" would burn LLM calls for nothing during a Feedly outage. |

Per-article gates (the loop continues with the next article):

| Condition | Behavior |
|-----------|----------|
| `our_published_at` older than 24 h | Loop breaks (iter is newest-first, the rest is even older) |
| `summarized_at >= cycle_started_at` | Skip (same-cycle, not yet published) |
| `originId` already in Feedly's stream | Skip (Feedly has it, refresh would be invisible) |
| `fetch_discussion()` returns `None` or a dupe pointer | Skip with log |
| `comment_count < min_discussion_comments` | Skip with log |
| Discussion section not found in body | Skip with log `refresh_discussion_splice_missed` |
| LLM error (`AllModelsFailedError`, `LLMError`) | Skip with log, **no `_failed/` move** (a failed refresh must not destroy a working summary) |

The cost breaker is also re-checked after each successful refresh, so
the loop bails out gracefully if the daily limit gets hit mid-run.

## The Feedly developer token

The whole feature depends on `FEEDLY_DEV_TOKEN`, an OAuth-style token
that authorizes calls to Feedly Cloud's `/v3/streams/contents`
endpoint for the feed the user is subscribed to.

### Generating a token

1. Sign in to Feedly with the account that subscribes to
   `feed.fr.xml` (the feed must be in that account's subscriptions,
   otherwise the API returns an empty `items` list).
2. Open <https://feedly.com/v3/auth/dev>.
3. Click "Generate token".
4. The page returns two values, `access_token` and `refresh_token`.
   We use the `access_token` only. The `refresh_token` is for
   automated refresh flows we do not implement (overkill for a
   diagnostic-grade feature).

Feedly developer tokens expire. They are typically valid for around
one month. When the token expires, Feedly returns HTTP 401 or 403,
and the pipeline logs it cleanly without crashing, but the refresh
step becomes a no-op until the token is replaced.

### Local setup

Add the token to `.env` next to `OPENROUTER_API_KEY`:

```bash
FEEDLY_DEV_TOKEN=A0123...
```

Verify with the diagnostic command, which uses the same endpoint:

```bash
uv run app feedly-lag --feed-url https://yoannaubineau.github.io/HackerNewsBestWithSummary/feed.fr.xml
```

A successful run prints a table with one row per matched article and
the lag stats. A 401 means the token is rejected (regenerate it). An
empty result means the token is valid but Feedly does not subscribe
to the URL passed in `--feed-url` (check the URL).

### GitHub Actions setup

Two pieces are needed for the feature to actually run on GitHub:

1. **Repository secret**. In GitHub, go to Settings -> Secrets and
   variables -> Actions -> New repository secret. Name it
   `FEEDLY_DEV_TOKEN`, paste the `access_token` value.

2. **Workflow plumbing**. Add the secret to the env block of the
   "Run cycle" step in `.github/workflows/cycle.yml`:

   ```yaml
   - name: Run cycle
     id: cycle
     env:
       OPENROUTER_API_KEY: ${{ secrets.OPENROUTER_API_KEY }}
       WEBSHARE_PROXY_USERNAME: ${{ secrets.WEBSHARE_PROXY_USERNAME }}
       WEBSHARE_PROXY_PASSWORD: ${{ secrets.WEBSHARE_PROXY_PASSWORD }}
       FEEDLY_DEV_TOKEN: ${{ secrets.FEEDLY_DEV_TOKEN }}
     run: |
       ...
   ```

   Without that line, the secret exists but is invisible to the job,
   and the step silently no-ops every hour.

### Renewing the token

When the daily cycle starts logging
`feedly_origin_ids_auth_failed error='HTTP 401'` (or 403), the token
has expired. The renewal procedure is:

1. Generate a fresh token at <https://feedly.com/v3/auth/dev>.
2. Replace the value locally in `.env` (so the diagnostic
   `feedly-lag` keeps working from your laptop).
3. Replace the value in the GitHub repository secret. Settings ->
   Secrets and variables -> Actions -> `FEEDLY_DEV_TOKEN` -> Update.
   The next scheduled cycle picks up the new value automatically. No
   workflow change, no redeploy.

The `refresh_token` value Feedly hands out alongside the access token
could in principle be exchanged for a fresh access token without
revisiting the dev page. We deliberately do not automate that. The
manual flow takes 30 seconds once a month, and the implementation
cost of automating it (storing two secrets, handling token rotation,
catching refresh-failure modes) is not worth it.

## Cost considerations

Each refresh is one LLM call (the discussion synthesis) on the
configured `openrouter_model` (Claude Haiku 4.5 by default). Typical
cost per refresh, around 0.001 to 0.003 USD.

At hourly cadence, expect 5 to 15 refreshable articles per cycle and
a daily cost in the 0.10 to 1.20 USD range, well under the
`daily_cost_limit_usd` of 2.0. The cost breaker is the safety net.

At 15-minute cadence, the daily cost does not multiply by 4, because
the gate "Feedly already has this article" trips quickly once Feedly
catches up. A given article gets refreshed 1 to 3 times in its life.
Expected daily cost in the 0.20 to 3.60 USD range. May brush against
the 2.0 USD limit, in which case either raise
`daily_cost_limit_usd` or shorten the 24 h window in
`refresh_discussions._MAX_AGE`.

## Diagnostics

`uv run app feedly-lag` is the companion diagnostic. It prints a
table of `(crawled_at, our_published_at, delta, title)` rows for the
50 most recent items Feedly knows about, plus min, median, mean, max
of the lag. Useful to confirm the Feedly subscription is healthy and
that the lag stays in the expected range.

The pipeline writes these structured log events when running on
GitHub Actions. Any of them can be greppped from the run log:

| Event | Meaning |
|-------|---------|
| `refresh_discussions` (with `processed=N`) | Step finished, N articles refreshed |
| `refresh_discussions_skipped_no_token` | Whole step skipped, no token |
| `refresh_discussions_skipped_feedly_unavailable` | Whole step skipped, Feedly call failed |
| `refresh_discussions_cost_breaker` | Whole step skipped, daily cost limit hit |
| `refresh_discussion_done` | One article was successfully refreshed |
| `refresh_discussion_skipped_same_cycle` | Article was summarized in the current cycle |
| `refresh_discussion_skipped_dupe` | Discussion is now flagged as a HN dupe |
| `refresh_discussion_skipped_thin` | Discussion is below the comment threshold |
| `refresh_discussion_splice_missed` | Body did not match the expected structure |
| `refresh_discussion_fetch_failed` | Algolia returned nothing for the HN id |
| `refresh_discussion_llm_failed` | All LLM models failed for that article |
| `feedly_origin_ids_auth_failed` | Feedly rejected the token (renew it) |
| `feedly_origin_ids_http_failed` | Network or 5xx talking to Feedly |
