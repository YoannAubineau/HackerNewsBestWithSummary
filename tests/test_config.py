import pytest
from pydantic import ValidationError

from app import config as config_module
from app.config import Settings


def test_settings_default_openrouter_api_key_is_empty(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    assert Settings().openrouter_api_key == ""


def test_get_settings_succeeds_without_openrouter_api_key_env_var(
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.delenv("OPENROUTER_API_KEY", raising=False)
    config_module.reset_settings()
    try:
        settings = config_module.get_settings()
    finally:
        config_module.reset_settings()
    assert settings.openrouter_api_key == ""


def test_log_level_accepts_uppercase():
    assert Settings(openrouter_api_key="k", log_level="DEBUG").log_level == "DEBUG"


@pytest.mark.parametrize(
    "level",
    [
        "debug",  # lowercase is rejected
        "DEGUB",  # typo
        "getLogger",  # a logging-module attribute, but not a level
    ],
)
def test_log_level_rejects_invalid(level: str):
    with pytest.raises(ValidationError):
        Settings(openrouter_api_key="k", log_level=level)
