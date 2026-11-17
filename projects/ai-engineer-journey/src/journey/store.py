"""Read and write the learner's progress files.

- progress/log.csv      one row per study session (easy to diff, open in Excel)
- progress/results.yaml  every quiz and exercise attempt
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import yaml

LOG_FIELDS = ["date", "hours", "track", "note"]
TRACKS = ("depth", "build", "career", "review")
MAX_HOURS_PER_SESSION = 16


@dataclass(frozen=True)
class Session:
    day: date
    hours: float
    track: str
    note: str


def validate_session(session: Session) -> None:
    if not 0 < session.hours <= MAX_HOURS_PER_SESSION:
        raise ValueError(f"hours must be more than 0 and at most {MAX_HOURS_PER_SESSION}")
    if session.track not in TRACKS:
        raise ValueError(f"track must be one of: {', '.join(TRACKS)}")
    if not session.note.strip():
        raise ValueError("add a short note about what you studied")


def read_log(path: Path) -> list[Session]:
    if not path.is_file():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return [
            Session(date.fromisoformat(row["date"]), float(row["hours"]), row["track"], row["note"])
            for row in csv.DictReader(handle)
            if row.get("date")
        ]


def add_session(path: Path, session: Session) -> None:
    validate_session(session)
    path.parent.mkdir(parents=True, exist_ok=True)
    new_file = not path.is_file() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=LOG_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow(
            {
                "date": session.day.isoformat(),
                "hours": f"{session.hours:g}",
                "track": session.track,
                "note": session.note.strip(),
            }
        )


def hours_between(sessions: list[Session], start: date, end: date) -> float:
    return round(sum(s.hours for s in sessions if start <= s.day <= end), 2)


def hours_by_track(sessions: list[Session]) -> dict[str, float]:
    totals = dict.fromkeys(TRACKS, 0.0)
    for s in sessions:
        totals[s.track] = round(totals.get(s.track, 0.0) + s.hours, 2)
    return totals


def plural(count: int, word: str) -> str:
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def streak(sessions: list[Session], today: date) -> int:
    """Consecutive days with study, ending today (or yesterday, if today is still open)."""
    days = {s.day for s in sessions}
    cursor = today if today in days else today - timedelta(days=1)
    count = 0
    while cursor in days:
        count += 1
        cursor -= timedelta(days=1)
    return count


def load_results(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"quizzes": {}, "exercises": {}}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    data.setdefault("quizzes", {})
    data.setdefault("exercises", {})
    return data


def record_attempt(path: Path, kind: str, name: str, entry: dict[str, Any]) -> None:
    if kind not in ("quizzes", "exercises"):
        raise ValueError(f"unknown result kind: {kind}")
    data = load_results(path)
    data[kind] = data.get(kind) or {}
    data[kind].setdefault(name, []).append(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Written by `journey quiz` and `journey check`. Safe to read; avoid hand edits.\n"
        + yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def best_attempt(attempts: list[dict[str, Any]], numerator: str, denominator: str) -> dict | None:
    scored = [a for a in attempts if a.get(denominator)]
    return max(scored, key=lambda a: a[numerator] / a[denominator], default=None)
