import base64
from dataclasses import dataclass

import pytest

from app import fetch_article as fetch_article_module
from app.fetch_article import (
    _collect_noscript_text,
    _extract_github_pr_issue,
    _extract_image_url,
    _extract_mastodon_handle,
    _extract_pdf_text,
    _extract_substack_slug,
    _extract_tweet_id,
    _extract_youtube_video_id,
    _is_cloudflare_challenge,
    _is_cookie_banner_only,
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


def test_is_cloudflare_challenge_matches_cf_chl_opt_marker():
    # The challenge JS always sets `window._cf_chl_opt = {...}` — the
    # most specific signal across challenge variants.
    html = (
        "<html><body>"
        "<script>(function(){window._cf_chl_opt = {cFPWv:'g',cH:'abc'};})();</script>"
        "</body></html>"
    )
    assert _is_cloudflare_challenge(html) is True


def test_is_cloudflare_challenge_matches_user_visible_string():
    html = (
        "<html><body>"
        "<h1>Enable JavaScript and cookies to continue</h1>"
        "</body></html>"
    )
    assert _is_cloudflare_challenge(html) is True


def test_is_cloudflare_challenge_false_on_normal_html():
    html = (
        "<html><head><title>Real article</title></head><body>"
        "<article><p>Content about JavaScript and cookies in browsers.</p></article>"
        "</body></html>"
    )
    assert _is_cloudflare_challenge(html) is False


def test_fetch_article_detects_cloudflare_challenge(httpx_mock):
    # Faithful shape of the body curl returned for epicfurious.com:
    # tiny page, `_cf_chl_opt` JS variable, the user-visible string.
    html = (
        "<!DOCTYPE html><html><body>"
        "<h1>Enable JavaScript and cookies to continue</h1>"
        "<script>(function(){window._cf_chl_opt = {cFPWv:'g',cH:'P5u8'};})();"
        "</script></body></html>"
    )
    httpx_mock.add_response(
        url="https://example.com/cf",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://example.com/cf")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


@pytest.mark.parametrize(
    "extracted",
    [
        "We use cookies to improve your experience. Accept all cookies",
        "Manage cookie preferences and continue",
        "Accept all cookies\nReject all cookies",
        "Nous utilisons des cookies. Accepter tous les cookies. Refuser tous les cookies.",
        "Gérer mes préférences cookies",
    ],
)
def test_is_cookie_banner_only_matches_consent_phrases(extracted):
    assert _is_cookie_banner_only(extracted) is True


@pytest.mark.parametrize(
    "extracted",
    [
        # Real article that happens to mention cookies — must not match.
        "This article explains how HTTP cookies work in modern browsers"
        " and what session cookies are used for.",
        # Short technical note about cookie security; no consent UI.
        "Setting the Secure flag on cookies is mandatory for HTTPS.",
        # Empty / blank input.
        "",
        "   \n  ",
    ],
)
def test_is_cookie_banner_only_false_on_real_content(extracted):
    assert _is_cookie_banner_only(extracted) is False


def test_fetch_article_drops_cookie_banner_to_feed_fallback(httpx_mock):
    # trafilatura legitimately extracts the visible body of a cookie
    # consent wall when the publisher's CMP is rendered server-side
    # (epicfurious-style scenarios beyond the Cloudflare path). The
    # extracted text is a banner, not the article — must not reach the
    # LLM as if it were content.
    html = (
        "<html><body><article>"
        "<p>We use cookies to improve your experience. Accept all cookies"
        " or manage cookie preferences below.</p>"
        "</article></body></html>"
    )
    httpx_mock.add_response(
        url="https://example.com/cookie-wall",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    result = fetch_article("https://example.com/cookie-wall")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


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


def test_is_js_app_shell_detects_spa_shell():
    shell = (
        "<html><head><title>Click</title></head>"
        "<body><main></main><script src='bundle.js'></script></body></html>"
    )
    assert fetch_article_module._is_js_app_shell(shell)


def test_is_js_app_shell_false_when_body_has_text():
    page = (
        "<html><body><p>Du vrai texte d'article ici.</p>"
        "<script src='a.js'></script></body></html>"
    )
    assert not fetch_article_module._is_js_app_shell(page)


def test_is_js_app_shell_false_without_script():
    assert not fetch_article_module._is_js_app_shell(
        "<html><body><main></main></body></html>"
    )


def test_fetch_article_reports_js_required_for_app_shell(httpx_mock):
    # An SPA shell: empty <main> mount + bundle script, no static prose and
    # no <noscript>. trafilatura extracts nothing; the reason must say JS,
    # not the generic "extraction failed". (clickclickclick.click in the wild.)
    shell = (
        "<html><head><title>Click</title></head>"
        "<body><main></main>"
        "<script type='text/javascript' src='bundle.js'></script>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://clickclickclick.example/",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=shell,
    )
    result = fetch_article("https://clickclickclick.example/")
    assert result.source == ContentSource.JS_REQUIRED
    assert result.failure_reason == "JavaScript required"
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


@pytest.mark.parametrize(
    "url,expected",
    [
        (
            "https://github.com/oven-sh/bun/pull/30412",
            ("oven-sh", "bun", "pull", "30412"),
        ),
        (
            "https://github.com/oven-sh/bun/issues/123",
            ("oven-sh", "bun", "issues", "123"),
        ),
        (
            "https://github.com/oven-sh/bun/pull/30412/files",
            ("oven-sh", "bun", "pull", "30412"),
        ),
        (
            "https://www.github.com/o/r/pull/1",
            ("o", "r", "pull", "1"),
        ),
        ("https://github.com/oven-sh/bun", None),
        ("https://github.com/oven-sh/bun/pulls", None),
        ("https://github.com/oven-sh/bun/discussions/1", None),
        ("https://gist.github.com/anon/abc/pull/1", None),
        ("https://example.com/oven-sh/bun/pull/1", None),
    ],
)
def test_extract_github_pr_issue(url, expected):
    assert _extract_github_pr_issue(url) == expected


def test_fetch_article_github_pr_via_api(httpx_mock):
    httpx_mock.add_response(
        url="https://api.github.com/repos/oven-sh/bun/pulls/30412",
        status_code=200,
        json={
            "title": "Rewrite Bun in Rust",
            "body": "This PR rewrites Bun's runtime in Rust.\n\nDetails follow.",
            "user": {"login": "Jarred-Sumner"},
        },
    )
    result = fetch_article("https://github.com/oven-sh/bun/pull/30412")
    assert result.source == ContentSource.EXTRACTED
    assert "Rewrite Bun in Rust" in result.text
    assert "This PR rewrites Bun's runtime in Rust." in result.text
    assert "@Jarred-Sumner" in result.text
    assert "PR #30412" in result.text


def test_fetch_article_github_issue_via_api(httpx_mock):
    httpx_mock.add_response(
        url="https://api.github.com/repos/o/r/issues/7",
        status_code=200,
        json={
            "title": "Bug: thing crashes",
            "body": "Steps to reproduce: …",
            "user": {"login": "alice"},
        },
    )
    result = fetch_article("https://github.com/o/r/issues/7")
    assert result.source == ContentSource.EXTRACTED
    assert "Bug: thing crashes" in result.text
    assert "Steps to reproduce" in result.text
    assert "Issue #7" in result.text


def test_fetch_article_github_empty_body_falls_back(httpx_mock):
    # A PR with no description is too thin to summarize. Don't pretend.
    httpx_mock.add_response(
        url="https://api.github.com/repos/o/r/pulls/9",
        status_code=200,
        json={"title": "x", "body": "", "user": {"login": "a"}},
    )
    result = fetch_article("https://github.com/o/r/pull/9")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_github_api_error_falls_back(httpx_mock):
    httpx_mock.add_response(
        url="https://api.github.com/repos/o/r/pulls/9",
        status_code=403,  # rate-limited
    )
    result = fetch_article("https://github.com/o/r/pull/9")
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
         ("hailey", "social.hails.org", "116446826733136456")),
        ("https://partyon.xyz/@nullagent/116499715071759135",
         ("nullagent", "partyon.xyz", "116499715071759135")),
        ("https://grapheneos.social/@GrapheneOS/116550899908879585",
         ("GrapheneOS", "grapheneos.social", "116550899908879585")),
        ("https://social.example/@user/12345/", ("user", "social.example", "12345")),
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


_MASTODON_REST_STATUS = {
    "id": "12345",
    "content": (
        "<p>Annonce d'un produit, premier paragraphe avec assez de"
        " contenu pour franchir les seuils.</p>"
    ),
    "media_attachments": [],
    "url": "https://social.example/@hailey/12345",
}


def test_fetch_article_mastodon_falls_back_to_rest_api_on_authorized_fetch(
    httpx_mock,
):
    # Mastodon servers with "authorized fetch" enabled reject anonymous
    # ActivityPub requests with 401. The public Mastodon REST API
    # /api/v1/statuses/<id> still serves the same content without auth.
    httpx_mock.add_response(
        url="https://partyon.xyz/@nullagent/116499715071759135",
        status_code=401,
        match_headers={"Accept": "application/activity+json"},
    )
    httpx_mock.add_response(
        url="https://partyon.xyz/api/v1/statuses/116499715071759135",
        status_code=200,
        json=_MASTODON_REST_STATUS,
    )
    result = fetch_article("https://partyon.xyz/@nullagent/116499715071759135")
    assert result.source == ContentSource.EXTRACTED
    assert "Annonce d'un produit" in result.text
    assert "@nullagent@partyon.xyz" in result.text


def test_fetch_article_mastodon_falls_back_to_rest_api_on_403(httpx_mock):
    httpx_mock.add_response(
        url="https://social.example/@hailey/12345",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://social.example/api/v1/statuses/12345",
        status_code=200,
        json=_MASTODON_REST_STATUS,
    )
    result = fetch_article("https://social.example/@hailey/12345")
    assert result.source == ContentSource.EXTRACTED
    assert "Annonce d'un produit" in result.text


def test_fetch_article_mastodon_rest_extracts_first_image(httpx_mock):
    status = {
        **_MASTODON_REST_STATUS,
        "media_attachments": [
            {
                "id": "1",
                "type": "image",
                "url": "https://cdn.social.example/abc.jpg",
                "preview_url": "https://cdn.social.example/abc-preview.jpg",
            },
            {
                "id": "2",
                "type": "image",
                "url": "https://cdn.social.example/second.jpg",
            },
        ],
    }
    httpx_mock.add_response(
        url="https://social.example/@hailey/12345",
        status_code=401,
    )
    httpx_mock.add_response(
        url="https://social.example/api/v1/statuses/12345",
        status_code=200,
        json=status,
    )
    result = fetch_article("https://social.example/@hailey/12345")
    assert result.image_url == "https://cdn.social.example/abc.jpg"


def test_fetch_article_mastodon_rest_falls_back_when_unavailable(httpx_mock):
    httpx_mock.add_response(
        url="https://social.example/@hailey/12345",
        status_code=401,
    )
    httpx_mock.add_response(
        url="https://social.example/api/v1/statuses/12345",
        status_code=500,
    )
    result = fetch_article("https://social.example/@hailey/12345")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_mastodon_skips_rest_on_404(httpx_mock):
    # A genuine 404 means the post is gone — no point trying the REST
    # API which would also 404 and waste a request.
    httpx_mock.add_response(
        url="https://social.example/@hailey/deleted",
        status_code=404,
    )
    result = fetch_article("https://social.example/@hailey/deleted")
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


def test_fetch_article_isolates_article_inside_main_before_trafilatura(
    httpx_mock, monkeypatch
):
    """Some pages (e.g. theregister.com) put sidebar widgets inside <main>
    that defeat trafilatura's main-content heuristics: the precision pass
    latches onto the sidebar and the recall retry does the same. Targeting
    the first <article> descendant of <main> isolates the real body."""
    html = (
        "<html><body>"
        "<main>"
        "<aside><ul>"
        "<li>Sidebar widget link one carrying enough text to look meaningful</li>"
        "<li>Sidebar widget link two padded with additional chatter</li>"
        "<li>Sidebar widget link three repeating yet more boilerplate prose</li>"
        "</ul></aside>"
        "<article>"
        "<h1>Real article title</h1>"
        "<p>Body paragraph alpha with the substantive prose we actually want.</p>"
        "<p>Body paragraph beta reinforcing the article body so it has substance.</p>"
        "</article>"
        "</main>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://example.com/register-like",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    seen_html: list[str] = []

    def fake_extract(html_arg, **_kwargs):
        seen_html.append(html_arg)
        if "<article>" in html_arg and "Sidebar widget link one" not in html_arg:
            return (
                "Real article title\n\n"
                "Body paragraph alpha with the substantive prose we actually want.\n\n"
                "Body paragraph beta reinforcing the article body so it has substance."
            )
        return "Sidebar widget link one\nSidebar widget link two\nSidebar widget link three"

    monkeypatch.setattr(
        fetch_article_module.trafilatura, "extract", fake_extract
    )
    result = fetch_article("https://example.com/register-like")
    assert result.source == ContentSource.EXTRACTED
    assert "Body paragraph alpha" in result.text
    assert "Sidebar widget link" not in result.text
    assert seen_html, "trafilatura.extract was never called"
    assert "<article>" in seen_html[0]
    assert "Sidebar widget link one" not in seen_html[0]


def test_fetch_article_falls_back_to_full_html_when_no_article_tag(
    httpx_mock, monkeypatch
):
    """Pages without <main>/<article> keep the legacy precision/recall
    pass on the full HTML — the new isolation step must not regress
    them when there is nothing to isolate."""
    html = (
        "<html><body>"
        "<div class='content'>"
        "<p>Legacy article body that lives outside any semantic tag.</p>"
        "<p>Second legacy paragraph rounding out the body content.</p>"
        "</div>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://example.com/no-article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=html,
    )
    seen_html: list[str] = []

    def fake_extract(html_arg, **_kwargs):
        seen_html.append(html_arg)
        return "Legacy article body extracted from the full HTML."

    monkeypatch.setattr(
        fetch_article_module.trafilatura, "extract", fake_extract
    )
    result = fetch_article("https://example.com/no-article")
    assert result.source == ContentSource.EXTRACTED
    assert "Legacy article body" in result.text
    assert seen_html, "trafilatura.extract was never called"
    assert "Legacy article body that lives outside" in seen_html[0]


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


@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://radleybalko.substack.com/p/truth-power-and-honest-journalism",
         ("radleybalko", "truth-power-and-honest-journalism")),
        ("https://newsletter.substack.com/p/article-slug/",
         ("newsletter", "article-slug")),
        # Sub-subdomains are not what Substack uses but the regex should
        # only take the first label as the publication slug.
        ("https://www.substack.com/p/foo", None),
        # Substack home, archive, etc. — not an article URL.
        ("https://example.substack.com/", None),
        ("https://example.substack.com/archive", None),
        ("https://example.substack.com/about", None),
        # Custom domain — not detected, falls through to normal path.
        ("https://blog.example.com/p/foo", None),
        # Trailing path segments — not a clean article URL.
        ("https://example.substack.com/p/foo/comments", None),
    ],
)
def test_extract_substack_slug(url, expected):
    assert _extract_substack_slug(url) == expected


