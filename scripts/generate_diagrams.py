#!/usr/bin/env python3
"""
Simple diagram generator that uses shell=True to avoid PATH issues
"""

import os
import subprocess
import tempfile

def generate_diagram(mmd_content, output_file):
    """Generate a PNG diagram from Mermaid content."""
    # Create a temporary file for the diagram
    with tempfile.NamedTemporaryFile(mode='w', suffix='.mmd', delete=False, encoding='utf-8') as temp:
        temp.write(mmd_content)
        temp_path = temp.name
    
    try:
        # Use shell=True to avoid PATH issues and increase width to 1200px for better readability
        cmd = f'npx @mermaid-js/mermaid-cli -i "{temp_path}" -o "{output_file}" -b transparent -w 1200'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"Generated: {output_file}")
        else:
            print(f"Error generating {output_file}: {result.stderr}")
            
    except Exception as e:
        print(f"Exception generating {output_file}: {e}")
    finally:
        # Clean up the temporary file
        os.unlink(temp_path)

def main():
    """Generate all required diagrams."""
    # Create images directory in the output folder
    os.makedirs('../output/images', exist_ok=True)
    
    # Define the diagrams to generate
    diagrams = {
        'migration_lifecycle': '''
graph TD
    A[Pre-Sales Discovery] --> B[Detailed Design & Planning]
    B --> C[Build & Configure]
    C --> D[QA & Validation]
    D --> E[Go-Live & Handoff]
    
    B --> F[Dependency Review]
    C --> G[Dependency Review]
    D --> H[Dependency Review]
    
    style A fill:#e1f5fe
    style E fill:#c8e6c9
    style F fill:#fff3e0
    style G fill:#fff3e0
    style H fill:#fff3e0
''',
        'pre_sales_discovery': '''
mindmap
  root((Pre-Sales Discovery))
    Business Context
      Organization Type
      Industry & Size
      Geographic Reach
      Business Processes
      Program Scale
      Development Resources
    Assessment Delivery
      Content Types
      Media Usage
      Exam Classification
      Test Structure
    Technical Environment
      Delivery Method
      Client Technology
      Proctoring
      Test Centers
      Integration
      Hosting
      Development
''',
        'structure_planning': '''
graph TD
    A[Structure Planning] --> B[Module Configuration]
    A --> C[Integration Planning]
    A --> D[Security Planning]
    
    B --> E[Assessment Configuration]
    B --> F[Delivery Configuration]
    B --> G[Reporting Configuration]
    
    C --> H[API Integration]
    C --> I[Data Exchange]
    C --> J[Third-party Systems]
    
    D --> K[Authentication]
    D --> L[Authorization]
    D --> M[Data Protection]
    
    style A fill:#e3f2fd
    style E fill:#f3e5f5
    style F fill:#f3e5f5
    style G fill:#f3e5f5
''',
        'dependency_review': '''
graph TD
    A[Dependency Review] --> B[Module Dependencies]
    A --> C[Integration Dependencies]
    A --> D[Data Dependencies]
    
    B --> E[Assessment ↔ Delivery]
    B --> F[Delivery ↔ Reporting]
    B --> G[Assessment ↔ Reporting]
    
    C --> H[API Dependencies]
    C --> I[Data Flow Dependencies]
    C --> J[Security Dependencies]
    
    D --> K[Content Dependencies]
    D --> L[User Dependencies]
    D --> M[Configuration Dependencies]
    
    style A fill:#fff8e1
    style E fill:#e8f5e8
    style F fill:#e8f5e8
    style G fill:#e8f5e8
''',
        'module_relationships': '''
graph TD
    A[Surpass Platform] --> B[Assessment Module]
    A --> C[Delivery Module]
    A --> D[Reporting Module]
    A --> E[Administration Module]
    
    B --> F[Item Management]
    B --> G[Test Construction]
    B --> H[Content Management]
    
    C --> I[Test Delivery]
    C --> J[Proctoring]
    C --> K[Results Collection]
    
    D --> L[Analytics]
    D --> M[Reports]
    D --> N[Data Export]
    
    E --> O[User Management]
    E --> P[System Configuration]
    E --> Q[Security Settings]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#f3e5f5
    style D fill:#f3e5f5
    style E fill:#f3e5f5
''',
        'cli_workflow': '''
graph TD
    A[CLI Workflow] --> B[Configuration Check]
    A --> C[Dependency Validation]
    A --> D[Migration Execution]
    
    B --> E[Module Status]
    B --> F[Integration Status]
    B --> G[Security Status]
    
    C --> H[Dependency Graph]
    C --> I[Conflict Detection]
    C --> J[Resolution Planning]
    
    D --> K[Data Migration]
    D --> L[Configuration Migration]
    D --> M[Validation Checks]
    
    style A fill:#e8f5e8
    style E fill:#fff3e0
    style F fill:#fff3e0
    style G fill:#fff3e0
''',
        'data_flow': '''
graph LR
    A[Source System] --> B[Data Extraction]
    B --> C[Data Transformation]
    C --> D[Data Validation]
    D --> E[Data Loading]
    E --> F[Target System]
    
    B --> G[Content Data]
    B --> H[User Data]
    B --> I[Configuration Data]
    
    C --> J[Format Conversion]
    C --> K[Data Mapping]
    C --> L[Data Cleansing]
    
    D --> M[Integrity Checks]
    D --> N[Business Rules]
    D --> O[Quality Validation]
    
    style A fill:#e1f5fe
    style F fill:#c8e6c9
    style G fill:#f3e5f5
    style H fill:#f3e5f5
    style I fill:#f3e5f5
''',
        'project_timeline': '''
gantt
    title Surpass Migration Project Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Discovery & Architecture    :done, p1, 2024-01-01, 2024-01-15
    section Phase 2
    Detailed Design & Planning  :active, p2, 2024-01-16, 2024-02-15
    section Phase 3
    Build & Configure          :p3, 2024-02-16, 2024-04-15
    section Phase 4
    QA & Validation            :p4, 2024-04-16, 2024-05-15
    section Phase 5
    Go-Live & Handoff          :p5, 2024-05-16, 2024-06-15
'''
    }
    
    # Generate each diagram
    for name, content in diagrams.items():
        output_file = f'../output/images/{name}.png'
        generate_diagram(content, output_file)
    
    print("\nDiagram generation complete!")

if __name__ == "__main__":
    main() 