#!/usr/bin/env python3
"""
Complete Export Workflow for Surpass Migration Framework
This script handles the entire export process from diagram generation to final outputs.
"""

import os
import subprocess
import sys
from pathlib import Path

def check_prerequisites():
    """Check if all required files and directories exist."""
    print("Checking prerequisites...")
    
    required_files = [
        '../surpass_migration_framework_export_friendly.md',
        'generate_diagrams.py',
        'simple_html_export.py',
        'export_to_pdf.py'
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    print("✓ All required files found")
    return True

def generate_diagrams():
    """Generate all required diagram images."""
    print("\nStep 1: Generating diagram images...")
    
    if not os.path.exists('generate_diagrams.py'):
        print("❌ generate_diagrams.py not found")
        return False
    
    try:
        result = subprocess.run([sys.executable, 'generate_diagrams.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Diagrams generated successfully")
            
            # Check if images directory was created
            if os.path.exists('images'):
                image_files = [f for f in os.listdir('images') if f.endswith('.png')]
                print(f"✓ {len(image_files)} diagram images created")
                return True
            else:
                print("❌ Images directory not created")
                return False
        else:
            print(f"❌ Diagram generation failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error generating diagrams: {e}")
        return False

def export_to_html():
    """Export markdown to HTML."""
    print("\nStep 2: Exporting to HTML...")
    
    if not os.path.exists('simple_html_export.py'):
        print("❌ simple_html_export.py not found")
        return False
    
    try:
        result = subprocess.run([sys.executable, 'simple_html_export.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            if os.path.exists('surpass_migration_framework_export_friendly.html'):
                print("✓ HTML export completed")
                return True
            else:
                print("❌ HTML file not created")
                return False
        else:
            print(f"❌ HTML export failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Error exporting to HTML: {e}")
        return False
        
def export_to_pdf():
    """Export HTML to PDF."""
    print("\nStep 3: Exporting to PDF...")
    
    if not os.path.exists('export_to_pdf.py'):
        print("❌ export_to_pdf.py not found")
        return False
    
    try:
        result = subprocess.run([sys.executable, 'export_to_pdf.py'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            if os.path.exists('surpass_migration_framework_export_friendly.pdf'):
                print("✓ PDF export completed")
                return True
            else:
                print("❌ PDF file not created")
                return False
        else:
            print(f"❌ PDF export failed: {result.stderr}")
            print("Note: You can still use the HTML file and save as PDF from your browser.")
            return False
            
    except Exception as e:
        print(f"❌ Error exporting to PDF: {e}")
        print("Note: You can still use the HTML file and save as PDF from your browser.")
        return False

def create_summary_report():
    """Create a summary report of the export process."""
    print("\nStep 4: Creating summary report...")
    
    summary = []
    summary.append("# Surpass Migration Framework - Export Summary")
    summary.append("")
    summary.append("## Export Process Completed")
    summary.append("")
    summary.append("### Generated Files:")
    summary.append("")
    
    # Check for generated files
    files_to_check = [
        ('../output/surpass_migration_framework_export_friendly.html', 'HTML Export'),
        ('../output/surpass_migration_framework_export_friendly.pdf', 'PDF Export (if available)'),
        ('../output/images/', 'Diagram Images Directory')
    ]
    
    for file_path, description in files_to_check:
        if os.path.exists(file_path):
            if os.path.isdir(file_path):
                files = [f for f in os.listdir(file_path) if f.endswith('.png')]
                summary.append(f"- **{description}**: ✓ {len(files)} diagram images")
            else:
                file_size = os.path.getsize(file_path)
                summary.append(f"- **{description}**: ✓ ({file_size:,} bytes)")
        else:
            summary.append(f"- **{description}**: ❌ Not created")
    
    summary.append("")
    summary.append("### Export-Friendly Features:")
    summary.append("")
    summary.append("- ✅ Pre-rendered diagram images")
    summary.append("- ✅ HTML page breaks for PDF export")
    summary.append("- ✅ Simplified formatting for maximum compatibility")
    summary.append("- ✅ Responsive design for web viewing")
    summary.append("- ✅ Clean typography and styling")
    
    summary.append("")
    summary.append("### Usage Instructions:")
    summary.append("")
    summary.append("1. **HTML Version**: Open `surpass_migration_framework_export_friendly.html` in any web browser")
    summary.append("2. **PDF Export**: Use your browser's print function (Ctrl+P) to save as PDF")
    summary.append("3. **Print Version**: The HTML file is optimized for printing with proper page breaks")
    
    summary.append("")
    summary.append("### Next Steps:")
    summary.append("")
    summary.append("- Review the HTML export for accuracy")
    summary.append("- Test PDF generation using browser print function")
    summary.append("- Share the export-friendly version with stakeholders")
    summary.append("- Use the HTML version for web deployment if needed")
    
    # Write summary to file
    with open('../output/EXPORT_SUMMARY.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary))
    
    print("✓ Summary report created: ../output/EXPORT_SUMMARY.md")
    return True

def main():
    """Main function to run the complete export workflow."""
    print("Surpass Migration Framework - Complete Export Workflow")
    print("=" * 60)
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please ensure all required files exist.")
        return
    
    # Step 1: Generate diagrams
    if not generate_diagrams():
        print("\n❌ Diagram generation failed. Stopping workflow.")
        return
    
    # Step 2: Export to HTML
    if not export_to_html():
        print("\n❌ HTML export failed. Stopping workflow.")
        return
    
    # Step 3: Export to PDF (optional)
    pdf_success = export_to_pdf()
    
    # Step 4: Create summary
    create_summary_report()
    
    print("\n" + "=" * 60)
    print("🎉 EXPORT WORKFLOW COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\nGenerated files:")
    
    files_created = []
    if os.path.exists('../output/surpass_migration_framework_export_friendly.html'):
        size = os.path.getsize('../output/surpass_migration_framework_export_friendly.html')
        files_created.append(f"  📄 output/surpass_migration_framework_export_friendly.html ({size:,} bytes)")
    
    if os.path.exists('../output/images'):
        image_count = len([f for f in os.listdir('../output/images') if f.endswith('.png')])
        files_created.append(f"  🖼️  output/images/ directory ({image_count} diagram images)")
    
    if os.path.exists('../output/EXPORT_SUMMARY.md'):
        files_created.append(f"  📋 output/EXPORT_SUMMARY.md")
    
    for file_info in files_created:
        print(file_info)
    
    print(f"\n📖 You can now review the export-friendly version of your documentation!")
    print(f"🌐 Open output/surpass_migration_framework_export_friendly.html in your browser to view the results.")

if __name__ == "__main__":
    main() 