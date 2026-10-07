# Research and role fit

[Documentation index](README.md)

Independent portfolio work inspired by the supplied Linamar AI Systems Analyst, Intermediate posting. No affiliation, company access, stakeholder interviews or production implementation is claimed. All manufacturing data is fictional. The supplied posting is authoritative for this tailoring; an independently accessible official copy was not located.

## Interpretation of the role

The responsibilities connect business problem discovery to AI opportunity assessment, requirements, POC coordination, testing, responsible implementation, onboarding and ongoing outcomes. Programming is a supporting capability. A convincing portfolio therefore needs decision evidence and understandable documentation alongside code.

| Posting requirement | Opportunity tracker evidence | Knowledge assistant evidence |
|---|---|---|
| Assess business value, feasibility, risk, readiness | Transparent scoring and gates | Retrieval scope and evaluation failures |
| Requirements, process flows, success measures | BRD and traceability matrix | Source, response and access requirements |
| Coordinate POC and pilot | State transitions, evidence, audit trail | Test cases, source-level evaluations |
| Responsible AI and ownership | Named simulated owners; blocked high-risk use case | Version filters, escalation, telemetry design |
| Rollout, training, adoption | Pilot metrics and rollout plan | User guide and categorized feedback |
| Python, SQL, APIs, dashboards | Python, SQLite, JSON HTTP endpoints | Python BM25, SQLite monitoring, Ollama adapter |
| Enterprise low-code tools | Implementation mapping only | Implementation mapping only |

## Primary sources reviewed 2026-10-07 UTC

1. [Microsoft: Enhance AI responses with RAG](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/retrieval-augmented-generation). Informed the approved-source retrieval, citation and access-filter design. Enterprise delegated access is considerably stronger than a simulated role selector.
2. [NIST: AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/). Informed ownership, intended-use boundaries, risk assessment, evaluation and continuous monitoring. This project borrows the four functions; it is not a certification or full conformity assessment.
3. [NIST: AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework). Provides voluntary AI risk-management context.

4. [Microsoft: About agent evaluation](https://learn.microsoft.com/microsoft-copilot-studio/analytics-agent-evaluation-intro). Supports explicit test cases, expected outcomes and per-case evaluation rather than judging a demo impression.
5. [Ollama API reference](https://github.com/ollama/ollama/blob/main/docs/api.md). Informed the local chat adapter contract.

## Enterprise implementation mapping (design, not implemented)

| Prototype | Possible Microsoft implementation | Validation needed |
|---|---|---|
| Opportunity records | Power Apps + Dataverse or SharePoint list | Licensing, approval roles, retention |
| Local stage-change event | Power Automate approval flow | Identity, retries, audit retention |
| JSON approved source corpus | SharePoint approved library | Owner metadata, delegated permissions, revision handling |
| Local retrieval / optional Ollama | Copilot Studio + approved knowledge sources | Tenant policies, permission trimming, regional processing |
| SQLite monitoring | Approved analytics store + Power BI | Access, privacy, cohort measures |

Copilot Studio, Power Apps, Power Automate and SharePoint are not implemented here. Do not list them as hands-on skills based solely on this mapping.
