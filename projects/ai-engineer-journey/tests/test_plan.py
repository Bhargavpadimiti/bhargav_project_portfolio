from datetime import date
from pathlib import Path

import pytest

from journey.plan import PlanError, load_plan

PROJECT = Path(__file__).resolve().parents[1]
PLAN = load_plan(PROJECT / "curriculum" / "plan.yaml")


def test_programme_runs_39_weeks_from_1_december_2026():
    assert len(PLAN.weeks) == 39
    assert PLAN.start_date == date(2026, 12, 1)
    assert PLAN.end_date == date(2027, 8, 29)


def test_week_one_starts_on_the_start_date_and_ends_sunday():
    week = PLAN.week(1)
    assert (week.start, week.end) == (date(2026, 12, 1), date(2026, 12, 6))
    assert week.end.weekday() == 6


def test_later_weeks_run_monday_to_sunday():
    for week in PLAN.weeks[1:]:
        assert week.start.weekday() == 0
        assert (week.end - week.start).days == 6


@pytest.mark.parametrize(
    ("day", "number"),
    [
        (date(2026, 11, 17), 0),  # before the start
        (date(2026, 12, 1), 1),
        (date(2026, 12, 6), 1),  # Sunday of week 1
        (date(2026, 12, 7), 2),  # Monday of week 2
        (date(2027, 2, 28), 13),  # 3-month checkpoint
        (date(2027, 8, 29), 39),  # last day
        (date(2027, 8, 30), 40),  # finished
    ],
)
def test_week_number(day, number):
    assert PLAN.week_number(day) == number


def test_phases_are_contiguous_and_match_their_weeks():
    for phase in PLAN.phases:
        first, last = phase["weeks"]
        assert {w.phase for w in PLAN.weeks[first - 1 : last]} == {phase["id"]}
    covered = [n for p in PLAN.phases for n in range(p["weeks"][0], p["weeks"][1] + 1)]
    assert covered == list(range(1, 40))


def test_checkpoints_at_3_6_and_9_months():
    assert [c["week"] for c in PLAN.checkpoints] == [13, 26, 39]


def test_every_project_has_a_valid_week_range_and_appears_in_the_plan():
    referenced = {w.project for w in PLAN.weeks if w.project}
    for project in PLAN.projects:
        first, last = project["weeks"]
        assert 1 <= first <= last <= 39
        if project["id"] != "ai-engineer-journey":
            assert project["id"] in referenced, f"{project['id']} is never scheduled"


def test_every_week_has_a_focus_and_deliverables():
    for week in PLAN.weeks:
        assert week.focus("depth") or week.focus("build"), f"week {week.number} has no focus"
        assert week.items("deliverables"), f"week {week.number} has no deliverables"


def test_materials_for_the_first_two_weeks_exist():
    for week in PLAN.weeks[:2]:
        assert (PROJECT / "assessments" / "quizzes" / f"{week.quiz}.yaml").is_file()
        assert (PROJECT / "exercises" / week.exercises).is_dir()
        assert (PROJECT / "weeks" / f"week-{week.number:02d}.md").is_file()


def test_expected_hours_grow_with_time():
    assert PLAN.expected_hours(date(2026, 11, 30)) == 0
    assert PLAN.expected_hours(date(2026, 12, 7)) == 10.0
    assert PLAN.expected_hours(date(2028, 1, 1)) == PLAN.expected_hours(PLAN.end_date)


def test_week_one_counts_hours_logged_before_the_start():
    start, end = PLAN.hours_window(PLAN.week(1))
    assert start == date.min and end == date(2026, 12, 6)


def test_out_of_range_week_raises():
    with pytest.raises(PlanError):
        PLAN.week(40)


def test_misnumbered_weeks_are_rejected(tmp_path):
    bad = tmp_path / "plan.yaml"
    bad.write_text(
        "start_date: 2026-12-01\nhours_per_week: 10\nphases: [{id: 0, name: x, weeks: [1, 2]}]\n"
        "weeks:\n  - {week: 1, phase: 0, title: a}\n  - {week: 3, phase: 0, title: b}\n",
        encoding="utf-8",
    )
    with pytest.raises(PlanError, match="numbered"):
        load_plan(bad)


def test_unknown_phase_is_rejected(tmp_path):
    bad = tmp_path / "plan.yaml"
    bad.write_text(
        "start_date: 2026-12-01\nhours_per_week: 10\nphases: [{id: 0, name: x, weeks: [1, 1]}]\n"
        "weeks:\n  - {week: 1, phase: 7, title: a}\n",
        encoding="utf-8",
    )
    with pytest.raises(PlanError, match="phase"):
        load_plan(bad)
