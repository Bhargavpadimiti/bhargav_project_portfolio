# System design track

System design runs through the whole programme instead of being crammed at the
end. Every project gets a short design doc, and Phase 4 goes deep.

| When | Focus | Output |
| ---- | ----- | ------ |
| Weeks 5, 8 | Client–server, HTTP, REST APIs, where state lives | Chatbot API design notes |
| Weeks 10, 12 | Search systems; RAG ingestion vs query pipelines | RAG architecture diagram |
| Weeks 19–24 | Agent architectures, tracing, cost and latency | Agent design doc and threat model |
| Weeks 29–30 | Scaling, caching, databases, queues, reliability, cloud | Design doc 1, deploys from CI |
| Week 31 | ML and LLM system design | Design docs 2 and 3 |
| Weeks 33–36 | Capstone architecture and decision records | Capstone design doc and ADRs |

## Fundamentals checklist

- [ ] Latency vs throughput; p50/p95/p99
- [ ] Vertical vs horizontal scaling; stateless services; load balancers
- [ ] Caching layers (client, CDN, application, database) and invalidation
- [ ] SQL vs NoSQL; indexes; transactions; replication; sharding (concepts)
- [ ] Message queues and background workers; at-least-once delivery; idempotency
- [ ] CAP theorem and consistency models (concepts)
- [ ] Rate limiting, timeouts, retries with backoff, circuit breakers, bulkheads
- [ ] Authentication vs authorisation; secrets management; least privilege
- [ ] Observability: logs, metrics, traces, alerts, SLOs
- [ ] Containers, orchestration (Kubernetes concepts), CI/CD, infrastructure as code
- [ ] Cost: compute, storage, egress, tokens; budgets and alerts

## ML and LLM system design checklist

- [ ] Framing: requirements, users, scale, latency and quality targets, budget
- [ ] Data: sources, labelling, freshness, privacy, leakage
- [ ] Model choice: API vs open-weights, size, prompting vs RAG vs fine-tuning
- [ ] Serving: batch vs real-time, streaming, batching, quantisation, GPU sizing
- [ ] Retrieval: chunking, hybrid search, reranking, metadata, **per-user access control**
- [ ] Agents: tools, step limits, approvals, memory, failure recovery
- [ ] Gateway: routing between models, fallbacks, semantic caching, quotas
- [ ] Evaluation: offline golden sets, online A/B tests, LLM-as-judge with checks, human review
- [ ] Monitoring: quality drift, cost per request, latency, refusals, user feedback
- [ ] Safety: injection defences, PII handling, output filtering, audit logs

## Design doc template

Each project gets a `docs/design.md` with these sections:

1. **Context:** the problem and who has it
2. **Goals and non-goals**
3. **Requirements:** functional, plus numbers for scale, latency, quality and cost
4. **Architecture:** a diagram and the components' responsibilities
5. **Data flow:** request path and ingestion path
6. **Key decisions:** options considered, choice made, trade-off (one ADR each)
7. **Failure modes:** what breaks and what happens then (see [edge-cases.md](edge-cases.md))
8. **Evaluation and monitoring:** how you know it works, and keeps working
9. **Cost estimate:** back-of-the-envelope tokens, requests and dollars per month
10. **Future work**

## Back-of-the-envelope numbers

- 1 token ≈ 4 characters of English ≈ ¾ of a word; non-English text often costs more
- 1 day = 86,400 s, so 1M requests/day ≈ 12 requests/s on average (plan for peaks of 3–10×)
- Monthly LLM cost ≈ requests/month × (input tokens × input price + output tokens × output price) ÷ 1M
- Typical latencies: memory reads take nanoseconds, SSD reads microseconds, same-region network calls about a millisecond, LLM responses hundreds of milliseconds to many seconds (so stream them)

## Practice prompts

Use these in mock interviews with your tutor:

1. A support chatbot for an e-commerce site with 1M monthly users
2. Document Q&A for 10,000 employees where each user sees only their documents
3. An agent that books meetings by reading email and calendars (approvals and safety)
4. A model gateway that routes requests across three providers with fallbacks and budgets
5. Semantic search over 50M product listings with filters
6. Nightly batch summarisation of 1M support tickets
7. Real-time content moderation for a chat app
8. An evaluation platform that runs regression evals on every prompt change
9. A voice assistant with under 1 second of perceived latency
10. A fine-tune-and-serve pipeline for a domain-specific model

## Resources

- [System Design Primer](https://github.com/donnemartin/system-design-primer) (free)
- _Designing Machine Learning Systems_, Chip Huyen (optional purchase)
- _Designing Data-Intensive Applications_, Martin Kleppmann (optional purchase, try a library)
