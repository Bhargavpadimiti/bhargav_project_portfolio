# Edge-case checklist

The difference between a demo and a product is what happens when inputs are weird,
services fail or users are adversarial. Use this list:

- **while learning:** every exercise has edge-case tests; read why each exists
- **while building:** each project README has a _Failure modes handled_ section that ticks items from here
- **in interviews:** "what could go wrong?" is asked in nearly every design and project round

## Python and data

- [ ] Empty input: `""`, `[]`, `{}`, `None`, whitespace-only strings
- [ ] Boundaries: 0, negative numbers, exactly-on-the-limit values (≥ vs >), very large values
- [ ] Floats: `0.1 + 0.2 != 0.3`, use `math.isclose`; `round(2.5) == 2`; money as `Decimal`
- [ ] Type surprises: `input()` is always `str`; `bool("False")` is `True`; `int("3.5")` raises
- [ ] Mutability: aliasing (`b = a`), mutable default arguments, modifying a list while looping
- [ ] Text: Unicode, emoji, accents, right-to-left text, different newline styles, BOM, encodings
- [ ] Files: missing, empty, huge, locked, wrong encoding, relative-path confusion
- [ ] Dates and times: time zones, daylight saving, leap years, ISO formats, "today" in tests
- [ ] Data: missing values (NaN), duplicates, outliers, wrong dtypes, shape `(n,)` vs `(n, 1)`

## Numerical computing and ML

- [ ] Overflow and underflow: `exp(1000)`, softmax without subtracting the max, `log(0)`
- [ ] Division by zero: zero vectors in cosine similarity, precision with no positive predictions
- [ ] Data leakage: scaling or feature selection fit before the train/test split; duplicates across splits
- [ ] Class imbalance: accuracy looks great while the model never predicts the rare class
- [ ] Learning rate too high (diverges) or too low (no progress); NaN loss
- [ ] Overfitting: train ≫ validation score; always keep an untouched test set
- [ ] Distribution shift: production data differs from training data; monitor it
- [ ] Reproducibility: random seeds, library versions, non-deterministic GPU ops

## Deep learning and transformers

- [ ] Shape mismatches; CPU vs GPU tensors; forgetting `model.eval()` at inference
- [ ] Vanishing or exploding gradients; dead ReLUs; forgetting to zero gradients
- [ ] Attention: missing causal mask (future leakage); not scaling by √d
- [ ] Tokenisation: unusual Unicode, numbers split oddly, non-English text costs more tokens
- [ ] Context length: inputs longer than the model's window
- [ ] GPU out of memory: batch size, sequence length, gradient accumulation, checkpointing
- [ ] Quantisation: accuracy loss; check it against your evals

## LLM API calls

- [ ] Errors: 400 (bad request), 401 (bad key), 429 (rate limit), 5xx, timeouts, dropped streams
- [ ] Retries: exponential backoff with jitter; respect `retry-after`; cap the attempts
- [ ] Non-determinism: same prompt, different answers; evaluate on sets, not single runs
- [ ] Output format: invalid JSON, missing fields, invented enum values; use schemas and validation
- [ ] Refusals and truncation: check the stop reason before using the output
- [ ] Context overflow: trim or summarise history to a token budget
- [ ] Cost runaway: per-request and per-day limits, logging tokens and cost per call
- [ ] Model changes: pin model names; re-run evals when models change or are deprecated
- [ ] Secrets: keys in `.env` and secret stores, never in code, logs or screenshots

## RAG

- [ ] Nothing relevant retrieved → say "I don't know" instead of guessing
- [ ] Chunking breaks meaning (tables, code, lists split across chunks)
- [ ] Keyword-shaped queries (IDs, codes, acronyms) where pure vector search fails
- [ ] Contradictory or outdated sources; show citations and dates
- [ ] Duplicate documents crowding the top-k results
- [ ] Embedding model mismatch between index time and query time
- [ ] Scanned PDFs without text; very large documents; non-English documents
- [ ] **Access control:** users must only retrieve documents they're allowed to see
- [ ] Indirect prompt injection planted in a document

## Agents and tools

- [ ] Infinite loops; set a step limit and a cost budget
- [ ] Tool errors, timeouts and partial results; return errors to the model, don't crash
- [ ] The model calls a tool that doesn't exist or passes invalid arguments
- [ ] Tool output too large for the context; truncate or summarise it
- [ ] Destructive actions need human approval; use read-only credentials where possible
- [ ] Injection through tool results (web pages, emails, files)
- [ ] State: resuming after a crash, duplicate actions (idempotency)

## Security (OWASP Top 10 for LLM apps)

- [ ] Direct prompt injection and jailbreaks
- [ ] Indirect injection through retrieved content and tools
- [ ] Sensitive data in prompts, logs and training data (PII redaction)
- [ ] Data exfiltration through links, markdown images or tool calls
- [ ] Excessive agency: tools with more permission than the task needs
- [ ] Unbounded consumption: token floods, denial-of-wallet

## Production and systems

- [ ] Timeouts on every network call; circuit breakers for failing dependencies
- [ ] Retry storms (thundering herd); add jitter
- [ ] Caching: stale answers, cache stampede, personalisation vs cache hits
- [ ] Race conditions and duplicate jobs; idempotency keys
- [ ] Rate limits per user and per tenant; quotas shared across teams
- [ ] Cold starts on free or serverless hosting
- [ ] Observability: logs, metrics, traces, with no secrets or PII in them
- [ ] Provider outage: fallback model or degraded mode
- [ ] Cost alerts and budgets set **before** deploying to the cloud
