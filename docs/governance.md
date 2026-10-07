# Responsible AI and ownership

| Risk | Potential impact | Prototype control | Remaining limitation | Owner persona |
|---|---|---|---|---|
| Superseded procedure retrieved | Incorrect action | Current/approved filter and archived fixture | Metadata maintenance depends on owner | Document controller |
| Department content exposed | Confidentiality breach | Role filter before BM25 | User can choose any role; no authentication | IT |
| Generated unsupported claim | Wrong advice | Cited context and review status | Citation labels do not verify grounding | Quality lead |
| Prompt injection | Control override | Small pattern-check suite | Unseen phrasing and adversarial sources unprotected | IT/security |
| Unsafe equipment advice | Injury or damage | Escalation patterns and no tools | Regex is not a complete safety system | Engineering/EHS |
| Excessive abstention | Low adoption | Evaluation failures and feedback categories | Five known supported queries fail | Analyst |
| Employee surveillance | Privacy concern | No question text or user identity stored | HTTP logs may contain IP/path; no retention automation | IT/data owner |
| Withdrawal not propagated | Stale knowledge | Source flags loaded each request | No approval system or expiration validation | Document controller |

NIST-inspired mapping: Govern = owners, scope and incident decisions; Map = users, knowledge sources and impacts; Measure = fixtures, failures and user tasks; Manage = stop conditions and remediation. This is a lightweight design exercise, not NIST certification or legal compliance advice.

Before a real deployment, replace role selection with validated identity and delegated source access, enforce approved ingestion, define query/feedback retention, threat-model prompts and source content, and maintain a human escalation route. Do not connect this assistant to operational technology or release/approval tools.

Stop pilot on restricted-source exposure, withdrawn source retrieval or critical incorrect guidance. Disable generated answers, return users to approved document lookup and preserve permitted incident evidence. Resume only with documented fix, retest and owner authorization.
