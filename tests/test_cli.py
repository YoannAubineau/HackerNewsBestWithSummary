from pathlib import Path

from app.cli import _emit_failures
from app.pipeline import CycleResult


def test_emit_failures_skips_github_output_when_env_missing(monkeypatch):
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    _emit_failures(CycleResult(failures=[("guid://a", "boom")]))


def test_emit_failures_writes_count_and_json(tmp_path: Path, monkeypatch):
    output = tmp_path / "gh_output.txt"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))

    _emit_failures(
        CycleResult(
            failures=[
                ("https://news.ycombinator.com/item?id=1", "fetch_article: 404"),
                ("https://news.ycombinator.com/item?id=2", "nothing to summarize"),
            ]
        )
    )

    lines = output.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "failures_count=2"
    assert lines[1].startswith("failures_json=")
    payload = lines[1].removeprefix("failures_json=")
    assert (
        payload
        == '[{"guid":"https://news.ycombinator.com/item?id=1","error":"fetch_article: 404"},'
        '{"guid":"https://news.ycombinator.com/item?id=2","error":"nothing to summarize"}]'
    )


def test_emit_failures_writes_zero_when_no_failures(tmp_path: Path, monkeypatch):
    output = tmp_path / "gh_output.txt"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))

    _emit_failures(CycleResult(failures=[]))

    lines = output.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "failures_count=0"
    assert lines[1] == "failures_json=[]"
