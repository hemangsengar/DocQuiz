#!/usr/bin/env bash
set -e

echo "=== DocQuiz setup ==="

# 1. Detect OS
OS_NAME="$(uname -s)"
case "$OS_NAME" in
    Linux*)             PLATFORM="linux" ;;
    Darwin*)            PLATFORM="mac" ;;
    MINGW*|MSYS*|CYGWIN*) PLATFORM="windows" ;;
    *)                  PLATFORM="unknown" ;;
esac
echo "Detected platform: $PLATFORM"

# 2. Find a Python interpreter
if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "Python not found. Install Python 3.10+ from https://python.org and re-run this script."
    exit 1
fi
echo "Using $($PYTHON --version)"

# 3. Create venv + install deps (prefer uv if available)
if command -v uv >/dev/null 2>&1; then
    echo "uv found, using it..."
    uv venv .venv
    uv pip install -r requirements.txt --python .venv
else
    echo "uv not found, using standard venv + pip..."
    "$PYTHON" -m venv .venv
    if [ "$PLATFORM" = "windows" ]; then
        ./.venv/Scripts/pip.exe install --upgrade pip
        ./.venv/Scripts/pip.exe install -r requirements.txt
    else
        ./.venv/bin/pip install --upgrade pip
        ./.venv/bin/pip install -r requirements.txt
    fi
fi

# 4. Set up .env
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env from .env.example — add your GROQ_API_KEY before running anything."
else
    echo ".env already exists, leaving it alone."
fi

# 5. Print next steps
echo ""
echo "=== Setup done ==="
if [ "$PLATFORM" = "windows" ]; then
    echo "Activate with:  source .venv/Scripts/activate"
else
    echo "Activate with:  source .venv/bin/activate"
fi
echo "Then add GROQ_API_KEY to .env and run:"
echo "  python starter/main.py sample_notes/python_oop_basics.pdf"
