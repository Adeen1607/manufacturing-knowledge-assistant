# Troubleshooting

[Documentation index](README.md)

| Symptom | Explanation | Resolution |
|---|---|---|
| Python command missing | Interpreter naming differs | Use `python3` or Windows `py -3`; Python 3.10+ required |
| Tests cannot import `core` | Wrong current directory | Run from the repository root |
| Port 8052 occupied | Another process is listening | Use `--port 8062` and open that port |
| Database cannot open | Missing/unwritable parent | Choose an existing writable path or `--db walkthrough.db` |
| A supported question abstains | Lexical coverage below 75% | Inspect the documented failures; report a synthetic paraphrase rather than lowering the threshold blindly |
| Engineering source absent for operator | Selected role is ineligible | Expected demo filter behavior; role switching does not establish real authorization |
| Old revision or invoice draft absent | Not current or not approved | Expected source exclusion |
| High confidence but unhelpful answer | Confidence is token coverage | Inspect intent and evidence; give `incorrect_source` or `missing_information` feedback |
| `generation_failed` | Ollama unavailable, model missing or citation/response issue | Check the local service and installed model, or use offline mode |
| Page appears unresponsive during generation | Single-threaded server waiting on model | Allow the request to settle; avoid sending many more requests; restart locally if necessary |
| Helpful rate says `No feedback` | No rated query IDs exist | Rate a returned answer in the same database |
| Feedback edit does not increase count | One latest rating per request | Expected behavior; verify helpful percentage instead |
| Feedback reports `Unknown answer` | ID belongs to another database or does not exist | Submit the ID returned by the current app instance |
| `/api/metrics?x=1` returns 404 | Exact path matching | Use `/api/metrics` without query strings |
| CI green despite failed scenarios | Evaluator does not enforce a quality exit gate | Read `reports/evaluation-results.json` and the evaluation interpretation |

Documents are reloaded each retrieval, so edits affect later questions without reseeding a database. Invalid fixture schema can crash retrieval; use trusted synthetic shapes and validate proposed changes. Telemetry persists until a different database is selected; a new corpus does not erase previous query counts.

When reporting a defect, include only synthetic question text, selected role/mode, expected source/status and observed response. Omit confidential documents, personal information and credentials. See [Security](../SECURITY.md).
