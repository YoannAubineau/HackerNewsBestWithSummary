import pytest

from app.llm import AllModelsFailedError, complete


def _openrouter_response(
    text: str = "résumé",
    *,
    model: str | None = None,
    prompt_tokens: int = 12,
    completion_tokens: int = 34,
):
    payload = {
        "choices": [{"message": {"role": "assistant", "content": text}}],
        "usage": {"prompt_tokens": prompt_tokens, "completion_tokens": completion_tokens},
    }
    if model is not None:
        payload["model"] = model
    return payload


def test_complete_returns_primary_model_on_success(httpx_mock, isolated_settings):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("OK"),
    )
    result = complete("system", "user")
    assert result.content == "OK"
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
    assert result.content == "fallback output"


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
    assert result.content == "contenu"


def test_complete_exposes_usage_and_latency(httpx_mock, isolated_settings):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response(
            "OK",
            model="anthropic/claude-haiku-4.5",
            prompt_tokens=123,
            completion_tokens=45,
        ),
    )
    result = complete("system", "user")
    assert result.model == "anthropic/claude-haiku-4.5"
    assert result.input_tokens == 123
    assert result.output_tokens == 45
    assert isinstance(result.latency_ms, int)
    assert result.latency_ms >= 0
