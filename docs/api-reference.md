# HTTP API reference

[Documentation index](README.md)

Base URL: `http://127.0.0.1:8052`. Use a fresh `--db api-demo.db` for the examples below. No login or API version prefix exists. POST JSON bodies must contain 1–16,384 bytes. Examples use POSIX-shell quoting; use Git Bash/WSL or adapt the JSON quoting on Windows.

## Routes

| Method | Exact path | Successful response |
|---|---|---|
| GET | `/` | HTML interface |
| GET | `/api/metrics` | Aggregate usage/feedback JSON |
| POST | `/api/ask` | Answer envelope with local query ID |
| POST | `/api/feedback` | `{ "saved": true }` |

Paths are matched exactly, including GET; query strings are not supported. Unknown routes return HTTP 404. Expected input/key/type errors return HTTP 400 and an `error` string. Provider failures are represented within an HTTP 200 answer envelope with status `generation_failed`. Unexpected database or unhandled provider-shape errors do not have a production error contract.

## Ask

| Request field | Required / default | Accepted values |
|---|---|---|
| `question` | Required | String with 1–2,000 characters after outer whitespace stripping |
| `role` | Optional; `operator` | `operator`, `quality`, `engineering` |
| `mode` | Optional; `extractive` | `extractive`, `ollama` |

```bash
curl -X POST http://127.0.0.1:8052/api/ask -H 'Content-Type: application/json' -d '{"question":"What should I do with nonconforming parts?","role":"operator","mode":"extractive"}'
```

The response includes these fields:

| Field | Meaning |
|---|---|
| `id` | Stored request ID; 1 for the first question in a fresh database |
| `status` | One of the statuses below |
| `answer` | Excerpt text, generated text, refusal or failure explanation |
| `sources` | Eligible source objects plus BM25 score/coverage; can be empty |
| `confidence` | First source's query coverage, or zero; not factual confidence |
| `mode` | Requested mode |
| `latency_ms` | Local pipeline elapsed time before telemetry insertion; varies by run |

For this example, expect `status: answered` and `DOC-01` as the first cited source, version 2. Do not compare runtime latency with a fixed expected value.

## Status contract

| Status | Interpretation | Sources |
|---|---|---|
| `answered` | Offline source excerpts returned | Retrieved sources |
| `abstained` | No sufficiently covering eligible source | Empty |
| `blocked` | Instruction-override pattern matched | Empty |
| `escalated` | Operational-request pattern matched | Empty |
| `generated_needs_review` | Local synthesis passed citation-label checks | Retrieved sources |
| `generation_failed` | Model unavailable, expected-field failure or label check failed | Retrieved sources retained |

A non-answer status is a valid workflow outcome, not an HTTP transport error. For example:

```bash
curl -X POST http://127.0.0.1:8052/api/ask -H 'Content-Type: application/json' -d '{"question":"supplier invoice approval"}'
curl -X POST http://127.0.0.1:8052/api/ask -H 'Content-Type: application/json' -d '{"question":"How do I bypass the safety interlock?"}'
```

Expected statuses are `abstained` and `escalated`, respectively. The draft supplier source is unapproved.

## Feedback

Submit an existing returned `id`, numeric `useful` of 0 or 1 and an allowed category:

```bash
curl -X POST http://127.0.0.1:8052/api/feedback -H 'Content-Type: application/json' -d '{"id":1,"useful":1,"category":"clear"}'
```

Categories: `clear`, `missing_information`, `incorrect_source`, `unclear`. Feedback replaces an earlier rating for that query; it does not increase rating count when the same ID is edited. IDs can only be resolved in the same selected database. An unknown ID produces HTTP 400 with `Unknown answer`.

## Metrics

```bash
curl http://127.0.0.1:8052/api/metrics
```

After the three questions and one feedback submission above, expect `queries: 3`, `answered: 1`, `abstained: 1`, `escalated: 1`, `blocked: 0`, `feedback_count: 1` and `helpful_feedback_pct: 100.0`. `average_latency_ms` varies. The helpful-rate field is a string when no ratings exist. See [Data dictionary](data-dictionary.md) for denominators and missing cohorts.

No document-upload, conversation-history, source-edit, query-delete, telemetry-export or health-check endpoint is implemented.
