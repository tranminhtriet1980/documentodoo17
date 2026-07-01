@echo off
chcp 65001 >nul
cd /d "%~dp0"
REM Che do dev: mkdocs serve (reload khi sua .md) — chi 1 cua so, dong server cu truoc

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\kill_port.ps1" -Port 8000
timeout /t 2 /nobreak >nul

py -3 scripts\build_quy_trinh_docs.py
echo.
echo Dev server: http://127.0.0.1:8000 — Ctrl+C de tat
timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:8000/ke-toan/quy-trinh-hinh-anh.html"
mkdocs serve -a 127.0.0.1:8000
