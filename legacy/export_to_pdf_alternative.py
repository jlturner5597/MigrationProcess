#!/usr/bin/env python3
"""
Alternative PDF export using reportlab library.
This works better on Windows systems where weasyprint has dependency issues.
"""

import os
import subprocess
import sys
from pathlib import Path

def convert_html_to_pdf_reportlab(html_file, output_pdf):
    """Convert HTML to PDF using reportlab and html2text."""
    try:
        import html2text
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
        
        # Read HTML file
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Convert HTML to text (simplified approach)
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        text_content = h.handle(html_content)
        
        # Create PDF
        doc = SimpleDocTemplate(output_pdf, pagesize=A4)
        story = []
        
        # Get styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=16,
            spaceAfter=30,
            textColor=colors.darkblue
        )
        heading_style = ParagraphStyle(
            'CustomHeading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=20,
            textColor=colors.darkblue
        )
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=12,
            alignment=TA_JUSTIFY
        )
        
        # Split content into lines and process
        lines = text_content.split('\n')
        current_section = ""
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detect headings
            if line.startswith('# '):
                story.append(Paragraph(line[2:], title_style))
                story.append(Spacer(1, 12))
            elif line.startswith('## '):
                story.append(Paragraph(line[3:], heading_style))
                story.append(Spacer(1, 12))
            elif line.startswith('### '):
                story.append(Paragraph(line[4:], heading_style))
                story.append(Spacer(1, 12))
            elif line.startswith('!['):
                # Handle images
                img_path = line.split('(')[1].split(')')[0] if '(' in line else None
                if img_path and os.path.exists(img_path):
                    try:
                        img = Image(img_path, width=6*inch, height=4*inch)
                        story.append(img)
                        story.append(Spacer(1, 12))
                    except:
                        story.append(Paragraph(f"[Image: {img_path}]", normal_style))
                        story.append(Spacer(1, 12))
            elif line.startswith('|'):
                # Handle tables (simplified)
                story.append(Paragraph(line, normal_style))
                story.append(Spacer(1, 6))
            else:
                # Regular text
                if line:
                    story.append(Paragraph(line, normal_style))
                    story.append(Spacer(1, 6))
        
        # Build PDF
        doc.build(story)
        print(f"PDF exported to: {output_pdf}")
        return True
        
    except ImportError as e:
        print(f"Error: Required library not installed: {e}")
        print("Install required packages: pip install reportlab html2text")
        return False
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def install_required_packages():
    """Install required Python packages."""
    packages = ['reportlab', 'html2text']
    
    for package in packages:
        try:
            __import__(package)
            print(f"✓ {package} is already installed")
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✓ {package} installed successfully")

def main():
    """Main function to export to PDF using alternative method."""
    print("Surpass Migration Framework - Alternative PDF Export")
    print("=" * 55)
    
    # Check if HTML file exists
    html_file = 'surpass_migration_framework_export_friendly.html'
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found!")
        print("Please run the HTML export first.")
        return
    
    # Install required packages
    print("\nChecking and installing required packages...")
    install_required_packages()
    
    # Export to PDF
    print("\nExporting to PDF...")
    pdf_file = 'surpass_migration_framework_export_friendly_alt.pdf'
    if convert_html_to_pdf_reportlab(html_file, pdf_file):
        print("✓ PDF export completed")
    else:
        print("✗ PDF export failed")
    
    print("\nExport process completed!")
    if os.path.exists(pdf_file):
        print(f"PDF file created: {pdf_file}")

if __name__ == "__main__":
    main() 