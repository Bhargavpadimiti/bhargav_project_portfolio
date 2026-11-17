<div align="center">

# Bhargav Padimiti · Project Portfolio

**Software projects I've designed and built, each one self-contained, tested and documented.**

[![CI](https://github.com/Bhargavpadimiti/bhargav_project_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/Bhargavpadimiti/bhargav_project_portfolio/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com)
[![Conventional Commits](https://img.shields.io/badge/commits-conventional-fe5196.svg)](https://www.conventionalcommits.org)

</div>

## About

Hi, I'm Bhargav. This repository is my hands-on portfolio: every folder under
[`projects/`](projects) is a complete project with its own README, tests and
setup instructions, and every change goes through automated checks.

<!-- Make this yours: 2–3 sentences on what you focus on (e.g. backend, data, web),
what you're learning, and the kind of role you're looking for. -->

## Projects

<!-- projects:start -->
| Project | Description | Tech | Status |
| ------- | ----------- | ---- | ------ |
| _Your first project will appear here_ | Create one with `make new NAME=my-project` | — | — |
<!-- projects:end -->

<sub>Status: ✅ Complete · 🚧 In progress · 🧪 Experimental</sub>

## Repository layout

```text
.
├── projects/              # one folder per project, each fully self-contained
├── templates/             # starter kits for new projects: python, node, generic
├── scripts/portfolio.py   # helper CLI: setup, new, test, list
├── docs/                  # git cheat sheet and guides
├── .github/               # CI workflow, issue & PR templates, Dependabot
└── Makefile               # shortcuts: make setup / new / test / lint
```

## Quick start

```bash
git clone https://github.com/Bhargavpadimiti/bhargav_project_portfolio.git
cd bhargav_project_portfolio
make setup                       # one time: git hooks + git settings

make new NAME=weather-cli TYPE=python DESC="Command-line weather forecast"
make test P=projects/weather-cli
```

No `make` (e.g. on Windows)? Every command works directly:
`python scripts/portfolio.py setup | new | test | list`.

## Built-in tooling

| When | What runs |
| ---- | --------- |
| Every commit | [pre-commit](.pre-commit-config.yaml) hooks: formatting, linting (Ruff, markdownlint, actionlint), secret scanning (gitleaks), commit message check, and a guard against committing straight to `main` |
| Every pull request | [GitHub Actions](.github/workflows/ci.yml): lint, then tests for **only the projects that changed**, plus a smoke test of the project templates |
| Every month | [Dependabot](.github/dependabot.yml): grouped PRs that keep dependencies and actions up to date |
| New project | `make new` scaffolds code, tests and a README from a template, adds the project to the table above and creates a `feat/<name>` branch |

The full workflow is in [CONTRIBUTING.md](CONTRIBUTING.md), and the commands I use
day to day are in the [git cheat sheet](docs/git-cheatsheet.md).

## Contact

- GitHub: [@Bhargavpadimiti](https://github.com/Bhargavpadimiti)
<!-- - LinkedIn: [your-name](https://www.linkedin.com/in/your-name) -->
<!-- - Portfolio site: https://... -->

## License

[MIT](LICENSE). Feel free to learn from or reuse anything here.
