"""Where the programme lives on disk, and what "today" is.

Both can be overridden with environment variables, which keeps the tests
independent of the real repository and the real calendar:

- ``JOURNEY_HOME``  - folder that holds curriculum/, progress/, exercises/ ...
- ``JOURNEY_TODAY`` - ISO date (YYYY-MM-DD) to treat as today
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path


def today() -> date:
    override = os.environ.get("JOURNEY_TODAY")
    return date.fromisoformat(override) if override else date.today()


@dataclass(frozen=True)
class Paths:
    root: Path

    @classmethod
    def discover(cls) -> Paths:
        override = os.environ.get("JOURNEY_HOME")
        # src/journey/config.py -> parents[2] is the project folder
        root = Path(override) if override else Path(__file__).resolve().parents[2]
        return cls(root.resolve())

    @property
    def plan(self) -> Path:
        return self.root / "curriculum" / "plan.yaml"

    @property
    def log(self) -> Path:
        return self.root / "progress" / "log.csv"

    @property
    def results(self) -> Path:
        return self.root / "progress" / "results.yaml"

    @property
    def quizzes(self) -> Path:
        return self.root / "assessments" / "quizzes"

    @property
    def exercises(self) -> Path:
        return self.root / "exercises"

    @property
    def weeks(self) -> Path:
        return self.root / "weeks"

    @property
    def dashboard(self) -> Path:
        return self.root / "PROGRESS.md"

    @property
    def readme(self) -> Path:
        return self.root / "README.md"

    @property
    def curriculum_readme(self) -> Path:
        return self.root / "curriculum" / "README.md"

    @property
    def portfolio_projects(self) -> Path:
        """The repository's projects/ folder (this project's parent)."""
        return self.root.parent
