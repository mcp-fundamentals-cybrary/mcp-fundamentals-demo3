#!/usr/bin/env bash
# Demo 3 setup -- run this ONCE before the demo.
# Creates a local Python virtual environment (.venv) and installs the two
# things the demo needs: the MCP Python SDK (to run the notes server) and
# mcpo (the bridge that lets Open WebUI talk to the server over HTTP).
#
#   bash setup.sh
#
# Works on Linux, macOS, and WSL. Do NOT run with sudo.

set -euo pipefail
cd "$(dirname "$0")"

echo "[setup] checking prerequisites ..."
command -v python3 >/dev/null || { echo "ERROR: python3 not found. Install Python 3 and try again."; exit 1; }
echo "[setup] python: $(python3 --version)"

echo "[setup] creating virtual environment (.venv) ..."
python3 -m venv .venv

echo "[setup] installing the MCP Python SDK and mcpo ..."
./.venv/bin/pip install --upgrade pip >/dev/null
./.venv/bin/pip install "mcp" "mcpo"

chmod +x ./*.sh 2>/dev/null || true

echo
echo "[setup] done."
echo "[setup] start the demo with:   bash start_demo3.sh"
