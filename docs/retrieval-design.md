# Retrieval, control and generation design

[Documentation index](README.md)

## Why this baseline

BM25 supplies an inspectable lexical baseline without downloading an embedding model or requiring cloud credentials. The decision problem is factual document lookup. Offline responses quote complete source fixtures so the user can inspect exactly what was retrieved. The optional model adapter adds synthesis, but that path needs separate answer-quality evaluation.

## Token normalization

`tokens` lowercases text and extracts ASCII letters/digits with `[a-z0-9]+`. It removes the explicit stop-word set in `core.py`, applies a small synonym mapping, then strips a final `s` from words longer than four characters unless they end in `ss` or `us`. This is a lightweight heuristic, not language-aware stemming. Query tokens become a set, so repeated query terms do not add weight. Source term counts preserve repetition.

The corpus uses `title + text`. There is no chunking, semantic expansion, fuzzy spelling matching or multilingual tokenization. Heuristic morphology can create awkward tokens; a mature retriever should evaluate those effects rather than assume they improve recall.

## Eligibility precedes scoring

A document enters the retrieval corpus only when `approved` and `current` are truthy and the selected role occurs in `roles`. Unknown roles are rejected. BM25 term frequencies and corpus statistics are calculated only on eligible documents, so inaccessible content does not contribute to scoring statistics.

This demonstrates filter placement. It is not secure access control because any caller can choose `engineering`, and the corpus is a locally trusted JSON file. Revision flags are respected, but dates do not drive expiration and duplicate/current revision consistency is not independently validated.

## BM25 score

For each unique query term occurring in a document:

```text
idf = log(1 + (N − df + 0.5) / (df + 0.5))
contribution = idf × tf × 2.5 /
               (tf + 1.5 × (0.25 + 0.75 × document_length/average_length))
```

`N` is eligible document count, `df` is documents containing the term and `tf` is its frequency in the document. These constants correspond to `k1 = 1.5` and `b = 0.75`. Scores are summed and rounded to four decimals. Positive-score sources must also meet coverage of at least 0.75. At most three sources are returned, descending by rounded score.

## Coverage and abstention

Coverage = number of unique normalized query tokens found in a source / total unique normalized query tokens. At least three quarters must occur. Queries with no meaningful tokens or no eligible sufficiently covering source abstain. The response's `confidence` is the first source's coverage, rounded to four decimals. It is not a probability, factuality score or model confidence.

This conservative threshold produces known false abstentions. For example, “How do I find calibration records?” includes `find`, which does not match the source's `locate`; two of three meaningful terms match, below the 0.75 gate. A document can also match vocabulary without answering the intent. See [Evaluation](evaluation.md) for all five baseline failures.

## Control checks

Regex patterns illustrate instruction-override detection and machine-operation escalation. Injection patterns run before operational patterns. Both are narrow and can miss paraphrases or overmatch benign questions. No comprehensive content policy engine, adversarial document scanner or industrial safety validation exists.

## Two answer modes

`extractive` returns up to three cited source texts without generation. `ollama` sends question/context plus restrictive system instructions to the fixed local endpoint. A generated answer must include at least one `[DOC-number]` citation, and every recognized citation must belong to the retrieved sources. This checks label membership only; it cannot validate each claim or detect every malformed citation style.

Successful generation receives `generated_needs_review`; provider errors, malformed expected fields or failed label checks receive `generation_failed` while retaining source evidence. There is no silent substitution of generated output with excerpts. A real model was not exercised in baseline verification.

## Improvement sequence

Version an independently authored question set, compare lexical/semantic/hybrid approaches with the same eligibility filter, and inspect wrong sources and false abstentions separately. Then evaluate generated claims against sources and validate malicious-source behavior. Stronger retrieval alone does not establish safety, access enforcement or rollout readiness.
