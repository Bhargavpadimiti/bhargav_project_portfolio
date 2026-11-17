# Template Project

> One-line description of what this project does and who it is for.

<!-- Recruiters skim. Answer in the first 3 lines: what is it, why does it matter, what did you use? -->

## Highlights

- **Problem:** What problem does this solve?
- **Approach:** How did you solve it? Key design decisions.
- **Result:** Measurable outcome, e.g. "processes 10k rows in 2 s" or "92% test accuracy".

## Demo

<!-- Add a screenshot or GIF: ![Demo](docs/demo.gif) -->

```console
$ template-project Ada
Hello, Ada!
```

## Tech stack

Python 3.11+ · pytest · ruff

## Getting started

```bash
# from the repository root
python scripts/portfolio.py test projects/template-project   # creates .venv, installs, runs tests

# or manually
cd projects/template-project
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
template-project Ada
pytest
```

## Project structure

```text
template-project/
├── src/template_project/   # application code
├── tests/                  # pytest tests
└── pyproject.toml          # metadata, dependencies, tool config
```

## What I learned

<!-- 2–4 bullets. Interviewers love this section. -->

## Roadmap

- [ ] Next improvement
