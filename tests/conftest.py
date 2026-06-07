from pathlib import Path

import pytest

from app import config as config_module


@pytest.fixture(autouse=True)
def isolated_settings(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("OPENROUTER_API_KEY", "sk-test")
    monkeypatch.chdir(tmp_path)
    config_module.reset_settings()
    settings = config_module.get_settings()
    settings.artifacts_dir = tmp_path / "artifacts"
    settings.artifacts_dir.mkdir(parents=True, exist_ok=True)
    settings.articles_dir = tmp_path / "articles"
    settings.articles_dir.mkdir(parents=True, exist_ok=True)
    # Tests opt in to Wayback explicitly. Leaving it on would force every
    # existing fetch_article test that exercises a failure path to also
    # mock archive.org calls, which is unrelated to what they verify.
    settings.wayback_enabled = False
    # Same rationale as wayback above: tests opt in to the reader fallback
    # explicitly so existing failure-path tests don't have to mock r.jina.ai.
    settings.reader_enabled = False
    yield settings
    config_module.reset_settings()
