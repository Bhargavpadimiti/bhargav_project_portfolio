# Curriculum

**From first line of code to production AI engineer: 39 weeks, ~10 hours a week,
1 December 2026 → 29 August 2027.**

The machine-readable plan is [plan.yaml](plan.yaml). `journey week N` prints any
week in full, and `journey report` regenerates the table below from it.

## Design principles

1. **Two tracks every week** (from Phase 2): _Depth_ builds understanding from scratch (math, algorithms, models by hand); _Build_ ships the AI-engineering skills that job postings ask for. Each track makes the other easier: cosine similarity in Depth is the same week as semantic search in Build.
2. **From scratch first, framework second.** Build it by hand (autograd, attention, BPE, an agent loop, a vector index), then use the library knowing what it does underneath.
3. **Edge cases are part of the spec.** Every exercise tests them, and every project documents its failure modes ([edge-cases.md](edge-cases.md)).
4. **Ship in public.** Every phase ends with a portfolio project with tests, CI, a README and a demo.
5. **Measure everything.** Quizzes, exercise pass rates, hours, project rubrics and a skills matrix compared against real job postings.
6. **Spaced retrieval beats re-reading.** Each quiz repeats earlier material; add Anki cards daily.

## Phases

| Phase | Weeks | Dates | Goal | Portfolio project |
| ----- | ----- | ----- | ---- | ----------------- |
| 0 · Launch | 1 | 1–6 Dec | Tools, diagnostic, learning routine | ai-engineer-journey (this) |
| 1 · Programming foundations | 2–9 | 7 Dec – 31 Jan | Real Python: testing, files, HTTP, classes, NumPy/pandas, FastAPI | **llm-chatbot** |
| 2 · Math & ML from scratch + RAG | 10–17 | 1 Feb – 28 Mar | Linear algebra, calculus and probability through code; regression and backprop by hand; RAG with evals | **rag-assistant**, **ml-from-scratch** |
| 3 · Deep learning, transformers + agents | 18–26 | 29 Mar – 30 May | PyTorch, BPE, attention, mini-GPT; tool use, MCP, LangGraph, guardrails, observability | **mini-gpt**, **ai-agent** |
| 4 · Fine-tuning, serving & system design | 27–33 | 31 May – 18 Jul | LoRA/QLoRA, vLLM, scaling, reliability, cloud, ML/LLM system design | **fine-tuning-lab**, design docs |
| 5 · Capstone & career launch | 34–39 | 19 Jul – 29 Aug | End-to-end product in your domain, interview prep, open source | **capstone** |

### Checkpoints

| Week | Checkpoint | You should have |
| ---- | ---------- | --------------- |
| 13 (end Feb) | 🏁 3 months | Chatbot plus deployed RAG v1 with evals; résumé v1 out; applying to bridge roles |
| 26 (end May) | 🏁 **6 months, your original target** | 5 public projects, a transformer built from scratch, a production agent; applying to junior/associate AI engineer roles |
| 39 (end Aug) | 🏁 9 months | Fine-tuned and served model, system-design depth, capstone in production |

### 6 months or 9?

Starting from zero coding experience at 8–12 h/week, the full "from scratch, in depth"
scope needs about 390 hours, which is 9 months. **The 6-month checkpoint is a real
milestone:** by week 26 you're job-ready for junior/associate AI engineering roles. Months
7–9 add the depth (fine-tuning, serving, system design, a capstone) that gets you hired as
an AI engineer rather than a junior one. If you find extra hours (holidays,
weekends), `journey status` shows you running ahead, and your tutor can compress later weeks.

## A typical week (~10 h)

| Day | Time | What |
| --- | ---- | ---- |
| Mon | 1.5 h | Depth: lecture or reading, coding along |
| Tue | 1.5 h | Depth: exercises |
| Thu | 1.5 h | Build: project work |
| Sat | 3 h | Build: project work, then the exercises' edge cases |
| Sun | 2.5 h | Quiz, journal, `journey report`, pull request, weekly check-in with the tutor |

Plus 10–15 minutes of Anki on most days. Job hunting (2–3 h/week) comes on top: see [career.md](career.md).

## How progress is measured

| Measure | Target | Tool |
| ------- | ------ | ---- |
| Weekly quiz | ≥ 80% (retake after reviewing if lower) | `journey quiz week-NN` |
| Exercises | 100% of tests, edge cases included | `journey check week-NN` |
| Hours | ~10/week; status warns when more than 2 h behind | `journey log`, `journey status` |
| Phase exams and checkpoints | ≥ 75% (final ≥ 80%) | `journey quiz exam-phase-N` |
| Projects | Rubric: README, tests, CI, demo, evals, failure modes | Tutor review of each pull request |
| Skills | Self-rating against job-market demand | [skills-matrix.md](../assessments/skills-matrix.md) |

## Week by week

