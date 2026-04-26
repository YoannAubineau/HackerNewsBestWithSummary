import time
from datetime import UTC, datetime
from itertools import chain
from pathlib import Path
from typing import NamedTuple

import structlog

from app.archive import write_archive
from app.config import get_settings
from app.fetch_article import fetch_article
from app.fetch_discussion import fetch_discussion, fetch_submitter_text
from app.llm import AllModelsFailedError, LLMCallResult, LLMError
from app.models import Article, ContentSource, Status
from app.publish import write_feed
from app.rss_in import FeedEntry, fetch_source_feed
from app.storage import (
    clear_sidecars,
    ensure_articles_dir,
    find_existing,
    iter_by_status,
    move_to_failed,
    path_for,
    read_sidecar,
    save,
    write_sidecar,
)
from app.summarize import (
    compose_body,
    summarize_article,
    summarize_discussion,
    translate_title,
)
from app.usage import today_spend

log = structlog.get_logger()


class CycleResult(NamedTuple):
    failures: list[tuple[str, str]]


def step_fetch_feed() -> int:
    ensure_articles_dir()
    try:
        entries = fetch_source_feed()
    except Exception as exc:  # noqa: BLE001
        # hnrss.org or the runner's network can flake transiently. Swallow the
        # error, skip the cycle. Next cron run will retry naturally.
        log.warning("fetch_feed_failed", error=str(exc))
        return 0
    created = 0
    for entry in entries:
        if find_existing(entry.guid) is not None:
            continue
        if entry.title.lower().startswith("[flagged]"):
            log.info("entry_skipped_flagged", guid=entry.guid, title=entry.title)
            continue
        _create_pending(entry)
        created += 1
    log.info("fetch_feed", fetched=len(entries), created=created)
    return created


def step_fetch_articles(failures: list[tuple[str, str]] | None = None) -> int:
    done = 0
    for path, article, body in list(iter_by_status(Status.DISCUSSION_FETCHED)):
        if article.is_ask_or_show_hn:
            try:
                submitter_text = fetch_submitter_text(article.hn_item_id)
            except Exception as exc:  # noqa: BLE001
                _record_attempt(path, article, body, f"fetch_submitter_text: {exc}", failures)
                continue
            if submitter_text:
                write_sidecar(path, "article", submitter_text)
            article.content_source = ContentSource.ASK_SHOW_HN
            article.status = Status.ARTICLE_FETCHED
            article.article_fetched_at = _now()
            save(article, body)
            done += 1
            continue
        try:
            result = fetch_article(article.url, article.feed_summary)
        except Exception as exc:  # noqa: BLE001
            _record_attempt(path, article, body, f"fetch_article: {exc}", failures)
            continue
        if result.text:
            write_sidecar(path, "article", result.text)
        article.content_source = result.source
        article.image_url = result.image_url
        article.article_fetched_at = _now()
        article.status = Status.ARTICLE_FETCHED
        save(article, body)
        done += 1
    log.info("fetch_articles", processed=done)
    return done


