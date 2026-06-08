import json as json_mod

import pytest

from app.llm import (
    AllModelsFailedError,
    ContextLengthExceededError,
    LLMError,
    complete,
)


def test_complete_raises_context_error_on_overflow(httpx_mock, isolated_settings):
    body = json_mod.dumps(
        {
            "error": {
                "message": (
                    "This endpoint's maximum context length is 200000 tokens. "
                    "However, you requested about 222911 tokens (222911 of text input)."
                ),
                "code": 400,
            }
        }
    )
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=400,
        text=body,
    )
    with pytest.raises(ContextLengthExceededError) as exc_info:
        complete("system", "user")
    assert exc_info.value.limit == 200000
    assert exc_info.value.requested == 222911


def test_complete_raises_generic_error_on_other_400(httpx_mock, isolated_settings):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        status_code=400,
        text='{"error": {"message": "invalid model"}}',
    )
    with pytest.raises(LLMError) as exc_info:
        complete("system", "user")
    assert not isinstance(exc_info.value, ContextLengthExceededError)


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


def test_complete_omits_response_format_by_default(httpx_mock, isolated_settings):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response("OK"),
    )
    complete("system", "user")
    sent = json_mod.loads(httpx_mock.get_request().content)
    assert "response_format" not in sent


def test_complete_sets_json_object_response_format_when_requested(
    httpx_mock, isolated_settings
):
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/chat/completions",
        json=_openrouter_response('{"k": "v"}'),
    )
    complete("system", "user", json=True)
    sent = json_mod.loads(httpx_mock.get_request().content)
    assert sent["response_format"] == {"type": "json_object"}


def test_complete_raises_when_api_key_is_empty(httpx_mock, isolated_settings):
    isolated_settings.openrouter_api_key = ""
    with pytest.raises(LLMError, match="OPENROUTER_API_KEY"):
        complete("system", "user")
    assert httpx_mock.get_requests() == []


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
