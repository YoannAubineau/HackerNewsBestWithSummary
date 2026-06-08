from youtube_transcript_api.proxies import WebshareProxyConfig

from app.config import get_settings


def webshare_proxy_config() -> WebshareProxyConfig | None:
    """Build the Webshare residential proxy config, or ``None`` when unset.

    Returns ``None`` unless both credentials are configured, so callers can
    branch on a single check instead of repeating the username/password
    guard. Used by the article fetch fallback, the YouTube transcript path
    and the HN comment-ranking scrape.
    """
    settings = get_settings()
    if settings.webshare_proxy_username and settings.webshare_proxy_password:
        return WebshareProxyConfig(
            proxy_username=settings.webshare_proxy_username,
            proxy_password=settings.webshare_proxy_password,
        )
    return None
