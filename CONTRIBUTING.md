# Contributing

## Local workflow

Read the [documentation index](docs/README.md), then clone the repository and run the current tests before editing. Use a separate database for manual exploration; do not commit `local.db`, personal information, real company documents or credentials.

Keep changes focused. Business-rule changes should update requirements and acceptance criteria; response changes should update API examples; fixture changes should update the data dictionary and evaluation interpretation. Configuration must remain documented and optional external services must fail clearly.

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

## Meaningful validation

Use regression tests for externally visible behavior and decision boundaries. Include an appropriate negative case when changing a gate or filter. For retrieval changes, report both improved and regressed queries. Preserve evaluation failures in the published report. An evaluation fixture used during tuning is development evidence, not a held-out benchmark.

Run documented API examples against a fresh database. Check relative Markdown links, code-fence pairing and that documented fields match actual responses. Inspect the interface manually at desktop and narrow widths when a browser is available; tests do not establish visual correctness.

## Pull request checklist

- Explain the concrete trigger and resulting behavior.
- Link affected requirements or evaluation cases.
- Provide relevant test results and known limitations.
- Update documentation for changed assumptions or API contracts.
- Keep synthetic examples clearly labeled and preserve real access/privacy boundaries.

## Scope

This is a local portfolio prototype. Authentication, enterprise connectors, production deployment and independently validated user outcomes are not established by adding documentation or an integration sketch. New capabilities should be marked implemented only after their behavior is exercised and evidenced.

The [MIT license](LICENSE) covers the project. Report security concerns without including credentials or confidential records; see [Security](SECURITY.md).
