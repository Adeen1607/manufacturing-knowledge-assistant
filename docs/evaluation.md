# Evaluation and pilot readiness

[Documentation index](README.md)

## Reproduce and interpret

Run `python evaluate.py`. `data/evaluation.json` contains 30 developer-authored synthetic fixtures: 16 answerable, seven unsupported or restricted, four unsafe machine-operation requests and three instruction-override requests. Full observed outputs are in `reports/evaluation-results.json`.

Observed offline baseline: 25/30 expected status-and-top-source checks pass; status accuracy is 83.3%; expected source at rank 1 for answerable queries is 11/16 (68.8%). These fixtures informed development, are not independent/held-out, and are too small to establish generalization. The 15 regression tests protect implementation behavior; passing them is not the same as meeting pilot quality targets.

## Observed defects

Five supported questions abstain: defective-part handling; quality-log details for rejected parts; finding calibration records; calibration ownership; and parts failing inspection. Conservative token coverage misses unfamiliar phrasing. This is a known recall limitation. The short direct query “nonconforming parts” works, but normal users should not need to know document wording.

All seven expected unsupported/restricted cases abstain in this suite. This does not establish comprehensive access or answer safety. Filtering excludes inaccessible content, but related allowed sources can still be retrieved for other phrasings. A source-excerpt answer is not guaranteed to answer the user's exact intent.

## Decision

**Do not recommend enterprise rollout yet.** Improve morphology/semantic retrieval and test with genuinely unseen operator questions. Compare BM25 against enhanced folder search and a semantic/hybrid retriever using identical access filters. Version a new evaluation set before tuning. Reevaluate false answers and false abstentions separately; prefer abstention when evidence is weak.

## Proposed pilot criteria

At least 90% expected-source hit at rank 1 on an independently authored representative question set; zero inaccessible/withdrawn sources returned in access tests; 100% correct escalation on the agreed critical-request suite; no critical incorrect operational advice; median task time at least 20% below manual search; 60% weekly active/eligible pilot users; satisfaction at least 4/5. These are proposed targets, not achieved results.

## LLM evaluation gap

No real Ollama model was executed here. Before enabling generation, evaluate each claim's factual support, source citation accuracy, abstention, malicious source content and operational advice. Compare against extractive mode. Citation-label checks only reject absent or unknown citation IDs; they cannot catch unsupported claims carrying a valid citation. Include reviewer agreement, model/version, prompt version and latency percentiles in the report.

## Measurement definitions

Pass = expected response status and, for answerable cases, expected first source. Source hit@1 = correct first-source count / all answerable cases, including abstentions. Response latency is local measured elapsed time; no universal latency claim is made. Feedback helpful rate = useful ratings / rated responses, not all queries. Aggregate monitoring does not calculate weekly active users.
