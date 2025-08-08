# Surpass Migration Framework

This repository contains the Surpass Migration Framework - a structured yet adaptable approach to assessment platform migrations. Built on real-world implementation experience and TOGAF principles, this framework balances the art and science of migration planning to ensure successful outcomes for diverse customer needs.

## Framework Documentation

The documentation is organized in the `docs` directory:

- [Simplified Guide](docs/surpass_migration_framework_simplified.md) - A straightforward guide to the migration framework for non-technical audiences
- [Executive Summary](docs/surpass_migration_framework_ultra_condensed.md) - Ultra-condensed version focusing on key points and timeline
- [HTML Versions](docs/) - HTML versions of the documents with interactive diagrams

## Directory Structure

- **`/docs`** - Main documentation files and assets
  - **`/docs/assets`** - Images and other assets
  - **`/docs/scripts`** - Scripts for converting Markdown to HTML
  - **`/docs/images`** - Generated diagram images

- **`/output`** - Generated output files from the export process
  - **`/output/images`** - Generated diagram images

- **`/legacy`** - Older scripts and files kept for reference

- **`/scripts`** - Utility scripts for the project

- **`/components`** - Original Mermaid diagram files

## Diagram Files

1. **migration_master_flow.mmd** - High-level overview of the migration process phases
2. **presales_discovery.mmd** - Mind map of pre-sales discovery components
3. **surpass_structure_planning.mmd** - Detailed flow of the structure planning process
4. **dependency_review.mmd** - Class diagram showing the dependency review framework
5. **migration_timeline.mmd** - Gantt chart visualizing the migration timeline
6. **migration_data_flow.mmd** - Data flow diagram from source systems to Surpass
7. **surpass_module_relationships.mmd** - Visualization of Surpass module relationships
8. **migration_cli_workflow.mmd** - Sequence diagram of the interactive CLI workflow

## Viewing the Diagrams

These diagrams are written in Mermaid syntax. To view them:

1. Use a Mermaid-compatible Markdown viewer
2. Use the Mermaid Live Editor at https://mermaid.live/
3. Use VS Code with the Mermaid extension
4. View the HTML versions in the `docs` directory

## Surpass Branding Colors

The diagrams use the following Surpass branding colors:
- Blue (#0078D7) - Discovery phase and structure
- Teal (#00B294) - Design phase and transformation
- Yellow (#FFB900) - Build phase and target systems
- Red (#E81123) - QA phase and administration
- Purple (#68217A) - Go-Live phase and reporting
- Green (#107C10) - Review processes and security