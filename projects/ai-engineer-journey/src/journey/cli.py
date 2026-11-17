"""`journey` - the command-line tracker for the AI Engineer Journey.

journey status                    where am I, what's due, am I on track?
journey week [N]                  the full plan for this week (or week N)
journey log 1.5 "notes" -t build  record a study session
journey quiz week-02              take a quiz (scores are saved)
journey check week-02             run a week's coding exercises
journey report                    refresh PROGRESS.md and the README tables
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from . import store
from .config import Paths, today
from .exercises import run_checks
from .plan import Plan, PlanError, load_plan
from .quiz import QuizAborted, QuizError, load_quiz, run_quiz, summarise
from .report import (
    current_or_first,
    dashboard,
    fmt_day,
    fmt_range,
    plan_table,
    readme_summary,
    status_line,
    sync_block,
)


def _plan(paths: Paths) -> Plan:
    return load_plan(paths.plan)


def cmd_status(args: argparse.Namespace, paths: Paths) -> int:
    plan = _plan(paths)
    now = today()
    week = current_or_first(plan, now)
    sessions = store.read_log(paths.log)
    results = store.load_results(paths.results)
    number = plan.week_number(now)

    print(f"AI Engineer Journey · {fmt_day(now, weekday=True)}")
    print(status_line(plan, now))
    if number == 0:
        print("Tip: you can start Week 1 (setup + diagnostic) early.")
    print()
    print(f"Week {week.number}: {week.title}  ({fmt_range(week.start, week.end)})")
    print(f"  Depth : {week.focus('depth') or '—'}")
    print(f"  Build : {week.focus('build') or '—'}")
    for item in week.items("deliverables"):
        print(f"  [ ] {item}")

    this_week = store.hours_between(sessions, *plan.hours_window(week))
    total = store.hours_between(sessions, date.min, now)
    expected = plan.expected_hours(now)
    print()
    print(f"Hours  : {this_week:g} / {plan.hours_per_week:g} h this week · {total:g} h total")
    if number >= 1:
        gap = round(total - expected, 1)
        pace = (
            "on track" if gap >= -2 else f"{-gap:g} h behind - see weeks/README.md for catching up"
        )
        print(f"Pace   : expected {expected:g} h by today → {pace}")
    print(f"Streak : {store.plural(store.streak(sessions, now), 'day')}")

    todo = []
    if week.quiz and week.quiz not in (results.get("quizzes") or {}):
        todo.append(f"journey quiz {week.quiz}")
    if week.exercises:
        attempts = (results.get("exercises") or {}).get(week.exercises, [])
        if not any(a["total"] and a["passed"] == a["total"] for a in attempts):
            todo.append(f"journey check {week.exercises}")
    guide = paths.weeks / f"week-{week.number:02d}.md"
    if guide.is_file():
        todo.insert(0, f"read {guide.relative_to(paths.root).as_posix()}")
    if todo:
        print("Next   : " + "  ·  ".join(todo))
    return 0


def cmd_week(args: argparse.Namespace, paths: Paths) -> int:
    plan = _plan(paths)
    week = plan.week(args.number) if args.number else current_or_first(plan, today())
    phase = plan.phase(week.phase)
    print(f"Week {week.number}: {week.title}")
    print(f"{fmt_range(week.start, week.end)} · Phase {phase['id']}: {phase['name']}")
    checkpoint = plan.checkpoint(week.number)
    if checkpoint:
        print(f"🏁 {checkpoint['name']}: {checkpoint['goal']}")
    for track, label in (
        ("depth", "DEPTH - understand it from scratch"),
        ("build", "BUILD - ship something real"),
    ):
        if week.focus(track):
            print(f"\n{label}\n  {week.focus(track)}")
            for topic in week.topics(track):
                print(f"   • {topic}")
    for key, label in (
        ("edge_cases", "EDGE CASES to test and explain"),
        ("design", "SYSTEM DESIGN"),
        ("career", "CAREER"),
        ("deliverables", "DELIVERABLES"),
        ("resources", "RESOURCES (all free unless marked)"),
    ):
        items = week.items(key)
        if items:
            print(f"\n{label}")
            for item in items:
                print(f"   • {item}")
    extras = []
    if week.quiz:
        extras.append(f"quiz: journey quiz {week.quiz}")
    if week.exercises:
        extras.append(f"exercises: journey check {week.exercises}")
    if extras:
        print("\n" + "  ·  ".join(extras))
    guide = paths.weeks / f"week-{week.number:02d}.md"
    if guide.is_file():
        print(f"Day-by-day guide: {guide.relative_to(paths.root).as_posix()}")
    else:
        print("Day-by-day guide: your tutor prepares it the week before.")
    return 0


def cmd_log(args: argparse.Namespace, paths: Paths) -> int:
    day = date.fromisoformat(args.date) if args.date else today()
    if day > today():
        raise ValueError("can't log a session in the future")
    session = store.Session(day=day, hours=args.hours, track=args.track, note=" ".join(args.note))
    store.add_session(paths.log, session)
    sessions = store.read_log(paths.log)
    plan = _plan(paths)
    week = current_or_first(plan, day)
    this_week = store.hours_between(sessions, *plan.hours_window(week))
    print(f"Logged {session.hours:g} h of {session.track} on {fmt_day(day)}.")
    streak = store.plural(store.streak(sessions, today()), "day")
    print(f"Week {week.number}: {this_week:g} / {plan.hours_per_week:g} h · streak {streak}")
    return 0


def cmd_quiz(args: argparse.Namespace, paths: Paths) -> int:
    if args.list:
        for path in sorted(paths.quizzes.glob("*.yaml")):
            quiz = load_quiz(path)
            print(f"{quiz.name:<14} {len(quiz.questions):>3} questions  {quiz.title}")
        return 0
    if not args.name:
        raise ValueError("name a quiz, e.g. `journey quiz diagnostic` (or --list)")
    path = paths.quizzes / f"{args.name}.yaml"
    if not path.is_file():
        raise QuizError(
            f"no quiz named '{args.name}' yet. Your tutor prepares each week's quiz "
            "the week before (see `journey quiz --list`)."
        )
    quiz = load_quiz(path)
    try:
        result = run_quiz(quiz, ask=input, say=print)
    except (QuizAborted, EOFError, KeyboardInterrupt):
        print("\nQuiz stopped - nothing was recorded.")
        return 1
    print(summarise(quiz, result))
    store.record_attempt(paths.results, "quizzes", quiz.name, result.as_record(today().isoformat()))
    print("\nSaved to progress/results.yaml. Run `journey report` to update the dashboard.")
    return 0


def cmd_check(args: argparse.Namespace, paths: Paths) -> int:
    folder = paths.exercises / args.name
    if not folder.is_dir():
        raise FileNotFoundError(f"no exercises named '{args.name}' yet (looked in {folder})")
    result = run_checks(folder, cwd=paths.root)
    if result.total == 0:
        print(
            "\nNo tests ran - there is probably a syntax or import error above. Fix it and re-run."
        )
        return 1
    store.record_attempt(
        paths.results,
        "exercises",
        args.name,
        {"date": today().isoformat(), "passed": result.passed, "total": result.total},
    )
    print()
    if result.complete:
        print(f"✅ {args.name}: all {result.total} tests pass, edge cases included. Nice work.")
    else:
        print(
            f"{args.name}: {result.passed}/{result.total} tests pass. Read the first failing "
            "test's name and its assert - it tells you which case to handle."
        )
    return 0 if result.complete else 1


def cmd_report(args: argparse.Namespace, paths: Paths) -> int:
    plan = _plan(paths)
    now = today()
    sessions = store.read_log(paths.log)
    results = store.load_results(paths.results)
    paths.dashboard.write_text(
        dashboard(plan, sessions, results, now, paths.portfolio_projects), encoding="utf-8"
    )
    print(f"Wrote {paths.dashboard.name}")
    if sync_block(paths.readme, "progress", readme_summary(plan, sessions, results, now)):
        print("Updated progress summary in README.md")
    if sync_block(paths.curriculum_readme, "plan", plan_table(plan)):
        print("Updated the weekly table in curriculum/README.md")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="journey", description="Track the AI Engineer Journey.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="where am I and what's next").set_defaults(func=cmd_status)

    week = sub.add_parser("week", help="show a week's full plan")
    week.add_argument("number", nargs="?", type=int, help="week number (default: current week)")
    week.set_defaults(func=cmd_week)

    log = sub.add_parser("log", help="record a study session")
    log.add_argument("hours", type=float, help="hours studied, e.g. 1.5")
    log.add_argument("note", nargs="+", help="what you studied")
    log.add_argument("-t", "--track", choices=store.TRACKS, default="depth")
    log.add_argument("--date", help="YYYY-MM-DD (default: today)")
    log.set_defaults(func=cmd_log)

    quiz = sub.add_parser("quiz", help="take a quiz")
    quiz.add_argument("name", nargs="?", help="quiz name, e.g. diagnostic or week-02")
    quiz.add_argument("--list", action="store_true", help="list available quizzes")
    quiz.set_defaults(func=cmd_quiz)

    check = sub.add_parser("check", help="run a week's coding exercises")
    check.add_argument("name", help="exercise set, e.g. week-02")
    check.set_defaults(func=cmd_check)

    sub.add_parser("report", help="refresh PROGRESS.md and README tables").set_defaults(
        func=cmd_report
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        return args.func(args, Paths.discover())
    except (PlanError, QuizError, ValueError, FileNotFoundError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