<!-- plan:start -->
| Wk | Dates | Theme | Depth (understand) | Build (ship) |
| -- | ----- | ----- | ------ | ----- |
| 1 | 1–6 Dec 2026 | **Launch - setup, diagnostic, learning how to learn** | How programs run, and the map of AI | Set up the toolkit and the tracker |
| 2 | 7–13 Dec 2026 | **Python basics - values, types, decisions** | How Python represents data and makes decisions | A prompt-builder script |
| 3 | 14–20 Dec 2026 | **Collections and loops** | Lists, dicts, sets and iteration | A chat-history manager |
| 4 | 21–27 Dec 2026 | **Functions, errors and testing (holiday week)** | Functions, exceptions and tests | Refactor and test weeks 2-3 |
| 5 | 28 Dec – 3 Jan 2027 | **Files, JSON, HTTP and your first LLM call (catch-up week)** | Data on disk and on the network | Your first LLM API call |
| 6 | 4–10 Jan 2027 | **Classes, types and clean code** | Objects and readable code | A ChatSession class |
| 7 | 11–17 Jan 2027 | **NumPy, pandas and plotting** | Arrays and tables, the language of ML | Analyse your own study log |
| 8 | 18–24 Jan 2027 | **Production Python - CLIs, logging, async, web APIs** | How real services are built | Start Project 1 - LLM Chatbot |
| 9 | 25–31 Jan 2027 | **Ship Project 1 - LLM Chatbot + Phase 1 exam** | Consolidate Phase 1 | Finish and publish the chatbot |
| 10 | 1–7 Feb 2027 | **Vectors and embeddings** | Linear algebra through code | Semantic search from scratch (Project 2 begins) |
| 11 | 8–14 Feb 2027 | **Derivatives, gradients and optimisation** | Calculus for ML, through code | Document ingestion and chunking |
| 12 | 15–21 Feb 2027 | **Probability, softmax and how LLMs pick words** | Probability for ML | RAG v1 end to end |
| 13 | 22–28 Feb 2027 | **Ship RAG Assistant v1 + 3-month review** 🏁 3-month checkpoint | Consolidate weeks 10-12 | Deploy RAG v1 |
| 14 | 1–7 Mar 2027 | **Linear regression from scratch** | Your first model, by hand (Project 3 begins) | Structured outputs |
| 15 | 8–14 Mar 2027 | **Classification and evaluation** | Logistic regression and metrics | Evaluating LLM apps |
| 16 | 15–21 Mar 2027 | **The classical ML toolkit** | scikit-learn and when not to use an LLM | Better retrieval |
| 17 | 22–28 Mar 2027 | **Neural networks and backprop from scratch + Phase 2 exam** | Build an autograd engine | Ship Project 3 - ML from Scratch |
| 18 | 29 Mar – 4 Apr 2027 | **PyTorch fundamentals and tool calling** | PyTorch | Tool calling (Project 5 begins) |
| 19 | 5–11 Apr 2027 | **Training networks well and the agent loop** | Making training work | An agent loop from scratch (no framework) |
| 20 | 12–18 Apr 2027 | **Tokenisation and the Model Context Protocol** | How text becomes numbers (Project 6 begins) | MCP servers |
| 21 | 19–25 Apr 2027 | **Attention and the transformer** | Self-attention from scratch | Agent frameworks |
| 22 | 26 Apr – 2 May 2027 | **Build a mini-GPT, and guardrails** | Train your own small GPT | Security and guardrails |
| 23 | 3–9 May 2027 | **How LLMs are trained and served** | The LLM life cycle | Ship Project 6 - Mini-GPT |
| 24 | 10–16 May 2027 | **Observability and LLMOps** | Statistics for experiments | Tracing and monitoring LLM apps |
| 25 | 17–23 May 2027 | **Ship Project 5 - AI Agent** | Review transformers and agents | A production-grade agent |
| 26 | 24–30 May 2027 | **6-month review and job push** 🏁 6-month checkpoint | Checkpoint exam and mock interviews | Portfolio audit |
| 27 | 31 May – 6 Jun 2027 | **Fine-tuning with LoRA and QLoRA** | Customising models (Project 7 begins) | Fine-tune a small open model |
| 28 | 7–13 Jun 2027 | **Serving models** | Inference engineering | Ship Project 7 - Fine-tuning Lab |
| 29 | 14–20 Jun 2027 | **System design I - scaling and data** | Fundamentals | Upgrade rag-assistant's architecture |
| 30 | 21–27 Jun 2027 | **System design II - reliability, security and cloud** | Keeping systems up and safe | CI/CD to the cloud |
| 31 | 28 Jun – 4 Jul 2027 | **ML and LLM system design** | Designing AI systems | Two written designs |
| 32 | 5–11 Jul 2027 | **Multimodal elective** | Beyond text (pick one) | Add the elective to your agent or RAG |
| 33 | 12–18 Jul 2027 | **Capstone design** | Design before code | Capstone skeleton |
| 34 | 19–25 Jul 2027 | **Capstone sprint 1 - core features** | — | Build the core workflow end to end |
| 35 | 26 Jul – 1 Aug 2027 | **Capstone sprint 2 - quality** | — | Evals, guardrails, observability |
| 36 | 2–8 Aug 2027 | **Capstone sprint 3 - production** | — | Deploy, load test, write it up |
| 37 | 9–15 Aug 2027 | **Interview preparation** | Interview loops for AI engineers | — |
| 38 | 16–22 Aug 2027 | **Open source and portfolio polish** | — | Show you can work in other people's code |
| 39 | 23–29 Aug 2027 | **Final review and next steps** 🏁 Final checkpoint | Final exam and retrospective | — |
<!-- plan:end -->

## Also in this folder

- [system-design.md](system-design.md): the architecture track, design-doc template and practice prompts
- [edge-cases.md](edge-cases.md): the failure-mode checklist used by every exercise and project
- [resources.md](resources.md): free resources by phase, plus what (not) to buy
- [career.md](career.md): bridge roles, the 3-month job plan, résumé and interviews
