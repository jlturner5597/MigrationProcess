# Surpass Migration Framework - Export Instructions

This document provides instructions for exporting the Surpass Migration Framework documentation to PDF or HTML format with optimal rendering.

## Export Options

### Option 1: Export-Friendly Version (Recommended)

The file `surpass_migration_framework_export_friendly.md` is specifically designed for exporting to PDF/HTML. It uses:

- Standard HTML for page breaks
- Image references instead of Mermaid diagrams
- Simplified formatting for maximum compatibility

#### Steps for Export:

1. **Generate diagram images:**
   - Run the `export_diagrams.py` script to convert all Mermaid diagrams to PNG images
   - This will populate the `images/` directory with all required diagram files

   ```
   python export_diagrams.py
   ```

2. **Export to PDF:**
   - Use a Markdown-to-PDF converter like Pandoc:

   ```
   pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.pdf --pdf-engine=wkhtmltopdf
   ```

   - Or use a Markdown editor with PDF export (VS Code with Markdown PDF extension, Typora, etc.)

3. **Export to HTML:**
   - Use Pandoc for clean HTML:

   ```
   pandoc surpass_migration_framework_export_friendly.md -o surpass_migration_framework.html
   ```

### Option 2: Direct Export of Enhanced Version

If you prefer to export the enhanced version directly:

1. Use a tool that supports Mermaid diagrams rendering, such as:
   - VS Code with Markdown PDF extension (with Mermaid support enabled)
   - Typora (with Mermaid support enabled)
   - Pandoc with a Mermaid filter

2. Command for Pandoc with Mermaid support:
   ```
   pandoc surpass_migration_framework_enhanced_v2.md --filter mermaid-filter -o surpass_migration_framework.pdf
   ```

## Troubleshooting Common Export Issues

### Mermaid Diagrams Not Rendering
- Ensure your export tool supports Mermaid
- Try the export-friendly version with pre-rendered images
- Consider using the mermaid-cli tool to pre-render diagrams

### Page Breaks Not Working
- The export-friendly version uses HTML page breaks (`<div style="page-break-after: always;"></div>`)
- Some tools may require different page break syntax
- Try adding the `--css` option with a custom CSS file that defines page breaks

### Table Formatting Issues
- The export-friendly version uses left-aligned tables for better compatibility
- If tables appear misaligned, try adjusting column widths in the markdown

### Missing Links in Table of Contents
- The export-friendly version uses numbered links for better compatibility
- If links don't work, ensure your export tool supports anchor links

## Recommended Export Tools

- **Pandoc**: Versatile document converter with extensive options
- **Typora**: WYSIWYG Markdown editor with good export capabilities
- **VS Code Extensions**: Markdown PDF, Markdown Preview Enhanced
- **Marked 2** (macOS): Premium Markdown preview and export tool
