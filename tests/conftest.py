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
    yield settings
    config_module.reset_settings()
