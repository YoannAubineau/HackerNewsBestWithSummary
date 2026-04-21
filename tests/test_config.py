import pytest
from pydantic import ValidationError

from app.config import Settings


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
