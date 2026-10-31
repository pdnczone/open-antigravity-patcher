@echo off
cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Python 3 is not found in PATH. Please install Python from https://www.python.org/
    pause
    exit /b 1
)

if not exist ".venv" (
    echo [*] Initializing virtual environment...
    python -m venv .venv
    .venv\Scripts\python.exe -m pip install --upgrade pip -q
    .venv\Scripts\python.exe -m pip install -r source\requirements.txt -q
)

.venv\Scripts\python.exe source\main.py %*
