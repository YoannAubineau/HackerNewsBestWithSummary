from app.fetch_article import fetch_article
from app.models import ContentSource


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
