import pytest

from app.llm import AllModelsFailedError, complete


def _openrouter_response(text: str = "résumé"):
    return {
        "choices": [
            {"message": {"role": "assistant", "content": text}}
        ]
    }


def test_complete_returns_primary_model_on_success(httpx_mock, isolated_settings):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("OK"),
    )
    result = complete("system", "user")
    assert result.text == "OK"
    assert result.model == isolated_settings.openrouter_model


def test_complete_falls_back_on_429(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "primary/free"
    isolated_settings.openrouter_fallback_models = ("secondary/free",)
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=429,
    )
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("fallback output"),
    )
    result = complete("system", "user")
    assert result.model == "secondary/free"
    assert result.text == "fallback output"


def test_complete_falls_back_on_5xx(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "primary/free"
    isolated_settings.openrouter_fallback_models = ("secondary/free",)
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=503,
    )
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("from fallback"),
    )
    result = complete("system", "user")
    assert result.model == "secondary/free"


def test_complete_raises_when_all_models_fail(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "primary/free"
    isolated_settings.openrouter_fallback_models = ("secondary/free",)
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=429,
    )
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=503,
    )
    with pytest.raises(AllModelsFailedError):
        complete("system", "user")


def test_empty_content_is_retryable(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "primary/free"
    isolated_settings.openrouter_fallback_models = ("secondary/free",)
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response(""),
    )
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("contenu"),
    )
    result = complete("system", "user")
    assert result.model == "secondary/free"
    assert result.text == "contenu"
