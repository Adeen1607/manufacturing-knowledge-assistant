# Adoption plan and user guide

## Proposed rollout

1. Confirm source ownership, revision metadata and intended role access with operations, quality, engineering and IT.
2. Resolve retrieval failures and complete an independently authored task evaluation.
3. Train a small representative cohort from more than one shift. Compare task lookup against manual search with counterbalanced order.
4. Collect source correctness, paired task time, weekly active/eligible usage, satisfaction and categorized failures. The app captures aggregate query/feedback counts only; a separately approved study must collect cohort adoption and timing.
5. Prepare a plain-language leadership decision: observed benefit, critical defects, affected users, required fixes, accountable owner and proposed next scope.

## Ten-minute training agenda

Explain what the assistant can locate; demonstrate source owner and version inspection; ask a supported question; show unsupported-query abstention; demonstrate escalation; record useful and unhelpful feedback. Explain that role selection is a demo and cannot prove access permission. In LLM mode every generated claim needs verification.

## User steps

Run `python app.py`, open http://127.0.0.1:8052 and use offline mode first. Choose a simulated role, enter a concise document question, and inspect cited excerpts. If the assistant abstains, contact the source owner rather than guessing. If it escalates, use the approved site procedure and authorized personnel. Report incorrect-source or missing-information feedback. Do not enter real company or personal information into this prototype.

For Ollama mode, install and run a local model separately. If unavailable, the UI reports generation failure instead of silently claiming an answer. Switch to offline excerpts to continue. Stop the server with Ctrl+C.

## Interview walkthrough

Explain why source approval, versioning and role filtering precede retrieval. Show operator vs engineering scope, an archived source that never appears, and an invoice draft that triggers abstention. Open the evaluation report and explain the five false abstentions. A strong analyst explains why this prototype is not ready for rollout and what evidence would change that decision.
