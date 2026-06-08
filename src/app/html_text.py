import html
import re

TAG_RE = re.compile(r"<[^>]+>")
_BLOCK_BREAK_RE = re.compile(r"</?(p|div|pre|blockquote|li)\s*>", re.IGNORECASE)
_LINE_BREAK_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)
_BLANK_LINES_RE = re.compile(r"\n{3,}")


def strip_html_preserving_paragraphs(text: str) -> str:
    """Strip HTML tags while keeping block boundaries as blank lines.

    Plain tag removal glues consecutive paragraphs into a single run
    (``Para 1Para 2``), which the summarization LLM then reads as one
    mashed token. Converting block-level closers and ``<br>`` into
    newlines before stripping keeps the prose readable. Shared by the
    Mastodon/ActivityPub path in ``fetch_article`` and the HN comment
    rendering in ``fetch_discussion``.
    """
    text = _BLOCK_BREAK_RE.sub("\n\n", text)
    text = _LINE_BREAK_RE.sub("\n", text)
    text = TAG_RE.sub("", text)
    text = html.unescape(text)
    return _BLANK_LINES_RE.sub("\n\n", text).strip()
