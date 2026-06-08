import re
import time
from dataclasses import dataclass

import httpx
import structlog

from app.config import get_settings

_OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

log = structlog.get_logger()


class LLMError(RuntimeError):
    pass


class AllModelsFailedError(LLMError):
    pass


class ContextLengthExceededError(LLMError):
    """Raised when a request overflows the model's context window.

    Carries the limit and the requested token count parsed from the
    provider's 400 body (either may be ``None`` when the wording changes),
    so the caller can shrink its input by the exact ratio and retry.
    """

    def __init__(self, message: str, *, limit: int | None, requested: int | None) -> None:
        super().__init__(message)
        self.limit = limit
        self.requested = requested


_CONTEXT_LIMIT_RE = re.compile(r"maximum context length is\s+([\d,]+)", re.IGNORECASE)
_CONTEXT_REQUESTED_RE = re.compile(r"requested about\s+([\d,]+)", re.IGNORECASE)


def _context_length_error(model: str, body: str) -> ContextLengthExceededError | None:
    """Return a ContextLengthExceededError if ``body`` is a context-window 400.

    The limit prefers the model's known context window (an intrinsic property)
    and falls back to the number parsed from the message, so a change in the
    provider's error wording cannot blind the truncation retry.
    """
    lowered = body.lower()
    if "context length" not in lowered and "context_length" not in lowered:
        return None
    limit = _CONTEXT_LIMIT_RE.search(body)
    requested = _CONTEXT_REQUESTED_RE.search(body)
    known_limit = get_settings().model_context_windows.get(model)
    parsed_limit = int(limit.group(1).replace(",", "")) if limit else None
    return ContextLengthExceededError(
        f"{model}: context length exceeded",
        limit=known_limit or parsed_limit,
        requested=int(requested.group(1).replace(",", "")) if requested else None,
    )


@dataclass
class LLMCallResult:
    content: str
    model: str
    input_tokens: int
    output_tokens: int
    latency_ms: int


def complete(system_prompt: str, user_prompt: str, *, json: bool = False) -> LLMCallResult:
    """Call OpenRouter, trying the primary model then each fallback.

    A 429 or 5xx triggers the next model; any other 4xx aborts.

    When ``json`` is True, request ``response_format: json_object`` so the
    model emits a parseable JSON string. Best-effort across the cascade —
    callers must tolerate malformed JSON from providers that ignore it.
    """
    settings = get_settings()
    if not settings.openrouter_api_key:
        raise LLMError("OPENROUTER_API_KEY is required to call the LLM")
    candidates = [settings.openrouter_model, *settings.openrouter_fallback_models]
    last_error: Exception | None = None
    for model in candidates:
        try:
            return _call(model, system_prompt, user_prompt, json=json)
        except _Retryable as exc:
            last_error = exc
            log.warning("llm_retry", model=model, reason=str(exc))
            continue
        except httpx.HTTPStatusError as exc:
            context_error = _context_length_error(model, exc.response.text)
            if context_error is not None:
                raise context_error from exc
            raise LLMError(f"{model}: {exc.response.status_code} {exc.response.text}") from exc
    raise AllModelsFailedError(f"all models failed: {last_error}")


def _call(
    model: str, system_prompt: str, user_prompt: str, *, json: bool = False
) -> LLMCallResult:
    settings = get_settings()
    payload: dict = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    if json:
        payload["response_format"] = {"type": "json_object"}
    headers = {
        "Authorization": f"Bearer {settings.openrouter_api_key}",
        "Content-Type": "application/json",
        "User-Agent": settings.user_agent,
    }
    start = time.monotonic()
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
    content = (message.get("content") or "").strip()
    if not content:
        raise _Retryable(f"{model}: empty content")
    latency_ms = int((time.monotonic() - start) * 1000)
    usage = data.get("usage") or {}
    input_tokens = int(usage.get("prompt_tokens") or 0)
    output_tokens = int(usage.get("completion_tokens") or 0)
    actual_model = data.get("model") or model
    log.info(
        "llm_call",
        model=actual_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_ms=latency_ms,
    )
    return LLMCallResult(
        content=content,
        model=actual_model,
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        latency_ms=latency_ms,
    )


class _Retryable(Exception):
    pass
