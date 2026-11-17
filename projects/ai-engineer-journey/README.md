# AI Engineer Journey

> From my first line of code to building production AI systems in 39 weeks:
> the curriculum, tested exercises, quizzes and progress tracker, all in the open.

**Started:** 1 December 2026 · **Pace:** ~10 h/week · **Ends:** 29 August 2027

## Progress

<!-- progress:start -->
Status: **Starts Tue 1 Dec 2026 (14 days to go)**

`░░░░░░░░░░░░░░░░░░░░ 0%` of the programme · **0 h** studied · **0** quiz attempts · **0** exercise sets fully passing

Full dashboard: [PROGRESS.md](PROGRESS.md) (updated 17 Nov 2026)
<!-- progress:end -->

## Why this exists

I have 3+ years of experience in tech and I'm becoming an **AI engineer**: someone who
designs, builds, evaluates and runs AI systems in production. Rather than collecting
certificates, I'm building **from scratch first** (autograd, attention, a tokeniser, an
agent loop), then shipping real projects with the tools employers use, and measuring
every step.

The curriculum is driven by [what AI engineer job postings actually ask for](research/job-market-2026.md)
in India, the UK/Europe and remote roles: Python, LLMs, RAG, **evaluation**, **agents**,
cloud and system design.

## Roadmap

| Phase | Weeks | Focus | Project |
| ----- | ----- | ----- | ------- |
| 0 · Launch | 1 | Setup, diagnostic, learning system | this repo |
| 1 · Programming foundations | 2–9 | Python, testing, HTTP, FastAPI, NumPy/pandas | LLM Chatbot |
| 2 · Math & ML from scratch + RAG | 10–17 | Linear algebra, calculus, probability, regression, backprop; RAG with evals | RAG Assistant, ML from Scratch |
| 3 · Transformers + agents | 18–26 | PyTorch, BPE, attention, mini-GPT; tool use, MCP, LangGraph, guardrails, observability | Mini-GPT, AI Agent |
| 4 · Fine-tuning & system design | 27–33 | LoRA/QLoRA, serving, scaling, reliability, cloud, LLM system design | Fine-tuning Lab |
| 5 · Capstone & career | 34–39 | End-to-end product, interviews, open source | Capstone |

The week-by-week plan is in [curriculum/](curriculum/README.md), with tracks for
[system design](curriculum/system-design.md), [edge cases](curriculum/edge-cases.md) and
[career](curriculum/career.md).

## How learning is measured

- **Weekly quizzes** with explanations, choices shuffled, and an honest "I don't know yet" option (target ≥ 80%)
- **Coding exercises** graded by pytest, with dedicated **edge-case tests** (target 100%)
- **Hours** against pace, by track (depth / build / review / career)
- **Projects** reviewed against a rubric: tests, CI, demo, evals, failure modes, what I learned
- **Skills matrix** rated against job-market demand at each checkpoint ([assessments/](assessments/skills-matrix.md))

## The `journey` tracker

A small, tested Python CLI that runs the programme:

```bash
journey status                     # current week, what's due, hours against pace
journey week 12                    # any week's full plan: topics, edge cases, resources
journey log 1.5 "attention maths" -t depth
journey quiz week-02               # interactive quiz, scores saved
journey check week-02              # run the week's exercises with pytest
journey report                     # regenerate PROGRESS.md and the tables in these READMEs
```

Set up once from the repository root:

```bash
python scripts/portfolio.py test projects/ai-engineer-journey   # creates .venv and runs the tests
cd projects/ai-engineer-journey
source .venv/bin/activate                                        # Windows: source .venv/Scripts/activate
journey status
```

## Layout

```text
ai-engineer-journey/
├── curriculum/      # plan.yaml (source of truth), roadmap, system design, edge cases, resources, career
├── research/        # job-market analysis behind the curriculum
├── weeks/           # day-by-day guide for each week
├── assessments/     # quizzes (YAML) and the skills matrix
├── exercises/       # weekly coding exercises + tests
├── journal/         # weekly reflections
├── progress/        # log.csv and results.yaml, written by the tracker
├── src/journey/     # the tracker
├── tests/           # tests for the tracker, the plan and every quiz
└── CLAUDE.md        # protocol for my AI tutor (hints, never solutions)
```

## AI-assisted, human-done

An AI tutor (Claude) prepares each week's materials, quizzes me, and reviews my pull
requests, following [CLAUDE.md](CLAUDE.md). It gives hints, never exercise solutions: the
exercise code, projects and journal are my own work.
