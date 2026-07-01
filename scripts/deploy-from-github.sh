#!/usr/bin/env bash
# Cài đặt lần đầu trên máy Docker — clone từ GitHub và chạy container
set -euo pipefail

REPO_URL="${1:-https://github.com/tranminhtriet1980/documentodoo17.git}"
DEPLOY_DIR="${2:-/opt/documentodoo17}"

echo "=== Clone / cap nhat tu GitHub ==="
if [ -d "$DEPLOY_DIR/.git" ]; then
  git -C "$DEPLOY_DIR" pull --ff-only
else
  git clone "$REPO_URL" "$DEPLOY_DIR"
fi

cd "$DEPLOY_DIR"

if [ ! -f config/htpasswd ]; then
  echo "=== Tao mat khau Ky thuat mac dinh ==="
  python3 scripts/generate_htpasswd.py -p "${TECH_PASSWORD:-Edupath2026!}"
fi

echo "=== Docker build & start ==="
export TECH_PASSWORD="${TECH_PASSWORD:-Edupath2026!}"
docker compose build
docker compose up -d

echo ""
echo "Xong:"
echo "  HTTP:  http://$(hostname -I | awk '{print $1}'):4546/"
echo "  HTTPS: https://$(hostname -I | awk '{print $1}'):4547/"
