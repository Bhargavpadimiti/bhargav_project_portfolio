# Contributing & workflow

This is a personal portfolio, but it follows the same workflow a professional team
would: every change is on a branch, checked automatically, and merged through a
pull request. That keeps `main` always working and makes the history easy to read.

## Prerequisites

| Tool | Why | Install |
| ---- | --- | ------- |
| Git | version control | <https://git-scm.com/downloads> (on Windows this includes **Git Bash**) |
| Python 3.11+ | helper script, Python projects, pre-commit | <https://www.python.org/downloads/> |
| Node.js 22+ | Node projects only | <https://nodejs.org> |
| GitHub CLI (`gh`) | create and merge PRs from the terminal | <https://cli.github.com>, then `gh auth login` |

## One-time setup

```bash
make setup        # or: python scripts/portfolio.py setup
```

This installs the git hooks and sets a few **repository-local** git options
(your global git config is not touched):

| Setting | Effect |
| ------- | ------ |
| `commit.template` | `git commit` opens a pre-filled guide to writing a good message |
| `pull.rebase` | `git pull` keeps history linear (no "Merge branch…" noise) |
| `rebase.autoStash` | pulling works even with uncommitted changes |
| `fetch.prune` | branches deleted on GitHub disappear locally too |
| `push.autoSetupRemote` | a plain `git push` works on a brand-new branch |

## Everyday workflow

```bash
git switch main && git pull                 # 1. start from the latest main
git switch -c feat/weather-alerts           # 2. create a branch
# ... edit, then run the tests ...
python scripts/portfolio.py test projects/weather-cli
git add -A && git commit                    # 3. commit (hooks run automatically)
git push                                    # 4. push the branch
gh pr create --fill                         # 5. open a pull request
gh pr merge --squash --delete-branch        # 6. merge once CI is green
git switch main && git pull                 # 7. back to main, ready for the next change
```

Branch names: `feat/…`, `fix/…`, `docs/…`, `refactor/…`, `chore/…`.

## Adding a new project

```bash
make new NAME=weather-cli TYPE=python DESC="Command-line weather forecast"
# TYPE is one of: python (default), node, generic
```

This will:

1. create and switch to a `feat/weather-cli` branch,
2. copy the template into `projects/weather-cli/` with your names filled in,
3. add a row to the project table in the root `README.md`.

CI picks the project up automatically: a `pyproject.toml` means Python
(`pytest`), a `package.json` means Node (`npm test`), and a `test.sh` means
anything else.

### What makes a project portfolio-ready

- [ ] The README explains **what** it does, **why** it matters, and **how** to run it, within the first screen
- [ ] A screenshot, GIF or live demo link
- [ ] Tests that pass in CI
- [ ] A "What I learned" section with real trade-offs and decisions
- [ ] No secrets, API keys or large datasets committed (use `.env.example` and download scripts)
- [ ] Status in the root README updated to ✅ when done

## Commit messages

Commits follow [Conventional Commits](https://www.conventionalcommits.org), and
a hook rejects messages that don't match:

```text
feat(weather-cli): add 7-day forecast command
fix(portfolio-site): correct broken contact link
docs: add architecture diagram to README
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`.

## Milestones and releases

Tag a project when it reaches a meaningful version, so recruiters (and you) can
see its progress:

```bash
git tag -a weather-cli/v1.0.0 -m "weather-cli 1.0: first complete release"
git push --tags
gh release create weather-cli/v1.0.0 --generate-notes
```

## Recommended GitHub settings

These are one-time clicks in **Settings** on GitHub that enforce the workflow above:

- **General → Pull Requests:** allow only *Squash merging*, tick *Always suggest updating
  pull request branches* and *Automatically delete head branches*.
- **Rules → Rulesets → New branch ruleset** for `main`: *Require a pull request before
  merging*, *Require status checks to pass* (add **CI passed**), *Block force pushes*.
- **Advanced Security:** enable *Dependabot alerts*, *Secret scanning* with *Push
  protection*, and *CodeQL analysis* (Default setup).
- **About** (the gear on the repo home page): add a description, topics such as
  `portfolio`, `python` and `javascript`, and your website or LinkedIn.
