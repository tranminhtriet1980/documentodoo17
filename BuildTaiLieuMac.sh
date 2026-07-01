#!/usr/bin/env bash
# Build site (giu nguyen file .md da sua tay)
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
# shellcheck source=/dev/null
[ -f .venv/bin/activate ] && source .venv/bin/activate
echo "=== Build site ==="
mkdocs build --clean
echo "Xong: file://$ROOT/site/index.html"
