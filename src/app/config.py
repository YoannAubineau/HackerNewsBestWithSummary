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
    feed_self_url: str = "http://localhost/feed.xml"
    feed_items_limit: int = 200
    feed_title: str = "Hacker News Best summarized"
    feed_description: str = "Hacker News Best with article and discussion summaries."

    # Max comments sent to the LLM for the discussion summary. Spent recursively:
    # degressive split across root comments (those with ≥1 reply), the top-ranked
    # roots getting a bigger sub-budget that is itself split degressively among
    # their own replying children, and so on. Leaf comments are never included.
    discussion_budget: int = 500
    llm_sleep_seconds: float = 3.0
    http_timeout: float = 20.0
    max_attempts: int = 3
    user_agent: str = "hn-best-summary/0.1 (+https://github.com/)"

    articles_dir: Path = Path("artefacts/articles")
    failed_dir: Path = Path("artefacts/articles/_failed")
    feed_output_path: Path = Path("artefacts/feed.xml")

    log_level: LogLevel = "INFO"


_settings: Settings | None = None


def get_settings() -> Settings:
    global _settings
    if _settings is None:
        _settings = Settings()
    return _settings


def reset_settings() -> None:
    global _settings
    _settings = None
