#!/usr/bin/env python3
"""
Mermaid Diagram Exporter for Surpass Migration Framework

This script extracts Mermaid diagrams from the markdown file and exports them as PNG images.
It requires the mermaid-cli (mmdc) to be installed:
npm install -g @mermaid-js/mermaid-cli

Usage:
python export_diagrams.py
"""

import os
import re
import subprocess
import tempfile
import sys

# Configuration
SOURCE_FILE = 'surpass_migration_framework_enhanced_v2.md'
OUTPUT_DIR = 'images'
DIAGRAM_NAMES = {
    0: 'migration_lifecycle',
    1: 'pre_sales_discovery',
    2: 'structure_planning',
    3: 'dependency_review',
    4: 'module_relationships',
    5: 'cli_workflow',
    6: 'data_flow',
    7: 'project_timeline'
}

def check_mmdc_installed():
    """Check if mermaid-cli is installed."""
    try:
        subprocess.run(['mmdc', '--version'], 
                      stdout=subprocess.PIPE, 
                      stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def extract_mermaid_diagrams(markdown_file):
    """Extract Mermaid diagrams from markdown file."""
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Find all Mermaid diagrams
    pattern = r'```mermaid\n(.*?)```'
    diagrams = re.findall(pattern, content, re.DOTALL)
    
    return diagrams

def export_diagram(diagram_content, output_file):
    """Export a Mermaid diagram to PNG."""
    # Create a temporary file for the diagram
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False) as temp:
        temp.write(diagram_content)
        temp_path = temp.name
    
    try:
        # Run mmdc to convert the diagram to PNG
        subprocess.run([
            'mmdc',
            '-i', temp_path,
            '-o', output_file,
            '-b', 'transparent',
            '-w', '800'
        ], check=True)
        print(f"Exported: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error exporting diagram: {e}")
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def main():
    """Main function to extract and export diagrams."""
    if not check_mmdc_installed():
        print("Error: mermaid-cli is not installed.")
        print("Please install it using: npm install -g @mermaid-js/mermaid-cli")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Extract diagrams
    diagrams = extract_mermaid_diagrams(SOURCE_FILE)
    print(f"Found {len(diagrams)} Mermaid diagrams")
    
    # Export each diagram
    for i, diagram in enumerate(diagrams):
        name = DIAGRAM_NAMES.get(i, f'diagram_{i}')
        output_file = os.path.join(OUTPUT_DIR, f"{name}.png")
        export_diagram(diagram, output_file)
    
    print(f"\nExport complete. {len(diagrams)} diagrams exported to {OUTPUT_DIR}/")
    print("You can now use the export-friendly markdown file for PDF/HTML export.")

if __name__ == "__main__":
    main()
