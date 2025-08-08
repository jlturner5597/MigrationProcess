#!/usr/bin/env python3
"""
Script to convert markdown to HTML with pre-rendered SVG diagrams
"""

import os
import markdown
import re
import subprocess
import tempfile
import base64

def render_mermaid_to_svg(mermaid_code):
    """Render Mermaid code to SVG using mmdc CLI if available, otherwise return None"""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False, encoding='utf-8') as temp_in:
            temp_in.write(mermaid_code)
            temp_in_path = temp_in.name
        
        temp_out_path = temp_in_path + '.svg'
        
        # Try using npx to run mmdc
        try:
            cmd = f'npx @mermaid-js/mermaid-cli -i "{temp_in_path}" -o "{temp_out_path}"'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0 and os.path.exists(temp_out_path):
                with open(temp_out_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                os.unlink(temp_out_path)
                os.unlink(temp_in_path)
                return svg_content
        except Exception as e:
            print(f"Failed to render with mmdc: {e}")
        
        # If mmdc fails, return None
        if os.path.exists(temp_in_path):
            os.unlink(temp_in_path)
        if os.path.exists(temp_out_path):
            os.unlink(temp_out_path)
        return None
    except Exception as e:
        print(f"Error rendering Mermaid: {e}")
        return None

def convert_markdown_to_html(input_file, output_file):
    """Convert markdown to HTML with pre-rendered SVG diagrams"""
    try:
        # Read the markdown file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract the style tag content
        style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
        style_content = style_match.group(1) if style_match else ""
        
        # Find all Mermaid code blocks
        mermaid_blocks = re.findall(r'```mermaid\n(.*?)\n```', content, re.DOTALL)
        
        # Replace Mermaid blocks with SVG if possible
        for i, mermaid_code in enumerate(mermaid_blocks):
            svg_content = render_mermaid_to_svg(mermaid_code)
            if svg_content:
                # Replace the Mermaid block with SVG
                content = content.replace(f"```mermaid\n{mermaid_code}\n```", 
                                         f'<div class="mermaid-svg">{svg_content}</div>')
        
        # Convert markdown to HTML
        html_content = markdown.markdown(content, extensions=['tables', 'fenced_code'])
        
        # Create complete HTML document
        html_doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surpass Migration Framework: The Simple Guide</title>
    <style>
{style_content}
    .mermaid-svg {{
        display: block;
        margin: 20px auto;
        max-width: 100%;
        overflow-x: auto;
    }}
    </style>
    <!-- Include Mermaid as fallback -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@8.14.0/dist/mermaid.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            mermaid.initialize({{
                startOnLoad: true,
                theme: 'default'
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
    input_file = "surpass_migration_framework_simplified.md"
    output_file = "surpass_migration_framework_simplified.html"
    
    if convert_markdown_to_html(input_file, output_file):
        print("Conversion successful!")
    else:
        print("Conversion failed!")