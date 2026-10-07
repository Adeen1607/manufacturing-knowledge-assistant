# Optional local LLM setup

[Documentation index](README.md)

## Scope

The offline application works without a model. Generation is an optional adapter using Ollama's local chat API. A real model was not run during baseline verification, so these instructions describe the implemented integration path rather than a validated model-quality claim.

## Start the model service

Install Ollama separately from its official distribution and ensure your machine can run the selected model. Installation/model download is outside the repository; hardware needs depend on the model and runtime.

With Ollama installed, start its local service if it is not already running:

```bash
ollama serve
```

In another terminal, pull the default model:

```bash
ollama pull llama3.2:3b
```

Keep the local service available at `http://127.0.0.1:11434`. The application calls `/api/chat`; the endpoint is fixed in `core.py`, not configurable with an environment variable.

## Configure a different installed model

The only adapter environment setting is `OLLAMA_MODEL`; it defaults to `llama3.2:3b`.

POSIX shell:

```bash
export OLLAMA_MODEL=llama3.2:3b
python app.py
```

PowerShell:

```powershell
$env:OLLAMA_MODEL = 'llama3.2:3b'
python app.py
```

Use a model name that is actually installed in your local Ollama instance. Select **Local LLM / Ollama** in the interface, or submit `mode: ollama` to `/api/ask`.

## Request and validation behavior

The adapter sends system instructions, the user question and the retrieved source texts with `stream: false` and requested `temperature: 0`. The network timeout is 90 seconds. This is a synchronous request; other API calls wait while the server is handling it.

The response must contain `message.content`. The adapter extracts `[DOC-number]` labels and requires at least one recognized citation, with all recognized labels drawn from the supplied sources. Successful output is marked `generated_needs_review`. Label validity does not prove source entailment, accurate summarization or absence of unsafe advice.

There is no cloud key, endpoint discovery, automatic download, background model startup or streaming UI. The application does not run model-produced tools or machine actions.

## Failure handling

Unavailable service, missing model, invalid JSON/expected fields or failed citation checks can return `generation_failed`. Sources remain available for user inspection. Switch to offline excerpts to continue; the app does not silently claim generated success. Some malformed response types may be unhandled because provider validation is not exhaustive.

## Verification before making a RAG claim

Run at least one real local-model request, retain model/version and prompt configuration, then evaluate factual support and citations on representative questions. Include unsupported queries, adversarial sources, access boundaries and operational requests. Compare with offline excerpts and an approved manual-search baseline. The existing 30-case report exercises offline mode only; rerunning it does not evaluate generation.
