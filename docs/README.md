# Surpass Migration Framework Documentation

This directory contains the documentation for the Surpass Migration Framework.

## Directory Structure

- **`/`** - Root directory containing the main documentation files
  - `surpass_migration_framework_simplified.md` - Simplified version of the migration framework
  - `surpass_migration_framework_simplified.html` - HTML version of the simplified document
  - `surpass_migration_framework_ultra_condensed.md` - Executive summary version of the migration framework
  - `surpass_migration_framework_ultra_condensed.html` - HTML version of the executive summary

- **`/assets`** - Contains images and other assets used in the documentation
  - `SurpassPA_logo.png` - Surpass logo

- **`/scripts`** - Contains scripts for converting Markdown to HTML
  - `convert_to_html.py` - Main script for converting Markdown to HTML with Mermaid support
  - `convert_to_html_with_svg.py` - Alternative script that attempts to pre-render SVGs
  - `gantt_test.html` - Test file for Gantt chart rendering

- **`/images`** - Directory for storing generated diagram images

## Usage

To convert a Markdown file to HTML:

```bash
python scripts/convert_to_html.py path/to/markdown/file.md path/to/output/file.html
```

## Document Versions

1. **Simplified Version** - A straightforward guide to the Surpass Migration Framework, designed for a non-technical audience.

2. **Ultra-Condensed Version** - An executive summary of the migration framework, focusing on the key points and timeline.