def _build_substack_feed(entries):
    """Return a minimal RSS 2.0 feed bytes with content:encoded entries.

    Each entry is ``{"link": <url>, "title": <str>, "content": <html>}``.
    """
    items = "".join(
        f"<item><title>{e['title']}</title>"
        f"<link>{e['link']}</link>"
        f"<guid>{e['link']}</guid>"
        f"<content:encoded><![CDATA[{e['content']}]]></content:encoded>"
        "</item>"
        for e in entries
    )
    rss = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<rss version="2.0" '
        'xmlns:content="http://purl.org/rss/1.0/modules/content/">'
        "<channel><title>Test Substack</title>"
        "<link>https://example.substack.com</link>"
        f"{items}"
        "</channel></rss>"
    )
    return rss.encode("utf-8")


_SUBSTACK_ARTICLE_HTML = (
    "<article>"
    "<h1>Le titre de l'article</h1>"
    "<p>Premier paragraphe substantiel rédigé pour passer le seuil de"
    " trafilatura en mode précision. Avec assez de mots concrets.</p>"
    "<p>Deuxième paragraphe avec encore du contenu utile pour que le"
    " détecteur de contenu principal ne rejette pas la page.</p>"
    "</article>"
)


def test_fetch_article_substack_returns_extracted_from_feed(httpx_mock):
    feed = _build_substack_feed(
        [
            {
                "link": "https://example.substack.com/p/article-cible",
                "title": "Article cible",
                "content": _SUBSTACK_ARTICLE_HTML,
            },
        ]
    )
    httpx_mock.add_response(
        url="https://example.substack.com/feed",
        status_code=200,
        headers={"content-type": "application/rss+xml"},
        content=feed,
    )
    result = fetch_article("https://example.substack.com/p/article-cible")
    assert result.source == ContentSource.EXTRACTED
    assert "Premier paragraphe substantiel" in result.text


