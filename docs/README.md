# Manufacturing Knowledge Assistant: documentation

[Project overview](../README.md)

This index separates running the prototype, understanding its contracts, and assessing the analyst evidence. All business scenarios and stakeholder personas are synthetic. Proposed deployment capabilities are explicitly identified; a written plan is not a completed rollout.

## Guides

| Document | Purpose |
|---|---|
| [Getting started](getting-started.md) | Clone, run and select an isolated database |
| [Local LLM](local-llm.md) | Optional Ollama setup and verification gap |
| [User guide and adoption](adoption-and-user-guide.md) | Demonstration, training and rollout plan |
| [Architecture](architecture.md) | Request lifecycle and synchronous runtime |
| [Data dictionary](data-dictionary.md) | Document/evaluation schemas and monitoring denominators |
| [API reference](api-reference.md) | Ask, feedback, metrics and response statuses |
| [Retrieval design](retrieval-design.md) | Normalization, BM25, coverage and control boundaries |
| [Requirements](requirements.md) | Intended use, requirements and process map |
| [Evaluation and pilot readiness](evaluation.md) | Observed failures and proposed rollout criteria |
| [Governance](governance.md) | Risk register, ownership and stop conditions |
| [Testing](testing.md) | Regression, HTTP and generation-verification scope |
| [Troubleshooting](troubleshooting.md) | Abstention, provider failure and expected filters |
| [Research and role fit](research-and-role-fit.md) | Role coverage and design references |

## Suggested reading paths

**First-time user:** getting started → user guide → troubleshooting.

**Technical reviewer:** architecture → data dictionary → API reference → algorithm/decision guide → testing.

**Systems-analysis reviewer:** requirements → business case or evaluation decision → governance → pilot/adoption plan.

## Project maintenance

- [Contributing](../CONTRIBUTING.md): local workflow and relevant verification.
- [Security](../SECURITY.md): local-use boundaries and safe issue reporting.
- [Changelog](../CHANGELOG.md): initial prototype and documentation update.
- [License](../LICENSE): MIT terms.
- [Build validation](../reports/validation.md): original verification scope and unverified paths.

Documentation describes the current implementation. Read baseline reports alongside CI results; an automated run does not establish real user adoption, operational safety or financial benefit.
