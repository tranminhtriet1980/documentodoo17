@echo off
chcp 65001 >nul
cd /d "%~dp0"

set "DEST=%~1"
if "%DEST%"=="" set "DEST=C:\Docker\docs"

if not exist "site\index.html" (
    echo Chua co site\ — chay BuildTaiLieu.bat...
    call BuildTaiLieu.bat
    if errorlevel 1 exit /b 1
)

echo Dong goi Docker deploy vao: %DEST%
if not exist "%DEST%" mkdir "%DEST%"

copy /Y "Dockerfile" "%DEST%\"
copy /Y "docker-compose.yml" "%DEST%\"
copy /Y "nginx.conf" "%DEST%\"
if not exist "%DEST%\config" mkdir "%DEST%\config"
if exist "config\htpasswd" copy /Y "config\htpasswd" "%DEST%\config\"
copy /Y ".dockerignore" "%DEST%\" 2>nul
copy /Y "ChayDocker.bat" "%DEST%\" 2>nul
copy /Y "DungDocker.bat" "%DEST%\" 2>nul

echo Copy thu muc site (co the mat vai phut)...
if exist "%DEST%\site" rmdir /S /Q "%DEST%\site"
xcopy /E /I /Y "site" "%DEST%\site"

echo.
echo Xong. Tren may Docker chay:
echo   cd /d %DEST%
echo   docker compose build
echo   docker compose up -d
echo.
pause
