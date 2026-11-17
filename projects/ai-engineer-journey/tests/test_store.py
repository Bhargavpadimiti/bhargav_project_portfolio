from datetime import date

import pytest

from journey import store
from journey.store import Session


def s(day: str, hours: float = 1, track: str = "depth", note: str = "x") -> Session:
    return Session(date.fromisoformat(day), hours, track, note)


def test_log_roundtrip_writes_header_once(tmp_path):
    path = tmp_path / "progress" / "log.csv"
    store.add_session(path, s("2026-12-01", 1.5, "build", "  setup  "))
    store.add_session(path, s("2026-12-02", 2))
    assert path.read_text().count("date,hours,track,note") == 1
    sessions = store.read_log(path)
    assert sessions == [s("2026-12-01", 1.5, "build", "setup"), s("2026-12-02", 2)]


def test_header_only_file_reads_as_empty(tmp_path):
    path = tmp_path / "log.csv"
    path.write_text("date,hours,track,note\n")
    assert store.read_log(path) == []
    store.add_session(path, s("2026-12-01"))
    assert len(store.read_log(path)) == 1


def test_missing_log_reads_as_empty(tmp_path):
    assert store.read_log(tmp_path / "nope.csv") == []


def test_notes_with_commas_and_quotes_survive(tmp_path):
    path = tmp_path / "log.csv"
    store.add_session(path, s("2026-12-01", note='read "Attention", part 1, again'))
    assert store.read_log(path)[0].note == 'read "Attention", part 1, again'


@pytest.mark.parametrize(
    "session",
    [
        s("2026-12-01", 0),
        s("2026-12-01", -1),
        s("2026-12-01", 16.5),
        s("2026-12-01", track="fun"),
        s("2026-12-01", note="  "),
    ],
)
def test_invalid_sessions_are_rejected(tmp_path, session):
    with pytest.raises(ValueError):
        store.add_session(tmp_path / "log.csv", session)
    assert not (tmp_path / "log.csv").exists()


def test_hours_between_is_inclusive():
    sessions = [s("2026-12-01", 1), s("2026-12-06", 2), s("2026-12-07", 4)]
    assert store.hours_between(sessions, date(2026, 12, 1), date(2026, 12, 6)) == 3


def test_hours_by_track():
    totals = store.hours_by_track(
        [s("2026-12-01", 1, "build"), s("2026-12-02", 2.5, "build"), s("2026-12-03", 1)]
    )
    assert totals == {"depth": 1, "build": 3.5, "career": 0, "review": 0}


def test_streak_counts_consecutive_days_up_to_today_or_yesterday():
    sessions = [s("2026-12-01"), s("2026-12-02"), s("2026-12-03"), s("2026-12-03")]
    assert store.streak(sessions, date(2026, 12, 3)) == 3
    assert store.streak(sessions, date(2026, 12, 4)) == 3  # today not studied yet
    assert store.streak(sessions, date(2026, 12, 5)) == 0  # missed a day
    assert store.streak([], date(2026, 12, 5)) == 0


def test_plural():
    assert store.plural(1, "day") == "1 day"
    assert store.plural(0, "day") == "0 days"


def test_record_attempt_appends_history(tmp_path):
    path = tmp_path / "results.yaml"
    store.record_attempt(
        path, "quizzes", "week-02", {"date": "2026-12-09", "score": 5, "total": 10}
    )
    store.record_attempt(
        path, "quizzes", "week-02", {"date": "2026-12-10", "score": 9, "total": 10}
    )
    data = store.load_results(path)
    assert [a["score"] for a in data["quizzes"]["week-02"]] == [5, 9]
    assert data["exercises"] == {}
    assert store.best_attempt(data["quizzes"]["week-02"], "score", "total")["score"] == 9


def test_best_attempt_ignores_empty_runs():
    assert store.best_attempt([{"passed": 0, "total": 0}], "passed", "total") is None


def test_unknown_result_kind_is_rejected(tmp_path):
    with pytest.raises(ValueError):
        store.record_attempt(tmp_path / "r.yaml", "grades", "x", {})
