# Getting started

[Documentation index](README.md) · [Project overview](../README.md)

## Prerequisites

Python 3.10 or newer and a modern browser. Git is needed only for cloning. Both projects use the Python standard library, including SQLite; `pip install` is unnecessary. The checked-in `requirements.txt` records this. Python 3.12 was used for automated verification.

## Obtain the project

```bash
git clone https://github.com/Adeen1607/manufacturing-knowledge-assistant.git
cd manufacturing-knowledge-assistant
```

Alternatively, download the repository ZIP from GitHub, extract it, and open a terminal in the directory containing `app.py` and `core.py`.

## Start the application

```bash
python app.py
```

If your system calls Python `python3`, use `python3` throughout. On Windows, `py -3` can be used if the Python launcher is installed.

Open http://127.0.0.1:8052 in your browser. Keep the terminal running; Ctrl+C stops the server. The server binds to `127.0.0.1` and is intended for local demonstrations.

## Use an isolated demonstration database

```bash
python app.py --port 8052 --db walkthrough.db
```

`--db` selects the SQLite file. The default is `local.db` beside the application, regardless of your shell's current directory. A relative custom database path is resolved from the directory where you run the command. Its parent directory must already exist. Files are created automatically on first use. Database files are excluded from Git.

To begin a clean walkthrough, stop the running process and use a new filename, for example `walkthrough-02.db`. Existing files are preserved. This resets the app's stored records only; source fixtures stay in the repository.

## Verify the project

From the repository root:

```bash
python -m unittest discover -s tests -v
python evaluate.py
```

The tests use temporary databases and ephemeral localhost ports. The evaluator writes the reproducible JSON report under `reports/`. It does not modify the application database.

## Operating settings

| Setting | Default | How to change |
|---|---|---|
| HTTP port | 8052 | `--port 8060` |
| Listening address | `127.0.0.1` | Fixed in `app.py`; no CLI setting |
| Application database | `local.db` beside `app.py` | `--db walkthrough.db` |
| Python dependencies | Standard library | No installation required |

Start in `extractive` mode. To enable generation, follow the [Local LLM setup](local-llm.md). Continue to the [User guide](adoption-and-user-guide.md) for a demonstration.

## Troubleshooting

See [Troubleshooting](troubleshooting.md) for port conflicts, database issues and expected refusals. See [Contributing](../CONTRIBUTING.md) before changing fixtures or behavior.
