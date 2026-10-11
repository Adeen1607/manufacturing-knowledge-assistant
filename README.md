# Manufacturing Knowledge Assistant

**Find approved manufacturing information, inspect the evidence, and measure failures.**

[![Verify prototype](https://github.com/Adeen1607/manufacturing-knowledge-assistant/actions/workflows/checks.yml/badge.svg)](https://github.com/Adeen1607/manufacturing-knowledge-assistant/actions/workflows/checks.yml)

A local Python/SQLite prototype that filters fictional documents by approval, revision status and simulated role, then ranks relevant sources using BM25. Offline mode displays cited excerpts. Optional Ollama mode sends the retrieved evidence to a local language model for synthesis.

## Quick start

Requires Python 3.10+. Offline mode needs no packages or API key.

```bash
git clone https://github.com/Adeen1607/manufacturing-knowledge-assistant.git
cd manufacturing-knowledge-assistant
python app.py
```

Open http://127.0.0.1:8052. Ask **“What should I do with nonconforming parts?”** and inspect the source ID, version, owner and excerpt.

See [Getting started](docs/getting-started.md) for platform options and [Local LLM setup](docs/local-llm.md) for optional generation.

## Response paths

| Path | Implemented behavior |
|---|---|
| Source filtering | Only current, approved documents with the selected role are eligible |
| Retrieval | BM25 ranks title/body tokens; a query-coverage gate determines abstention |
| Offline answer | Up to three cited source excerpts, with no LLM generation |
| Optional generation | Fixed localhost Ollama endpoint; citation-label checks; human-review status |
| Control demonstrations | Pattern-based instruction-override blocking and operational-request escalation |
| Monitoring | Query status, mode, role, latency and categorized feedback in SQLite |

The role selector is a simulation, not identity-based access control. The API field `confidence` means normalized query-token coverage, not probability of correctness.

## Baseline evidence

**15 automated tests pass.** The offline evaluation passes **25 of 30 synthetic development cases**. Expected source hit at rank 1 is **11/16 (68.8%)** across answerable cases; five supported paraphrases incorrectly abstain. The [complete report](reports/evaluation-results.json) preserves those failures.

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

The evaluator reports quality results but does not fail its process exit code when fixture cases fail. A green workflow confirms the configured tests/evaluation commands completed; it does not mean all evaluation cases passed. No real Ollama model was executed during baseline verification.

## Documentation

Start with the [Documentation index](docs/README.md), or choose a route:

- **Run and demonstrate:** [Setup](docs/getting-started.md), [Local LLM](docs/local-llm.md), [User guide](docs/adoption-and-user-guide.md), [Troubleshooting](docs/troubleshooting.md).
- **Understand the implementation:** [Architecture](docs/architecture.md), [Data dictionary](docs/data-dictionary.md), [API reference](docs/api-reference.md), [Retrieval design](docs/retrieval-design.md).
- **Review the analyst work:** [Requirements](docs/requirements.md), [Evaluation and pilot decision](docs/evaluation.md), [Governance](docs/governance.md), [Adoption plan](docs/adoption-and-user-guide.md).
- **Assess evidence:** [Testing](docs/testing.md), [Build validation](reports/validation.md), [Research and role fit](docs/research-and-role-fit.md).

## Scope and next steps

Independent portfolio work by Mohammed Adeen Shaik. All documents and stakeholders are fictional; no Linamar relationship or production outcomes are claimed. The assistant cannot authorize machine operation, product release or engineering changes. Pattern checks and citation labels do not guarantee security, safety or factual grounding.

The next evidence-based step is to improve retrieval and evaluate genuinely unseen user questions before a real pilot. Authentication, delegated enterprise source access, controlled ingestion and answer-quality validation remain proposed work. See [Security](SECURITY.md), [Contributing](CONTRIBUTING.md) and the [MIT license](LICENSE).


## Rebuild the reading edition

```bash
python -m pip install -r requirements-research.txt
python scripts/build_research_site.py
```

This renders saved notebook outputs without rerunning model training or external APIs. To refresh findings, run the analysis commands above first, update `reports/research-findings.md`, and rebuild.

<!-- research-edition:start -->
## Research edition

[Research report and final visual results](research/report.md) · [Browser-ready notebook catalogue](research/notebooks.html)

Fresh offline evaluation on 11 October 2026: **25/30 fixtures pass**. Status accuracy is **83.3%** and expected-source hit at rank 1 is **68.8%** on answerable fixtures. These are developer-authored synthetic cases, not a held-out benchmark. **5 failures remain visible** in evaluation-results.json. Optional LLM generation was not evaluated.

| Measure | Value |
|---|---:|
| mode | offline extractive; LLM generation not evaluated |
| dataset | 30 developer-authored synthetic fixtures; not held out |
| cases | 30 |
| passed | 25 |
| status accuracy | 0.8333 |
| expected source hit at 1 | 0.6875 |



The `research/` folder contains a professional static reading edition. The Pages workflow deploys it after GitHub Pages is enabled with **GitHub Actions** as the publishing source. Intended URL: `https://adeen1607.github.io/manufacturing-knowledge-assistant/`. Deployment status must be checked in Actions before treating that address as live.

<!-- research-edition:end -->
