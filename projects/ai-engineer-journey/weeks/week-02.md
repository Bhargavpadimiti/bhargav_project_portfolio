# Week 2 · Python basics: values, types, decisions (Mon 7 – Sun 13 December 2026)

**Goal:** read and write small Python programs confidently, and start thinking in
edge cases.

**Main course:** [CS50P](https://cs50.harvard.edu/python/) lectures 0 and 1 (free). Code
along in VS Code; don't just watch. Paste confusing snippets into
[Python Tutor](https://pythontutor.com) to see each step.

**Time:** ~10 hours.

## Mon: lecture 0, functions and variables (1.5 h)

- `print`, `input`, variables, strings, f-strings, `int`/`float`
- Writing your own function with `def`
- **Try:** what does `input()` return when you type `42`? Check with `type(...)`.

## Tue: finish lecture 0, then the problem set (1.5 h)

- Do at least 3 of the lecture 0 problems on the CS50P site
- Anki cards: string methods, `/` vs `//`, f-string formatting

## Thu: lecture 1, conditionals (1.5 h)

- `if`/`elif`/`else`, comparison operators, `and`/`or`/`not`, `match`
- **Truthiness:** which of these are falsy? `0`, `""`, `"0"`, `"False"`, `[]`, `None`. Predict first, then check.

## Sat: exercises (3 h)

```bash
journey check week-02
```

Work through `exercises/week-02/week02.py` top to bottom. The last two are **STRETCH**
(they use ideas from week 3); attempt them last.

For each function:

1. Read the docstring and the matching tests.
2. Before coding, **list the edge cases in a comment**: empty input? zero? negative? exactly on a boundary?
3. Implement, run, fix.

These functions aren't random: `estimate_tokens` and `estimate_cost` are how you'll
budget LLM calls from week 5 on, and `truncate` and `normalize_whitespace` are the
text-cleaning steps every RAG pipeline needs.

## Sun: build, quiz, reflect (2.5 h)

1. **Build `prompt_builder.py`** (in a `practice/` folder under this project). It asks
   for a topic, an audience (beginner/expert) and a tone, then prints a clear prompt
   for an LLM, with a role, the task, constraints and an output format. Handle empty
   answers with sensible defaults.
2. `journey quiz week-02` (target 80%+; review the explanations and retake if lower)
3. `journal/week-02.md`, then `journey report`, then commit on `learn/week-02` and open a pull request
4. Check-in with your tutor

## Edge cases to be able to explain

- Why `0.1 + 0.2 != 0.3`, and what to use instead
- Why `-7 // 2` is `-4`, not `-3`
- Why `round(2.5)` is `2`
- Why `bool("False")` is `True`
- What `int("3.5")` does, and how you'd parse it safely

## Done when

- [ ] `journey check week-02` → all tests pass (stretch ones included, ideally)
- [ ] `prompt_builder.py` runs and handles empty input
- [ ] Quiz ≥ 80%
- [ ] Journal written, pull request merged
