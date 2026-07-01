@echo off
chcp 65001 >nul
cd /d "%~dp0\.."

echo === Cap nhat tai lieu Odoo 17 tren server ===
echo Thu muc: %CD%
echo.

if not exist ".git" (
    echo LOI: Thu muc nay chua phai git repo.
    echo Chay lan dau:
    echo   cd C:\Docker
    echo   ren docs docs-cu
    echo   git clone https://github.com/tranminhtriet1980/documentodoo17.git docs
    echo   cd docs
    echo   scripts\CapNhatTrenServer.bat
    pause
    exit /b 1
)

echo [1/4] Pull tu GitHub...
git pull --ff-only
if errorlevel 1 (
    echo Loi git pull. Kiem tra mang / quyen truy cap GitHub.
    pause
    exit /b 1
)

if not exist "config\htpasswd" (
    echo Tao config\htpasswd...
    py -3 scripts\generate_htpasswd.py -p Edupath2026!
)

echo [2/4] Dung container cu...
docker compose down

echo [3/4] Build lai image (MkDocs build ben trong Docker)...
docker compose build --no-cache
if errorlevel 1 (
    echo Loi build. Kiem tra Docker Desktop / docker dang chay.
    pause
    exit /b 1
)

echo [4/4] Khoi dong container...
docker compose up -d

echo.
echo Xong. Mo: http://127.0.0.1:4546/
echo Neu van thay noi dung cu: Ctrl+F5 ho hoac cache trinh duyet.
pause
