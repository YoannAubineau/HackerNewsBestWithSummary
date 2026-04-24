from app import summarize
from app.llm import LLMCallResult
from app.summarize import (
    _parse_article_response,
    compose_body,
    summarize_article,
    summarize_discussion,
    translate_title,
)


def _call_result(content: str, model: str = "m") -> LLMCallResult:
    return LLMCallResult(
        content=content,
        model=model,
        input_tokens=10,
        output_tokens=5,
        latency_ms=42,
    )


def test_parse_article_response_well_formed_json():
    text = (
        '{"title": "un titre factuel", '
        '"summary": "**TL;DR** : phrase.\\n- bullet 1\\n- bullet 2"}'
    )
    title, summary = _parse_article_response(text)
    assert title == "un titre factuel"
    assert summary.startswith("**TL;DR**")
    assert "bullet 2" in summary


def test_parse_article_response_invalid_json_falls_back_to_raw():
    text = "Juste du texte sans JSON"
    title, summary = _parse_article_response(text)
    assert title is None
    assert summary == text


def test_parse_article_response_missing_summary_falls_back_to_raw():
    text = '{"title": "un titre"}'
    title, summary = _parse_article_response(text)
    assert title is None
    assert summary == text


def test_parse_article_response_missing_title_keeps_summary():
    text = '{"summary": "le corps"}'
    title, summary = _parse_article_response(text)
    assert title is None
    assert summary == "le corps"


def test_compose_body_shows_discussion_comment_count():
    body = compose_body(
        article_summary="**Note.**\n\n- point",
        discussion_summary="**Confirmations** :\n- yes",
        discussion_comment_count=42,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    assert "## Discussion sur Hacker News (42 commentaires analysés)" in body


def test_compose_body_singular_for_one_comment():
    body = compose_body(
        article_summary=None,
        discussion_summary="**Confirmations** :\n- solo",
        discussion_comment_count=1,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    assert "(1 commentaire analysé)" in body


def test_compose_body_omits_count_when_none():
    body = compose_body(
        article_summary=None,
        discussion_summary="**Confirmations** :\n- yes",
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    assert "## Discussion sur Hacker News\n" in body
    assert "commentaires analysés" not in body


def test_translate_title_returns_first_line(monkeypatch):
    def fake_complete(system, user):
        return _call_result("  Sous-système Windows 9x pour Linux  \n")

    monkeypatch.setattr(summarize, "complete", fake_complete)
    translated, call = translate_title("Windows 9x Subsystem for Linux")
    assert translated == "Sous-système Windows 9x pour Linux"
    assert call.model == "m"


def test_translate_title_none_on_empty_response(monkeypatch):
    def fake_complete(system, user):
        return _call_result("   \n\n")

    monkeypatch.setattr(summarize, "complete", fake_complete)
    translated, call = translate_title("whatever")
    assert translated is None
    assert call.model == "m"


def test_summarize_article_propagates_call_metrics(monkeypatch):
    captured: dict = {}

    def fake_complete(system, user, *, json=False):
        captured["json"] = json
        return LLMCallResult(
            content='{"title": "un titre", "summary": "- point"}',
            model="anthropic/claude-haiku-4.5",
            input_tokens=1000,
            output_tokens=200,
            latency_ms=1234,
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary, call = summarize_article("texte", "titre original")
    assert captured["json"] is True
    assert summary.rewritten_title == "un titre"
    assert summary.summary_markdown == "- point"
    assert call.model == "anthropic/claude-haiku-4.5"
    assert call.input_tokens == 1000
    assert call.output_tokens == 200
    assert call.latency_ms == 1234


def test_summarize_discussion_propagates_call_metrics(monkeypatch):
    def fake_complete(system, user):
        return LLMCallResult(
            content="**Avis positifs** :\n- ok",
            model="z-ai/glm-4.6:free",
            input_tokens=300,
            output_tokens=80,
            latency_ms=900,
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary_markdown, call = summarize_discussion("commentaires", "titre")
    assert summary_markdown.startswith("**Avis positifs**")
    assert call.model == "z-ai/glm-4.6:free"
    assert call.input_tokens == 300
    assert call.output_tokens == 80
    assert call.latency_ms == 900


def test_compose_body_omits_count_when_zero():
    body = compose_body(
        article_summary=None,
        discussion_summary="**Confirmations** :\n- yes",
        discussion_comment_count=0,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    assert "## Discussion sur Hacker News\n" in body
    assert "commentaires analysés" not in body
