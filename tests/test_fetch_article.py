import base64
from dataclasses import dataclass

import pytest

from app import fetch_article as fetch_article_module
from app.fetch_article import (
    _collect_noscript_text,
    _extract_image_url,
    _extract_mastodon_handle,
    _extract_pdf_text,
    _extract_tweet_id,
    _extract_youtube_video_id,
    _is_js_required_notice,
    _NoscriptCollector,
    fetch_article,
)
from app.models import ContentSource

# 587-byte minimal PDF containing the literal text "HN test PDF" on a
# single page. Hand-crafted so the suite does not depend on a fixture
# file. Parses cleanly with pypdfium2; if it ever stops doing so, the
# extraction unit test below will catch the regression.
_TINY_PDF_BYTES = base64.b64decode(
    "JVBERi0xLjQKMSAwIG9iago8PCAvVHlwZSAvQ2F0YWxvZyAvUGFnZXMgMiAwIFIgPj4KZW5kb2"
    "JqCjIgMCBvYmoKPDwgL1R5cGUgL1BhZ2VzIC9LaWRzIFszIDAgUl0gL0NvdW50IDEgPj4KZW5k"
    "b2JqCjMgMCBvYmoKPDwgL1R5cGUgL1BhZ2UgL1BhcmVudCAyIDAgUiAvTWVkaWFCb3ggWzAgMC"
    "A2MTIgNzkyXSAvQ29udGVudHMgNCAwIFIgL1Jlc291cmNlcyA8PCAvRm9udCA8PCAvRjEgNSAw"
    "IFIgPj4gPj4gPj4KZW5kb2JqCjQgMCBvYmoKPDwgL0xlbmd0aCA0NCA+PgpzdHJlYW0KQlQgL0"
    "YxIDI0IFRmIDEwMCA3MDAgVGQgKEhOIHRlc3QgUERGKSBUaiBFVAplbmRzdHJlYW0KZW5kb2Jq"
    "CjUgMCBvYmoKPDwgL1R5cGUgL0ZvbnQgL1N1YnR5cGUgL1R5cGUxIC9CYXNlRm9udCAvSGVsdm"
    "V0aWNhID4+CmVuZG9iagp4cmVmCjAgNgowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwMDkg"
    "MDAwMDAgbiAKMDAwMDAwMDA1OCAwMDAwMCBuIAowMDAwMDAwMTE1IDAwMDAwIG4gCjAwMDAwMD"
    "AyNDEgMDAwMDAgbiAKMDAwMDAwMDMzNCAwMDAwMCBuIAp0cmFpbGVyCjw8IC9TaXplIDYgL1Jv"
    "b3QgMSAwIFIgPj4Kc3RhcnR4cmVmCjQwNAolJUVPRgo="
)


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
    monkeypatch.setattr(
        fetch_article_module, "YouTubeTranscriptApi", lambda **_kwargs: fake
    )


def test_http_error_returns_empty_feed_fallback(httpx_mock):
    httpx_mock.add_response(url="https://example.com/a", status_code=500)
    result = fetch_article("https://example.com/a")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_non_html_content_type_returns_empty_feed_fallback(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/blob.bin",
        status_code=200,
        headers={"content-type": "application/octet-stream"},
        content=b"\x00\x01\x02 raw binary",
    )
    result = fetch_article("https://example.com/blob.bin")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


_FORESTER_XML_BODY = (
    '<?xml version="1.0" encoding="UTF-8"?>'
    '<?xml-stylesheet type="text/xsl" href="/forest/default.xsl"?>'
    '<fr:tree xmlns:fr="http://www.forester-notes.org"'
    ' xmlns:html="http://www.w3.org/1999/xhtml" root="false">'
    "<fr:frontmatter><fr:title text=\"A note\">A note</fr:title></fr:frontmatter>"
    "<fr:mainmatter>"
    "<html:p>Un paragraphe substantiel destiné à l'extraction du contenu principal"
    " de la note.</html:p>"
    "<html:p>Un second paragraphe contenant des phrases utiles pour faire dépasser"
    " le seuil de précision de l'extracteur.</html:p>"
    "<html:ul>"
    "<html:li>premier item de la liste avec assez de mots pour compter</html:li>"
    "<html:li>second item de la liste avec assez de mots pour compter</html:li>"
    "</html:ul>"
    "</fr:mainmatter>"
    "</fr:tree>"
)


def test_xml_forester_content_extracted(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/note.xml",
        status_code=200,
        headers={"content-type": "application/xml"},
        text=_FORESTER_XML_BODY,
    )
    result = fetch_article("https://example.com/note.xml")
    assert result.source == ContentSource.EXTRACTED
    assert "paragraphe substantiel" in result.text


