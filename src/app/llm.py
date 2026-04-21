from dataclasses import dataclass

import httpx

from app.config import get_settings

_OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


class LLMError(RuntimeError):
    pass


class AllModelsFailedError(LLMError):
    pass


@dataclass
class LLMResult:
    text: str
    model: str


def complete(system_prompt: str, user_prompt: str) -> LLMResult:
    """Call OpenRouter, trying the primary model then each fallback.

    A 429 or 5xx triggers the next model; any other 4xx aborts.
    """
    settings = get_settings()
    candidates = [settings.openrouter_model, *settings.openrouter_fallback_models]
    last_error: Exception | None = None
    for model in candidates:
        try:
            return _call(model, system_prompt, user_prompt)
        except _Retryable as exc:
            last_error = exc
            continue
        except httpx.HTTPStatusError as exc:
            raise LLMError(f"{model}: {exc.response.status_code} {exc.response.text}") from exc
    raise AllModelsFailedError(f"all models failed: {last_error}")


def _call(model: str, system_prompt: str, user_prompt: str) -> LLMResult:
    settings = get_settings()
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    headers = {
        "Authorization": f"Bearer {settings.openrouter_api_key}",
        "Content-Type": "application/json",
        "User-Agent": settings.user_agent,
    }
    response = httpx.post(
        _OPENROUTER_URL,
        json=payload,
        headers=headers,
        timeout=settings.http_timeout * 3,
    )
    if response.status_code == 429 or 500 <= response.status_code < 600:
        raise _Retryable(f"{model}: {response.status_code}")
    response.raise_for_status()
    data = response.json()
    choices = data.get("choices") or []
    if not choices:
        raise _Retryable(f"{model}: response without choices")
    message = choices[0].get("message") or {}
    text = (message.get("content") or "").strip()
    if not text:
        raise _Retryable(f"{model}: empty content")
    return LLMResult(text=text, model=model)


class _Retryable(Exception):
    pass