def test_fetch_article_substack_matches_link_with_trailing_slash(httpx_mock):
    feed = _build_substack_feed(
        [
            {
                "link": "https://example.substack.com/p/article-slug/",
                "title": "Slash",
                "content": _SUBSTACK_ARTICLE_HTML,
            },
        ]
    )
    httpx_mock.add_response(
        url="https://example.substack.com/feed",
        status_code=200,
        headers={"content-type": "application/rss+xml"},
        content=feed,
    )
    result = fetch_article("https://example.substack.com/p/article-slug")
    assert result.source == ContentSource.EXTRACTED
    assert "Premier paragraphe substantiel" in result.text


def test_fetch_article_substack_falls_through_when_article_missing(httpx_mock):
    feed = _build_substack_feed(
        [
            {
                "link": "https://example.substack.com/p/other",
                "title": "Other",
                "content": _SUBSTACK_ARTICLE_HTML,
            },
        ]
    )
    httpx_mock.add_response(
        url="https://example.substack.com/feed",
        status_code=200,
        headers={"content-type": "application/rss+xml"},
        content=feed,
    )
    # When the article isn't in the feed (too old), the dispatcher must
    # fall through to the normal HTTP path. Mock the article URL too so
    # the test can observe the normal path succeeding.
    httpx_mock.add_response(
        url="https://example.substack.com/p/missing",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=(
            "<html><body><article>"
            "<p>Contenu récupéré directement depuis le HTML de la page,"
            " assez long pour passer le seuil de trafilatura.</p>"
            "<p>Second paragraphe pour bien assurer le seuil.</p>"
            "</article></body></html>"
        ),
    )
    result = fetch_article("https://example.substack.com/p/missing")
    assert result.source == ContentSource.EXTRACTED
    assert "Contenu récupéré directement" in result.text


