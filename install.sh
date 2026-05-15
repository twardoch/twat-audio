#!/usr/bin/env bash
# install.sh — Install twat-audio locally
# Audio processing plugin for TWAT
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "Installing twat-audio..."
uv pip install -e . 2>/dev/null || pip install -e .
echo "Done."
