# Week 1 · Launch (Tue 1 – Sun 6 December 2026)

**Goal:** a working setup, an honest picture of where you're starting, and the
weekly routine running. You can start this before 1 December; early hours count towards week 1.

**Time:** ~9 hours across 6 sessions.

## Session 1: install your tools (1.5 h)

Install these in order, accepting the defaults unless noted:

| Tool | Get it | Check it works |
| ---- | ------ | -------------- |
| Git (Windows: includes **Git Bash**, so use it as your terminal) | <https://git-scm.com/downloads> | `git --version` |
| Python 3.13 (Windows: tick **"Add python.exe to PATH"**) | <https://www.python.org/downloads/> | `python --version` (macOS/Linux: `python3 --version`) |
| VS Code, plus the extensions it suggests for this repo | <https://code.visualstudio.com> | Opens the repo folder |
| GitHub CLI | <https://cli.github.com> | `gh auth login`, then `gh auth status` |

Then tell Git who you are (use the email on your GitHub account, or GitHub's private
`noreply` address from <https://github.com/settings/emails>):

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**If something fails:** read the last line of the error first. `command not found` /
`is not recognized` almost always means the program isn't on your PATH, so close and
reopen the terminal, and if that doesn't help, reinstall with the PATH option ticked.

## Session 2: terminal basics and the repo (1.5 h)

Watch the first lecture of [The Missing Semester](https://missing.csail.mit.edu/)
(the shell), typing along. Practise `pwd`, `ls`, `cd`, `mkdir` and `cd ..` until they feel normal.

Then get the portfolio and the tracker running:

```bash
gh repo clone Bhargavpadimiti/bhargav_project_portfolio
cd bhargav_project_portfolio
python scripts/portfolio.py setup
python scripts/portfolio.py test projects/ai-engineer-journey
```

The last command creates the project's virtual environment and runs the tracker's
tests; they should all pass. Now activate the environment. You'll do this every time
you open a new terminal (VS Code can do it automatically once you select the
`.venv` interpreter):

```bash
cd projects/ai-engineer-journey
source .venv/bin/activate          # Windows Git Bash: source .venv/Scripts/activate
journey status
```

## Session 3: the diagnostic (1 h)

```bash
journey quiz diagnostic
```

30 questions. **Choose "I don't know yet" rather than guessing.** A low score is fine
and expected; this is a baseline, and you'll retake it at weeks 13 and 26 to see the
change. Then fill in the **Dec** column of
[assessments/skills-matrix.md](../assessments/skills-matrix.md).

## Session 4: the big picture (1.5 h)

Watch [Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)
(Andrej Karpathy, 1 h). Pause and write down, in your own words:

1. What is an LLM, physically? (Hint: two files.)
2. How is it trained, in stages?
3. Name 3 ways LLMs can fail or be attacked.

Then skim [research/job-market-2026.md](../research/job-market-2026.md): this is why
the curriculum looks the way it does.

## Session 5: your first exercises (1.5 h)

Open `exercises/week-01/week01.py` and `exercises/week-01/test_week01.py` side by side.

```bash
journey check week-01
```

Everything fails at first; that's how exercises start. Implement one function at a
time and re-run. Notice the tests whose names end in `_edge_case`: an empty name, zero,
negative numbers. **Handling those is the job.** Don't edit the tests.

## Session 6: the learning loop (2 h)

1. Install [Anki](https://apps.ankiweb.net). Make 10 cards from this week (for example "What does `cd ..` do?", "Why keep API keys in .env?").
2. `journey quiz week-01`
3. Copy [the journal template](../journal/TEMPLATE.md) to `journal/week-01.md` and fill it in.
4. Log your hours for each session, for example `journey log 1.5 "installed tools" -t build`.
5. `journey report`
6. Your first pull request, which is the workflow you'll use for everything:

```bash
git switch -c learn/week-01
git add -A
git commit                      # the template opens: write "docs(journey): complete week 1"
git push
gh pr create --fill
```

When the checks on the pull request turn green, merge it:

```bash
gh pr merge --squash --delete-branch
git switch main && git pull
```

## Done when

- [ ] `journey status` works
- [ ] Diagnostic taken, skills matrix "Dec" column filled in
- [ ] `journey check week-01` → all tests pass
- [ ] `journey quiz week-01` ≥ 80%
- [ ] First pull request merged
- [ ] Sunday check-in with your tutor (it reviews your diagnostic and fine-tunes week 2)
