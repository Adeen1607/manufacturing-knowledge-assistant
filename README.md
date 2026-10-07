# Manufacturing Knowledge Assistant

**Retrieve approved manufacturing information, show evidence, and measure what fails.**

An independent portfolio prototype by Mohammed Adeen Shaik. Python BM25 retrieval searches a versioned fictional document corpus after approval/current-version and simulated role filtering. Offline mode returns cited excerpts. An optional Ollama adapter synthesizes a locally generated answer from those excerpts.


## Run without credentials

Python 3.10+; no packages required:

```bash
python app.py
```

Open http://127.0.0.1:8052. Optional: `python app.py --port 8052 --db demo.db`.

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

Ask “What should I do with nonconforming parts?” and inspect DOC-01 version 2. Compare engineering change access as operator vs engineering. Try a supplier invoice question (unapproved source), an interlock-bypass request (escalation), and an instruction-override request (block). Record feedback and inspect monitoring counts.

## Optional local LLM: actual RAG path

Install Ollama separately, start its local service and pull `llama3.2:3b` using `ollama pull llama3.2:3b`. Set `OLLAMA_MODEL` to choose another installed model. Select **Local LLM / Ollama** in the interface. The adapter calls the fixed localhost chat endpoint with retrieved context and citation instructions. Ollama installation requires its own internet access and sufficient hardware.

The LLM path is implemented and its unavailable-provider behavior is tested; a real model was **not run in the build environment**. Offline tests evaluate retrieval and control behavior, not LLM answer quality. Do not call the extractive mode generative AI. Citation-label validation cannot prove factual grounding.

## Reproducible results

- 15 automated tests pass: approval/version filters, role access, abstention, escalation, injection patterns, feedback accounting and model failure behavior.
- 30 small developer-authored synthetic evaluation cases: **25/30 pass (83.3%)**.
- Expected source at rank 1 for answerable cases: **11/16 (68.8%)**.
- Five answerable paraphrases abstain. All seven expected unsupported/restricted questions abstain, four unsafe requests escalate, and three tested injection phrases block.

These cases are not held out and are not a production or security benchmark. See [full results, including failures](reports/evaluation-results.json) and [evaluation interpretation](docs/evaluation.md).

## Capabilities

- Eight document fixtures including six current approved documents, one archived revision and one unapproved draft.
- BM25 ranking with simple token normalization and a conservative query-coverage threshold.
- Source IDs, versions, owners and review dates surfaced to users.
- Optional local-model synthesis with human-review status and citation-label checks.
- Local SQLite usage counts, response status, latency and categorized feedback; question text is not stored.

## Analyst deliverables

- [Requirements and process flow](docs/requirements.md)
- [Evaluation, failures and pilot criteria](docs/evaluation.md)
- [Risk register and ownership](docs/governance.md)
- [Rollout plan, training and user guide](docs/adoption-and-user-guide.md)
- [Architecture and API contract](docs/architecture.md)
- [Research and role mapping](docs/research-and-role-fit.md)

## Scope boundaries

Role selection is simulated and is not authentication. The application is localhost-only, not production-ready. Regex checks are incomplete injection/safety demonstrations. No real work instructions, machine control, company data, stakeholder study or deployed Microsoft integration is included. Source files are locally trusted; adversarial source ingestion is not defended. The “confidence” value is query token coverage, not probability of correctness. No stale-review expiration policy is implemented; current/approved flags require document-owner maintenance.

## Resume wording

“Developed a manufacturing knowledge-assistant prototype with version-aware, role-filtered retrieval, cited evidence, unsupported-query abstention, safety escalation and SQLite feedback monitoring; evaluated 30 synthetic scenarios and documented retrieval failures and rollout criteria.”

MIT licensed. Independent portfolio work; no Linamar affiliation.
