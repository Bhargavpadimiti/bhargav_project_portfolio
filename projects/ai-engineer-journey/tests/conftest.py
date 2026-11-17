import shutil
from pathlib import Path

import pytest

PROJECT = Path(__file__).resolve().parents[1]


@pytest.fixture
def home(tmp_path, monkeypatch):
    """A throwaway copy of the programme with an empty progress history."""
    (tmp_path / "curriculum").mkdir()
    shutil.copy(PROJECT / "curriculum" / "plan.yaml", tmp_path / "curriculum" / "plan.yaml")
    shutil.copytree(PROJECT / "assessments", tmp_path / "assessments")
    (tmp_path / "progress").mkdir()
    (tmp_path / "exercises").mkdir()
    (tmp_path / "README.md").write_text(
        "# Journey\n\n<!-- progress:start -->\nold\n<!-- progress:end -->\n", encoding="utf-8"
    )
    (tmp_path / "curriculum" / "README.md").write_text(
        "# Plan\n\n<!-- plan:start -->\n<!-- plan:end -->\n", encoding="utf-8"
    )
    monkeypatch.setenv("JOURNEY_HOME", str(tmp_path))
    monkeypatch.setenv("JOURNEY_TODAY", "2026-12-09")  # Wednesday of week 2
    return tmp_path
