from dataclasses import dataclass

import pytest

from app import fetch_article as fetch_article_module
from app.fetch_article import (
    _collect_noscript_text,
    _extract_image_url,
    _extract_youtube_video_id,
    _is_js_required_notice,
    _NoscriptCollector,
    fetch_article,
)
from app.models import ContentSource


@dataclass
class _FakeSnippet:
    text: str


class _FakeTranscriptApi:
    def __init__(self, snippets=None, exc=None):
        self._snippets = snippets or []
        self._exc = exc

    def fetch(self, video_id, languages=None):  # noqa: ARG002
        if self._exc is not None:
            raise self._exc
        return self._snippets


def _patch_transcript_api(monkeypatch, *, snippets=None, exc=None):
    fake = _FakeTranscriptApi(snippets=snippets, exc=exc)
    monkeypatch.setattr(fetch_article_module, "YouTubeTranscriptApi", lambda: fake)


def test_http_error_falls_back_to_feed_summary(httpx_mock):
    httpx_mock.add_response(url="https://example.com/a", status_code=500)
    result = fetch_article("https://example.com/a", feed_fallback="summary from RSS")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == "summary from RSS"


def test_non_html_content_type_falls_back_to_feed_summary(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/paper.pdf",
        status_code=200,
        headers={"content-type": "application/pdf"},
        content=b"%PDF-1.4 binary blob",
    )
    result = fetch_article(
        "https://example.com/paper.pdf", feed_fallback="summary from RSS"
    )
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == "summary from RSS"


def test_empty_extraction_falls_back_to_feed_summary(httpx_mock):
    # trafilatura returns None/empty for pages with no extractable main content.
    # An almost-empty HTML body is a reliable way to trigger that branch.
    httpx_mock.add_response(
        url="https://example.com/empty",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body></body></html>",
    )
    result = fetch_article(
        "https://example.com/empty", feed_fallback="summary from RSS"
    )
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == "summary from RSS"


def test_successful_extraction_returns_extracted_source(httpx_mock):
    html = """
    <html><body>
      <article>
        <h1>Titre principal</h1>
        <p>Premier paragraphe de l'article avec du contenu substantiel et réel.</p>
        <p>Deuxième paragraphe contenant des informations utiles à extraire.</p>
      </article>
    </body></html>
    """
    httpx_mock.add_response(
        url="https://example.com/good",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article(
        "https://example.com/good", feed_fallback="summary from RSS"
    )
    assert result.source == ContentSource.EXTRACTED
    assert "paragraphe" in result.text
    assert "summary from RSS" not in result.text


def test_extract_image_url_picks_og_image():
    html = """
    <html><head>
      <meta property="og:image" content="https://cdn.example.com/hero.jpg">
    </head><body>x</body></html>
    """
    assert _extract_image_url(html, "https://example.com/a") == "https://cdn.example.com/hero.jpg"


def test_extract_image_url_resolves_relative_urls():
    html = '<meta property="og:image" content="/images/hero.jpg">'
    assert _extract_image_url(html, "https://example.com/blog/post-1") == (
        "https://example.com/images/hero.jpg"
    )


def test_extract_image_url_falls_back_to_twitter_image():
    html = '<meta name="twitter:image" content="https://cdn.example.com/tw.jpg">'
    assert _extract_image_url(html, "https://example.com/a") == (
        "https://cdn.example.com/tw.jpg"
    )


def test_extract_image_url_prefers_og_over_twitter():
    html = (
        '<meta property="og:image" content="https://a.example.com/og.jpg">'
        '<meta name="twitter:image" content="https://b.example.com/tw.jpg">'
    )
    assert _extract_image_url(html, "https://example.com/a") == (
        "https://a.example.com/og.jpg"
    )


def test_extract_image_url_returns_none_when_absent():
    html = "<html><head><title>no meta</title></head><body>x</body></html>"
    assert _extract_image_url(html, "https://example.com/a") is None


def test_noscript_collector_concatenates_blocks():
    collector = _NoscriptCollector()
    collector.feed(
        "<html><body>"
        "<noscript>Enable JS.</noscript>"
        "<div>ignored</div>"
        "<noscript>Another notice.</noscript>"
        "</body></html>"
    )
    assert collector.text() == "Enable JS. Another notice."


def test_noscript_collector_handles_nesting():
    collector = _NoscriptCollector()
    collector.feed(
        "<noscript>outer <noscript>inner</noscript> outer-tail</noscript>"
    )
    text = collector.text()
    assert "outer" in text
    assert "inner" in text


def test_noscript_collector_empty_when_absent():
    collector = _NoscriptCollector()
    collector.feed("<html><body><p>no noscript here</p></body></html>")
    assert collector.text() == ""


def test_collect_noscript_text_strips_malformed_html():
    # HTMLParser tolerates malformed input; the helper should not raise.
    text = _collect_noscript_text("<noscript>hello</noscript")
    assert "hello" in text


def test_is_js_required_notice_exact_match():
    html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    extracted = "You need to enable JavaScript to run this app."
    assert _is_js_required_notice(extracted, html) is True


def test_is_js_required_notice_tolerates_trailing_punctuation():
    html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    extracted = "You need to enable JavaScript to run this app"
    assert _is_js_required_notice(extracted, html) is True


def test_is_js_required_notice_rejects_real_articles():
    html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "<article><p>A long article paragraph covering many topics.</p></article>"
        "</body></html>"
    )
    extracted = (
        "A long article paragraph covering many topics and going into a lot "
        "of detail about the subject matter at hand."
    )
    assert _is_js_required_notice(extracted, html) is False


