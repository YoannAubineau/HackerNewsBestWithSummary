from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Required at runtime only by code paths that actually call OpenRouter
    # (LLM completions in llm.py, spend probing in usage.py). Leaving it
    # empty lets non-LLM subcommands and dev tooling (lint, tests, publish,
    # fetch-feed...) run without the secret configured.
    openrouter_api_key: str = ""
    openrouter_model: str = "anthropic/claude-haiku-4.5"
    openrouter_fallback_models: tuple[str, ...] = (
        "nvidia/nemotron-3-super-120b-a12b:free",
        "meta-llama/llama-3.3-70b-instruct:free",
    )

    source_feed_url: str = "https://hnrss.org/best"
    feed_self_url: str = "http://localhost/feed.fr.xml"
    feed_items_limit: int = 100
    feed_ttl_minutes: int = 15
    feed_title: str = "Hacker News: Best, with Summary"
    feed_description: str = (
        "Hacker News highest-voted recent links with article and discussion summaries "
        "in French."
    )
    channel_site_url: str = "https://news.ycombinator.com/best"

    llm_sleep_seconds: float = 3.0
    http_timeout: float = 20.0
    max_attempts: int = 3
    # Articles whose HN discussion has fewer comments than this stay at
    # their current status (PENDING in the swapped pipeline, ARTICLE_FETCHED
    # for legacy in-flight items) and are re-checked on every later cycle.
    # Once the discussion grows past the threshold the article advances
    # normally; if it never does it just stays parked. Set to 0 to disable.
    min_discussion_comments: int = 20
    # Escape valve for the parking above: articles older than this many
    # hours (counted from our_published_at, i.e. when they first hit our
    # ingest) graduate even with a thin discussion, so an interesting
    # Best-feed entry that never grows past the comment threshold still
    # produces a feed item (article summary alone) rather than rotting at
    # PENDING forever. Set to 0 to disable (legacy behaviour: never expire).
    pending_grace_hours: int = 24
    # Circuit breaker. When today's OpenRouter spend (current cumulative
    # minus the highest cumulative seen on any earlier UTC day) exceeds
    # this value, step_summarize bails out for the rest of the cycle.
    # Set to 0 to disable.
    daily_cost_limit_usd: float = 1.0
    # Tweets shorter than this are quoted verbatim instead of summarized.
    # Below the typical LLM summary length (~1000 chars on this feed), the
    # summary would be longer than the original — pointless and noisy.
    tweet_verbatim_max_chars: int = 1000
    user_agent: str = (
        "hn-best-summary/0.1 "
        "(+https://github.com/YoannAubineau/HackerNewsBestWithSummary)"
    )

    # Webshare residential proxy credentials. Optional. Only used by the
    # YouTube transcript path — YouTube blocks datacenter IPs (GitHub
    # Actions runners included), so transcript fetching from CI requires
    # routing through a residential IP. When either value is empty, the
    # request is made directly (fine from a non-blocked home IP).
    webshare_proxy_username: str = ""
    webshare_proxy_password: str = ""

    # Optional GitHub API token. Anonymous calls are rate-limited to
    # 60/hr per IP, which is usually enough for our cadence (~1 cycle/hr,
    # rarely more than a few GitHub URLs per cycle). Setting a token
    # lifts the limit to 5000/hr.
    github_token: str = ""

    # Wayback Machine fallback. When the direct HTTP + Webshare path fails
    # to produce usable content (paywall 403, Cloudflare challenge, JS-only
    # SPA, empty extraction), the dispatcher asks
    # archive.org/wayback/available for the closest snapshot and extracts
    # from there. No auth required. Set to False to disable.
    wayback_enabled: bool = True

    # r.jina.ai reader fallback. Tried after the Wayback miss: the reader
    # fetches and renders the page server-side (running its JavaScript) and
    # returns already-extracted prose, recovering client-rendered SPA pages
    # and soft anti-bot blocks that defeat the direct + Wayback paths. No
    # auth required on the free tier. Set to False to disable.
    reader_enabled: bool = True

    artifacts_dir: Path = Path("artifacts")
    articles_dir: Path = Path("articles")

    @property
    def failed_dir(self) -> Path:
        return self.articles_dir / "_failed"

    @property
    def feed_output_path(self) -> Path:
        return self.artifacts_dir / "feed.fr.xml"

    log_level: LogLevel = "INFO"


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        # pydantic-settings populates required fields from the environment;
        # pyright can't see through that, so the call looks arg-less to it.
        _settings = Settings()  # pyright: ignore[reportCallIssue]
    return _settings


def reset_settings() -> None:
    global _settings
    _settings = None
