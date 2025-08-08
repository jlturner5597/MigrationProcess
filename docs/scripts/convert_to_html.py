#!/usr/bin/env python3
"""
Simple script to convert markdown to HTML with Mermaid diagram support
"""

import os
import markdown
import re

def convert_markdown_to_html(input_file, output_file):
    """Convert markdown to HTML with Mermaid support"""
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown to HTML with additional extensions for lists
        html_content = markdown.markdown(content, extensions=['tables', 'fenced_code', 'extra'])
        
        # Extract the style tag content
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        style_content = style_match.group(1) if style_match else ""
        
        # Replace Markdown code blocks with proper Mermaid divs
        html_content = re.sub(
            r'<pre><code class="language-mermaid">(.*?)</code></pre>',
            r'<div class="mermaid">\1</div>',
            html_content,
            flags=re.DOTALL
        )
        
        # Create complete HTML document with Mermaid support
        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surpass Migration Framework: Executive Summary</title>
    <style>
{style_content}
    </style>
    <!-- Include Mermaid -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            mermaid.initialize({{
                startOnLoad: true,
                theme: 'default',
                flowchart: {{
                    useMaxWidth: true,
                    htmlLabels: true,
                    curve: 'linear'
                }}
            }});
        }});
    </script>
</head>
<body>
{html_content}
</body>
</html>"""
        
        # Write to HTML file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_doc)
        
        print(f"HTML file created: {output_file}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 2:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    else:
        input_file = "surpass_migration_framework_simplified.md"
        output_file = "surpass_migration_framework_simplified.html"
    
    if convert_markdown_to_html(input_file, output_file):
        print(f"HTML file created: {output_file}")
        print("Conversion successful!")
    else:
        print("Conversion failed!")