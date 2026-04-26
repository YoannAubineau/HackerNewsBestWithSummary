import re
import time
from datetime import UTC, datetime, timedelta
from pathlib import Path

import structlog

from app.config import get_settings
from app.feedly_lag import fetch_feedly_origin_ids
from app.fetch_discussion import fetch_discussion
from app.llm import AllModelsFailedError, LLMError
from app.models import Article
from app.storage import iter_summarized, save, short_hash
from app.summarize import summarize_discussion
from app.usage import today_spend

log = structlog.get_logger()

_MAX_AGE = timedelta(hours=24)
_DISCUSSION_BLOCK_RE = re.compile(
    r"^## Discussion sur Hacker News.*?(?=\n---\n)", re.DOTALL | re.MULTILINE
)


def step_refresh_discussions(cycle_started_at: datetime) -> int:
    """Refresh discussion sections for SUMMARIZED articles not yet
    visible to Feedly. Returns the number of articles updated.

    `cycle_started_at` is the timestamp of the current cycle's start,
    used to skip articles summarized in this same cycle (which haven't
    been published yet, so Feedly couldn't see them anyway). Pass
    `_now()` when calling outside a cycle (e.g. from the CLI command).
    """
    settings = get_settings()
    if not settings.feedly_dev_token:
        log.info("refresh_discussions_skipped_no_token")
        return 0
    if _cost_breaker_tripped(settings):
        return 0

    seen_ids = fetch_feedly_origin_ids(count=100)
    if seen_ids is None:
        log.info("refresh_discussions_skipped_feedly_unavailable")
        return 0
    now = _now()
    refreshed = 0
    for path, article, body in iter_summarized():
        if now - article.our_published_at > _MAX_AGE:
            break
        if not _should_refresh(article, seen_ids, cycle_started_at):
            continue
        try:
            if _refresh_article(path, article, body):
                refreshed += 1
        except (AllModelsFailedError, LLMError) as exc:
            log.warning(
                "refresh_discussion_llm_failed",
                guid=article.guid,
                error=str(exc),
            )
            continue
        if _cost_breaker_tripped(settings):
            break
        time.sleep(settings.llm_sleep_seconds)
    log.info("refresh_discussions", processed=refreshed)
    return refreshed


def _should_refresh(
    article: Article, seen_ids: set[str], cycle_started_at: datetime
) -> bool:
    if article.summarized_at is not None and article.summarized_at >= cycle_started_at:
        log.info(
            "refresh_discussion_skipped_same_cycle",
            guid=article.guid,
        )
        return False
    return short_hash(article.guid) not in seen_ids


def _refresh_article(path: Path, article: Article, body: str) -> bool:
    settings = get_settings()
    discussion = fetch_discussion(article.hn_item_id)
    if discussion is None:
        log.warning("refresh_discussion_fetch_failed", guid=article.guid)
        return False
    if discussion.canonical_dupe_id is not None:
        log.info(
            "refresh_discussion_skipped_dupe",
            guid=article.guid,
            canonical_id=discussion.canonical_dupe_id,
        )
        return False
    if (
        not discussion.text
        or discussion.comment_count < settings.min_discussion_comments
    ):
        log.info(
            "refresh_discussion_skipped_thin",
            guid=article.guid,
            comment_count=discussion.comment_count,
        )
        return False

    summary, call = summarize_discussion(discussion.text, article.title)
    new_block = _build_discussion_block(
        comment_count=discussion.comment_count,
        summary=summary,
        top_comments_markdown=discussion.top_comments_markdown,
    )
    new_body = _splice_discussion(body, new_block)
    if new_body is None:
        log.warning("refresh_discussion_splice_missed", guid=article.guid)
        return False

    article.discussion_comment_count = discussion.comment_count
    article.discussion_fetched_at = _now()
    models = list(article.llm_models_used or [])
    if call.model not in models:
        models.append(call.model)
    article.llm_models_used = models
    article.llm_input_tokens = (article.llm_input_tokens or 0) + call.input_tokens
    article.llm_output_tokens = (article.llm_output_tokens or 0) + call.output_tokens
    article.llm_latency_ms = (article.llm_latency_ms or 0) + call.latency_ms
    save(article, new_body)
    log.info(
        "refresh_discussion_done",
        guid=article.guid,
        comment_count=discussion.comment_count,
    )
    return True


def _build_discussion_block(
    *, comment_count: int, summary: str, top_comments_markdown: str
) -> str:
    word = "commentaire" if comment_count == 1 else "commentaires"
    heading = f"## Discussion sur Hacker News ({comment_count} {word})"
    block = f"{heading}\n\n{summary.strip()}"
    if top_comments_markdown and top_comments_markdown.strip():
        block += "\n\n" + top_comments_markdown.strip()
    return block


def _splice_discussion(body: str, new_block: str) -> str | None:
    match = _DISCUSSION_BLOCK_RE.search(body)
    if match is None:
        return None
    return body[: match.start()] + new_block + body[match.end() :]


def _cost_breaker_tripped(settings) -> bool:
    if settings.daily_cost_limit_usd <= 0:
        return False
    spent = today_spend()
    if spent is None:
        return False
    if spent >= settings.daily_cost_limit_usd:
        log.warning(
            "refresh_discussions_cost_breaker",
            today_spend_usd=spent,
            limit_usd=settings.daily_cost_limit_usd,
        )
        return True
    return False


def _now() -> datetime:
    return datetime.now(UTC)
