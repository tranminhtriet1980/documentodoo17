@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo === Build site (khong ghi de file .md da sua) ===
mkdocs build --clean
if errorlevel 1 goto err

echo.
echo === Dong server cu tren port 8000 (neu con) ===
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\kill_port.ps1" -Port 8000
timeout /t 2 /nobreak >nul

echo.
echo === Mo web tu thu muc site (co dang nhap muc Ky thuat) ===
echo URL: http://127.0.0.1:8000/index.html
echo Muc /technical/ — tai khoan mac dinh: technical (xem config\htpasswd, doi bang scripts\generate_htpasswd.py)
echo Ctrl+C trong cua so nay de tat server.
echo.

REM Mo trinh duyet sau ~2 giay — server chay o foreground ben duoi
start "" cmd /c "timeout /t 2 /nobreak >nul && start http://127.0.0.1:8000/index.html?v=build"
py -3 "%~dp0scripts\serve_docs.py" --port 8000 --bind 127.0.0.1
goto end

:err
echo Loi build. Kiem tra: pip install mkdocs mkdocs-material
pause
exit /b 1

:end
