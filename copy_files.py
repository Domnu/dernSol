import os


def copy_files_to_text(base_dir, output_dir, extensions=None):
    if extensions is None:
        extensions = ['.py', '.html', '.txt']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Creating the output file path
                relative_path = os.path.relpath(file_path, base_dir)
                output_file_path = os.path.join(output_dir, relative_path)
                output_file_dir = os.path.dirname(output_file_path)

                if not os.path.exists(output_file_dir):
                    os.makedirs(output_file_dir)

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

    print(f"All files copied to {output_dir}")


base_directory = 'dernSol'
output_directory = 'output_files'

copy_files_to_text(base_directory, output_directory)
