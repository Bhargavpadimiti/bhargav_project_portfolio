# Resources and budget

Everything core is **free**. The whole programme can run on about **$5–20 in total**.

## What to buy (and what not to)

| Item | When | Cost | Verdict |
| ---- | ---- | ---- | ------- |
| The laptop you already have (8 GB RAM works; 16 GB is nicer for local models) | Now | 0 | ✅ Enough. Heavy training runs on free cloud GPUs. |
| Python, VS Code, Git, GitHub, GitHub CLI, Anki (desktop/Android), Ollama | Week 1 | Free | ✅ Required |
| Google Colab and Kaggle notebooks (free GPU time) | Week 18+ | Free | ✅ Required |
| **LLM API credit**: one top-up of about **$5** | Week 5 | ~$5 | ✅ Recommended (details below) |
| Hosting: Hugging Face Spaces, Render, Streamlit Community Cloud free tiers | Week 13+ | Free | ✅ Required |
| AWS or Azure free tier, with a **$5 budget alert set first** | Week 30 | 0–5 | ✅ Required |
| Colab Pro | Weeks 27–28, **only** if free GPU quota runs out | About $10/month, price varies by country | ⚪ Optional, 1 month at most |
| One book: _AI Engineering_ by Chip Huyen (O'Reilly, 2025) | Phase 3 | One technical book | ⚪ Optional (try a library or an employer's O'Reilly access) |
| Paid courses or bootcamps | — | — | ❌ Not needed; the free material below is as good |
| Certifications | — | — | ❌ About 1% of postings mention them ([research](../research/job-market-2026.md)); projects count far more |
| Domain name, GPU, new hardware | — | — | ❌ Not needed |

### LLM API budget

- **Free:** run open models locally with [Ollama](https://ollama.com) for practice and tests.
- **Cheap and good for exercises:** Claude Haiku 5.5 (`claude-haiku-5-5`) costs **$0.10 per million input tokens and $0.50 per million output tokens**. A heavy month of learning (around 5M tokens in, 1M out) costs about **$1**.
- **For final demos and LLM-as-judge evals:** Claude Opus 5.5 (`claude-opus-5-5`), the most capable Opus model, costs $4 / $20 per million tokens. Use it sparingly, where quality matters.
- Assume there are no free credits. Set a **monthly spend limit** in the provider console before your first call, and log the cost of every call (week 2's `estimate_cost` exercise is the start of that habit).
- Postings also mention OpenAI, Gemini, Azure OpenAI and AWS Bedrock, so the projects keep the provider behind an interface you can swap. That design shows up in the week 9 chatbot.

## Core free resources by phase

### Phase 0–1: programming foundations

- [CS50's Introduction to Programming with Python (CS50P)](https://cs50.harvard.edu/python/): the main Python course; lectures map to weeks 2–8
- [The Python Tutorial](https://docs.python.org/3/tutorial/): the official reference
- [Python Tutor](https://pythontutor.com): visualise code step by step
- [The Missing Semester](https://missing.csail.mit.edu/): terminal, Git, editors
- [NumPy for absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) · [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html)
- [Kaggle Learn](https://www.kaggle.com/learn): short, free, hands-on Python, pandas and intro-ML courses
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)

### Phase 2: math and ML from scratch, RAG

- [3Blue1Brown](https://www.3blue1brown.com/): _Essence of Linear Algebra_, _Essence of Calculus_, _Neural Networks_
- [Mathematics for Machine Learning](https://mml-book.github.io/): free book, use as a reference
- [StatQuest](https://www.youtube.com/@statquest): statistics and ML explained clearly
- [Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction), Andrew Ng: audit for free
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [Sentence Transformers](https://www.sbert.net) · [Chroma](https://docs.trychroma.com) · [pgvector](https://github.com/pgvector/pgvector)
- [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html), Andrej Karpathy: micrograd first, the rest in Phase 3

### Phase 3: deep learning, transformers, agents

- [PyTorch tutorials](https://pytorch.org/tutorials/beginner/basics/intro.html)
- [Dive into Deep Learning](https://d2l.ai/): free interactive book
- [Practical Deep Learning for Coders](https://course.fast.ai/): fast.ai, top-down complement
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [minbpe](https://github.com/karpathy/minbpe) · [nanoGPT](https://github.com/karpathy/nanoGPT)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course) · [Hugging Face Agents course](https://huggingface.co/learn/agents-course)
- [Claude API docs](https://platform.claude.com/docs) · [Anthropic courses](https://github.com/anthropics/courses)
- [Model Context Protocol](https://modelcontextprotocol.io) · [LangGraph](https://github.com/langchain-ai/langgraph)
- [OWASP GenAI Security Project](https://genai.owasp.org/) · [Langfuse docs](https://langfuse.com/docs) · [MLflow](https://mlflow.org/docs/latest/)

### Phase 4–5: fine-tuning, serving, system design

- [PEFT](https://huggingface.co/docs/peft) · [TRL](https://huggingface.co/docs/trl) · [vLLM](https://docs.vllm.ai)
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Docker get started](https://docs.docker.com/get-started/)
- [NeetCode roadmap](https://neetcode.io/roadmap): coding-interview practice

## Study tools

- **Anki** for spaced repetition: add 5–10 cards after every session (definitions, "why does X fail?", shapes, commands)
- **An AI tutor** (see [CLAUDE.md](../CLAUDE.md)): explains, quizzes and reviews code, but **never writes your exercise solutions**
