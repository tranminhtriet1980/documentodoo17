@echo off
chcp 65001 >nul
cd /d "%~dp0"

set "REPO=https://github.com/tranminhtriet1980/documentodoo17.git"
set "REPO_ROOT=C:\Docker\documentodoo17"
set "DEPLOY_DIR=C:\Docker\documentodoo17"

echo === Dong bo tu GitHub ===
if exist "%REPO_ROOT%\.git" (
    cd /d "%REPO_ROOT%"
    git pull --ff-only
) else (
    if not exist "C:\Docker" mkdir "C:\Docker"
    git clone "%REPO%" "%REPO_ROOT%"
)

cd /d "%DEPLOY_DIR%"
if not exist "docker-compose.yml" (
    echo Loi: chua co docker-compose.yml trong %DEPLOY_DIR%
    pause
    exit /b 1
)

if not exist "config\htpasswd" (
    echo Tao mat khau Ky thuat mac dinh...
    py -3 scripts\generate_htpasswd.py -p Edupath2026!
)

echo === Docker build ^& start ===
docker compose build
if errorlevel 1 exit /b 1
docker compose up -d

echo.
echo HTTP:  http://127.0.0.1:4546/
echo HTTPS: https://127.0.0.1:4547/
pause