def step_fetch_discussions(failures: list[tuple[str, str]] | None = None) -> int:
    settings = get_settings()
    threshold = settings.min_discussion_comments
    done = 0
    skipped = 0
    # The second iterator drains any article left in ARTICLE_FETCHED by the
    # pre-swap pipeline order (article fetch used to precede discussion fetch).
    # Under the new order it is always empty in steady state. Remove once the
    # in-flight inventory has cycled through.
    sources = chain(
        iter_by_status(Status.PENDING),
        iter_by_status(Status.ARTICLE_FETCHED),
    )
    for path, article, body in list(sources):
        try:
            discussion = fetch_discussion(article.hn_item_id)
        except Exception as exc:  # noqa: BLE001
            _record_attempt(path, article, body, f"fetch_discussion: {exc}", failures)
            continue

        if discussion and discussion.canonical_dupe_id is not None:
            canonical_id = discussion.canonical_dupe_id
            canonical_guid = f"https://news.ycombinator.com/item?id={canonical_id}"

            if find_existing(canonical_guid) is not None:
                clear_sidecars(path)
                path.unlink(missing_ok=True)
                log.info(
                    "dupe_skipped",
                    guid=article.guid,
                    dupe_id=article.hn_item_id,
                    canonical_id=canonical_id,
                )
                continue

            try:
                canonical_discussion = fetch_discussion(canonical_id)
            except Exception as exc:  # noqa: BLE001
                _record_attempt(
                    path,
                    article,
                    body,
                    f"fetch_discussion (canonical {canonical_id}): {exc}",
                    failures,
                )
                continue
            if (
                canonical_discussion is None
                or canonical_discussion.title is None
                or canonical_discussion.source_published_at is None
            ):
                _record_attempt(
                    path,
                    article,
                    body,
                    f"dupe canonical {canonical_id} unavailable",
                    failures,
                )
                continue

            dupe_id = article.hn_item_id
            clear_sidecars(path)
            path.unlink(missing_ok=True)
            article.hn_item_id = canonical_id
            article.guid = canonical_guid
            article.hn_url = canonical_guid
            article.title = canonical_discussion.title
            article.source_published_at = canonical_discussion.source_published_at

            discussion = canonical_discussion
            path = path_for(article.guid, article.our_published_at)
            log.info(
                "dupe_substituted",
                dupe_id=dupe_id,
                canonical_id=canonical_id,
                canonical_guid=canonical_guid,
            )

        if discussion is not None and discussion.comment_count < threshold:
            if not path.exists():
                # Substitution rewrote the article identity to a canonical
                # that doesn't yet exist on disk. Persist it at PENDING so
                # the next cycle re-evaluates the canonical against fresh
                # counts; otherwise the unlinked old path leaves us with
                # no on-disk entry at all.
                save(article, body)
            log.info(
                "article_skipped_low_comments",
                guid=article.guid,
                comment_count=discussion.comment_count,
                threshold=threshold,
            )
            skipped += 1
            continue

        if discussion:
            if discussion.url:
                article.url = discussion.url
            if discussion.text:
                write_sidecar(path, "discussion", discussion.text)
            if discussion.top_comments_markdown:
                write_sidecar(path, "top_comments", discussion.top_comments_markdown)
            article.discussion_comment_count = discussion.comment_count
        article.discussion_fetched_at = _now()
        article.status = Status.DISCUSSION_FETCHED
        save(article, body)
        done += 1
    log.info("fetch_discussions", processed=done, skipped=skipped)
    return done


def step_summarize(failures: list[tuple[str, str]] | None = None) -> int:
    settings = get_settings()
    if settings.daily_cost_limit_usd > 0:
        spent = today_spend()
        if spent is not None and spent >= settings.daily_cost_limit_usd:
            log.warning(
                "summarize_skipped_cost_breaker",
                today_spend_usd=spent,
                limit_usd=settings.daily_cost_limit_usd,
            )
            return 0
    done = 0
    for path, article, body in list(iter_by_status(Status.ARTICLE_FETCHED)):
        article_text = read_sidecar(path, "article")
        discussion_text = read_sidecar(path, "discussion")
        top_comments_md = read_sidecar(path, "top_comments")

        try:
            article_summary: str | None = None
            discussion_summary: str | None = None
            calls: list[LLMCallResult] = []

            if article.content_source == ContentSource.JS_REQUIRED:
                translated, call = translate_title(article.title)
                calls.append(call)
                if translated:
                    article.rewritten_title = translated
                article_summary = "(no content)"
                time.sleep(settings.llm_sleep_seconds)
            elif article_text:
                summary, call = summarize_article(article_text, article.title)
                calls.append(call)
                article_summary = summary.summary_markdown
                if summary.rewritten_title:
                    article.rewritten_title = summary.rewritten_title
                time.sleep(settings.llm_sleep_seconds)

            if discussion_text:
                discussion_summary, call = summarize_discussion(discussion_text, article.title)
                calls.append(call)
                time.sleep(settings.llm_sleep_seconds)

            if not article_summary and not discussion_summary:
                _record_attempt(path, article, body, "nothing to summarize", failures)
                continue

            final_body = compose_body(
                article_summary=article_summary,
                discussion_summary=discussion_summary,
                discussion_comment_count=article.discussion_comment_count,
                top_comments_markdown=top_comments_md,
                url=article.url,
                hn_url=article.hn_url,
            )
            article.status = Status.SUMMARIZED
            article.summarized_at = _now()
            article.llm_models_used = list(dict.fromkeys(c.model for c in calls))
            article.llm_input_tokens = sum(c.input_tokens for c in calls)
            article.llm_output_tokens = sum(c.output_tokens for c in calls)
            article.llm_latency_ms = sum(c.latency_ms for c in calls)
            article.error = None
            save(article, final_body)
            clear_sidecars(path)
            done += 1
        except (AllModelsFailedError, LLMError) as exc:
            _record_attempt(path, article, body, str(exc), failures)
    log.info("summarize", processed=done)
    return done


