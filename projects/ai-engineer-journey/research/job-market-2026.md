# AI engineer job market: what employers ask for

_Researched 17 November 2026 for the markets I'm targeting: **India, UK/Europe and remote**.
Refreshed at each checkpoint (weeks 13, 26 and 39)._

> **How to read these numbers.** They come from different job boards, sample sizes
> and dates, so they are **directional, not precise**, and percentages from different
> studies shouldn't be compared directly. Several are secondary write-ups whose full
> reports I couldn't open. The pattern across sources is what matters, and it is
> consistent.

## 1. The role is growing fast

- **AI engineer is the #1 fastest-growing job** in LinkedIn's _Jobs on the Rise 2026_ (US), and the fastest-growing role in Hyderabad. The top listed skills for it are **LangChain, RAG and PyTorch**. ([Dice](https://www.dice.com/career-advice/ai-related-jobs-top-linkedins-fastest-growing-roles-list-for-2026), [Deccan Chronicle](https://www.deccanchronicle.com/jobs-and-education/ai-engineer-is-fastest-growing-job-role-in-hyderabad-linkedin-2026-report-1931848))
- **India:** AI engineering postings rose **~59.5% year on year** (LinkedIn, April 2026), the fastest of the major markets. Bengaluru leads, Hyderabad is growing fast (+51%), and Tier-II cities are emerging. ([Telangana Today](https://telanganatoday.com/ai-engineering-jobs-in-india-surge-59-5-pc-outpacing-us-and-europe-linkedin-report), [YourStory](https://yourstory.com/ai-story/hiring-ai-professionals-india-rises-59-percent-linkedin-report)) Demand for agentic-AI talent is reported up **260%** (CIEL HR). ([Outlook Business](https://www.outlookbusiness.com/news/demand-for-agentic-ai-talent-rises-260-as-enterprises-embrace-ai-report))
- **Europe:** Germany leads in AI-related job titles (288 in Q1 2026, 4.2% of titles), ahead of the UK (160), France (138) and the Netherlands (84) (Indeed Hiring Lab). Across the EU, the share of postings that need _in-depth_ AI knowledge rose from 0.7% (2022) to 1.7% (2025) (PwC). ([Hiring Lab](https://www.hiringlab.org/?p=20706), [PwC AI Jobs Barometer, Germany](https://www.pwc.com/gx/en/issues/artificial-intelligence/job-barometer/aijb-2026-germany.pdf))

## 2. Skills that appear in AI engineer postings

| Skill | Share of postings | Source and sample |
| ----- | ----------------- | ----------------- |
| Python | 61.5%–71% | Axial Search, 43,480 US postings; 3,449-posting analysis, May 2026 |
| LLMs / generative AI | 55.5%–66% | 4,155 postings, June 2026; 3,449-posting analysis |
| **AI evaluation (evals)** | **56%** | 390 AI engineer postings, 2026 (InterviewStack) |
| Cloud platform (any) | 54.7% | Axial Search |
| **AI agents** | **50%** | 390 AI engineer postings, 2026 |
| RAG | 26%–40% | 390 postings (26% _required_); 3,449-posting analysis (40%) |
| AWS · Azure · GCP | 37% · 33% · 25% | 3,449-posting analysis (Axial: AWS 39.0%, Azure 38.7%) |
| LangChain / LangGraph | ~25% | 3,449-posting analysis |
| Kubernetes · Docker | 12.8% · 11.1% | AI Pulse, 3,897 postings |
| Certifications | ~1% or less | Axial Search |

Sources: [Axial Search](https://axialsearch.com/insights/ai-engineering-jobs), [3,449-posting analysis](https://dev.to/gnana_6392e836fd500a957dc/ai-engineer-skills-companies-want-in-2026-3449-posting-analysis-5f9l), [InterviewStack](https://interviewstack.io/blog/how-ai-is-changing-ai-engineer-2026), [AI Pulse](https://theaimarketpulse-com.pages.dev/insights/), [365 Data Science](https://365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/), [Interview Query](https://www.interviewquery.com/p/ai-engineers-demand).

Individual postings from 2026 repeat the same themes, especially **evals and observability** (LangSmith, Langfuse, RAGAS, DeepEval, LLM-as-judge), **MCP/tool integration**, **RAG with vector stores**, and production skills (CI/CD, monitoring, REST APIs, AWS/GCP/Azure).

## 3. How demand has shifted (2023 → 2026)

| Then | Now | Evidence |
| ---- | --- | -------- |
| "Prompt engineer" as a job title | Prompting is a skill inside other roles | In Hacker News hiring posts, prompt engineering peaked near 0.9% (Apr 2026) and fell to 0.4% by Sep 2026, overtaken by **evals** and **MCP** ([analysis of 32,924 HN posts](https://levelup.gitconnected.com/the-10-ai-skills-employers-actually-asked-for-in-32-924-hacker-news-job-posts-and-prompt-239a8272445d)) |
| Agents were rare | Agents are mainstream | Agent mentions grew from ~0.4% of HN posts (2023) to ~14% (2026); Dice reports agentic-AI demand up 587% YoY |
| "Knows how to use ChatGPT" | Can **build** with AI | Workday: demand for _basic_ AI skills fell ~25% after a January peak while AI-building skills rose ([BERI](https://www.beri.net/article/workday-global-workforce-report-2026-basic-ai-skills-demand-down-25-ai-building-up-51-training-budget)) |
| Demos | Production | Evals, cost optimisation and observability have become core skills in postings |

**Lesson for this plan:** skills that compound (Python, ML fundamentals, evals, system design, production engineering) beat skills that decay (tool-specific prompt tricks). Frameworks such as LangChain matter, but they're taught **after** building the same thing from scratch.

## 4. Market by market

### India

- Typical GenAI/AI engineer postings ask for **Python, LangChain/LangGraph, RAG, FAISS/Chroma, FastAPI, Docker** and one cloud, often **Azure OpenAI** or **AWS Bedrock**. ([GlobalLogic posting](https://www.globallogic.com/careers/engineer-gen-ai-irc279034/), [Hirist posting](https://www.hirist.tech/j/ai-engineer-llm-generative-ai-1653260), [Taggd role guide](https://taggd.in/blogs/gen-ai-engineer/))
- **Seniority:** mid-level roles (3–5 years) focus on RAG and LLMs; senior roles (6–10 years) add MLOps, agent frameworks and enterprise deployment.
- Press coverage of an Indeed–Nasscom report says **half of employers now weigh demonstrated AI capability above credentials**. Projects beat certificates.

### UK

- "AI Engineer" in the UK often means an **LLM application or product engineer**. ML engineer roles need deeper maths. ([Experis](https://www.experis.co.uk/blog/2026/07/the-ai-engineer-title-is-already-meaningless-here-is-what-actually-matters), [IT Job Board guide](https://www.itjobboard.co.uk/blog/386/ai-engineer-vs-prompt-engineer-vs-ml-engineer:-2026-guide/))
- Ads ask for Python or TypeScript, the OpenAI, Claude, Gemini, Azure OpenAI and Bedrock APIs, RAG with vector databases, evaluation and testing, guardrails, function calling and fine-tuning basics. ([Jobrise London guide](https://jobrise.io/en/blog/ai-engineer-jobs-london-2026-application-guide/))
- Live salary and demand benchmarks: [ITJobsWatch, LLM (England)](https://www.itjobswatch.co.uk/jobs/england/llm.do).

### Europe

- AI governance roles (the EU AI Act) exist, but companies hire **about 7 builders for every governor** ([Axipro study](https://technologymagazine.com/globenewswire/3326317)). Building skills come first. Knowing the AI Act basics is a plus for EU applications (covered in week 22).
- Most AI-skilled jobs now sit outside tech occupations ([Euronews](https://www.euronews.com/2026/07/24/the-majority-of-ai-jobs-now-sit-outside-technological-occupations-in-europe)), so **domain knowledge plus AI** is a real hiring advantage.

### Remote / global

- **Forward deployed engineer** roles (AI engineering that faces customers) ask for evals, observability, tracing and guardrails, and usually 5+ years in an engineering or solutions role. They're a realistic later target for someone with years of tech experience. ([Scale AI](https://jobs.spacecapital.com/companies/scale-ai/jobs/69454082-forward-deployed-engineer-genai), [Arize](https://www.jobera.com/job/arizeai-forward-deployed-engineer-us-86372b0e/))

## 5. Entry reality for a career switcher

- Only **~6% of ML engineer postings are entry-level** ([365 Data Science, 1,000+ LinkedIn postings](https://365datascience.com/career-advice/machine-learning-engineer-job-outlook/)).
- Realistic switch timelines for working professionals are **9–18 months** ([MentorCruise](https://mentorcruise.com/blog/is-an-ai-career-worth-it-in-2026-a-realistic-assessment/)).
- Easier first steps include AI workflow/automation, AI business analysis, AI consulting and evaluation roles ([Simplilearn](https://www.simplilearn.com/best-ai-career-switches-article)). LinkedIn also lists AI consultants and data annotators among the fastest-growing roles.

**So:** "AI Engineer" titles within 3 months of starting to code are unlikely. **Bridge roles** that combine my 3+ years in tech with new AI skills are realistic, and the portfolio makes junior and associate AI engineer roles realistic by month 6. See [curriculum/career.md](../curriculum/career.md).

## 6. How the curriculum maps to demand

| Demand signal | Covered in | Proven by |
| ------------- | ---------- | --------- |
| Python (60–70%) | Phase 1 (weeks 2–9), then every week | llm-chatbot, all projects |
| LLM APIs, structured output, tool calling | Weeks 5, 8–9, 14, 18 | llm-chatbot, ai-agent |
| RAG and vector databases (26–40%) | Weeks 10–13, 16, 29 | rag-assistant |
| **Evaluation (56%)** | Weeks 13, 15, 24 and every project after | Eval scores in every README |
| **Agents (50%)**, LangGraph, MCP | Weeks 18–25 | ai-agent |
| Cloud (55%), AWS/Azure | Week 30 (deploys from week 13) | Automated deploys, capstone |
| Docker / Kubernetes | Weeks 13, 29–30 | Every deployed project |
| Observability, cost, latency | Weeks 24, 30–31 | ai-agent, capstone |
| Security and guardrails | Week 22 | Threat model plus attack tests |
| Fine-tuning and serving | Weeks 27–28 | fine-tuning-lab |
| ML fundamentals, PyTorch, transformers | Weeks 10–23 | ml-from-scratch, mini-gpt |
| System design | Weeks 5, 8, 12, 29–33 | Design docs, capstone |
| Certifications (~1% of postings) | Deliberately skipped; revisit after week 39 if target postings ask | — |
