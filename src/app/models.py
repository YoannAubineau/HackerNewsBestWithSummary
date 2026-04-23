from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class Status(StrEnum):
    PENDING = "pending"
    ARTICLE_FETCHED = "article_fetched"
    DISCUSSION_FETCHED = "discussion_fetched"
    SUMMARIZED = "summarized"
    FAILED = "failed"


class ContentSource(StrEnum):
    EXTRACTED = "extracted"
    FEED_FALLBACK = "feed_fallback"
    ASK_SHOW_HN = "ask_show_hn"
    JS_REQUIRED = "js_required"
    VIDEO_TRANSCRIPT = "video_transcript"


class Article(BaseModel):
    guid: str
    url: str
    hn_url: str
    hn_item_id: int
    title: str
    rewritten_title: str | None = None
    source_published_at: datetime
    our_published_at: datetime
    status: Status = Status.PENDING
    is_ask_or_show_hn: bool = False
    content_source: ContentSource | None = None
    article_fetched_at: datetime | None = None
    discussion_fetched_at: datetime | None = None
    discussion_comment_count: int | None = None
    summarized_at: datetime | None = None
    image_url: str | None = None
    attempts: int = 0
    llm_models_used: list[str] | None = None
    llm_input_tokens: int | None = None
    llm_output_tokens: int | None = None
    llm_latency_ms: int | None = None
    error: str | None = None
    feed_summary: str = Field(
        default="",
        description="Summary provided by the source feed, kept as a fallback.",
    )
