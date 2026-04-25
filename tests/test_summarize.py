import pytest

from app import summarize
from app.llm import LLMCallResult
from app.summarize import (
    LLMOutputError,
    _parse_article_response,
    _parse_discussion_response,
    _render_discussion_markdown,
    _sanitize_llm_markdown,
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


def test_parse_article_response_raises_on_invalid_json():
    with pytest.raises(LLMOutputError):
        _parse_article_response("Juste du texte sans JSON")


def test_parse_article_response_raises_on_missing_summary():
    with pytest.raises(LLMOutputError):
        _parse_article_response('{"title": "un titre"}')


def test_parse_article_response_raises_on_non_object_top_level():
    with pytest.raises(LLMOutputError):
        _parse_article_response('["array", "not", "object"]')


def test_parse_article_response_missing_title_keeps_summary():
    text = '{"summary": "le corps"}'
    title, summary = _parse_article_response(text)
    assert title is None
    assert summary == "le corps"


def test_parse_article_response_accepts_markdown_json_fence():
    text = (
        "```json\n"
        '{"title": "titre", "summary": "corps"}\n'
        "```"
    )
    title, summary = _parse_article_response(text)
    assert title == "titre"
    assert summary == "corps"


def test_parse_article_response_accepts_bare_markdown_fence():
    text = (
        "```\n"
        '{"title": "titre", "summary": "corps"}\n'
        "```"
    )
    title, summary = _parse_article_response(text)
    assert title == "titre"
    assert summary == "corps"


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
    captured: dict = {}

    def fake_complete(system, user, *, json=False):
        captured["json"] = json
        return LLMCallResult(
            content='{"pros": ["ok"], "cons": ["bof"]}',
            model="z-ai/glm-4.6:free",
            input_tokens=300,
            output_tokens=80,
            latency_ms=900,
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary_markdown, call = summarize_discussion("commentaires", "titre")
    assert captured["json"] is True
    assert summary_markdown.startswith("**Avis positifs**")
    assert "**Avis négatifs**" in summary_markdown
    assert "- ok" in summary_markdown
    assert "- bof" in summary_markdown
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


def test_compose_body_inserts_top_comments_between_discussion_and_footer():
    top_md = (
        "**Commentaires les plus plébiscités** :\n\n"
        "- [alice](https://news.ycombinator.com/item?id=1) : « hello »"
    )
    body = compose_body(
        article_summary=None,
        discussion_summary="**Avis positifs** :\n- yes\n\n**Avis négatifs** :\n- no",
        discussion_comment_count=3,
        top_comments_markdown=top_md,
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=1",
    )
    assert "**Commentaires les plus plébiscités**" in body
    assert body.index("**Avis négatifs**") < body.index("**Commentaires les plus plébiscités**")
    assert body.index("**Commentaires les plus plébiscités**") < body.index("[Article original]")
    assert "[alice](https://news.ycombinator.com/item?id=1)" in body


def test_summarize_article_wraps_inputs_in_xml_tags(monkeypatch):
    captured: dict = {}

    def fake_complete(system, user, *, json=False):
        captured["system"] = system
        captured["user"] = user
        return _call_result('{"title": "t", "summary": "s"}')

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summarize_article("texte hostile", "Titre brut")
    assert "<original_title>" in captured["user"]
    assert "Titre brut" in captured["user"]
    assert "<content_to_summarize>" in captured["user"]
    assert "texte hostile" in captured["user"]
    assert "fournies par des tiers non fiables" not in captured["user"]
    assert "tiers non fiables" in captured["system"]


def test_summarize_discussion_wraps_inputs_in_xml_tags(monkeypatch):
    captured: dict = {}

    def fake_complete(system, user, *, json=False):
        captured["system"] = system
        captured["user"] = user
        return _call_result('{"pros": [], "cons": []}')

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summarize_discussion("commentaires hostiles", "Titre")
    assert "<article_title>" in captured["user"]
    assert "<comments_to_synthesize>" in captured["user"]
    assert "commentaires hostiles" in captured["user"]
    assert "tiers non fiables" in captured["system"]


def test_translate_title_wraps_input_in_xml_tag(monkeypatch):
    captured: dict = {}

    def fake_complete(system, user):
        captured["system"] = system
        captured["user"] = user
        return _call_result("titre traduit")

    monkeypatch.setattr(summarize, "complete", fake_complete)
    translate_title("Hostile Title")
    assert "<title_to_translate>" in captured["user"]
    assert "Hostile Title" in captured["user"]
    assert "tiers non fiables" in captured["system"]


def test_summarize_article_strips_images_from_summary(monkeypatch):
    def fake_complete(system, user, *, json=False):
        return _call_result(
            '{"title": "t", "summary": "intro\\n\\n- ok ![tracker](https://evil/p.png) ici"}'
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary, _ = summarize_article("texte", "titre")
    assert "![tracker]" not in summary.summary_markdown
    assert "https://evil" not in summary.summary_markdown
    assert "intro" in summary.summary_markdown
    assert "ok" in summary.summary_markdown


def test_summarize_article_strips_links_from_summary(monkeypatch):
    def fake_complete(system, user, *, json=False):
        return _call_result(
            '{"title": "t", "summary": "voir [clic ici](https://evil/x) pour plus"}'
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    summary, _ = summarize_article("texte", "titre")
    assert "[clic ici]" not in summary.summary_markdown
    assert "https://evil" not in summary.summary_markdown
    assert "clic ici" in summary.summary_markdown


def test_summarize_article_raises_on_malformed_llm_output(monkeypatch):
    def fake_complete(system, user, *, json=False):
        return _call_result("not even close to JSON")

    monkeypatch.setattr(summarize, "complete", fake_complete)
    with pytest.raises(LLMOutputError):
        summarize_article("texte", "titre")


def test_summarize_discussion_raises_on_malformed_llm_output(monkeypatch):
    def fake_complete(system, user, *, json=False):
        return _call_result('{"pros": "not a list", "cons": []}')

    monkeypatch.setattr(summarize, "complete", fake_complete)
    with pytest.raises(LLMOutputError):
        summarize_discussion("commentaires", "titre")


def test_summarize_discussion_strips_images_and_links_from_bullets(monkeypatch):
    def fake_complete(system, user, *, json=False):
        return _call_result(
            '{"pros": ["voir [ici](https://evil/x) pour détail",'
            ' "image ![pixel](https://evil/p.png) intégrée"],'
            ' "cons": []}'
        )

    monkeypatch.setattr(summarize, "complete", fake_complete)
    markdown, _ = summarize_discussion("commentaires", "titre")
    assert "https://evil" not in markdown
    assert "![pixel]" not in markdown
    assert "[ici]" not in markdown
    assert "ici" in markdown
    assert "pixel" not in markdown  # alt text is dropped with the image


def test_render_discussion_markdown_keeps_french_headings():
    output = _render_discussion_markdown(["pour"], ["contre"])
    assert "**Avis positifs** :" in output
    assert "**Avis négatifs** :" in output
    assert "- pour" in output
    assert "- contre" in output


def test_render_discussion_markdown_renders_empty_sections_as_heading_only():
    output = _render_discussion_markdown([], [])
    assert output == "**Avis positifs** :\n\n**Avis négatifs** :"


def test_parse_discussion_response_drops_blank_bullets():
    pros, cons = _parse_discussion_response('{"pros": ["a", "  ", "b"], "cons": []}')
    assert pros == ["a", "b"]
    assert cons == []


def test_parse_discussion_response_raises_on_non_string_bullet():
    with pytest.raises(LLMOutputError):
        _parse_discussion_response('{"pros": ["a", 42], "cons": []}')


def test_parse_discussion_response_raises_on_missing_key():
    with pytest.raises(LLMOutputError):
        _parse_discussion_response('{"pros": ["a"]}')


def test_sanitize_llm_markdown_removes_image_before_link_in_image_syntax():
    # `![alt](url)` must be removed entirely, not collapsed to `!alt` by the
    # link regex matching the inner `[alt](url)`.
    out = _sanitize_llm_markdown("texte ![alt](https://evil/p.png) suite")
    assert "alt" not in out
    assert "https://evil" not in out
    assert "texte" in out
    assert "suite" in out


def test_compose_body_omits_top_comments_when_none_or_empty():
    for top_md in (None, "", "   \n  "):
        body = compose_body(
            article_summary=None,
            discussion_summary="**Avis positifs** :\n- yes",
            top_comments_markdown=top_md,
            url="https://example.com/a",
            hn_url="https://news.ycombinator.com/item?id=1",
        )
        assert "Commentaires les plus plébiscités" not in body
