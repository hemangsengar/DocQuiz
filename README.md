# DocQuiz

Upload study notes (PDF) → generate an AI-powered quiz. Day 1: we build the
three core building blocks — PDF text extraction, chunking notes into
sections, and LLM question generation that spreads across those sections —
as plain Python. The full web app (FastAPI, database, adaptive engine,
frontend) comes on Day 2.

## Prerequisites

- Python 3.10+
- Git
- A free Groq API key: https://console.groq.com

## Setup

```bash
git clone <repo-url>
cd docquiz
./setup.sh          # Windows: use Git Bash, run: bash setup.sh
```

This creates a virtual environment and installs dependencies (using `uv` if
you have it installed, otherwise standard `venv` + `pip`).

Activate the environment:

```bash
source .venv/bin/activate        # Mac/Linux
source .venv/Scripts/activate    # Windows (Git Bash)
```

Open `.env` (created automatically from `.env.example`) and paste in your
Groq API key:

```
GROQ_API_KEY=your_actual_key
```

## Folder guide

- `starter/` — where you write code today. Functions have a docstring and a
  `# TODO` — fill in the body.
- `solution/` — a working reference. Try the TODO yourself first; only peek
  if you're stuck.
- `sample_notes/` — a sample PDF (`python_oop_basics.pdf`) to test against.

## Running it

Once `pdf_service.py` (both `extract_text_from_pdf` and `chunk_text`) and
`llm_service.py` are filled in:

```bash
python starter/main.py sample_notes/python_oop_basics.pdf
```

This should print 5 generated multiple-choice questions.

## Troubleshooting

- **`groq.AuthenticationError` / 401** — check `GROQ_API_KEY` is set correctly in `.env`.
- **`ModuleNotFoundError: No module named 'pdfplumber'`** — make sure your venv is
  activated (`source .venv/bin/activate`) before running Python.
- **`json.decoder.JSONDecodeError` on the LLM response** — the model didn't return
  valid JSON; re-run, or check the prompt still asks for a JSON object.
- **`NotImplementedError`** — expected until you fill in the corresponding TODO.
