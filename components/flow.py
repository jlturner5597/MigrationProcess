import graphviz as gv

# Define the migration process diagram
g = gv.Digraph('SurpassMigration', format='png')
g.attr(rankdir='LR', fontsize='12')

# Nodes
g.node('Discovery', 'Discovery / \nArchitecture Vision\n(Pre‑Sales)')
g.node('Design', 'Detailed Design & Planning\n(Business • Data • Integration)')
g.node('Build', 'Build & Configure\n(Migration Scripts • Test Items)')
g.node('QA', 'QA & Validation\n(Manual + Automated)')
g.node('GoLive', 'Go‑Live & Handoff')
# Iterative dependency review note
g.node('Review', 'Dependency Review Loop', shape='note')

# Edges
g.edge('Discovery', 'Design', label='Kick‑off\nBRD')
g.edge('Design', 'Build', label='Solution\n& Migration\nRunbook')
g.edge('Build', 'QA', label='Data Loads\n& Config')
g.edge('QA', 'GoLive', label='User\nSign‑off')
# Loop
g.edge('Design', 'Review', style='dashed')
g.edge('Build', 'Review', style='dashed')
g.edge('QA', 'Review', style='dashed')
g.edge('Review', 'Design', style='dotted', label='Adjust')

# Render to file
file_path = r'C:\Users\JohnT\GitHub\MigrationProcess\surpass_migration_flow'
output_path = g.render(filename=file_path, cleanup=True)
output_path
