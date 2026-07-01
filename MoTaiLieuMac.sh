#!/usr/bin/env bash
# Build + mo web (tuong tu MoTaiLieu.bat)
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
# shellcheck source=/dev/null
[ -f .venv/bin/activate ] && source .venv/bin/activate

echo "=== Build site ==="
mkdocs build --clean

bash "$ROOT/scripts/kill_port.sh" 8000
sleep 1

URL="http://127.0.0.1:8000/index.html"
echo ""
echo "=== Mo web: $URL ==="
echo "Nhan Ctrl+C de tat server."
echo ""

(sleep 2 && open "$URL" 2>/dev/null) &

python3 "$ROOT/scripts/serve_docs.py" --port 8000 --bind 127.0.0.1
