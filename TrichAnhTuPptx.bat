@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Trich anh tu PowerPoint (MR UT)...
py -3 scripts\extract_pptx_images.py
if errorlevel 1 goto err
REM extract_pptx_images da goi process (bo logo, crop, resize)
py -3 scripts\build_quy_trinh_docs.py
if errorlevel 1 goto err
echo.
echo Xong. Chay BuildTaiLieu.bat de cap nhat site.
pause
exit /b 0
:err
echo Loi. Can Python 3.
pause
exit /b 1
