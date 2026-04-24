from app.fetch_discussion import _degressive_split, fetch_discussion, fetch_submitter_text


def _comment(author, text, children=None, points=None, id=None):
    return {
        "id": id,
        "author": author,
        "points": points,
        "text": text,
        "children": children or [],
    }


def test_degressive_split_sums_to_budget():
    assert _degressive_split(500, 10) == [95, 81, 72, 63, 54, 45, 36, 27, 18, 9]
    assert sum(_degressive_split(500, 10)) == 500


def test_degressive_split_is_monotonic():
    allocs = _degressive_split(100, 5)
    assert all(allocs[i] >= allocs[i + 1] for i in range(len(allocs) - 1))
    assert sum(allocs) == 100


def test_degressive_split_handles_edges():
    assert _degressive_split(0, 5) == []
    assert _degressive_split(100, 0) == []
    assert _degressive_split(1, 3) == [1, 0, 0]


def test_drops_leaf_comments(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 100
    payload = {
        "children": [
            _comment("alice", "root w/ reply", children=[_comment("bob", "leaf reply")]),
            _comment("carol", "leaf root"),  # no children → skipped entirely
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/42", json=payload)
    result = fetch_discussion(42)
    assert result is not None
    # alice is included (branch node). bob is a leaf → excluded. carol excluded.
    assert result.comment_count == 1
    assert "alice" in result.text
    assert "bob" not in result.text
    assert "carol" not in result.text


def test_budget_limits_total_count(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 3
    # Ten qualifying roots, each with a qualifying child (so each would include 2).
    payload = {
        "children": [
            _comment(
                f"r{i}",
                f"root {i}",
                children=[_comment(f"r{i}_a", "a", children=[_comment(f"r{i}_b", "b")])],
            )
            for i in range(10)
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/99", json=payload)
    result = fetch_discussion(99)
    assert result is not None
    assert result.comment_count <= 3


def test_top_root_gets_more_depth_than_later_root(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10

    # Each root is a long chain of branch nodes, so the budget binds before the
    # tree runs out. With split (7, 3), top emits 7 nodes, bottom emits 3.
    def chain(prefix: str, length: int) -> dict:
        # Deepest branch node = has one leaf child (so it counts as a branch node).
        node = _comment(f"{prefix}{length - 1}", f"{prefix}{length - 1}",
                        children=[_comment(f"{prefix}leaf", "leaf")])
        for i in range(length - 2, -1, -1):
            node = _comment(f"{prefix}{i}", f"{prefix}{i}", children=[node])
        return node

    payload = {"children": [chain("top_", 10), chain("bottom_", 10)]}
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/77", json=payload)
    result = fetch_discussion(77)
    assert result is not None

    top_count = sum(1 for line in result.text.splitlines() if "top_" in line)
    bottom_count = sum(1 for line in result.text.splitlines() if "bottom_" in line)
    assert top_count == 7
    assert bottom_count == 3


def test_output_grouped_by_root_subtree(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 20
    payload = {
        "children": [
            _comment(
                "alice",
                "first root",
                children=[
                    _comment(
                        "bob",
                        "alice's reply",
                        children=[_comment("bob_child_leaf", "leaf")],
                    )
                ],
            ),
            _comment(
                "carol",
                "second root",
                children=[
                    _comment(
                        "dave",
                        "carol's reply",
                        children=[_comment("dave_child_leaf", "leaf")],
                    )
                ],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/55", json=payload)
    result = fetch_discussion(55)
    assert result is not None
    lines = result.text.splitlines()
    # alice subtree (alice, bob) before carol subtree (carol, dave). Leaves excluded.
    authors = [line.lstrip().split("[")[1].split(",")[0].split("]")[0] for line in lines]
    assert authors == ["alice", "bob", "carol", "dave"]


def test_strips_html_and_entities(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
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


def test_submitter_leaf_comment_is_pinned(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
    payload = {
        "author": "op",
        "children": [
            _comment(
                "alice",
                "root by alice",
                children=[
                    _comment(
                        "bob",
                        "reply by bob",
                        children=[_comment("op", "leaf reply by submitter")],
                    )
                ],
            ),
            _comment("carol", "leaf by carol"),  # not submitter, not a branch → skipped
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/1", json=payload)
    result = fetch_discussion(1)
    assert result is not None
    # alice + bob + op (the leaf) all pinned as ancestor chain; carol dropped.
    authors = [line.lstrip().split("[")[1].split(",")[0].split("]")[0]
               for line in result.text.splitlines()]
    assert authors == ["alice", "bob", "op"]


def test_submitter_ancestor_chain_is_fully_included(httpx_mock, isolated_settings):
    # Budget 0 + no qualifying siblings → output is exactly the pinned chain.
    isolated_settings.discussion_budget = 0
    payload = {
        "author": "op",
        "children": [
            _comment(
                "alice",
                "depth 0",
                children=[
                    _comment(
                        "bob",
                        "depth 1",
                        children=[
                            _comment(
                                "carol",
                                "depth 2",
                                children=[_comment("op", "depth 3 by submitter")],
                            )
                        ],
                    )
                ],
            )
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/2", json=payload)
    result = fetch_discussion(2)
    assert result is not None
    authors = [line.lstrip().split("[")[1].split(",")[0].split("]")[0]
               for line in result.text.splitlines()]
    assert authors == ["alice", "bob", "carol", "op"]


def test_pinned_nodes_do_not_consume_budget(httpx_mock, isolated_settings):
    # A pinned chain of 6 nodes + 3 non-pinned qualifying roots. With budget=3
    # distributed degressively across the 3 non-pinned roots (alloc [2,1,0]),
    # u0 and u1 each emit themselves (their child is a leaf). The pinning does
    # not shift budget away from non-pinned siblings.
    isolated_settings.discussion_budget = 3
    pinned_chain = _comment(
        "alice",
        "depth 0",
        children=[
            _comment(
                "bob",
                "depth 1",
                children=[
                    _comment(
                        "carol",
                        "depth 2",
                        children=[
                            _comment(
                                "dave",
                                "depth 3",
                                children=[
                                    _comment(
                                        "erin",
                                        "depth 4",
                                        children=[_comment("op", "depth 5 by submitter")],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )
    other_roots = [
        _comment(f"u{i}", f"u{i}", children=[_comment(f"u{i}_child", "leaf")])
        for i in range(3)
    ]
    payload = {"author": "op", "children": [pinned_chain, *other_roots]}
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/3", json=payload)
    result = fetch_discussion(3)
    assert result is not None
    # 6 pinned + 2 non-pinned (u0 and u1, since alloc is [2,1,0] for 3 slots).
    assert result.comment_count == 8
    for author in ("alice", "bob", "carol", "dave", "erin", "op"):
        assert f"[{author}]" in result.text
    assert "[u0]" in result.text
    assert "[u1]" in result.text
    assert "[u2]" not in result.text


def test_siblings_of_pinned_path_not_privileged(httpx_mock, isolated_settings):
    # Budget 0: only the pinned path should survive, siblings of pinned
    # ancestors are dropped (no budget, not pinned themselves).
    isolated_settings.discussion_budget = 0
    pinned_path = _comment(
        "alice",
        "pinned root",
        children=[
            _comment(
                "bob",
                "pinned middle",
                children=[_comment("op", "submitter")],
            ),
            # Sibling of bob, has children → would qualify but no budget, not pinned.
            _comment("bob_sibling", "sibling", children=[_comment("leaf", "leaf")]),
        ],
    )
    # Root-level sibling of alice, also qualifying but not pinned.
    alice_sibling = _comment(
        "alice_sibling", "another root", children=[_comment("x", "leaf")]
    )
    payload = {"author": "op", "children": [pinned_path, alice_sibling]}
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/4", json=payload)
    result = fetch_discussion(4)
    assert result is not None
    authors = [line.lstrip().split("[")[1].split(",")[0].split("]")[0]
               for line in result.text.splitlines()]
    assert authors == ["alice", "bob", "op"]


def test_no_author_on_payload_behaves_like_budget_only(httpx_mock, isolated_settings):
    # Missing `author` on root → fallback: everything is non-pinned.
    isolated_settings.discussion_budget = 10
    payload = {
        "children": [
            _comment("alice", "root", children=[_comment("bob", "leaf")]),
            _comment("anon_leaf", "solo leaf"),
        ]
        # intentionally no "author" key
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/5", json=payload)
    result = fetch_discussion(5)
    assert result is not None
    # Only alice qualifies (bob is a leaf; anon_leaf is a leaf root → skipped).
    assert result.comment_count == 1
    assert "[alice]" in result.text


def test_submitter_with_multiple_comments_pins_all(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 0  # zero budget → only pins survive
    payload = {
        "author": "op",
        "children": [
            _comment(
                "alice", "root 1",
                children=[_comment("op", "op reply in root 1")],
            ),
            _comment(
                "bob", "root 2",
                children=[_comment("op", "op reply in root 2")],
            ),
            _comment("carol", "root 3", children=[_comment("leaf", "leaf")]),
        ],
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/6", json=payload)
    result = fetch_discussion(6)
    assert result is not None
    # alice + op_reply_1 + bob + op_reply_2; carol's thread dropped.
    assert result.comment_count == 4
    assert "[carol]" not in result.text
    assert result.text.count("[op]") == 2


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


def test_fetch_discussion_returns_none_when_no_qualifying_roots(httpx_mock, isolated_settings):
    payload = {"children": [_comment("alice", "leaf 1"), _comment("bob", "leaf 2")]}
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/77", json=payload)
    assert fetch_discussion(77) is None


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


def test_top_comments_picks_highest_scored_across_whole_tree(httpx_mock, isolated_settings):
    # Low budget so most branches would be dropped from the LLM text; top_comments
    # must still surface the 3 highest-scored nodes regardless of selection.
    isolated_settings.discussion_budget = 2
    payload = {
        "children": [
            _comment(
                "low_root", "low root", points=5, id=1001,
                children=[_comment("low_leaf", "leaf", id=1002)],
            ),
            _comment(
                "mid_root", "mid root", points=50, id=1003,
                children=[
                    _comment("deep_winner", "winner", points=999, id=1004),
                    _comment("deep_second", "second", points=500, id=1005),
                ],
            ),
            _comment(
                "third_root", "third", points=100, id=1006,
                children=[_comment("leaf2", "leaf", id=1007)],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/200", json=payload)
    result = fetch_discussion(200)
    assert result is not None
    md = result.top_comments_markdown
    assert md.startswith("**Meilleurs commentaires** :")
    # 999 > 500 > 100
    assert "[deep_winner, 999 pts](https://news.ycombinator.com/item?id=1004)" in md
    assert "[deep_second, 500 pts](https://news.ycombinator.com/item?id=1005)" in md
    assert "[third_root, 100 pts](https://news.ycombinator.com/item?id=1006)" in md
    # mid_root (50 pts) and low_root (5 pts) should not appear.
    assert "mid_root" not in md
    assert "low_root" not in md
    # Order: winner first, second second, third third.
    assert md.index("deep_winner") < md.index("deep_second") < md.index("third_root")


def test_top_comments_skips_missing_id_author_text_or_points(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 50
    payload = {
        "children": [
            _comment(None, "no author", points=100, id=1,
                     children=[_comment("leaf", "leaf", id=2)]),
            _comment("alice", None, points=100, id=3,
                     children=[_comment("leaf", "leaf", id=4)]),
            _comment("bob", "no id", points=100,
                     children=[_comment("leaf", "leaf", id=5)]),
            _comment("carol", "no points", id=6,
                     children=[_comment("leaf", "leaf", id=7)]),
            _comment("dave", "kept", points=1, id=8,
                     children=[_comment("leaf", "leaf", id=9)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/201", json=payload)
    result = fetch_discussion(201)
    assert result is not None
    md = result.top_comments_markdown
    assert "dave" in md
    assert "no author" not in md
    assert "no id" not in md
    assert "no points" not in md


def test_top_comments_truncates_to_300_chars_with_ellipsis(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
    long_text = "a" * 500
    exact_text = "b" * 300
    short_text = "c" * 100
    payload = {
        "children": [
            _comment(
                "parent", "parent", points=1, id=1,
                children=[
                    _comment("long", long_text, points=100, id=2),
                    _comment("exact", exact_text, points=99, id=3),
                    _comment("short", short_text, points=98, id=4),
                ],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/202", json=payload)
    result = fetch_discussion(202)
    assert result is not None
    md = result.top_comments_markdown
    # long_text: 500 chars → truncated, ends with … and has exactly 300 chars
    long_line = next(line for line in md.splitlines() if "[long, " in line)
    long_payload = long_line.split(" : « ", 1)[1].rstrip(" »")
    assert long_payload.endswith("\u2026")
    assert len(long_payload) == 300
    # exact 300 chars: untouched
    exact_line = next(line for line in md.splitlines() if "[exact, " in line)
    exact_payload = exact_line.split(" : « ", 1)[1].rstrip(" »")
    assert exact_payload == exact_text
    assert "\u2026" not in exact_payload
    # short: untouched
    short_line = next(line for line in md.splitlines() if "[short, " in line)
    assert short_text in short_line


def test_top_comments_collapses_internal_whitespace(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
    payload = {
        "children": [
            _comment(
                "root", "root", points=5, id=1,
                children=[
                    _comment(
                        "alice",
                        "<p>line one</p>\n<p>line  two</p>",
                        points=42, id=2,
                    ),
                ],
            ),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/203", json=payload)
    result = fetch_discussion(203)
    assert result is not None
    md = result.top_comments_markdown
    line = next(line for line in md.splitlines() if "[alice, " in line)
    # No newlines, no double spaces in the text payload.
    text = line.split(" : « ", 1)[1].rstrip(" »")
    assert "\n" not in text
    assert "  " not in text
    assert text == "line one line two"


def test_top_comments_empty_when_no_comment_has_points(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
    payload = {
        "children": [
            _comment("alice", "root", id=1, children=[_comment("leaf", "leaf", id=2)]),
            _comment("bob", "root 2", id=3, children=[_comment("leaf2", "leaf", id=4)]),
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/204", json=payload)
    result = fetch_discussion(204)
    assert result is not None
    assert result.top_comments_markdown == ""


def test_top_comments_limits_to_three(httpx_mock, isolated_settings):
    isolated_settings.discussion_budget = 10
    payload = {
        "children": [
            _comment(f"u{i}", f"text {i}", points=100 - i, id=1000 + i,
                     children=[_comment(f"leaf{i}", "leaf", id=2000 + i)])
            for i in range(10)
        ]
    }
    httpx_mock.add_response(url="https://hn.algolia.com/api/v1/items/205", json=payload)
    result = fetch_discussion(205)
    assert result is not None
    md = result.top_comments_markdown
    bullet_count = sum(1 for line in md.splitlines() if line.startswith("- ["))
    assert bullet_count == 3
    # The three with the highest points: u0 (100), u1 (99), u2 (98).
    assert "[u0, 100 pts]" in md
    assert "[u1, 99 pts]" in md
    assert "[u2, 98 pts]" in md
    assert "[u3," not in md


