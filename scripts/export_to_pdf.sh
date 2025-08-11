#!/bin/bash

echo "Surpass Migration Framework - PDF Export Tool"
echo "============================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH."
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

# Check if Pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo "Warning: Pandoc is not installed or not in PATH."
    echo "For best results, install Pandoc from https://pandoc.org/installing.html"
    echo
    echo "Continuing without Pandoc..."
    echo
fi

# Check if mermaid-cli is installed
if ! command -v mmdc &> /dev/null; then
    echo "Warning: mermaid-cli is not installed or not in PATH."
    echo "To export diagrams, install mermaid-cli using:"
    echo "npm install -g @mermaid-js/mermaid-cli"
    echo
    echo "Continuing without diagram export..."
    echo
else
    echo "Exporting diagrams to images..."
    python3 export_diagrams.py
    echo
fi

# Export to PDF if Pandoc is available
if command -v pandoc &> /dev/null; then
    echo "Exporting to PDF using Pandoc..."
    pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.pdf --pdf-engine=wkhtmltopdf
    echo
    echo "PDF export complete: surpass_migration_framework.pdf"
else
    echo "Skipping PDF export - Pandoc not available."
fi

# Export to HTML if Pandoc is available
if command -v pandoc &> /dev/null; then
    echo "Exporting to HTML using Pandoc..."
    pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.html
    echo
    echo "HTML export complete: surpass_migration_framework.html"
else
    echo "Skipping HTML export - Pandoc not available."
fi

echo
echo "Export process completed."
echo "See README_EXPORT.md for more export options."
