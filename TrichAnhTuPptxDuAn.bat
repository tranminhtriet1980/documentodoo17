@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Trich anh + xu ly tu PowerPoint (Mr Khanh - XLHS)...
py -3 scripts\extract_pptx_du_an.py
if errorlevel 1 goto err
py -3 scripts\build_du_an_docs.py
if errorlevel 1 goto err
echo Xong. Chay BuildTaiLieu.bat hoac mkdocs build
pause
exit /b 0
:err
pause
exit /b 1
