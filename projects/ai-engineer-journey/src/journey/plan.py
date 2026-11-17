"""Load the curriculum (curriculum/plan.yaml) and work out dates for each week.

Weeks run Monday to Sunday. Week 1 starts on the programme's start date
(which may be mid-week) and ends on the following Sunday.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml


class PlanError(ValueError):
    """The plan file is missing something or contradicts itself."""


@dataclass(frozen=True)
class Week:
    number: int
    phase: int
    title: str
    start: date
    end: date
    data: dict[str, Any] = field(repr=False)

    def focus(self, track: str) -> str:
        section = self.data.get(track) or {}
        return section.get("focus", "") if isinstance(section, dict) else ""

    def topics(self, track: str) -> list[str]:
        section = self.data.get(track) or {}
        return list(section.get("topics", [])) if isinstance(section, dict) else []

    def items(self, key: str) -> list[str]:
        value = self.data.get(key) or []
        return [value] if isinstance(value, str) else list(value)

    @property
    def quiz(self) -> str | None:
        return self.data.get("quiz")

    @property
    def exercises(self) -> str | None:
        return self.data.get("exercises")

    @property
    def project(self) -> str | None:
        return self.data.get("project")


@dataclass(frozen=True)
class Plan:
    start_date: date
    hours_per_week: float
    phases: list[dict[str, Any]]
    projects: list[dict[str, Any]]
    checkpoints: list[dict[str, Any]]
    weeks: list[Week]

    @property
    def end_date(self) -> date:
        return self.weeks[-1].end

    @property
    def total_hours(self) -> float:
        return self.hours_per_week * len(self.weeks)

    def week(self, number: int) -> Week:
        if not 1 <= number <= len(self.weeks):
            raise PlanError(f"week {number} is outside 1-{len(self.weeks)}")
        return self.weeks[number - 1]

    def week_number(self, day: date) -> int:
        """0 before the start, len(weeks) + 1 after the end, otherwise 1..N."""
        if day < self.start_date:
            return 0
        number = (day - _monday(self.start_date)).days // 7 + 1
        return min(number, len(self.weeks) + 1)

    def phase(self, phase_id: int) -> dict[str, Any]:
        for phase in self.phases:
            if phase["id"] == phase_id:
                return phase
        raise PlanError(f"unknown phase {phase_id}")

    def hours_window(self, week: Week) -> tuple[date, date]:
        """Dates whose study counts towards ``week``. Week 1 also counts an early start."""
        return (date.min if week.number == 1 else week.start), week.end

    def checkpoint(self, number: int) -> dict[str, Any] | None:
        return next((c for c in self.checkpoints if c["week"] == number), None)

    def expected_hours(self, day: date) -> float:
        """Hours a learner on schedule would have logged by the end of ``day``."""
        if day < self.start_date:
            return 0.0
        days_in = min((day - self.start_date).days + 1, (self.end_date - self.start_date).days + 1)
        return round(self.hours_per_week * days_in / 7, 1)


def _monday(day: date) -> date:
    return day - timedelta(days=day.weekday())


def load_plan(path: Path) -> Plan:
    if not path.is_file():
        raise PlanError(f"plan not found: {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}

    try:
        start = raw["start_date"]
        start = start if isinstance(start, date) else date.fromisoformat(str(start))
        hours = float(raw["hours_per_week"])
        phases = list(raw["phases"])
        raw_weeks = list(raw["weeks"])
    except (KeyError, TypeError, ValueError) as exc:
        raise PlanError(f"plan is missing or has an invalid field: {exc}") from exc

    if hours <= 0:
        raise PlanError("hours_per_week must be positive")
    if not raw_weeks:
        raise PlanError("plan has no weeks")

    phase_ids = {p["id"] for p in phases}
    first_monday = _monday(start)
    weeks: list[Week] = []
    for index, data in enumerate(raw_weeks, start=1):
        if data.get("week") != index:
            raise PlanError(
                f"weeks must be numbered 1, 2, 3...; found {data.get('week')} at {index}"
            )
        if data.get("phase") not in phase_ids:
            raise PlanError(f"week {index} refers to unknown phase {data.get('phase')}")
        if not data.get("title"):
            raise PlanError(f"week {index} has no title")
        monday = first_monday + timedelta(weeks=index - 1)
        weeks.append(
            Week(
                number=index,
                phase=data["phase"],
                title=data["title"],
                start=max(start, monday),
                end=monday + timedelta(days=6),
                data=data,
            )
        )

    return Plan(
        start_date=start,
        hours_per_week=hours,
        phases=phases,
        projects=list(raw.get("projects", [])),
        checkpoints=list(raw.get("checkpoints", [])),
        weeks=weeks,
    )
