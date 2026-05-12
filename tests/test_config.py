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


def test_log_level_rejects_lowercase():
    with pytest.raises(ValidationError):
        Settings(openrouter_api_key="k", log_level="debug")


def test_log_level_rejects_typos():
    with pytest.raises(ValidationError):
        Settings(openrouter_api_key="k", log_level="DEGUB")


def test_log_level_rejects_non_level_attribute_names():
    # `getLogger` is an attribute of the logging module but not a level.
    with pytest.raises(ValidationError):
        Settings(openrouter_api_key="k", log_level="getLogger")
