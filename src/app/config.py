from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict

LogLevel = Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    openrouter_api_key: str
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
    # Circuit breaker. When today's OpenRouter spend (current cumulative
    # minus the highest cumulative seen on any earlier UTC day) exceeds
    # this value, step_summarize bails out for the rest of the cycle.
    # Set to 0 to disable.
    daily_cost_limit_usd: float = 2.0
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

    artefacts_dir: Path = Path("artefacts")

    @property
    def articles_dir(self) -> Path:
        return self.artefacts_dir / "articles"

    @property
    def failed_dir(self) -> Path:
        return self.articles_dir / "_failed"

    @property
    def feed_output_path(self) -> Path:
        return self.artefacts_dir / "feed.fr.xml"

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
