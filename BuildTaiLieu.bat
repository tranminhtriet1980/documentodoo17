@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Build site (giu nguyen file .md da sua tay)...
REM Chi tao lai .md tu PowerPoint khi chay TrichAnhTuPptx.bat / TrichAnhTuPptxDuAn.bat
mkdocs build --clean
if errorlevel 1 (
    echo Build that bai.
    pause
    exit /b 1
)
echo Xong. Mo MoTaiLieu.bat hoac site\ke-toan\quy-trinh-hinh-anh.html
pause
