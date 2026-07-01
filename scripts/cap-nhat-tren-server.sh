#!/usr/bin/env bash
# Cập nhật tài liệu trên Linux server
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "=== Cap nhat tai lieu Odoo 17 ==="
echo "Thu muc: $ROOT"

if [ ! -d .git ]; then
  echo "LOI: Chua phai git repo. Clone truoc:"
  echo "  git clone https://github.com/tranminhtriet1980/documentodoo17.git /opt/documentodoo17"
  exit 1
fi

git pull --ff-only

if [ ! -f config/htpasswd ]; then
  python3 scripts/generate_htpasswd.py -p "${TECH_PASSWORD:-Edupath2026!}"
fi

docker compose down
docker compose build --no-cache
docker compose up -d

echo "Xong: http://$(hostname -I | awk '{print $1}'):4546/"