def test_xml_text_xml_content_type_accepted(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/note2.xml",
        status_code=200,
        headers={"content-type": "text/xml; charset=utf-8"},
        text=_FORESTER_XML_BODY,
    )
    result = fetch_article("https://example.com/note2.xml")
    assert result.source == ContentSource.EXTRACTED
    assert "paragraphe substantiel" in result.text


def test_malformed_xml_returns_feed_fallback(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/broken.xml",
        status_code=200,
        headers={"content-type": "application/xml"},
        content=b"\x00\x01\x02 not valid xml at all",
    )
    result = fetch_article("https://example.com/broken.xml")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_rss_atom_content_type_still_rejected(httpx_mock):
    rss = (
        "<?xml version='1.0'?><rss version='2.0'><channel><title>x</title>"
        "<item><title>t</title><description>d</description></item></channel></rss>"
    )
    httpx_mock.add_response(
        url="https://example.com/feed.rss",
        status_code=200,
        headers={"content-type": "application/rss+xml"},
        text=rss,
    )
    result = fetch_article("https://example.com/feed.rss")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_empty_extraction_returns_empty_feed_fallback(httpx_mock):
    # trafilatura returns None/empty for pages with no extractable main content.
    # An almost-empty HTML body is a reliable way to trigger that branch.
    httpx_mock.add_response(
        url="https://example.com/empty",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body></body></html>",
    )
    result = fetch_article("https://example.com/empty")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


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
    result = fetch_article("https://example.com/good")
    assert result.source == ContentSource.EXTRACTED
    assert "paragraphe" in result.text


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
        url="https://example.com/spa",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://example.com/spa")
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
    result = fetch_article("https://example.com/article")
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
    result = fetch_article("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert result.source == ContentSource.VIDEO_TRANSCRIPT
    assert result.text == "Bonjour tout le monde. Aujourd'hui on parle de Python."
    assert result.image_url == "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"


def test_fetch_article_youtube_falls_back_when_transcript_unavailable(monkeypatch):
    _patch_transcript_api(monkeypatch, exc=RuntimeError("no transcript"))
    result = fetch_article("https://youtu.be/dQw4w9WgXcQ")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""
    assert result.image_url == "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"


def test_fetch_article_youtube_falls_back_when_transcript_empty(monkeypatch):
    _patch_transcript_api(monkeypatch, snippets=[_FakeSnippet(text="   ")])
    result = fetch_article("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://x.com/jack/status/20", ("jack", "20")),
        ("https://twitter.com/jack/status/20", ("jack", "20")),
        ("https://mobile.x.com/jack/status/20", ("jack", "20")),
        ("https://mobile.twitter.com/jack/status/20", ("jack", "20")),
        ("https://www.x.com/jack/status/20", ("jack", "20")),
        ("https://x.com/jack/status/20/photo/1", ("jack", "20")),
        ("https://x.com/jack/status/20?s=20", ("jack", "20")),
        ("https://x.com/jack", None),
        ("https://x.com/i/lists/123", None),
        ("https://x.com/search?q=foo", None),
        ("https://example.com/jack/status/20", None),
        ("https://x.com/jack/status/notanumber", None),
    ],
)
def test_extract_tweet_id(url, expected):
    assert _extract_tweet_id(url) == expected


def _fxtwitter_payload(text="Hello world", screen_name="jack",
                       name="Jack", photos=None, quote=None):
    tweet: dict = {
        "text": text,
        "author": {"screen_name": screen_name, "name": name},
    }
    if photos is not None:
        tweet["media"] = {"photos": photos}
    if quote is not None:
        tweet["quote"] = quote
    return {"code": 200, "tweet": tweet}


def test_fetch_article_tweet_via_fxtwitter(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/jack/status/20",
        status_code=200,
        json=_fxtwitter_payload(
            text="Just setting up my twttr",
            screen_name="jack",
            name="jack",
            photos=[{"url": "https://pbs.twimg.com/media/abc.jpg"}],
        ),
    )
    result = fetch_article("https://x.com/jack/status/20")
    assert result.source == ContentSource.TWEET
    assert "@jack" in result.text
    assert "Just setting up my twttr" in result.text
    assert result.image_url == "https://pbs.twimg.com/media/abc.jpg"


def test_fetch_article_tweet_includes_quote(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/alice/status/100",
        status_code=200,
        json=_fxtwitter_payload(
            text="Look at this take",
            screen_name="alice",
            name="Alice",
            quote={
                "text": "Bold claim incoming",
                "author": {"screen_name": "bob"},
            },
        ),
    )
    result = fetch_article("https://twitter.com/alice/status/100")
    assert result.source == ContentSource.TWEET
    assert "@bob: Bold claim incoming" in result.text


