#!/usr/bin/env bash
# Demo 3: serve your notes MCP server to Open WebUI through mcpo (the bridge
# that turns an MCP server into an ordinary web API Open WebUI can connect to).
#
#   bash start_demo3.sh          # serves on port 8000
#   bash start_demo3.sh 9000     # or pick your own port
#
# Once it is running, add the server in Open WebUI:
#   Settings -> Tools -> Add Connection -> type OpenAPI -> URL http://localhost:8000
# Browse the live tool docs at http://localhost:8000/docs
# Press Ctrl-C to stop.

set -euo pipefail
cd "$(dirname "$0")"

# Make sure setup.sh has been run.
if [ ! -x "./.venv/bin/mcpo" ]; then
  echo "ERROR: the virtual environment is not set up yet."
  echo "Run this first:   bash setup.sh"
  exit 1
fi

PORT="${1:-8000}"
echo "[demo3] serving notes_server.py through mcpo on http://localhost:${PORT}"
echo "[demo3] live tool docs: http://localhost:${PORT}/docs   (Ctrl-C to stop)"
exec ./.venv/bin/mcpo --port "${PORT}" -- ./.venv/bin/python notes_server.py
