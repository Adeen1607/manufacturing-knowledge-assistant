# Architecture and API contract

Standard-library HTTP server serves a static accessible-label HTML interface and JSON API. `core.py` normalizes query tokens, filters documents, applies BM25 and minimum coverage, then returns excerpts or sends evidence to a fixed localhost Ollama endpoint. SQLite stores aggregate query telemetry and feedback, not questions or answers.

| Endpoint | Contract |
|---|---|
| GET `/` | HTML interface |
| GET `/api/metrics` | Query counts, status counts, mean latency, feedback count and helpful rate |
| POST `/api/ask` | `{ "question": "nonconforming parts", "role": "operator", "mode": "extractive" }` |
| POST `/api/feedback` | `{ "id": 1, "useful": 1, "category": "clear" }` |

Ask response: local ID, status, answer, source metadata/excerpts, coverage indicator called confidence, mode and latency. Invalid role, mode, question length or feedback yields HTTP 400. Only known endpoints are served. Payloads are capped at 16 KiB. The server is single-threaded; a long local-model request blocks other requests.

Document metadata includes stable ID, title, version, owner, review date, approved/current flags and roles. Every request reloads the fixture corpus, but metadata is not independently signed or authenticated. BM25 statistics are computed only on role-eligible documents. Coverage is the fraction of normalized meaningful query tokens found in a document; it is not calibrated confidence.

Ollama uses the localhost `/api/chat` endpoint, temperature zero and model name from `OLLAMA_MODEL`. Errors become `generation_failed`; successful synthesis is `generated_needs_review`. No cloud API key, embedding service or vector database is required.

Enterprise extension requires authenticated identity, managed source retrieval, version/withdrawal propagation, semantic retrieval evaluation, robust safety controls, protected telemetry and a production application server. These are planned extensions, not implemented integrations.
