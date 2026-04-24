from app import summarize
from app.llm import LLMCallResult
from app.summarize import (
    _split_title_and_summary,
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


def test_splits_well_formed_response():
    text = (
        "## Titre\n"
        "un titre factuel réécrit\n"
        "\n"
        "## Résumé\n"
        "**TL;DR** : phrase.\n"
        "- bullet 1\n"
        "- bullet 2"
    )
    title, summary = _split_title_and_summary(text)
    assert title == "un titre factuel réécrit"
    assert summary.startswith("**TL;DR**")
    assert "bullet 2" in summary


def test_handles_leading_whitespace_and_extra_lines():
    text = (
        "\n## Titre\n\n  un titre   \n\n## Résumé\n\nle corps\n"
    )
    title, summary = _split_title_and_summary(text)
    assert title == "un titre"
    assert summary == "le corps"


def test_returns_none_title_when_format_unexpected():
    text = "Juste un résumé sans les bonnes en-têtes"
    title, summary = _split_title_and_summary(text)
    assert title is None
    assert summary == text


def test_returns_none_title_if_sections_out_of_order():
    text = "## Résumé\ncorps\n\n## Titre\nun titre"
    title, summary = _split_title_and_summary(text)
    assert title is None
    assert "## Titre" in summary


def test_recovers_title_when_titre_header_is_missing():
    text = (
        "## OpenAI annonce GPT-5.5\n"
        "\n"
        "## Résumé\n"
        "Le corps du résumé."
    )
    title, summary = _split_title_and_summary(text)
    assert title == "OpenAI annonce GPT-5.5"
    assert summary == "Le corps du résumé."


def test_recovers_plain_title_line_when_titre_header_is_missing():
    text = "OpenAI annonce GPT-5.5\n\n## Résumé\nLe corps."
    title, summary = _split_title_and_summary(text)
    assert title == "OpenAI annonce GPT-5.5"
    assert summary == "Le corps."


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
    def fake_complete(system, user):
        return LLMCallResult(
            content="## Titre\nun titre\n\n## Résumé\n- point",
            model="anthropic/claude-haiku-4.5",
            input_tokens=1000,
            output_tokens=200,
            latency_ms=1234,
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary, call = summarize_article("texte", "titre original")
    assert summary.rewritten_title == "un titre"
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
