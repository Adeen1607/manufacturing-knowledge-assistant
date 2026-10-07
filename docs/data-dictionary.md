# Data dictionary and persistence

[Documentation index](README.md)

## Source documents

`data/documents.json` contains eight fixtures: six approved current documents, one superseded revision and one unapproved draft. All text and owner labels are fictional.

| Field | Intended shape and use |
|---|---|
| `id` | Stable citation identifier matching `DOC-number`, for example `DOC-01` |
| `title` | Human-readable title included in retrieval tokens |
| `version` | Displayed revision number |
| `owner` | Source-owner label shown to users |
| `reviewed_on` | Displayed ISO date; no automatic expiration check |
| `approved` | Intended Boolean; retrieval uses truthiness |
| `current` | Intended Boolean; retrieval uses truthiness |
| `roles` | Array containing any of `operator`, `quality`, `engineering` |
| `text` | Complete source excerpt; included in retrieval and optional synthesis |

The implementation assumes well-formed trusted fixtures. It does not fully validate the corpus schema, enforce unique IDs or enforce one approved current revision per real document. Keep the intended shape consistent and add dedicated validation before accepting external sources.

Returned sources add `score` (rounded BM25 score) and `coverage` (rounded meaningful-query-token overlap). They retain all source metadata, including roles and approval flags. Question text is not part of source records.

## Evaluation fixtures

| Field | Meaning |
|---|---|
| `question` | Synthetic development question |
| `role` | Role to simulate |
| `status` | Expected answer/control status |
| `source` | Optional expected first source for answerable cases |

The report adds `actual_status`, `source_ids` and `passed`. Its headline source-hit denominator includes all cases with an expected `source`, including abstentions.

## SQLite schema

| Table | Columns | Purpose |
|---|---|---|
| `queries` | `id INTEGER PRIMARY KEY`, `role TEXT`, `status TEXT`, `mode TEXT`, `latency_ms REAL`, `created_at TEXT DEFAULT CURRENT_TIMESTAMP` | Minimal per-request telemetry |
| `feedback` | `query_id INTEGER PRIMARY KEY REFERENCES queries(id)`, `useful INTEGER CHECK(useful IN (0,1))`, `category TEXT` | Latest rating for a request |

Foreign-key enforcement is enabled on each application connection. Feedback requires an existing query and replaces the prior rating for that query ID. Categories are `clear`, `missing_information`, `incorrect_source` and `unclear`. No free-text feedback, user account, question, answer, retrieved-source IDs or document snapshot is stored in SQLite.

Timestamps use SQLite's default UTC format. The standard HTTP handler can still print access metadata such as client address, method and route to the terminal; absence of stored question text does not imply all operational metadata is absent.

## Monitoring definitions

`queries` counts all logged responses, including generation failures. `answered` counts both offline answered and generated-needs-review statuses. `abstained`, `escalated` and `blocked` have separate counts; generation failures have no dedicated displayed counter. Average latency covers all logged response statuses, not only successful answers. `feedback_count` counts rated query IDs. Helpful rate = useful ratings / rated queries × 100; it is the string `No feedback` when none exist.

These values do not measure unique users, sessions, weekly adoption, task-time savings or response correctness. No retention scheduler, encryption or telemetry export API exists. Stop the application before making a simple local database backup.
