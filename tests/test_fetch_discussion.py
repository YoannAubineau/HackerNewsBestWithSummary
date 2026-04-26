import pytest

from app import fetch_discussion as fd
from app.fetch_discussion import (
    AlgoliaItem,
    fetch_discussion,
    fetch_submitter_text,
    find_dupe_canonical_id,
)
from app.fetch_discussion import (
    _fetch_hn_display_order as _real_fetch_hn_display_order,
)


@pytest.fixture(autouse=True)
def _stub_hn_display_order(monkeypatch):
    """Default every test to an empty HN order so fetch_discussion never
    tries to hit news.ycombinator.com. Tests that care about top comments
    override this via a local monkeypatch."""
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [])


def _comment(author, text, children=None, points=None, id=None):
    return {
        "id": id,
        "author": author,
        "points": points,
        "text": text,
        "children": children or [],
    }


def test_yields_every_comment_with_text(httpx_mock):
    # Walk emits every comment with text in depth-first pre-order, including
    # leaves and the submitter's own posts, with depth-driven indentation.
    payload = {
        "author": "op",
        "children": [
            _comment(
                "alice",
                "first root",
                children=[
                    _comment(
                        "bob",
                        "alice's reply",
                        children=[_comment("op", "submitter leaf")],
                    ),
                    _comment("bob_sibling", "another reply"),
                ],
            ),
            _comment("carol", "leaf root"),
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/55", json=payload)
    result = fetch_discussion(55)
    assert result is not None
    lines = result.text.splitlines()
    assert lines == [
        "[alice] first root",
        "  [bob] alice's reply",
        "    [op] submitter leaf",
        "  [bob_sibling] another reply",
        "[carol] leaf root",
    ]
    assert result.comment_count == 5


def test_skips_comments_with_empty_text(httpx_mock):
    # Deleted/dead comments come back with text=None and must not appear in
    # the rendered output, even though their children still do.
    payload = {
        "children": [
            _comment(
                "alice",
                "root",
                children=[_comment(None, None, children=[_comment("bob", "deep")])],
            )
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/56", json=payload)
    result = fetch_discussion(56)
    assert result is not None
    assert result.comment_count == 2
    authors = [line.lstrip().split("[")[1].split("]")[0] for line in result.text.splitlines()]
    assert authors == ["alice", "bob"]


def test_strips_html_and_entities(httpx_mock):
    payload = {
        "children": [
            _comment(
                "alice",
                "with &#x27;apostrophe&#x27; and <i>italics</i>",
                children=[_comment("bob", "reply")],
            )
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/42", json=payload)
    result = fetch_discussion(42)
    assert result is not None
    assert "<i>" not in result.text
    assert "'apostrophe'" in result.text


def test_fetch_discussion_returns_none_on_invalid_payload(httpx_mock):
    # A malformed Algolia response (e.g. children ends up as a scalar instead
    # of a list) should be rejected at validation time, and fetch_discussion
    # should degrade gracefully rather than crash.
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/42",
        json={"author": "op", "children": "not-a-list"},
    )
    assert fetch_discussion(42) is None


def test_fetch_discussion_returns_none_on_http_error(httpx_mock):
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/500",
        status_code=500,
    )
    assert fetch_discussion(500) is None


def test_fetch_discussion_returns_empty_when_no_comments(httpx_mock):
    # When Algolia succeeds but the discussion has no comments at all (or
    # every comment has empty text), the call still surfaces the canonical
    # URL captured from the root payload, so callers can still update
    # article.url. Comment fields are empty.
    payload = {
        "url": "https://example.com/canonical",
        "children": [_comment("alice", None), _comment("bob", "")],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/77", json=payload)
    result = fetch_discussion(77)
    assert result is not None
    assert result.comment_count == 0
    assert result.text == ""
    assert result.top_comments_markdown == ""
    assert result.url == "https://example.com/canonical"


def test_fetch_discussion_exposes_canonical_url(httpx_mock):
    payload = {
        "url": "https://example.com/article",
        "children": [
            _comment("alice", "root", children=[_comment("bob", "leaf reply")]),
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/88", json=payload)
    result = fetch_discussion(88)
    assert result is not None
    assert result.url == "https://example.com/article"


def test_fetch_discussion_url_is_none_for_self_post(httpx_mock):
    # Ask HN / Show HN / polls have no external URL: Algolia returns no url
    # field. Callers fall back to the feed URL.
    payload = {
        "children": [
            _comment("alice", "root", children=[_comment("bob", "leaf reply")]),
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/89", json=payload)
    result = fetch_discussion(89)
    assert result is not None
    assert result.url is None


def test_fetch_submitter_text_strips_html_and_entities(httpx_mock):
    payload = {
        "author": "op",
        "text": "<p>Hello &#x27;world&#x27;</p><p>second <i>para</i><br>with break</p>",
        "children": [],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/10", json=payload)
    assert fetch_submitter_text(10) == "Hello 'world'\n\nsecond para\nwith break"


def test_fetch_submitter_text_empty_when_root_has_no_text(httpx_mock):
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/11",
        json={"author": "op", "text": None, "children": []},
    )
    assert fetch_submitter_text(11) == ""


def test_fetch_submitter_text_empty_on_http_error(httpx_mock):
    httpx_mock.add_response(
        url="https://hn.algolia.com/api/v1/items/12",
        status_code=500,
    )
    assert fetch_submitter_text(12) == ""


def test_top_comments_follow_hn_display_order(
    httpx_mock, isolated_settings, monkeypatch
):
    # Algolia returns children in chronological order; HN's display order
    # can rearrange them by its internal best-ranking. top_comments must
    # follow HN's order, not the chronological Algolia order.
    payload = {
        "children": [
            _comment("alice", "posted first", id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
            _comment("bob", "posted second", id=2,
                     children=[_comment("leaf", "leaf", id=12)]),
            _comment("carol", "posted third", id=3,
                     children=[_comment("leaf", "leaf", id=13)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/200", json=payload)
    # HN ranks carol > alice > bob.
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [3, 1, 2])
    result = fetch_discussion(200)
    assert result is not None
    md = result.top_comments_markdown
    assert md.startswith("**Top commentaires** :")
    assert md.index("carol") < md.index("alice") < md.index("bob")


def test_top_comments_skip_deleted_or_missing_from_tree(
    httpx_mock, isolated_settings, monkeypatch
):
    # HN may surface IDs that correspond to deleted comments (text=None,
    # author=None) or that aren't in the Algolia tree for some reason.
    # We skip them and keep consuming the ordered list until we fill n.
    payload = {
        "children": [
            _comment(None, "no author", id=10,
                     children=[_comment("leaf", "leaf", id=11)]),
            _comment("alice", None, id=20,
                     children=[_comment("leaf", "leaf", id=12)]),
            _comment("carol", "first kept", id=40,
                     children=[_comment("leaf", "leaf", id=14)]),
            _comment("dave", "second kept", id=50,
                     children=[_comment("leaf", "leaf", id=15)]),
            _comment("erin", "third kept", id=60,
                     children=[_comment("leaf", "leaf", id=16)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/201", json=payload)
    # 10 and 20 are unusable; 99 isn't in the tree at all; the next three are fine.
    monkeypatch.setattr(
        fd, "_fetch_hn_display_order", lambda _id: [10, 20, 99, 40, 50, 60]
    )
    result = fetch_discussion(201)
    assert result is not None
    md = result.top_comments_markdown
    assert "carol" in md
    assert "dave" in md
    assert "erin" in md
    assert "no author" not in md


def test_top_comments_truncates_to_300_chars_with_ellipsis(
    httpx_mock, isolated_settings, monkeypatch
):
    long_text = "a" * 500
    exact_text = "b" * 300
    short_text = "c" * 100
    payload = {
        "children": [
            _comment("long", long_text, id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
            _comment("exact", exact_text, id=2,
                     children=[_comment("leaf", "leaf", id=12)]),
            _comment("short", short_text, id=3,
                     children=[_comment("leaf", "leaf", id=13)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/202", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1, 2, 3])
    result = fetch_discussion(202)
    assert result is not None
    md = result.top_comments_markdown
    long_line = next(line for line in md.splitlines() if "[long]" in line)
    long_payload = long_line.split(" : « ", 1)[1].rstrip(" »")
    assert long_payload.endswith("\u2026")
    assert len(long_payload) == 300
    exact_line = next(line for line in md.splitlines() if "[exact]" in line)
    exact_payload = exact_line.split(" : « ", 1)[1].rstrip(" »")
    assert exact_payload == exact_text
    assert "\u2026" not in exact_payload
    short_line = next(line for line in md.splitlines() if "[short]" in line)
    assert short_text in short_line


def test_top_comments_separates_paragraphs_with_space(
    httpx_mock, isolated_settings, monkeypatch
):
    payload = {
        "children": [
            _comment(
                "alice",
                "<p>First paragraph.</p><p>Second paragraph.</p>",
                id=1,
                children=[_comment("leaf", "leaf", id=11)],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/204", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1])
    result = fetch_discussion(204)
    assert result is not None
    md = result.top_comments_markdown
    line = next(line for line in md.splitlines() if "[alice]" in line)
    text = line.split(" : « ", 1)[1].rstrip(" »")
    assert text == "First paragraph. Second paragraph."


def test_top_comments_collapses_internal_whitespace(
    httpx_mock, isolated_settings, monkeypatch
):
    payload = {
        "children": [
            _comment(
                "alice", "<p>line one</p>\n<p>line  two</p>", id=1,
                children=[_comment("leaf", "leaf", id=11)],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/203", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1])
    result = fetch_discussion(203)
    assert result is not None
    md = result.top_comments_markdown
    line = next(line for line in md.splitlines() if "[alice]" in line)
    text = line.split(" : « ", 1)[1].rstrip(" »")
    assert "\n" not in text
    assert "  " not in text
    assert text == "line one line two"


def test_top_comments_limits_to_three(
    httpx_mock, isolated_settings, monkeypatch
):
    payload = {
        "children": [
            _comment(f"u{i}", f"text {i}", id=1000 + i,
                     children=[_comment(f"leaf{i}", "leaf", id=2000 + i)])
            for i in range(10)
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/205", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: list(range(1000, 1010)))
    result = fetch_discussion(205)
    assert result is not None
    md = result.top_comments_markdown
    bullet_count = sum(1 for line in md.splitlines() if line.startswith("- ["))
    assert bullet_count == 3
    assert "[u0]" in md
    assert "[u1]" in md
    assert "[u2]" in md
    assert "[u3]" not in md


def test_top_comments_skip_when_link_text_dominates(
    httpx_mock, isolated_settings, monkeypatch
):
    # A comment whose visible text is mostly the anchor text of a link
    # adds little value once truncated, so we skip it and pick the next
    # ranked comment instead. Here the link text (60 chars) covers more
    # than half of the visible comment ("See: " + 60 chars = 65 chars).
    link_text = "x" * 60
    dominated = (
        f'See: <a href="https://example.com/{link_text}">{link_text}</a>'
    )
    payload = {
        "children": [
            _comment("alice", dominated, id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
            _comment("bob", "second kept", id=2,
                     children=[_comment("leaf", "leaf", id=12)]),
            _comment("carol", "third kept", id=3,
                     children=[_comment("leaf", "leaf", id=13)]),
            _comment("dave", "fourth kept", id=4,
                     children=[_comment("leaf", "leaf", id=14)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/210", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1, 2, 3, 4])
    result = fetch_discussion(210)
    assert result is not None
    md = result.top_comments_markdown
    assert "[alice]" not in md
    assert "[bob]" in md
    assert "[carol]" in md
    assert "[dave]" in md


def test_top_comments_keep_when_link_text_is_short(
    httpx_mock, isolated_settings, monkeypatch
):
    # A short link inside a longer paragraph stays well under half of
    # the visible comment, so the comment is kept.
    text = (
        "I think this article misses the broader point about distributed "
        'systems. See <a href="https://example.com">here</a> for context, '
        "but the gist is that consistency trumps availability in finance."
    )
    payload = {
        "children": [
            _comment("alice", text, id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/211", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1])
    result = fetch_discussion(211)
    assert result is not None
    md = result.top_comments_markdown
    assert "[alice]" in md


def test_top_comments_keep_at_exactly_half(
    httpx_mock, isolated_settings, monkeypatch
):
    # Boundary: link text equals exactly 50% of the visible comment.
    # The threshold is strictly greater than half, so this is kept.
    # Visible text: "abcd" + "wxyz" = 8 chars, link text "wxyz" = 4 chars.
    text = 'abcd<a href="https://example.com">wxyz</a>'
    payload = {
        "children": [
            _comment("alice", text, id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/212", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1])
    result = fetch_discussion(212)
    assert result is not None
    md = result.top_comments_markdown
    assert "[alice]" in md


def test_top_comments_skip_when_multiple_links_dominate(
    httpx_mock, isolated_settings, monkeypatch
):
    # Two links whose combined text exceeds half the visible comment
    # cause the comment to be skipped, even when no single link does.
    text = (
        'see <a href="https://a.example">aaaaaaaaaaaaaaaa</a> '
        'and <a href="https://b.example">bbbbbbbbbbbbbbbb</a>'
    )
    payload = {
        "children": [
            _comment("alice", text, id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
            _comment("bob", "kept comment", id=2,
                     children=[_comment("leaf", "leaf", id=12)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/213", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1, 2])
    result = fetch_discussion(213)
    assert result is not None
    md = result.top_comments_markdown
    assert "[alice]" not in md
    assert "[bob]" in md


def test_top_comments_empty_when_hn_order_is_empty(httpx_mock, isolated_settings):
    # Stubbed _fetch_hn_display_order returns [] by default via the autouse
    # fixture; fetch_discussion must degrade to an empty section.
    payload = {
        "children": [
            _comment("alice", "root", id=1,
                     children=[_comment("leaf", "leaf", id=11)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/206", json=payload)
    result = fetch_discussion(206)
    assert result is not None
    assert result.top_comments_markdown == ""


def test_fetch_hn_display_order_parses_top_level_only(httpx_mock):
    # Synthetic HN HTML with three top-level comments (indent=0) and two
    # nested ones (indent=1, indent=2). Only the top-level IDs should come
    # back, in document order.
    html = (
        '<html><body><table>'
        '<tr class="athing comtr" id="100">'
        '<td><table><tr><td class="ind" indent="0">'
        '<img></td></tr></table></td></tr>'
        '<tr class="athing comtr" id="200">'
        '<td><table><tr><td class="ind" indent="1">'
        '<img></td></tr></table></td></tr>'
        '<tr class="athing comtr" id="300">'
        '<td><table><tr><td class="ind" indent="0">'
        '<img></td></tr></table></td></tr>'
        '<tr class="athing comtr" id="400">'
        '<td><table><tr><td class="ind" indent="2">'
        '<img></td></tr></table></td></tr>'
        '<tr class="athing comtr" id="500">'
        '<td><table><tr><td class="ind" indent="0">'
        '<img></td></tr></table></td></tr>'
        '</table></body></html>'
    )
    httpx_mock.add_response(
        url="https://news.ycombinator.com/item?id=7777",
        text=html,
    )
    assert _real_fetch_hn_display_order(7777) == [100, 300, 500]


def test_fetch_hn_display_order_returns_empty_on_http_error(httpx_mock):
    # 5xx is not in the retry list (only 429 / ConnectError / ReadTimeout
    # are transient). Returns immediately rather than retrying.
    httpx_mock.add_response(
        url="https://news.ycombinator.com/item?id=8888",
        status_code=503,
    )
    assert _real_fetch_hn_display_order(8888) == []


def test_fetch_hn_display_order_retries_on_429(httpx_mock, monkeypatch):
    import time
    monkeypatch.setattr(time, "sleep", lambda _: None)
    # First call rate-limited, second succeeds. The wrapper should retry
    # transparently and return the parsed order on the second response.
    httpx_mock.add_response(
        url="https://news.ycombinator.com/item?id=9999",
        status_code=429,
    )
    httpx_mock.add_response(
        url="https://news.ycombinator.com/item?id=9999",
        text=(
            '<tr class="athing comtr" id="42">'
            '<td><table><tr><td class="ind" indent="0">'
            '<img></td></tr></table></td></tr>'
        ),
    )
    assert _real_fetch_hn_display_order(9999) == [42]


def test_fetch_hn_display_order_gives_up_after_three_429_without_proxy(
    httpx_mock, monkeypatch, isolated_settings
):
    import time
    monkeypatch.setattr(time, "sleep", lambda _: None)
    isolated_settings.webshare_proxy_username = ""
    isolated_settings.webshare_proxy_password = ""
    for _ in range(3):
        httpx_mock.add_response(
            url="https://news.ycombinator.com/item?id=1111",
            status_code=429,
        )
    assert _real_fetch_hn_display_order(1111) == []


def test_fetch_hn_display_order_falls_back_to_proxy_when_direct_exhausts(
    httpx_mock, monkeypatch, isolated_settings
):
    import time
    monkeypatch.setattr(time, "sleep", lambda _: None)
    isolated_settings.webshare_proxy_username = "demo"
    isolated_settings.webshare_proxy_password = "secret"
    # Three direct 429s exhaust the tenacity retry, then the proxy attempt
    # against the same target URL succeeds. pytest-httpx matches at the
    # transport layer and consumes registered responses in order, so the
    # fourth response is the one returned to the proxy call.
    for _ in range(3):
        httpx_mock.add_response(
            url="https://news.ycombinator.com/item?id=2222",
            status_code=429,
        )
    httpx_mock.add_response(
        url="https://news.ycombinator.com/item?id=2222",
        text=(
            '<tr class="athing comtr" id="77">'
            '<td><table><tr><td class="ind" indent="0">'
            '<img></td></tr></table></td></tr>'
        ),
    )
    assert _real_fetch_hn_display_order(2222) == [77]


def test_top_comments_escape_markdown_in_author_and_text(
    httpx_mock, isolated_settings, monkeypatch
):
    # A commenter controlling their handle or text could otherwise inject an
    # active link into the rendered Markdown — and into the upstream LLM
    # context — by including `[evil](https://x)` or `*emphasis*` etc. The
    # escaper must neutralise these so the rendered bullet keeps the literal
    # characters as text, not as Markdown syntax.
    payload = {
        "children": [
            _comment(
                "[admin](https://evil)",
                "voir [clic](https://evil/x) ou *gras* `code` #titre",
                id=1,
                children=[_comment("leaf", "leaf", id=11)],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/300", json=payload)
    monkeypatch.setattr(fd, "_fetch_hn_display_order", lambda _id: [1])
    result = fetch_discussion(300)
    assert result is not None
    md = result.top_comments_markdown
    # Each control char appears backslash-escaped in the rendered line, so
    # Markdown won't parse the injected `[admin](...)` or `[clic](...)` as
    # links and won't render `*gras*` as emphasis.
    line = next(line for line in md.splitlines() if line.startswith("- "))
    assert r"\[admin\]" in line
    assert r"\(https://evil\)" in line
    assert r"\[clic\]" in line
    assert r"\(https://evil/x\)" in line
    assert r"\*gras\*" in line
    assert r"\`code\`" in line
    assert r"\#titre" in line
    # The HN URL we control is intact (constructed from the integer id).
    assert "(https://news.ycombinator.com/item?id=1)" in line


def test_fetch_hn_display_order_returns_empty_when_proxy_also_fails(
    httpx_mock, monkeypatch, isolated_settings
):
    import time
    monkeypatch.setattr(time, "sleep", lambda _: None)
    isolated_settings.webshare_proxy_username = "demo"
    isolated_settings.webshare_proxy_password = "secret"
    # Three direct 429s + one proxy 429 → empty.
    for _ in range(4):
        httpx_mock.add_response(
            url="https://news.ycombinator.com/item?id=3333",
            status_code=429,
        )
    assert _real_fetch_hn_display_order(3333) == []


def _algolia_item(**fields):
    children = [AlgoliaItem.model_validate(c) for c in fields.pop("children", [])]
    return AlgoliaItem(children=children, **fields)


def test_find_dupe_canonical_id_extracts_from_first_comment():
    # The HN-moderator pattern Algolia returns verbatim: forward slashes are
    # entity-encoded as &#x2F;. find_dupe_canonical_id must unescape before
    # matching, otherwise the regex misses the link.
    payload = _algolia_item(
        id=47895080,
        children=[
            {
                "author": "pingou",
                "text": (
                    'dupe: <a href="https:&#x2F;&#x2F;news.ycombinator.com'
                    '&#x2F;item?id=47894129">https:&#x2F;&#x2F;news.ycombinator.com'
                    '&#x2F;item?id=47894129</a>'
                ),
            },
        ],
    )
    assert find_dupe_canonical_id(payload) == 47894129


def test_find_dupe_canonical_id_returns_none_without_keyword():
    # First comment links to another HN thread but is not a dupe annotation;
    # we must not dedupe to avoid false positives on related-discussion links.
    payload = _algolia_item(
        id=10,
        children=[
            {
                "author": "alice",
                "text": (
                    'see also <a href="https://news.ycombinator.com/item?id=42">'
                    'this thread</a>'
                ),
            },
        ],
    )
    assert find_dupe_canonical_id(payload) is None


def test_find_dupe_canonical_id_returns_none_without_link():
    payload = _algolia_item(
        id=10,
        children=[{"author": "alice", "text": "looks like a dupe of an older one"}],
    )
    assert find_dupe_canonical_id(payload) is None


def test_find_dupe_canonical_id_returns_none_when_no_children():
    payload = _algolia_item(id=10, children=[])
    assert find_dupe_canonical_id(payload) is None


def test_find_dupe_canonical_id_returns_none_when_first_comment_text_empty():
    payload = _algolia_item(
        id=10,
        children=[{"author": "alice", "text": None}],
    )
    assert find_dupe_canonical_id(payload) is None


def test_find_dupe_canonical_id_ignores_self_pointer():
    # Defensive: if the parsed id matches the current item, treat as not a
    # dupe rather than trying to substitute the article with itself.
    payload = _algolia_item(
        id=10,
        children=[
            {
                "author": "alice",
                "text": 'dupe: <a href="https://news.ycombinator.com/item?id=10">x</a>',
            },
        ],
    )
    assert find_dupe_canonical_id(payload) is None


def test_find_dupe_canonical_id_returns_first_link_when_multiple():
    payload = _algolia_item(
        id=10,
        children=[
            {
                "author": "alice",
                "text": (
                    "dupe: https://news.ycombinator.com/item?id=42 "
                    "(see also https://news.ycombinator.com/item?id=99)"
                ),
            },
        ],
    )
    assert find_dupe_canonical_id(payload) == 42


def test_fetch_discussion_short_circuits_on_dupe(httpx_mock, monkeypatch):
    # When the first comment is a dupe pointer, fetch_discussion should
    # surface the canonical id and skip the HN HTML scrape entirely.
    payload = {
        "id": 100,
        "title": "Some article",
        "created_at": "2026-04-24T20:00:30Z",
        "children": [
            _comment(
                "pingou",
                'dupe: <a href="https:&#x2F;&#x2F;news.ycombinator.com'
                '&#x2F;item?id=99">x</a>',
            ),
            _comment("bob", "second comment, irrelevant"),
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/100", json=payload)

    def _explode(_id):
        raise AssertionError("HN scrape should not happen on a dupe entry")

    monkeypatch.setattr(fd, "_fetch_hn_display_order", _explode)
    result = fetch_discussion(100)
    assert result is not None
    assert result.canonical_dupe_id == 99
    assert result.text == ""
    assert result.top_comments_markdown == ""
    assert result.url is None


def test_fetch_discussion_populates_title_and_created_at(httpx_mock):
    payload = {
        "id": 200,
        "title": "Original title",
        "created_at": "2026-04-20T10:15:00Z",
        "url": "https://example.com/x",
        "children": [_comment("alice", "hello")],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/200", json=payload)
    result = fetch_discussion(200)
    assert result is not None
    assert result.title == "Original title"
    assert result.source_published_at is not None
    assert result.source_published_at.year == 2026
    assert result.source_published_at.month == 4
    assert result.source_published_at.day == 20


