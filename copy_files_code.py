import os


def copy_files_to_single_file(base_dir, output_file, extensions=None):
    if extensions is None:
        extensions = ['.py', '.html', '.txt']

    with open(output_file, 'w', encoding='utf-8') as output:
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    relative_path = os.path.relpath(file_path, base_dir)
                    output.write(f"\n\n{'#' * 10} {relative_path} {'#' * 10}\n\n")
                    output.write(content)

    print(f"All files copied to {output_file}")


base_directory = 'dernSol'
output_file_path = 'collected_codes.txt'

copy_files_to_single_file(base_directory, output_file_path)
