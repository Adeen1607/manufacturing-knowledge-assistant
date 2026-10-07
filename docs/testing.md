# Tests and quality evidence

[Documentation index](README.md)

## Run

From the repository root:

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

The 12 core tests check eligible current sources, role filtering, unknown roles, abstention, control patterns, source citations, invalid input, unavailable-provider behavior and feedback accounting. Three HTTP tests exercise served HTML, real ask/feedback/monitoring requests and invalid/unknown routes. Test databases and ports are temporary.

The baseline has 15 passing automated tests. The model-provider failure test mocks the adapter; it is not a real-model integration test. The suite does not demonstrate resistance to all injections or correct operational advice outside its fixtures.

## Evaluation is a separate quality measure

The evaluator uses 30 developer-authored question fixtures in offline mode. A case passes when the expected status matches and, if specified, the expected document is the first source. Baseline result: 25/30 pass; five supported queries abstain; expected-source hit@1 is 11/16.

`evaluate.py` writes `reports/evaluation-results.json`, prints summary/failures and returns normally even when cases fail. CI currently runs this command for reporting and uploads JSON artifacts. Therefore a successful workflow is compatible with known evaluation failures. There is no quality threshold enforced as a CI exit condition.

See [Evaluation and pilot readiness](evaluation.md) for the complete interpretation, proposed thresholds and independent-data gap.

## Useful regression strategy

For source-filter changes, include an inaccessible source, an archived revision and an unapproved draft. For retrieval changes, preserve the existing report, compare every old case, and evaluate new independently authored phrasing before tuning. For feedback changes, verify repeated ratings do not inflate the denominator. For generation changes, test provider errors, missing citations, foreign citations and real-model claim support.

## Manual checks still needed

The baseline checked embedded JavaScript syntax and real HTTP behavior. Browser visual interaction and a real Ollama model were not verified. Review source readability, keyboard interaction, narrow-screen layout, loading/error states and feedback refresh in a browser when available. No accessibility compliance, cross-browser compatibility or performance benchmark is claimed.
