"""Regenerate ONLY the article-summary block of already-summarized entries
whose article summary is still the "(unable to load content...)" placeholder,
for the ones the current ``fetch_article`` code can now extract.

This is the discussion-preserving cousin of ``app reprocess-placeholders``:
that command resets the whole article and re-runs the full cycle (discussion
re-fetch + re-summarization included); this script re-fetches the article and
re-runs ``summarize_article`` only, then surgically swaps the
"## Résumé de l'article" section while keeping everything from
"## Discussion sur Hacker News" onward byte-for-byte. Use it to backfill
article summaries after ``fetch_article`` gains a new extractor, without
spending tokens on discussions that were already synthesized.

A file is rewritten only when the re-fetch yields content the LLM judges
usable (``content_usable=True``); otherwise it is left untouched. Idempotent
and safe to re-run.

Run from the repository root (so ``articles/`` resolves):

    uv run python scripts/regen_article_summaries.py            # regenerate
    DRY_RUN=1 uv run python scripts/regen_article_summaries.py  # list candidates only

``OPENROUTER_API_KEY`` must be set (``.env`` or environment) for the real run;
DRY_RUN makes no LLM call and writes nothing.
"""

import os
import re
import time
from datetime import UTC, datetime

from app.config import get_settings
from app.fetch_article import fetch_article
from app.models import ContentSource
from app.storage import iter_summarized, save
from app.summarize import (
    format_tweet_verbatim,
    summarize_article,
    translate_title,
    tweet_body_char_count,
)

DRY_RUN = os.environ.get("DRY_RUN") == "1"

# Matches the article-summary section when it is the load-failure placeholder,
# in both the plain ("(unable to load content)") and annotated
# ("(unable to load content: <reason>)") shapes.
PLACEHOLDER_RE = re.compile(
    r"^## Résumé de l'article\s*\n+\(unable to load content(?::[^)]*)?\)",
    re.MULTILINE,
)
DISCUSSION_RE = re.compile(r"\n\n## Discussion sur Hacker News")
FOOTER_RE = re.compile(r"\n\n---\n\n\[Article original\]")


def _replace_article_summary(body: str, new_summary: str) -> str:
    """Swap the article-summary block, keep the discussion + footer verbatim."""
    m = DISCUSSION_RE.search(body) or FOOTER_RE.search(body)
    if m is None:
        raise ValueError("no discussion/footer boundary found in body")
    tail = body[m.start() :]
    return "## Résumé de l'article\n\n" + new_summary.strip() + tail


def _new_article_summary(article, content):
    """Return (summary, rewritten_title, call) or (None, None, call) on no benefit.

    Mirrors the article branch of pipeline.step_summarize, without the
    discussion path. Returns ``(None, ...)`` when the article still cannot be
    turned into a usable summary, so the caller leaves the file untouched.
    """
    settings = get_settings()
    text = (content.text or "").strip()
    if content.source in (ContentSource.JS_REQUIRED, ContentSource.FEED_FALLBACK) or not text:
        return None, None, None
    if (
        content.source == ContentSource.TWEET
        and tweet_body_char_count(text) <= settings.tweet_verbatim_max_chars
    ):
        translated, call = translate_title(article.title)
        return format_tweet_verbatim(text), translated, call
    summary, call = summarize_article(text, article.title)
    if not summary.content_usable:
        return None, None, call
    return summary.summary_markdown, summary.rewritten_title, call


def main() -> None:
    settings = get_settings()
    targets = [
        (path, article, body)
        for path, article, body in list(iter_summarized())
        if PLACEHOLDER_RE.search(body)
    ]
    print(f"placeholder articles found: {len(targets)} (DRY_RUN={DRY_RUN})\n")

    regenerated = skipped = errors = 0
    for _path, article, body in targets:
        try:
            content = fetch_article(article.url)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"  ERROR fetch  {article.url[:70]}  {type(exc).__name__}: {exc}")
            continue

        text_len = len((content.text or "").strip())
        unfetchable = content.source in (ContentSource.JS_REQUIRED, ContentSource.FEED_FALLBACK)
        if unfetchable or not text_len:
            skipped += 1
            reason = content.failure_reason or content.source.value
            print(f"  skip   still-failing [{reason}]  {article.url[:65]}")
            continue

        if DRY_RUN:
            regenerated += 1
            print(f"  CAND   fetch-ok [{content.source.value} len={text_len}]  {article.url[:60]}")
            continue

        try:
            new_summary, new_title, call = _new_article_summary(article, content)
        except Exception as exc:  # noqa: BLE001
            errors += 1
            print(f"  ERROR llm    {article.url[:70]}  {type(exc).__name__}: {exc}")
            continue

        if new_summary is None:
            skipped += 1
            print(f"  skip   unusable [{content.source.value} len={text_len}]  {article.url[:50]}")
            time.sleep(settings.llm_sleep_seconds)
            continue

        new_body = _replace_article_summary(body, new_summary)
        if new_title:
            article.rewritten_title = new_title
        article.content_source = content.source
        article.content_failure_reason = None
        if article.image_url is None and content.image_url:
            article.image_url = content.image_url
        article.summarized_at = datetime.now(UTC)
        if call is not None:
            article.llm_models_used = list(
                dict.fromkeys((article.llm_models_used or []) + [call.model])
            )
            article.llm_input_tokens = (article.llm_input_tokens or 0) + call.input_tokens
            article.llm_output_tokens = (article.llm_output_tokens or 0) + call.output_tokens
            article.llm_latency_ms = (article.llm_latency_ms or 0) + call.latency_ms
        article.error = None
        save(article, new_body)
        regenerated += 1
        print(f"  OK     regenerated [{content.source.value}]  {article.url[:60]}")
        time.sleep(settings.llm_sleep_seconds)

    label = "candidates" if DRY_RUN else "regenerated"
    print(f"\n{label}={regenerated}  skipped={skipped}  errors={errors}  total={len(targets)}")


if __name__ == "__main__":
    main()
