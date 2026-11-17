"""End-to-end tests of the `journey` command against a throwaway copy of the programme."""

from journey import store
from journey.cli import main
from journey.exercises import run_checks

PASSING = "def double(x):\n    return x * 2\n"
FAILING = "def double(x):\n    raise NotImplementedError\n"
TESTS = (
    "from week99 import double\n\n"
    "def test_positive():\n    assert double(2) == 4\n\n"
    "def test_zero_edge_case():\n    assert double(0) == 0\n"
)


def make_exercise(home, solution: str):
    folder = home / "exercises" / "week-99"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "week99.py").write_text(solution)
    (folder / "test_week99.py").write_text(TESTS)
    return folder


def test_status_shows_current_week_and_pace(home, capsys):
    assert main(["status"]) == 0
    out = capsys.readouterr().out
    assert "Week 2 of 39" in out
    assert "Python basics" in out
    assert "behind" in out  # nothing logged yet


def test_status_before_the_start(home, capsys, monkeypatch):
    monkeypatch.setenv("JOURNEY_TODAY", "2026-11-17")
    assert main(["status"]) == 0
    out = capsys.readouterr().out
    assert "14 days to go" in out and "Week 1" in out


def test_log_then_status_counts_hours(home, capsys):
    assert main(["log", "3", "CS50P", "lecture", "0", "-t", "depth"]) == 0
    assert main(["log", "2", "exercises", "--date", "2026-12-08", "-t", "build"]) == 0
    capsys.readouterr()
    main(["status"])
    out = capsys.readouterr().out
    assert "5 / 10 h this week" in out
    assert "Streak : 2 days" in out


def test_log_rejects_future_dates_and_bad_hours(home, capsys):
    assert main(["log", "1", "x", "--date", "2030-01-01"]) == 2
    assert main(["log", "0", "x"]) == 2
    assert "error" in capsys.readouterr().err


def test_week_command_prints_edge_cases_and_resources(home, capsys):
    assert main(["week", "12"]) == 0
    out = capsys.readouterr().out
    assert "Softmax overflow" in out and "RESOURCES" in out


def test_quiz_list_and_missing_quiz(home, capsys):
    assert main(["quiz", "--list"]) == 0
    assert "diagnostic" in capsys.readouterr().out
    assert main(["quiz", "week-30"]) == 2
    assert "tutor prepares" in capsys.readouterr().err


def test_quiz_run_is_recorded(home, monkeypatch, capsys):
    replies = iter(["e"] * 100)  # "I don't know yet" is option e on 4-choice questions
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(replies))
    assert main(["quiz", "week-01"]) == 0
    results = store.load_results(home / "progress" / "results.yaml")
    attempt = results["quizzes"]["week-01"][0]
    assert attempt["total"] == 12 and attempt["date"] == "2026-12-09"


def test_quitting_a_quiz_records_nothing(home, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _prompt="": "q")
    assert main(["quiz", "week-01"]) == 1
    assert store.load_results(home / "progress" / "results.yaml")["quizzes"] == {}


def test_run_checks_counts_passes(home):
    folder = make_exercise(home, FAILING)
    result = run_checks(folder, cwd=home, quiet=True)
    assert (result.passed, result.total, result.complete) == (0, 2, False)
    make_exercise(home, PASSING)
    assert run_checks(folder, cwd=home, quiet=True).complete


def test_check_records_attempts(home, capsys):
    make_exercise(home, FAILING)
    assert main(["check", "week-99"]) == 1
    make_exercise(home, PASSING)
    assert main(["check", "week-99"]) == 0
    attempts = store.load_results(home / "progress" / "results.yaml")["exercises"]["week-99"]
    assert [(a["passed"], a["total"]) for a in attempts] == [(0, 2), (2, 2)]


def test_check_with_syntax_error_records_nothing(home, capsys):
    make_exercise(home, "def double(x)\n    return x\n")
    assert main(["check", "week-99"]) == 1
    assert "syntax or import error" in capsys.readouterr().out
    assert store.load_results(home / "progress" / "results.yaml")["exercises"] == {}


def test_check_unknown_set(home, capsys):
    assert main(["check", "week-77"]) == 2


def test_report_writes_dashboard_and_syncs_readmes(home, capsys):
    main(["log", "2", "setup", "-t", "build"])
    make_exercise(home, PASSING)
    main(["check", "week-99"])
    assert main(["report"]) == 0
    dashboard = (home / "PROGRESS.md").read_text()
    assert "Week 2 of 39" in dashboard
    assert "| week-99 | 2/2 ✅" in dashboard
    assert "RAG Assistant" in dashboard
    readme = (home / "README.md").read_text()
    assert "old" not in readme and "2 h** studied" in readme
    plan = (home / "curriculum" / "README.md").read_text()
    assert plan.count("\n| ") == 41  # header + separator + 39 weeks
    assert "🏁 6-month checkpoint" in plan
    # running it again changes nothing
    capsys.readouterr()
    main(["report"])
    assert "Updated" not in capsys.readouterr().out