_WAYBACK_SNAPSHOT_HTML = (
    "<html><head><title>Archived</title></head><body>"
    "<article>"
    "<h1>Le titre</h1>"
    "<p>Le contenu archivé sur Wayback, avec assez de phrases substantielles"
    " pour passer le seuil de précision de trafilatura sans difficulté.</p>"
    "<p>Un second paragraphe avec du contenu utile et concret pour assurer"
    " la qualité de l'extraction par l'outil.</p>"
    "</article>"
    "</body></html>"
)


def _wayback_api_response(snapshot_url=None, *, available=True, status="200"):
    if snapshot_url is None:
        return {"archived_snapshots": {}}
    return {
        "archived_snapshots": {
            "closest": {
                "url": snapshot_url,
                "available": available,
                "status": status,
                "timestamp": "20250101120000",
            }
        }
    }


def test_fetch_article_wayback_recovers_on_403(httpx_mock, isolated_settings):
    isolated_settings.wayback_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fpaywalled.example%2Farticle",
        status_code=200,
        json=_wayback_api_response(
            "http://web.archive.org/web/20250101120000/https://paywalled.example/article"
        ),
    )
    httpx_mock.add_response(
        url="http://web.archive.org/web/20250101120000id_/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=_WAYBACK_SNAPSHOT_HTML,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.EXTRACTED
    assert "contenu archivé sur Wayback" in result.text


def test_fetch_article_wayback_bails_when_no_snapshot(httpx_mock, isolated_settings):
    isolated_settings.wayback_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/dead",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fpaywalled.example%2Fdead",
        status_code=200,
        json=_wayback_api_response(None),
    )
    result = fetch_article("https://paywalled.example/dead")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_wayback_bails_when_snapshot_unavailable(
    httpx_mock, isolated_settings
):
    isolated_settings.wayback_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/x",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fpaywalled.example%2Fx",
        status_code=200,
        json=_wayback_api_response(
            "http://web.archive.org/web/20250101120000/https://paywalled.example/x",
            available=False,
        ),
    )
    result = fetch_article("https://paywalled.example/x")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_wayback_bails_when_snapshot_fetch_fails(
    httpx_mock, isolated_settings
):
    isolated_settings.wayback_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/y",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fpaywalled.example%2Fy",
        status_code=200,
        json=_wayback_api_response(
            "http://web.archive.org/web/20250101120000/https://paywalled.example/y"
        ),
    )
    httpx_mock.add_response(
        url="http://web.archive.org/web/20250101120000id_/https://paywalled.example/y",
        status_code=404,
    )
    result = fetch_article("https://paywalled.example/y")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_wayback_recovers_on_empty_extraction(
    httpx_mock, isolated_settings
):
    isolated_settings.wayback_enabled = True
    # Direct fetch succeeds but trafilatura can't find any content on
    # this layout — the dispatcher should still try Wayback before
    # giving up.
    httpx_mock.add_response(
        url="https://example.com/sparse-page",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body></body></html>",
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fexample.com%2Fsparse-page",
        status_code=200,
        json=_wayback_api_response(
            "http://web.archive.org/web/20250101120000/https://example.com/sparse-page"
        ),
    )
    httpx_mock.add_response(
        url="http://web.archive.org/web/20250101120000id_/https://example.com/sparse-page",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=_WAYBACK_SNAPSHOT_HTML,
    )
    result = fetch_article("https://example.com/sparse-page")
    assert result.source == ContentSource.EXTRACTED
    assert "contenu archivé sur Wayback" in result.text


