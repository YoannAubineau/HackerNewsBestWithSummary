import httpx
import pytest

from app.check_models import NEWER_MODEL_EXIT_CODE, _parse_slug, check_llm_versions


def _models_response(ids: list[str]) -> dict:
    return {"data": [{"id": slug} for slug in ids]}


def test_parse_slug_extracts_family_and_version():
    ref = _parse_slug("anthropic/claude-haiku-4.5")
    assert ref is not None
    assert ref.family == "anthropic/claude-haiku"
    assert ref.version == (4, 5)


def test_parse_slug_strips_variant_suffix():
    ref = _parse_slug("anthropic/claude-haiku-4.5:thinking")
    assert ref is not None
    assert ref.family == "anthropic/claude-haiku"
    assert ref.version == (4, 5)


def test_parse_slug_returns_none_when_no_trailing_version():
    assert _parse_slug("openrouter/auto") is None


def test_check_returns_zero_when_no_newer_model(httpx_mock, isolated_settings, capsys):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/models",
        json=_models_response(
            [
                "anthropic/claude-haiku-4.5",
                "anthropic/claude-haiku-4.5:thinking",
                "anthropic/claude-sonnet-4.6",
                "meta-llama/llama-3.3-70b-instruct",
            ]
        ),
    )
    assert check_llm_versions() == 0
    out = capsys.readouterr().out
    assert "No newer model available" in out


def test_check_detects_newer_minor_version(httpx_mock, isolated_settings, capsys):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/models",
        json=_models_response(
            [
                "anthropic/claude-haiku-4.5",
                "anthropic/claude-haiku-4.6",
            ]
        ),
    )
    assert check_llm_versions() == NEWER_MODEL_EXIT_CODE
    out = capsys.readouterr().out
    assert "anthropic/claude-haiku-4.6" in out


def test_check_detects_newer_major_version(httpx_mock, isolated_settings, capsys):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/models",
        json=_models_response(
            [
                "anthropic/claude-haiku-4.5",
                "anthropic/claude-haiku-5.0",
            ]
        ),
    )
    assert check_llm_versions() == NEWER_MODEL_EXIT_CODE
    out = capsys.readouterr().out
    assert "anthropic/claude-haiku-5.0" in out


def test_check_ignores_other_families(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/models",
        json=_models_response(
            [
                "anthropic/claude-haiku-4.5",
                "anthropic/claude-sonnet-4.7",
                "anthropic/claude-opus-4.7",
            ]
        ),
    )
    assert check_llm_versions() == 0


def test_check_ignores_malformed_slugs(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_response(
        url="https://openrouter.ai/api/v1/models",
        json=_models_response(
            [
                "anthropic/claude-haiku-4.5",
                "openrouter/auto",
                "some-weird-slug-without-version",
            ]
        ),
    )
    assert check_llm_versions() == 0


def test_check_returns_zero_when_current_slug_unparseable(
    httpx_mock, isolated_settings, capsys
):
    isolated_settings.openrouter_model = "openrouter/auto"
    assert check_llm_versions() == 0
    out = capsys.readouterr().out
    assert "Cannot parse a version" in out


def test_check_raises_on_http_error(httpx_mock, isolated_settings):
    isolated_settings.openrouter_model = "anthropic/claude-haiku-4.5"
    httpx_mock.add_exception(httpx.ConnectError("network down"))
    with pytest.raises(httpx.ConnectError):
        check_llm_versions()