def test_is_js_required_notice_false_without_noscript():
    html = "<html><body><p>short content</p></body></html>"
    assert _is_js_required_notice("short content", html) is False


def test_fetch_article_detects_js_required_noscript(httpx_mock):
    html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://social.example/@user/1",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://social.example/@user/1", feed_fallback="x")
    assert result.source == ContentSource.JS_REQUIRED
    assert result.text == ""


def test_fetch_article_captures_image_url(httpx_mock):
    html = """
    <html><head>
      <meta property="og:image" content="https://cdn.example.com/hero.jpg">
    </head><body>
      <article><p>Un paragraphe consistant pour trafilatura.</p></article>
    </body></html>
    """
    httpx_mock.add_response(
        url="https://example.com/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://example.com/article", feed_fallback="x")
    assert result.image_url == "https://cdn.example.com/hero.jpg"


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtube.com/watch?v=dQw4w9WgXcQ&t=42s", "dQw4w9WgXcQ"),
        ("https://m.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://music.youtube.com/watch?v=dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtu.be/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://youtu.be/dQw4w9WgXcQ?si=abc", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/shorts/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/embed/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/v/dQw4w9WgXcQ", "dQw4w9WgXcQ"),
        ("https://www.youtube.com/watch", None),
        ("https://www.youtube.com/watch?v=tooShort", None),
        ("https://www.youtube.com/channel/UC123", None),
        ("https://example.com/watch?v=dQw4w9WgXcQ", None),
        ("https://vimeo.com/12345", None),
    ],
)
def test_extract_youtube_video_id(url, expected):
    assert _extract_youtube_video_id(url) == expected


def test_fetch_article_youtube_returns_transcript(monkeypatch):
    _patch_transcript_api(
        monkeypatch,
        snippets=[
            _FakeSnippet(text="Bonjour tout le monde."),
            _FakeSnippet(text="  Aujourd'hui on parle de Python.  "),
            _FakeSnippet(text=""),
        ],
    )
    result = fetch_article(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        feed_fallback="summary from RSS",
    )
    assert result.source == ContentSource.VIDEO_TRANSCRIPT
    assert result.text == "Bonjour tout le monde. Aujourd'hui on parle de Python."
    assert result.image_url == "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"


def test_fetch_article_youtube_falls_back_when_transcript_unavailable(monkeypatch):
    _patch_transcript_api(monkeypatch, exc=RuntimeError("no transcript"))
    result = fetch_article(
        "https://youtu.be/dQw4w9WgXcQ",
        feed_fallback="summary from RSS",
    )
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == "summary from RSS"
    assert result.image_url == "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"


def test_fetch_article_youtube_falls_back_when_transcript_empty(monkeypatch):
    _patch_transcript_api(monkeypatch, snippets=[_FakeSnippet(text="   ")])
    result = fetch_article(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        feed_fallback="summary from RSS",
    )
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == "summary from RSS"
