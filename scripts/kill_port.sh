#!/usr/bin/env bash
# Dung port tren Mac: bash scripts/kill_port.sh 8000
PORT="${1:-8000}"
if command -v lsof >/dev/null 2>&1; then
  PIDS=$(lsof -ti ":${PORT}" 2>/dev/null || true)
  if [ -n "$PIDS" ]; then
    echo "Dong process tren port ${PORT}..."
    kill -9 $PIDS 2>/dev/null || true
  fi
fi
