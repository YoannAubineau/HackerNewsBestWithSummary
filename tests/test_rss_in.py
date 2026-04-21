from app.rss_in import parse_feed_bytes

_FEED_SAMPLE = b"""<?xml version="1.0"?>
<rss version="2.0"><channel>
  <title>HN Best</title>
  <item>
    <title>Un article externe</title>
    <link>https://example.com/article</link>
    <comments>https://news.ycombinator.com/item?id=42</comments>
    <guid isPermaLink="false">https://news.ycombinator.com/item?id=42</guid>
    <pubDate>Tue, 21 Apr 2026 08:30:00 GMT</pubDate>
    <description>Article Title&lt;br&gt;Points: 120&lt;br&gt;Comments: 42</description>
  </item>
  <item>
    <title>Ask HN: Question ouverte</title>
    <link>https://news.ycombinator.com/item?id=43</link>
    <guid isPermaLink="false">https://news.ycombinator.com/item?id=43</guid>
    <pubDate>Tue, 21 Apr 2026 09:00:00 GMT</pubDate>
    <description>Corps de la question</description>
  </item>
</channel></rss>
"""


def test_parse_feed_extracts_entries():
    entries = parse_feed_bytes(_FEED_SAMPLE)
    assert len(entries) == 2


def test_regular_article_detects_external_link():
    entries = parse_feed_bytes(_FEED_SAMPLE)
    regular = entries[0]
    assert regular.url == "https://example.com/article"
    assert regular.hn_url == "https://news.ycombinator.com/item?id=42"
    assert regular.hn_item_id == 42
    assert regular.is_ask_or_show_hn is False


def test_ask_hn_flagged_when_link_equals_comments():
    entries = parse_feed_bytes(_FEED_SAMPLE)
    ask = entries[1]
    assert ask.hn_item_id == 43
    assert ask.is_ask_or_show_hn is True
    assert ask.hn_url == "https://news.ycombinator.com/item?id=43"


def test_feed_summary_captured():
    entries = parse_feed_bytes(_FEED_SAMPLE)
    assert "Points: 120" in entries[0].feed_summary


def test_published_at_parsed_as_utc():
    entries = parse_feed_bytes(_FEED_SAMPLE)
    assert entries[0].source_published_at.year == 2026
    assert entries[0].source_published_at.month == 4
    assert entries[0].source_published_at.day == 21
