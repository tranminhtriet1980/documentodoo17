@echo off
chcp 65001 >nul
cd /d "%~dp0"

if not exist "site\index.html" (
    echo Chua co thu muc site. Chay BuildTaiLieu.bat truoc...
    call BuildTaiLieu.bat
    if errorlevel 1 exit /b 1
)

echo === Docker: tai lieu Odoo 17 ===
echo HTTP:  http://127.0.0.1:4546/
echo HTTPS: https://127.0.0.1:4547/
echo.

docker compose build
if errorlevel 1 (
    echo Loi: kiem tra Docker Desktop da chay chua.
    pause
    exit /b 1
)

docker compose up -d
if errorlevel 1 (
    pause
    exit /b 1
)

timeout /t 2 /nobreak >nul
start "" "http://127.0.0.1:4546/index.html"
echo.
echo Dang chay. Dung: docker compose down
echo.
pause
