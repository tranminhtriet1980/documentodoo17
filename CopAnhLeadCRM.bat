@echo off
chcp 65001 >nul
cd /d "%~dp0"

set "SRC=%~dp0CRM VAN\images\04-lead-process"
set "DST=%~dp0docs\ban-hang\crm\images\lead-process"

echo === Copy anh Chương II Leads ===
echo Nguon: %SRC%
echo Dich:  %DST%
echo.

if not exist "%SRC%" (
    echo LOI: Chua co thu muc nguon.
    echo Hay copy anh vao: CRM VAN\images\04-lead-process\
    echo Hoac chi duong dan nguon:
    echo   CopAnhLeadCRM.bat "D:\duong\dan\04-lead-process"
    pause
    exit /b 1
)

if "%~1" neq "" set "SRC=%~1"

if not exist "%DST%" mkdir "%DST%"

xcopy /Y /I "%SRC%\*.*" "%DST%\"
if errorlevel 1 (
    echo Loi copy file.
    pause
    exit /b 1
)

echo.
py -3 "%~dp0scripts\check_lead_images.py" 2>nul
if errorlevel 1 (
    python "%~dp0scripts\check_lead_images.py" 2>nul
)
if errorlevel 1 (
    echo.
    echo Canh bao: chua du 31 anh. Kiem tra ten file trong manifest.txt
)

echo.
echo Xong. Chay tiep: mkdocs build --clean
pause
