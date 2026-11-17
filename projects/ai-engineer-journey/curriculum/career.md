# Career plan: land a role while learning

This runs alongside the curriculum. Job-hunting time (**2–3 h/week**) is **on top of**
the 10 study hours, so log it with `journey log 1 "applications" -t career` to keep it visible.

## The honest picture

| When | Realistic targets | Why |
| ---- | ----------------- | --- |
| **Months 1–3** (Dec–Feb) | **Bridge roles** and **AI work in your current company** | 3+ years in tech plus visible AI projects is a real asset, but "AI Engineer" titles expect shipped LLM systems. Only ~6% of ML engineer postings are entry-level ([research](../research/job-market-2026.md#5-entry-reality-for-a-career-switcher)). |
| **Months 4–6** (Mar–May) | **Junior / associate AI engineer, GenAI developer, AI application developer** | By week 26 you have 5 public projects (chatbot, deployed RAG with evals, ML from scratch, mini-GPT, production agent). |
| **Months 7–9** (Jun–Aug) | **AI engineer**, **LLM engineer**; later **forward deployed / solutions AI engineer** | Fine-tuning, system design and a production capstone, plus your domain experience. |

## Bridge roles by background

Your existing experience decides which bridge is shortest. Pick the row closest to your current role:

| If your background is... | Target these titles first | Lead with these projects |
| ------------------------ | ------------------------- | ------------------------ |
| QA / testing | AI QA engineer, **LLM evaluation** specialist, AI test automation | Eval harness (week 15), red-team tests (week 22). Evals appear in 56% of AI engineer postings. |
| Support / operations / service desk | GenAI support engineer, AI operations, AI implementation specialist | RAG assistant over support docs, chatbot |
| Business analysis / project or product management | AI business analyst, AI product owner, AI consultant | Requirements and design docs, RAG, evals |
| Infrastructure / DevOps / cloud | LLMOps / MLOps engineer, AI platform engineer | Docker, CI/CD, observability (weeks 24, 29–30) |
| Data / BI / reporting | AI data analyst, analytics engineer (GenAI), text-to-SQL | pandas work, structured outputs, text-to-SQL elective (week 32) |
| Consulting / client-facing | AI solutions consultant, pre-sales AI engineer | Deployed demos, cost/latency analysis |

**Internal moves are the fastest route.** Ask your current employer about AI pilots, and volunteer to prototype one with what you build in weeks 9–13.

## 3-month plan (December–February)

| Week | Action |
| ---- | ------ |
| 1–4 | Fix the basics: LinkedIn headline (`<Your role> · Building AI systems in public`), "About" section, link to this repo. Pick your bridge row above. Save 20 real postings in your target markets into a private tracker. |
| 5–8 | Résumé v1: experience first, then a **Projects** section; keep it honest about where you are. Post about the journey on LinkedIn every 2 weeks (what you built, one edge case you learned). |
| 9 | Chatbot shipped → start applying to bridge roles (5/week) and raise internal AI opportunities. |
| 13 | RAG v1 live → 10+ applications, a LinkedIn post with a demo GIF, and a re-rated skills matrix. |

Keep the application tracker **private** (a spreadsheet or a private repo), not in this public portfolio.

## Résumé rules

- One page; each project gets **one line of what it does plus one line of evidence** ("RAG over 300 docs, 87% answer accuracy on a 50-question eval set, deployed on Hugging Face Spaces").
- Put numbers on everything: eval scores, latency, cost per request, tests, users.
- Skills section = only things that appear in a project you can show.
- Tailor the top third to each posting's top 5 keywords (using the [job-market list](../research/job-market-2026.md#2-skills-that-appear-in-ai-engineer-postings)).

## What AI engineer interviews look like

| Round | What they test | Where you prepare |
| ----- | -------------- | ----------------- |
| Coding | Python, data structures (easy–medium) | 1 problem/week from week 14; intensive in week 37 |
| LLM / ML concepts | Embeddings, attention, RAG trade-offs, evals, fine-tuning vs RAG | Weekly quizzes, Anki, mock interviews (weeks 26, 37) |
| System design | "Design a document Q&A for 10k employees" | Weeks 29–31 design docs |
| Project deep-dive | Why you chose X, what broke, what you'd change | The "What I learned" and "Failure modes" sections of each README |
| Behavioural | Ownership, conflict, learning fast | STAR stories from your 3+ years (week 37) |

## Visibility (cheap and effective)

- **LinkedIn post every 2 weeks**: one thing built, one thing learned, one image or GIF.
- **Pinned repos** on your GitHub profile, plus the profile README.
- **Meetups**: local GenAI/LLM meetups (Bengaluru, Hyderabad, Pune, London, Berlin and Amsterdam all have active ones) and online communities. Show your projects and ask about teams' stacks.
- **Open source** (week 38): one merged contribution signals you can work in other people's code.

## Salary research

- India: AmbitionBox, Glassdoor, levels.fyi (filter by city and years).
- UK: [ITJobsWatch](https://www.itjobswatch.co.uk/jobs/england/llm.do) (live medians by skill), Glassdoor.
- Europe: Glassdoor and levels.fyi by country; check whether a role needs work authorisation.
