import random
import re
from pathlib import Path

import pytest

from journey.quiz import (
    DONT_KNOW,
    QuizAborted,
    QuizError,
    feedback_for,
    load_quiz,
    run_quiz,
    summarise,
)

QUIZZES = sorted((Path(__file__).resolve().parents[1] / "assessments" / "quizzes").glob("*.yaml"))


class Session:
    """Plays a quiz: remembers printed options and answers via a strategy."""

    def __init__(self, strategy):
        self.strategy = strategy
        self.options: dict[str, str] = {}
        self.printed: list[str] = []

    def say(self, line: str) -> None:
        self.printed.append(line)
        match = re.match(r"\s+([a-h])\) (.*)", line)
        if match:
            self.options[match.group(1)] = match.group(2)
        elif line.startswith("Q"):
            self.options = {}

    def ask(self, _prompt: str) -> str:
        return self.strategy(self.options)


def answer_with(text_for):
    def strategy(options):
        wanted = text_for(options)
        return next(letter for letter, text in options.items() if text == wanted)

    return strategy


@pytest.mark.parametrize("path", QUIZZES, ids=lambda p: p.stem)
def test_every_quiz_file_is_valid(path):
    quiz = load_quiz(path)
    assert len(quiz.questions) >= 10
    for question in quiz.questions:
        assert question.answer in question.choices


def make_quiz(tmp_path, body: str):
    path = tmp_path / "q.yaml"
    path.write_text(body, encoding="utf-8")
    return path


GOOD = """
title: T
questions:
  - {id: a, topic: x, q: "1+1?", choices: ["2", "3"], answer: 0, explain: maths}
  - {id: b, topic: y, q: "2+2?", choices: ["5", "4", "3"], answer: 1, explain: maths}
feedback:
  x:
    - {below: 0.5, message: revise x}
    - {message: good x}
"""


def test_all_correct_answers_score_full_marks(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    answers = {"1+1?": "2", "2+2?": "4"}
    session = Session(None)
    session.strategy = answer_with(
        lambda opts: next(t for t in opts.values() if t in answers.values())
    )
    result = run_quiz(quiz, session.ask, session.say, random.Random(1))
    assert (result.correct, result.total, result.dont_know) == (2, 2, 0)
    assert result.by_topic == {"x": [1, 1], "y": [1, 1]}


def test_dont_know_is_always_offered_last_and_counted(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    session = Session(answer_with(lambda opts: DONT_KNOW))
    result = run_quiz(quiz, session.ask, session.say, random.Random(1))
    assert result.correct == 0 and result.dont_know == 2
    assert len(result.missed) == 2


def test_invalid_input_reprompts_until_valid(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    replies = iter(["", "zz", "9", "a", "a"])
    session = Session(lambda _opts: next(replies))
    result = run_quiz(quiz, session.ask, session.say, random.Random(1))
    assert result.total == 2
    assert any("Please type one of" in line for line in session.printed)


def test_q_quits_without_a_result(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    session = Session(lambda _opts: "q")
    with pytest.raises(QuizAborted):
        run_quiz(quiz, session.ask, session.say, random.Random(1))


def test_choices_are_shuffled_between_attempts(tmp_path):
    body = "questions:\n  - {id: a, q: pick, choices: [w, x, y, z], answer: 0, explain: e}\n"
    quiz = load_quiz(make_quiz(tmp_path, body))
    orders = set()
    for seed in range(20):
        session = Session(lambda _opts: "a")
        run_quiz(quiz, session.ask, session.say, random.Random(seed))
        orders.add(tuple(session.options.values()))
    assert len(orders) > 1


def test_feedback_bands(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    assert feedback_for(quiz, "x", 0.2) == "revise x"
    assert feedback_for(quiz, "x", 0.9) == "good x"
    assert feedback_for(quiz, "y", 0.9) is None


def test_summary_explains_missed_questions(tmp_path):
    quiz = load_quiz(make_quiz(tmp_path, GOOD))
    session = Session(answer_with(lambda opts: DONT_KNOW))
    text = summarise(quiz, run_quiz(quiz, session.ask, session.say, random.Random(1)))
    assert "Score: 0/2" in text and "Why: maths" in text and "revise x" in text


@pytest.mark.parametrize(
    ("body", "message"),
    [
        ("questions: []", "no questions"),
        ("questions:\n  - {id: a, q: x, choices: [a, b], answer: 2, explain: e}", "answer must be"),
        (
            "questions:\n  - {id: a, q: x, choices: [a, b], answer: true, explain: e}",
            "answer must be",
        ),
        ("questions:\n  - {id: a, q: x, choices: [a, a], answer: 0, explain: e}", "distinct"),
        ("questions:\n  - {id: a, q: x, choices: [a], answer: 0, explain: e}", "distinct"),
        ("questions:\n  - {id: a, q: x, choices: [a, b], answer: 0}", "explain"),
        (
            "questions:\n  - {id: a, q: x, choices: [a, b], answer: 0, explain: e}\n"
            "  - {id: a, q: y, choices: [a, b], answer: 0, explain: e}",
            "duplicate",
        ),
        (
            f'questions:\n  - {{id: a, q: x, choices: [a, "{DONT_KNOW}"], answer: 0, explain: e}}',
            "automatically",
        ),
    ],
)
def test_malformed_quizzes_are_rejected(tmp_path, body, message):
    with pytest.raises(QuizError, match=message):
        load_quiz(make_quiz(tmp_path, body))
