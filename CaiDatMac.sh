#!/usr/bin/env bash
#
# CAI DAT TAI LIEU ODOO 17 TREN MAC (chay 1 lan dau)
#
# Cach 1 — Terminal:
#   cd "/duong/dan/Tai lieu odoo17"
#   bash CaiDatMac.sh
#
# Cach 2 — Double-click (sau khi chmod +x CaiDatMac.sh)
#
set -e

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

echo "=============================================="
echo "  Cai dat Tai lieu Odoo 17 — macOS"
echo "  Thu muc: $ROOT"
echo "=============================================="
echo ""

# --- Python 3 ---
if ! command -v python3 >/dev/null 2>&1; then
  echo "Chua co Python 3."
  echo "Cai bang Homebrew:  brew install python3"
  echo "Hoac tai: https://www.python.org/downloads/macos/"
  exit 1
fi
echo "Python: $(python3 --version)"

# --- Virtual env (cach ly thu vien) ---
if [ ! -d ".venv" ]; then
  echo ""
  echo "Tao moi truong ao .venv ..."
  python3 -m venv .venv
fi
# shellcheck source=/dev/null
source .venv/bin/activate

echo ""
echo "Cai thu vien (mkdocs, mkdocs-material, Pillow)..."
python3 -m pip install --upgrade pip -q
python3 -m pip install -r requirements.txt -q

# --- Quyen chay script phu ---
chmod +x "$ROOT/BuildTaiLieuMac.sh" 2>/dev/null || true
chmod +x "$ROOT/MoTaiLieuMac.sh" 2>/dev/null || true
chmod +x "$ROOT/scripts/kill_port.sh" 2>/dev/null || true

# --- Build site ---
echo ""
echo "Build site lan dau..."
mkdocs build --clean

echo ""
echo "=============================================="
echo "  CAI DAT XONG"
echo "=============================================="
echo ""
echo "  Xem tai lieu:"
echo "    bash MoTaiLieuMac.sh"
echo "    (hoac double-click MoTaiLieuMac.sh)"
echo ""
echo "  Chi build lai (sau khi sua .md):"
echo "    bash BuildTaiLieuMac.sh"
echo ""
echo "  Mo file tinh (khong can server):"
echo "    open site/index.html"
echo ""
echo "  Trich anh tu PowerPoint (khi can):"
echo "    python3 scripts/extract_pptx_images.py"
echo "    python3 scripts/extract_pptx_du_an.py"
echo ""

read -r -p "Mo trinh duyet ngay bay gio? [Y/n] " ans
ans="${ans:-Y}"
if [[ "$ans" =~ ^[Yy]$ ]]; then
  bash "$ROOT/MoTaiLieuMac.sh"
else
  echo "De mo sau: bash MoTaiLieuMac.sh"
fi
