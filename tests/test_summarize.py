from app.summarize import _split_title_and_summary


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
