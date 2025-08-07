# Surpass Migration Framework - Export Workflow

This document provides instructions for using the reorganized export workflow for the Surpass Migration Framework documentation.

## Directory Structure

The project has been reorganized for better maintainability:

- **`scripts/`**: Contains all export-related Python scripts
- **`output/`**: Contains all generated files (HTML, PDF, images)
- **`legacy/`**: Contains legacy/unused scripts for reference
- **`components/`**: Contains original Mermaid diagram files
- **`drafts/`**: Contains draft versions of the documentation

## Export Scripts

The following scripts are available in the `scripts/` directory:

1. **`complete_export_workflow.py`**: Main script that runs the entire export process
2. **`generate_diagrams.py`**: Generates diagram images from Mermaid definitions
3. **`simple_html_export.py`**: Converts markdown to HTML with proper styling
4. **`export_to_pdf.py`**: Converts HTML to PDF (requires wkhtmltopdf)

## How to Use

### Option 1: Complete Workflow (Recommended)

Run the complete workflow script to generate all outputs in one go:

```
cd scripts
python complete_export_workflow.py
```

This will:
1. Generate all diagram images with improved readability
2. Export the markdown to HTML with proper styling
3. Convert the HTML to PDF (if wkhtmltopdf is installed)
4. Create a summary report

All output files will be placed in the `output/` directory.

### Option 2: Individual Steps

If you prefer to run the steps individually:

1. **Generate diagrams:**
   ```
   cd scripts
   python generate_diagrams.py
   ```

2. **Export to HTML:**
   ```
   cd scripts
   python simple_html_export.py
   ```

3. **Export to PDF:**
   ```
   cd scripts
   python export_to_pdf.py
   ```

## Output Files

After running the workflow, the following files will be created in the `output/` directory:

- **`surpass_migration_framework_export_friendly.html`**: HTML version of the documentation
- **`surpass_migration_framework_export_friendly.pdf`**: PDF version of the documentation
- **`images/`**: Directory containing all diagram images
- **`EXPORT_SUMMARY.md`**: Summary report of the export process

## Diagram Improvements

The diagrams have been enhanced for better readability:

- Increased width from 800px to 1200px
- Added proper styling and containers in HTML
- Improved visual separation with margins and subtle shadows

## Troubleshooting

### PDF Export Issues

If the PDF export fails:
1. Make sure wkhtmltopdf is installed: https://wkhtmltopdf.org/downloads.html
2. After installation, you may need to restart your computer
3. Alternatively, open the HTML file in a browser and use the print function to save as PDF

### Image Generation Issues

If diagram generation fails:
1. Make sure Node.js and npm are installed
2. Install mermaid-cli: `npm install -g @mermaid-js/mermaid-cli`
3. Restart your terminal/command prompt

## Notes

- The original markdown file (`surpass_migration_framework_export_friendly.md`) remains in the root directory
- Legacy scripts are preserved in the `legacy/` directory for reference
- The workflow is designed to work on Windows, macOS, and Linux