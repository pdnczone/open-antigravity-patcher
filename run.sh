#!/usr/bin/env bash
set -e

# Change directory to script location
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Ensure virtual environment exists
if [ ! -d ".venv" ]; then
    echo "[*] Initializing virtual environment..."
    python3 -m venv .venv
    .venv/bin/pip install --upgrade pip -q
    .venv/bin/pip install -r source/requirements.txt -q
fi

# Run the patcher
exec .venv/bin/python3 source/main.py "$@"
