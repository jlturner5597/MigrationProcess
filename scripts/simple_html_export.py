#!/usr/bin/env python3
"""
Simple HTML export for Surpass Migration Framework
Uses only the markdown library to avoid dependency issues.
"""

import os
import re
import sys

def convert_markdown_to_html_simple(markdown_file, output_html):
    """Convert markdown to HTML using only the markdown library."""
    try:
        import markdown
        
        # Read the markdown file
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Configure markdown extensions
        extensions = [
            'tables', 
            'fenced_code',
            'codehilite',
            'nl2br'
        ]
        
        # Convert to HTML
        html_content = markdown.markdown(content, extensions=extensions)
        
        # Enhance image display by wrapping them in containers
        import re
        img_pattern = r'<img src="([^"]+)" alt="([^"]+)">'
        img_replacement = r'<div class="image-container"><img src="\1" alt="\2"></div>'
        html_content = re.sub(img_pattern, img_replacement, html_content)
        
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
            margin: 30px auto;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        /* Add a container for images to ensure they display properly */
        .image-container {{
            width: 100%;
            overflow-x: auto;
            margin: 20px 0;
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

def install_markdown():
    """Install the markdown library if needed."""
    try:
        import markdown
        print("[OK] markdown library is already installed")
        return True
    except ImportError:
        print("Installing markdown library...")
        try:
            import subprocess
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'markdown'])
            print("[OK] markdown library installed successfully")
            return True
        except Exception as e:
            print(f"Error installing markdown: {e}")
            return False

def main():
    """Main function to export the documentation to HTML."""
    print("Surpass Migration Framework - Simple HTML Export")
    print("=" * 50)
    
    # Check if the export-friendly markdown exists
    markdown_file = '../surpass_migration_framework_export_friendly.md'
    if not os.path.exists(markdown_file):
        print(f"Error: {markdown_file} not found!")
        return
    
    # Check if images directory exists
    if not os.path.exists('../output/images'):
        print("Error: images directory not found!")
        print("Please run the diagram generation script first.")
        return
    
    # Install required packages
    print("\nChecking and installing required packages...")
    if not install_markdown():
        print("Failed to install required packages.")
        return
    
    # Export to HTML
    print("\nExporting to HTML...")
    html_file = '../output/surpass_migration_framework_export_friendly.html'
    if convert_markdown_to_html_simple(markdown_file, html_file):
        print("[OK] HTML export completed")
        
        # Get file size
        file_size = os.path.getsize(html_file)
        print(f"HTML file size: {file_size:,} bytes")
        
        print("\nExport process completed!")
        print(f"HTML file created: {html_file}")
        print("You can open this file in any web browser to view the documentation.")
        print("To create a PDF, use your browser's print function (Ctrl+P) and save as PDF.")
    else:
        print("HTML export failed")

if __name__ == "__main__":
    main() 