def test_fetch_article_wayback_recovers_on_js_required(
    httpx_mock, isolated_settings
):
    isolated_settings.wayback_enabled = True
    js_only_html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=js_only_html,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fspa.example%2Froute",
        status_code=200,
        json=_wayback_api_response(
            "http://web.archive.org/web/20250101120000/https://spa.example/route"
        ),
    )
    httpx_mock.add_response(
        url="http://web.archive.org/web/20250101120000id_/https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=_WAYBACK_SNAPSHOT_HTML,
    )
    result = fetch_article("https://spa.example/route")
    assert result.source == ContentSource.EXTRACTED
    assert "contenu archivé sur Wayback" in result.text


def test_fetch_article_wayback_disabled_skips_archive_call(
    httpx_mock, isolated_settings
):
    isolated_settings.wayback_enabled = False
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    # No mock for the wayback API — if the code attempted it, httpx_mock
    # would error on the unmocked request.
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


_READER_TEXT = (
    "Title: Le titre\n\n"
    "Le contenu rendu et extrait par le reader r.jina.ai, avec assez de"
    " texte substantiel pour constituer un vrai corps d'article.\n\n"
    "Un second paragraphe pour faire bonne mesure."
)


def test_fetch_article_reader_recovers_on_403(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=_READER_TEXT,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.EXTRACTED
    assert "rendu et extrait par le reader" in result.text


def test_fetch_article_reader_recovers_on_js_required(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    js_only_html = (
        "<html><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=js_only_html,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=_READER_TEXT,
    )
    result = fetch_article("https://spa.example/route")
    assert result.source == ContentSource.EXTRACTED
    assert "rendu et extrait par le reader" in result.text


def test_fetch_article_reader_runs_after_wayback_miss(httpx_mock, isolated_settings):
    isolated_settings.wayback_enabled = True
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.org/wayback/available?url=https%3A%2F%2Fpaywalled.example%2Farticle",
        status_code=200,
        json=_wayback_api_response(None),
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=_READER_TEXT,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.EXTRACTED
    assert "rendu et extrait par le reader" in result.text


def test_fetch_article_reader_disabled_skips_call(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = False
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    # No mock for r.jina.ai — if the code attempted it, httpx_mock would
    # error on the unmocked request.
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_reader_bails_on_http_error(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=500,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_reader_bails_on_empty_body(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text="   \n  ",
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_reader_keeps_direct_image(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    js_only_html = (
        "<html><head>"
        '<meta property="og:image" content="https://spa.example/cover.png">'
        "</head><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=js_only_html,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=_READER_TEXT,
    )
    result = fetch_article("https://spa.example/route")
    assert result.source == ContentSource.EXTRACTED
    assert result.image_url == "https://spa.example/cover.png"


_READER_SOFT_ERROR_TEXT = (
    "Title: paywalled.example\n\n"
    "URL Source: https://paywalled.example/article\n\n"
    "Warning: Target URL returned error 403: Forbidden\n"
    "Warning: This page maybe requiring CAPTCHA, please make sure you are"
    " authorized to access this page.\n\n"
    "Markdown Content:"
)


def test_fetch_article_reader_rejects_soft_error(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=_READER_SOFT_ERROR_TEXT,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK
    assert result.text == ""


def test_fetch_article_reader_rejects_empty_markdown(httpx_mock, isolated_settings):
    isolated_settings.reader_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://r.jina.ai/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/plain; charset=utf-8"},
        text=(
            "Title: example\n\n"
            "URL Source: https://paywalled.example/article\n\n"
            "Markdown Content:\n   "
        ),
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


_ARCHIVE_TODAY_SNAPSHOT_HTML = (
    "<html><head><title>Archived</title></head><body>"
    "<article>"
    "<h1>Le titre</h1>"
    "<p>Le contenu archivé sur archive.today, avec assez de phrases"
    " substantielles pour passer le seuil de précision de trafilatura sans"
    " difficulté.</p>"
    "<p>Un second paragraphe avec du contenu utile et concret pour assurer"
    " la qualité de l'extraction par l'outil.</p>"
    "</article>"
    "</body></html>"
)


def test_fetch_article_archive_today_recovers_after_wayback_and_reader_miss(
    httpx_mock, isolated_settings
):
    # Wayback and reader are off by default in the fixture, so archive.today
    # is the only remaining fallback after the direct 403.
    isolated_settings.archive_today_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.ph/newest/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=_ARCHIVE_TODAY_SNAPSHOT_HTML,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.EXTRACTED
    assert "archivé sur archive.today" in result.text


def test_fetch_article_archive_today_disabled_skips_call(httpx_mock, isolated_settings):
    isolated_settings.archive_today_enabled = False
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    # No mock for archive.ph — if the code attempted it, httpx_mock would
    # error on the unmocked request.
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_archive_today_bails_when_no_snapshot(httpx_mock, isolated_settings):
    isolated_settings.archive_today_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.ph/newest/https://paywalled.example/article",
        status_code=404,
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_archive_today_bails_on_ddos_guard(httpx_mock, isolated_settings):
    isolated_settings.archive_today_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.ph/newest/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text="<html><body>Enable JavaScript and cookies to continue</body></html>",
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_archive_today_bails_on_captcha_200(httpx_mock, isolated_settings):
    # archive.ph sometimes serves its Cloudflare CAPTCHA interstitial with a
    # 200, not a 429 — without the guard its copy would become the "article".
    isolated_settings.archive_today_enabled = True
    httpx_mock.add_response(
        url="https://paywalled.example/article",
        status_code=403,
    )
    httpx_mock.add_response(
        url="https://archive.ph/newest/https://paywalled.example/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=(
            "<html><body><p>Completing the CAPTCHA proves you are a human and"
            " gives you temporary access to the web property.</p></body></html>"
        ),
    )
    result = fetch_article("https://paywalled.example/article")
    assert result.source == ContentSource.FEED_FALLBACK


def test_fetch_article_archive_today_keeps_direct_image(httpx_mock, isolated_settings):
    isolated_settings.archive_today_enabled = True
    js_only_html = (
        "<html><head>"
        '<meta property="og:image" content="https://spa.example/cover.png">'
        "</head><body>"
        "<noscript>You need to enable JavaScript to run this app.</noscript>"
        "</body></html>"
    )
    httpx_mock.add_response(
        url="https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=js_only_html,
    )
    httpx_mock.add_response(
        url="https://archive.ph/newest/https://spa.example/route",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=_ARCHIVE_TODAY_SNAPSHOT_HTML,
    )
    result = fetch_article("https://spa.example/route")
    assert result.source == ContentSource.EXTRACTED
    assert result.image_url == "https://spa.example/cover.png"


def test_fetch_article_substack_falls_through_on_feed_http_error(httpx_mock):
    httpx_mock.add_response(
        url="https://example.substack.com/feed",
        status_code=500,
    )
    httpx_mock.add_response(
        url="https://example.substack.com/p/article",
        status_code=200,
        headers={"content-type": "text/html; charset=utf-8"},
        text=(
            "<html><body><article>"
            "<p>Contenu de l'article récupéré directement via le HTML de"
            " la page de l'article, assez long pour trafilatura.</p>"
            "<p>Encore un paragraphe pour franchir le seuil.</p>"
            "</article></body></html>"
        ),
    )
    result = fetch_article("https://example.substack.com/p/article")
    assert result.source == ContentSource.EXTRACTED
    assert "Contenu de l'article récupéré directement" in result.text
