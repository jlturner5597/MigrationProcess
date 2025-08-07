#!/usr/bin/env python3
"""
PDF export for Surpass Migration Framework
Uses pdfkit (wkhtmltopdf) to convert HTML to PDF
"""

import os
import sys
import subprocess

def install_pdfkit():
    """Install pdfkit if needed."""
    try:
        import pdfkit
        print("[OK] pdfkit is already installed")
        return True
    except ImportError:
        print("Installing pdfkit...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pdfkit'])
            print("[OK] pdfkit installed successfully")
            return True
        except Exception as e:
            print(f"Error installing pdfkit: {e}")
            return False

def check_wkhtmltopdf():
    """Check if wkhtmltopdf is installed."""
    try:
        import pdfkit
        # Try to get the wkhtmltopdf version
        config = pdfkit.configuration()
        if config.wkhtmltopdf:
            print(f"[OK] wkhtmltopdf found at: {config.wkhtmltopdf}")
            return True
    except Exception:
        pass
    
    print("wkhtmltopdf not found or not properly configured.")
    print("Please install wkhtmltopdf from: https://wkhtmltopdf.org/downloads.html")
    print("After installation, you may need to restart your computer.")
    return False

def convert_html_to_pdf(html_file, pdf_file):
    """Convert HTML to PDF using pdfkit."""
    try:
        import pdfkit
        
        # Define options for PDF generation
        options = {
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'encoding': 'UTF-8',
            'enable-local-file-access': True,
            'print-media-type': True,
            'quiet': True
        }
        
        # Convert HTML to PDF
        pdfkit.from_file(html_file, pdf_file, options=options)
        
        print(f"PDF exported to: {pdf_file}")
        return True
    except Exception as e:
        print(f"Error converting to PDF: {e}")
        return False

def main():
    """Main function to export HTML to PDF."""
    print("Surpass Migration Framework - PDF Export")
    print("=" * 50)
    
    # Check if HTML file exists
    html_file = '../output/surpass_migration_framework_export_friendly.html'
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found!")
        print("Please run the HTML export first.")
        return
    
    # Install required packages
    print("\nChecking and installing required packages...")
    if not install_pdfkit():
        print("Failed to install required packages.")
        return
    
    # Check if wkhtmltopdf is installed
    if not check_wkhtmltopdf():
        print("\nAlternative PDF export option:")
        print("1. Open the HTML file in a web browser")
        print("2. Use the browser's print function (Ctrl+P)")
        print("3. Select 'Save as PDF' as the destination")
        return
    
    # Export to PDF
    print("\nExporting to PDF...")
    pdf_file = '../output/surpass_migration_framework_export_friendly.pdf'
    if convert_html_to_pdf(html_file, pdf_file):
        print("[OK] PDF export completed")
        
        # Get file size
        file_size = os.path.getsize(pdf_file)
        print(f"PDF file size: {file_size:,} bytes")
        
        print("\nExport process completed!")
        print(f"PDF file created: {pdf_file}")
    else:
        print("PDF export failed")
        print("\nAlternative PDF export option:")
        print("1. Open the HTML file in a web browser")
        print("2. Use the browser's print function (Ctrl+P)")
        print("3. Select 'Save as PDF' as the destination")

if __name__ == "__main__":
    main()