def test_fetch_article_tweet_falls_back_to_vxtwitter(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/alice/status/200",
        status_code=500,
    )
    httpx_mock.add_response(
        url="https://api.vxtwitter.com/alice/status/200",
        status_code=200,
        json={
            "text": "Recovered text",
            "user_screen_name": "alice",
            "user_name": "Alice",
            "media_extended": [{"url": "https://pbs.twimg.com/v/x.jpg"}],
        },
    )
    result = fetch_article("https://x.com/alice/status/200")
    assert result.source == ContentSource.TWEET
    assert "@alice" in result.text
    assert "Recovered text" in result.text
    assert result.image_url == "https://pbs.twimg.com/v/x.jpg"


def test_fetch_article_tweet_both_providers_fail(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/dead/status/300", status_code=500
    )
    httpx_mock.add_response(
        url="https://api.vxtwitter.com/dead/status/300", status_code=500
    )
    result = fetch_article("https://x.com/dead/status/300")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_tweet_deleted_returns_feed_fallback(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/gone/status/400",
        status_code=200,
        json={"code": 404, "message": "Tweet not found"},
    )
    httpx_mock.add_response(
        url="https://api.vxtwitter.com/gone/status/400", status_code=404
    )
    result = fetch_article("https://x.com/gone/status/400")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_tweet_empty_text_returns_feed_fallback(httpx_mock):
    httpx_mock.add_response(
        url="https://api.fxtwitter.com/quiet/status/500",
        status_code=200,
        json=_fxtwitter_payload(text="", screen_name="quiet", name="Quiet"),
    )
    httpx_mock.add_response(
        url="https://api.vxtwitter.com/quiet/status/500",
        status_code=200,
        json={"text": "", "user_screen_name": "quiet", "user_name": "Quiet"},
    )
    result = fetch_article("https://x.com/quiet/status/500")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_retries_via_proxy_on_http_error(httpx_mock, isolated_settings):
    isolated_settings.webshare_proxy_username = "demo"
    isolated_settings.webshare_proxy_password = "secret"
    httpx_mock.add_response(
        url="https://example.com/blocked",
        status_code=403,
    )
    html = (
        "<html><body><article>"
        "<p>Premier paragraphe substantiel récupéré via le proxy résidentiel.</p>"
        "<p>Second paragraphe avec assez de contenu pour passer le seuil de précision.</p>"
        "</article></body></html>"
    )
    httpx_mock.add_response(
        url="https://example.com/blocked",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://example.com/blocked")
    assert result.source == ContentSource.EXTRACTED
    assert "paragraphe substantiel" in result.text


def test_fetch_article_does_not_retry_when_proxy_creds_missing(
    httpx_mock, isolated_settings
):
    isolated_settings.webshare_proxy_username = ""
    isolated_settings.webshare_proxy_password = ""
    httpx_mock.add_response(
        url="https://example.com/blocked-no-creds",
        status_code=403,
    )
    result = fetch_article("https://example.com/blocked-no-creds")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_falls_back_when_proxy_also_fails(httpx_mock, isolated_settings):
    isolated_settings.webshare_proxy_username = "demo"
    isolated_settings.webshare_proxy_password = "secret"
    httpx_mock.add_response(
        url="https://example.com/double-blocked",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://example.com/double-blocked",
        status_code=403,
    )
    result = fetch_article("https://example.com/double-blocked")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://social.hails.org/@hailey/116446826733136456",
         ("hailey", "social.hails.org")),
        ("https://partyon.xyz/@nullagent/116499715071759135",
         ("nullagent", "partyon.xyz")),
        ("https://grapheneos.social/@GrapheneOS/116550899908879585",
         ("GrapheneOS", "grapheneos.social")),
        ("https://social.example/@user/12345/", ("user", "social.example")),
        # Twitter pattern — different shape, must not match.
        ("https://x.com/jack/status/20", None),
        # Mastodon-looking but with extra path segment — skip.
        ("https://social.example/@user/12345/photo/1", None),
        # No status id.
        ("https://social.example/@user", None),
        # Username without leading @ — not a Mastodon post URL.
        ("https://social.example/user/12345", None),
    ],
)
def test_extract_mastodon_handle(url, expected):
    assert _extract_mastodon_handle(url) == expected


_MASTODON_NOTE = {
    "@context": ["https://www.w3.org/ns/activitystreams"],
    "type": "Note",
    "id": "https://social.example/users/hailey/statuses/12345",
    "attributedTo": "https://social.example/users/hailey",
    "content": "<p>Un message fédiveré assez long pour être intéressant.</p>",
    "published": "2026-05-01T10:00:00Z",
}


def test_fetch_article_mastodon_returns_extracted(httpx_mock):
    httpx_mock.add_response(
        url="https://social.example/@hailey/12345",
        status_code=200,
        json=_MASTODON_NOTE,
        match_headers={"Accept": "application/activity+json"},
    )
    result = fetch_article("https://social.example/@hailey/12345")
    assert result.source == ContentSource.EXTRACTED
    assert "fédiveré" in result.text
    assert "@hailey@social.example" in result.text


