import os


def create_tree(startpath):
    tree = []
    for root, dirs, files in os.walk(startpath):
        if '.git' in dirs:
            dirs.remove('.git')  # Exclude .git directory
        if '.venv' in dirs:
            dirs.remove('.venv')  # Exclude .venv directory
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree.append(f"{subindent}{f}")
    return "\n".join(tree)


# Path to the Django project
project_path = 'H:/dernSol'

# Create the directory tree
directory_tree = create_tree(project_path)

# Paths to save the tree
text_output_path = 'H:/dernSol/01_Archiv_dernSol/tree_dernSol.txt'
html_output_path = 'H:/dernSol/01_Archiv_dernSol/tree_dernSol.html'

# Save the tree to a text file
with open(text_output_path, 'w') as text_file:
    text_file.write(directory_tree)

# Save the tree to an HTML file
html_content = f"<html><body><pre>{directory_tree}</pre></body></html>"
with open(html_output_path, 'w') as html_file:
    html_file.write(html_content)

print(f"Directory tree saved to {text_output_path} and {html_output_path}")
