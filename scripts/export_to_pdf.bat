@echo off
echo Surpass Migration Framework - PDF Export Tool
echo ============================================
echo.

REM Check if Python is installed
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    goto :EOF
)

REM Check if Pandoc is installed
where pandoc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Warning: Pandoc is not installed or not in PATH.
    echo For best results, install Pandoc from https://pandoc.org/installing.html
    echo.
    echo Continuing without Pandoc...
    echo.
)

REM Check if mermaid-cli is installed
where mmdc >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Warning: mermaid-cli is not installed or not in PATH.
    echo To export diagrams, install mermaid-cli using:
    echo npm install -g @mermaid-js/mermaid-cli
    echo.
    echo Continuing without diagram export...
    echo.
) else (
    echo Exporting diagrams to images...
    python export_diagrams.py
    echo.
)

REM Export to PDF if Pandoc is available
where pandoc >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Exporting to PDF using Pandoc...
    pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.pdf --pdf-engine=wkhtmltopdf
    echo.
    echo PDF export complete: surpass_migration_framework.pdf
) else (
    echo Skipping PDF export - Pandoc not available.
)

REM Export to HTML if Pandoc is available
where pandoc >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Exporting to HTML using Pandoc...
    pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.html
    echo.
    echo HTML export complete: surpass_migration_framework.html
) else (
    echo Skipping HTML export - Pandoc not available.
)

echo.
echo Export process completed.
echo See README_EXPORT.md for more export options.
pause
