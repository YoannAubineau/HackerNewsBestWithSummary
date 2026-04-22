from app.summarize import _split_title_and_summary, compose_body


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


def test_compose_body_keeps_hn_id_out_of_the_body():
    # The HN id shows up only in the XSL-rendered browser view (injected
    # via JS in feed.xsl). It must stay out of the body stored in the .md
    # so Feedly-style readers get the unchanged two-link footer line.
    body = compose_body(
        article_summary=None,
        discussion_summary="**Confirmations** :\n- x",
        url="https://example.com/a",
        hn_url="https://news.ycombinator.com/item?id=4242",
    )
    assert "HN #" not in body
    assert "[Article original](https://example.com/a)" in body
    assert "[Discussion HN](https://news.ycombinator.com/item?id=4242)" in body
