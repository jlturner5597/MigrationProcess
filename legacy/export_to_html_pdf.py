#!/usr/bin/env python3
"""
Export the Surpass Migration Framework to HTML and PDF formats.
Uses Python libraries to avoid dependency on external tools like Pandoc.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

def convert_markdown_to_html(markdown_file, output_html):
    """Convert markdown to HTML using Python markdown library."""
    try:
        import markdown
        from markdown.extensions import toc, tables, fenced_code
        
        # Read the markdown file
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Configure markdown extensions
        extensions = [
            'toc',
            'tables', 
            'fenced_code',
            'codehilite',
            'nl2br'
        ]
        
        # Convert to HTML
        html_content = markdown.markdown(content, extensions=extensions)
        
        # Create a complete HTML document
        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surpass Migration Framework</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #2c3e50;
            margin-top: 2em;
            margin-bottom: 1em;
        }}
        h1 {{
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 8px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px 12px;
            text-align: left;
        }}
        th {{
            background-color: #f8f9fa;
            font-weight: bold;
        }}
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 20px auto;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        code {{
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
        pre {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }}
        blockquote {{
            border-left: 4px solid #3498db;
            margin: 1em 0;
            padding-left: 1em;
            color: #666;
        }}
        .page-break {{
            page-break-after: always;
        }}
        @media print {{
            .page-break {{
                page-break-after: always;
            }}
            body {{
                font-size: 12pt;
            }}
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Write the HTML file
        with open(output_html, 'w', encoding='utf-8') as f:
            f.write(html_doc)
        
        print(f"HTML exported to: {output_html}")
        return True
        
    except ImportError:
        print("Error: markdown library not installed.")
        print("Install it using: pip install markdown")
        return False
    except Exception as e:
        print(f"Error converting to HTML: {e}")
        return False

def convert_html_to_pdf(html_file, output_pdf):
    """Convert HTML to PDF using weasyprint or similar."""
    try:
        import weasyprint
        
        # Convert HTML to PDF
        weasyprint.HTML(filename=html_file).write_pdf(output_pdf)
        print(f"PDF exported to: {output_pdf}")
        return True
        
    except ImportError:
        print("Error: weasyprint library not installed.")
        print("Install it using: pip install weasyprint")
        return False
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def install_required_packages():
    """Install required Python packages."""
    packages = ['markdown', 'weasyprint']
    
    for package in packages:
        try:
            __import__(package)
            print(f"[OK] {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"[OK] {package} installed successfully")

def main():
    """Main function to export the documentation."""
    print("Surpass Migration Framework - Export Tool")
    print("=" * 50)
    
    # Check if the export-friendly markdown exists
    markdown_file = 'surpass_migration_framework_export_friendly.md'
    if not os.path.exists(markdown_file):
        print(f"Error: {markdown_file} not found!")
        return
    
    # Check if images directory exists
    if not os.path.exists('images'):
        print("Error: images directory not found!")
        print("Please run the diagram generation script first.")
        return
    
    # Install required packages
    print("\nChecking and installing required packages...")
    install_required_packages()
    
    # Export to HTML
    print("\nExporting to HTML...")
    html_file = 'surpass_migration_framework_export_friendly.html'
    if convert_markdown_to_html(markdown_file, html_file):
        print("✓ HTML export completed")
    else:
        print("✗ HTML export failed")
        return
    
    # Export to PDF
    print("\nExporting to PDF...")
    pdf_file = 'surpass_migration_framework_export_friendly.pdf'
    if convert_html_to_pdf(html_file, pdf_file):
        print("✓ PDF export completed")
    else:
        print("✗ PDF export failed")
        print("Note: PDF generation requires weasyprint. You can still use the HTML file.")
    
    print("\nExport process completed!")
    print(f"Files created:")
    print(f"  - {html_file}")
    if os.path.exists(pdf_file):
        print(f"  - {pdf_file}")

if __name__ == "__main__":
    main() 