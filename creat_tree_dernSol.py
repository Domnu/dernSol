import os


def list_files(startpath):
    tree = []
    for root, dirs, files in os.walk(startpath):
        # Exclure les répertoires .venv et .git
        dirs[:] = [d for d in dirs if d not in ['.venv', '.git']]
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree.append(f"{subindent}{f}")
    return tree


def save_to_txt(tree, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        for line in tree:
            f.write(f"{line}\n")


def save_to_html(tree, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('<html><body><pre>\n')
        for line in tree:
            f.write(f"{line}\n")
        f.write('</pre></body></html>\n')


project_path = r"H:\dernSol"
output_txt = r"H:\dernSol\01_Archiv_dernSol\tree_dernSol.txt"
output_html = r"H:\dernSol\01_Archiv_dernSol\tree_dernSol.html"

tree = list_files(project_path)
save_to_txt(tree, output_txt)
save_to_html(tree, output_html)