def step_publish() -> str:
    feed_path = write_feed()
    archive_path = write_archive()
    log.info("publish", feed=str(feed_path), archive=str(archive_path))
    return str(feed_path)


def run_cycle() -> CycleResult:
    failures: list[tuple[str, str]] = []
    step_fetch_feed()
    step_fetch_discussions(failures)
    step_fetch_articles(failures)
    step_summarize(failures)
    # Always publish, even when no new articles were summarized: a code-only
    # change on the publish side (description format, feed structure, …) must
    # flow through on the next cycle without waiting for a fresh HN submission.
    step_publish()
    return CycleResult(failures=failures)


def backfill_images() -> int:
    """Fill missing image_url on already-summarized articles.

    Re-fetches the article URL (no LLM calls) and pulls og:image /
    twitter:image metadata into the frontmatter. Articles that already
    carry an image_url, Ask/Show HN entries, and URLs we fail to fetch
    are skipped in place.
    """
    from app.storage import iter_summarized

    filled = 0
    for _path, article, body in list(iter_summarized()):
        if article.image_url:
            continue
        if article.content_source == ContentSource.ASK_SHOW_HN:
            continue
        try:
            result = fetch_article(article.url, feed_fallback="")
        except Exception as exc:  # noqa: BLE001
            log.warning("backfill_fetch_failed", guid=article.guid, error=str(exc))
            continue
        if not result.image_url:
            continue
        article.image_url = result.image_url
        save(article, body)
        filled += 1
        log.info("backfill_filled", guid=article.guid, image_url=result.image_url)
    log.info("backfill_images", filled=filled)
    return filled


def _create_pending(entry: FeedEntry) -> None:
    article = Article(
        guid=entry.guid,
        url=entry.url,
        hn_url=entry.hn_url,
        hn_item_id=entry.hn_item_id,
        title=entry.title,
        source_published_at=entry.source_published_at,
        # Use the feed's lastBuildDate as the "entered /best" approximation
        # rather than our local wall-clock — it is anchored on the server's
        # view of /best and tighter than our polling cadence.
        our_published_at=entry.observed_at,
        status=Status.PENDING,
        is_ask_or_show_hn=entry.is_ask_or_show_hn,
        feed_summary=entry.feed_summary,
    )
    save(article)


def _record_attempt(
    path: Path,
    article: Article,
    body: str,
    error: str,
    failures: list[tuple[str, str]] | None = None,
) -> bool:
    settings = get_settings()
    article.attempts += 1
    article.error = error
    if article.attempts >= settings.max_attempts:
        move_to_failed(path, article, body)
        clear_sidecars(path)
        log.warning("article_failed", guid=article.guid, error=error, attempts=article.attempts)
        if failures is not None:
            failures.append((article.guid, error))
        return True
    save(article, body)
    log.warning("article_retry", guid=article.guid, error=error, attempts=article.attempts)
    return False


def _now() -> datetime:
    return datetime.now(tz=UTC)
