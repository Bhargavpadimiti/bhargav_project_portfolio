"""Multiple-choice quizzes stored as YAML.

Quiz file format (assessments/quizzes/<name>.yaml)::

    title: Week 2 - Python basics
    questions:
      - id: py-floor-div           # unique within the quiz
        topic: python              # used for per-topic scores and feedback
        q: What does `-7 // 2` evaluate to?
        choices: ["-4", "-3", "-3.5", "3"]
        answer: 0                  # index into choices
        explain: Floor division rounds towards negative infinity.
    feedback:                      # optional, per topic, first matching band wins
      python:
        - below: 0.6
          message: Redo the exercises before moving on.
        - message: Good - keep going.

Choices are shuffled on every attempt and an "I don't know yet" option is
always added, so guessing is never necessary and answer positions can't be
memorised.
"""

from __future__ import annotations

import random
from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

DONT_KNOW = "I don't know yet"
LETTERS = "abcdefgh"


class QuizError(ValueError):
    """The quiz file is malformed."""


class QuizAborted(Exception):
    """The learner quit before finishing; nothing is recorded."""


@dataclass(frozen=True)
class Question:
    id: str
    topic: str
    prompt: str
    choices: list[str]
    answer: str
    explain: str


@dataclass(frozen=True)
class Quiz:
    name: str
    title: str
    questions: list[Question]
    feedback: dict[str, list[dict[str, Any]]] = field(default_factory=dict)


@dataclass
class QuizResult:
    correct: int = 0
    dont_know: int = 0
    by_topic: dict[str, list[int]] = field(default_factory=dict)
    missed: list[tuple[Question, str]] = field(default_factory=list)

    @property
    def total(self) -> int:
        return sum(total for _, total in self.by_topic.values())

    @property
    def ratio(self) -> float:
        return self.correct / self.total if self.total else 0.0

    def as_record(self, day: str) -> dict[str, Any]:
        return {
            "date": day,
            "score": self.correct,
            "total": self.total,
            "dont_know": self.dont_know,
            "by_topic": {topic: list(pair) for topic, pair in self.by_topic.items()},
        }


def load_quiz(path: Path) -> Quiz:
    if not path.is_file():
        raise QuizError(f"quiz not found: {path.name}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    questions: list[Question] = []
    seen: set[str] = set()
    for i, item in enumerate(raw.get("questions") or [], start=1):
        where = f"{path.name} question {i}"
        qid = str(item.get("id") or "")
        choices = [str(c) for c in item.get("choices") or []]
        answer = item.get("answer")
        if not qid or qid in seen:
            raise QuizError(f"{where}: missing or duplicate id {qid!r}")
        if len(choices) < 2 or len(set(choices)) != len(choices):
            raise QuizError(f"{where}: needs at least 2 distinct choices")
        if DONT_KNOW in choices:
            raise QuizError(f"{where}: '{DONT_KNOW}' is added automatically")
        if (
            not isinstance(answer, int)
            or isinstance(answer, bool)
            or not 0 <= answer < len(choices)
        ):
            raise QuizError(f"{where}: answer must be an index from 0 to {len(choices) - 1}")
        if not item.get("q") or not item.get("explain"):
            raise QuizError(f"{where}: needs both 'q' and 'explain'")
        seen.add(qid)
        questions.append(
            Question(
                id=qid,
                topic=str(item.get("topic") or "general"),
                prompt=str(item["q"]).strip(),
                choices=choices,
                answer=choices[answer],
                explain=str(item["explain"]).strip(),
            )
        )
    if not questions:
        raise QuizError(f"{path.name}: has no questions")
    return Quiz(
        name=path.stem,
        title=str(raw.get("title") or path.stem),
        questions=questions,
        feedback=raw.get("feedback") or {},
    )


def feedback_for(quiz: Quiz, topic: str, ratio: float) -> str | None:
    for band in quiz.feedback.get(topic, []):
        if "below" not in band or ratio < float(band["below"]):
            return str(band["message"]).strip()
    return None


def run_quiz(
    quiz: Quiz,
    ask: Callable[[str], str],
    say: Callable[[str], None],
    rng: random.Random | None = None,
) -> QuizResult:
    rng = rng or random.Random()
    result = QuizResult()
    say(f"\n{quiz.title} - {len(quiz.questions)} questions. Type a letter; 'q' quits.\n")
    for number, question in enumerate(quiz.questions, start=1):
        options = question.choices[:]
        rng.shuffle(options)
        options.append(DONT_KNOW)
        say(f"Q{number}. [{question.topic}] {question.prompt}")
        for letter, option in zip(LETTERS, options, strict=False):
            say(f"   {letter}) {option}")
        valid = LETTERS[: len(options)]
        while True:
            reply = ask("Your answer: ").strip().lower()
            if reply == "q":
                raise QuizAborted
            if len(reply) == 1 and reply in valid:
                break
            say(f"   Please type one of: {', '.join(valid)} (or q to quit)")
        chosen = options[valid.index(reply)]
        pair = result.by_topic.setdefault(question.topic, [0, 0])
        pair[1] += 1
        if chosen == question.answer:
            result.correct += 1
            pair[0] += 1
            say("   ✓ correct\n")
        else:
            if chosen == DONT_KNOW:
                result.dont_know += 1
            result.missed.append((question, chosen))
            say(f"   ✗ answer: {question.answer}\n")
    return result


def summarise(quiz: Quiz, result: QuizResult) -> str:
    lines = [f"Score: {result.correct}/{result.total} ({result.ratio:.0%})"]
    if result.dont_know:
        lines.append(
            f"'I don't know yet': {result.dont_know} - honest answers make the plan better."
        )
    lines.append("\nBy topic:")
    for topic, (correct, total) in result.by_topic.items():
        lines.append(f"  {topic:<10} {correct}/{total}  ({correct / total:.0%})")
        note = feedback_for(quiz, topic, correct / total)
        if note:
            lines.append(f"             -> {note}")
    if result.missed:
        lines.append("\nReview these:")
        for question, chosen in result.missed:
            lines.append(f"  • {question.prompt}")
            lines.append(f"    You chose: {chosen}. Correct: {question.answer}")
            lines.append(f"    Why: {question.explain}")
    return "\n".join(lines)
