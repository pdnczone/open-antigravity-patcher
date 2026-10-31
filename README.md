# 🔑 Open Antigravity Patcher (Cross-Platform)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge)](./LICENSE)
[![Cross-Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-brightgreen?style=for-the-badge)](#-quick-start)
[![Build and Release](https://github.com/pdnczone/open-antigravity-patcher/actions/workflows/build-and-release.yml/badge.svg)](https://github.com/pdnczone/open-antigravity-patcher/actions/workflows/build-and-release.yml)

Open-source cross-platform patcher for **Antigravity 2.0**, **Antigravity IDE**, **Antigravity CLI (`agy`)**, and **Google Antigravity extension for VS Code**. Bypasses regional and eligibility checks locally without VPN, proxies, or changing your Google account region.

---

## 🚀 Features

- **Antigravity IDE**: Patches `main.js` to bypass `isGoogleInternal` region checks.
- **Antigravity 2.0**: Patches `language_server` binary byte signatures (x86_64 and ARM64).
- **Antigravity CLI (`agy`)**: Patches binary byte signatures to unlock CLI tools on x86_64 & Apple Silicon / ARM64.
- **VS Code Extension**: Patches `google.google-antigravity` extension (`extension.js`) and downloaded binaries under `~/.gemini/bin`.
- **Automatic Path Discovery**: Scans Windows Registry, macOS `/Applications` and `~/Applications`, Linux system directories, and VS Code extensions.
- **Safe & Reversible**: Automatic backups before any modification, with 1-click restore for all targets.
- **Automated macOS Re-signing**: Automatically applies ad-hoc codesign and clears quarantine attributes after patching on macOS.

---

## ⚡ Quick Start

### 🍏 macOS

```bash
git clone https://github.com/pdnczone/open-antigravity-patcher.git
cd open-antigravity-patcher
./run.sh
```

Or manually with Python:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r source/requirements.txt
python3 main.py
```

> **Note for macOS:** If modifying `/Applications/Antigravity.app`, the terminal needs write permission or Full Disk Access. The script prompts for `sudo` when needed.

---

### 🐧 Linux

```bash
git clone https://github.com/pdnczone/open-antigravity-patcher.git
cd open-antigravity-patcher
chmod +x run.sh
./run.sh
```

Or run directly:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r source/requirements.txt
python3 main.py
```

---

### 🪟 Windows

1. Clone or download the repository:
   ```cmd
   git clone https://github.com/pdnczone/open-antigravity-patcher.git
   cd open-antigravity-patcher
   ```
2. Double-click `run.bat` or run in Command Prompt / PowerShell:
   ```cmd
   run.bat
   ```

*Requires Python 3.8+ installed and added to PATH.*

---

## 📦 Install as Python CLI

You can install the package directly into your current Python environment:

```bash
pip install .
```

After installation, the CLI command is available anywhere:

```bash
open-antigravity-patcher
```

---

## 📋 Interactive Menu Options

When launched, the patcher scans for installations and displays an interactive menu:

```text
  ╔═══════════════════════════════════════════════╗
  ║  Open AG Patcher                       v1.3.8 ║
  ║  Region bypass for Antigravity                ║
  ╚═══════════════════════════════════════════════╝

  [PATCH]
  1. Antigravity IDE patch          (bypass region lock isGoogleInternal)
  2. Antigravity 2.0 patch          (patch language_server binary)
  3. Antigravity CLI (agy) patch    (unlock agy tool)
  4. Antigravity VS Code Patch      (patch extension.js + agy binary)

  [RESTORE]
  5. Antigravity IDE                (restore from backup)
  6. Antigravity 2.0                (restore from backup)
  7. Antigravity CLI                (restore from backup)
  8. Antigravity VS Code extension  (restore from backup)

  [TOOLS]
  9. Check for updates
  10. Open GitHub repository
  11. Select custom path
  12. About program
  0. Exit
```

---

## 🛠️ Building Standalone Binaries (PyInstaller)

Pre-built binaries can be produced automatically via GitHub Actions or locally with PyInstaller:

### Windows:
```cmd
cd source
pyinstaller --onefile --uac-admin --icon=icon.ico --name="Open_AG_Patcher_Windows" --noupx --clean --version-file=version.txt main.py
```

### Linux:
```bash
cd source
pyinstaller --onefile --icon=icon.ico --name="Open_AG_Patcher_Linux" --hidden-import=packaging --hidden-import=packaging.version --hidden-import=packaging.specifiers --hidden-import=packaging.requirements main.py
```

### macOS (Universal2 / Apple Silicon & Intel):
```bash
cd source
pyinstaller --onefile --name="Open_AG_Patcher_macOS" --target-arch universal2 --hidden-import=packaging --hidden-import=packaging.version --hidden-import=packaging.specifiers --hidden-import=packaging.requirements main.py
```

---

## 🍏 macOS Specific Notes

1. **`[Errno 1] Operation not permitted`**:
   - Grant Full Disk Access to Terminal / iTerm:
     **System Settings → Privacy & Security → Full Disk Access**
   - Clear quarantine attributes:
     ```bash
     sudo xattr -rd com.apple.quarantine "/Applications/Antigravity.app"
     ```

2. **App won't open after patching**:
   - Verify Xcode Command Line Tools are installed:
     ```bash
     xcode-select --install
     ```
   - Re-sign manually:
     ```bash
     codesign --force --deep --sign - "/Applications/Antigravity.app"
     ```

---

## ⚠️ Common API Errors

- **HTTP 400 Bad Request (`User location is not supported`)**:
  - Apply the patch (**PATCH → Option 1 or Option 2**). The patch removes local geographic restrictions.
- **HTTP 403 Forbidden / `SUBSCRIPTION_REQUIRED`**:
  - Account-level licensing limitation from Google API. The patcher modifies local binaries and cannot grant Google subscriptions. Use an account with official access or switch Google account region.
- **HTTP 429 Too Many Requests (`RESOURCE_EXHAUSTED`)**:
  - Request quota exceeded. Wait for quota reset or reset local conversation tokens.

---

## 📂 Project Structure

```text
├── .github/workflows/
│   └── build-and-release.yml   # Multi-platform CI/CD (Windows, macOS, Linux)
├── source/
│   ├── main.py                 # Core CLI entry point
│   ├── requirements.txt        # Python dependencies
│   ├── icon.ico                # App icon
│   └── patcher/
│       ├── cli.py              # Interactive console interface
│       ├── constants.py        # Signatures, versions & regex
│       ├── ide/                # Antigravity IDE patch logic (main.js)
│       ├── manager/            # Antigravity 2.0 language_server binary patch
│       ├── agy/                # Antigravity CLI binary patch
│       ├── vscode/             # VS Code extension patch
│       └── utils/              # OS elevation, console colors, hashing, backup
├── main.py                     # Root executable script
├── run.sh                      # Universal launcher for macOS & Linux
├── run.bat                     # Universal launcher for Windows
├── pyproject.toml              # Modern Python packaging configuration
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📜 License & Attribution

Distributed under the **GNU General Public License v3.0** (GPL-3.0). See [LICENSE](./LICENSE) for details.
Part of the patch logic incorporates research from [eligibility-antigravity-patcher](https://github.com/QNIX-Dev/eligibility-antigravity-patcher) (MIT).