def test_fetch_article_mastodon_strips_html_and_unescapes(httpx_mock):
    note = {**_MASTODON_NOTE, "content": "<p>Voir &lt;ici&gt; le détail.</p>"}
    httpx_mock.add_response(
        url="https://social.example/@hailey/12346",
        json=note,
    )
    result = fetch_article("https://social.example/@hailey/12346")
    assert "<ici>" in result.text
    assert "<p>" not in result.text


def test_fetch_article_mastodon_extracts_first_image(httpx_mock):
    note = {
        **_MASTODON_NOTE,
        "attachment": [
            {"type": "Document", "mediaType": "image/png",
             "url": "https://cdn.social.example/abc.png"},
            {"type": "Document", "mediaType": "image/jpeg",
             "url": "https://cdn.social.example/second.jpg"},
        ],
    }
    httpx_mock.add_response(
        url="https://social.example/@hailey/12347",
        json=note,
    )
    result = fetch_article("https://social.example/@hailey/12347")
    assert result.image_url == "https://cdn.social.example/abc.png"


def test_fetch_article_mastodon_falls_back_on_http_error(httpx_mock):
    httpx_mock.add_response(
        url="https://social.example/@hailey/dead",
        status_code=404,
    )
    result = fetch_article("https://social.example/@hailey/dead")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_mastodon_falls_back_on_empty_content(httpx_mock):
    note = {**_MASTODON_NOTE, "content": ""}
    httpx_mock.add_response(
        url="https://social.example/@hailey/empty",
        json=note,
    )
    result = fetch_article("https://social.example/@hailey/empty")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_retries_extraction_with_permissive_mode(
    httpx_mock, monkeypatch
):
    httpx_mock.add_response(
        url="https://example.com/sparse",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body><article><p>x</p></article></body></html>",
    )
    calls: list[dict] = []

    def fake_extract(_html, **kwargs):
        calls.append(kwargs)
        if kwargs.get("favor_precision"):
            return None
        return "Recovered prose via permissive mode."

    monkeypatch.setattr(
        fetch_article_module.trafilatura, "extract", fake_extract
    )
    result = fetch_article("https://example.com/sparse")
    assert result.source == ContentSource.EXTRACTED
    assert "Recovered prose" in result.text
    assert len(calls) == 2
    # First call is the strict precision attempt; the retry must not be
    # precision-favored (otherwise it would behave identically).
    assert calls[0].get("favor_precision") is True
    assert calls[1].get("favor_precision") is not True


def test_fetch_article_falls_back_when_both_extraction_modes_empty(
    httpx_mock, monkeypatch
):
    httpx_mock.add_response(
        url="https://example.com/nothing",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body></body></html>",
    )
    monkeypatch.setattr(
        fetch_article_module.trafilatura,
        "extract",
        lambda _html, **_kwargs: None,
    )
    result = fetch_article("https://example.com/nothing")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_returns_text_plain_verbatim(httpx_mock):
    advisory = (
        "FreeBSD-SA-26:13.exec Security Advisory\n"
        "The FreeBSD Project\n\n"
        "Topic: Improper handling of execve(2) flags.\n"
        "Affected: All currently supported versions of FreeBSD.\n"
    )
    httpx_mock.add_response(
        url="https://example.com/advisory.txt",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=advisory,
    )
    result = fetch_article("https://example.com/advisory.txt")
    assert result.source == ContentSource.EXTRACTED
    assert "FreeBSD-SA-26:13" in result.text


def test_fetch_article_empty_text_plain_falls_back(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/empty.txt",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text="   \n  ",
    )
    result = fetch_article("https://example.com/empty.txt")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_extract_pdf_text_returns_text_for_valid_pdf():
    assert _extract_pdf_text(_TINY_PDF_BYTES) == "HN test PDF"


def test_extract_pdf_text_returns_none_on_corrupt_bytes():
    assert _extract_pdf_text(b"%PDF-1.4 not a real document") is None


def test_extract_pdf_text_returns_none_on_empty_input():
    assert _extract_pdf_text(b"") is None


def test_fetch_article_extracts_pdf_content(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/paper.pdf",
        status_code=200,
        headers={"content-type": "application/pdf"},
        content=_TINY_PDF_BYTES,
    )
    result = fetch_article("https://example.com/paper.pdf")
    assert result.source == ContentSource.EXTRACTED
    assert "HN test PDF" in result.text


def test_fetch_article_corrupt_pdf_falls_back(httpx_mock):
    httpx_mock.add_response(
        url="https://example.com/broken.pdf",
        status_code=200,
        headers={"content-type": "application/pdf"},
        content=b"%PDF-1.4 garbage",
    )
    result = fetch_article("https://example.com/broken.pdf")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""
