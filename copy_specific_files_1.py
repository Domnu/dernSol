import os


def copy_specific_files_to_single_file(base_dir, output_file, specific_files):
    print('Lin 5 copy_specific_files.py - base_dir...... =', base_dir)
    print('Lin 6 copy_specific_files.py - output_file... =', output_file)
    print('Lin 7 copy_specific_files.py - specific_files =', specific_files)
    with open(output_file, 'w', encoding='utf-8') as output:
        for file in specific_files:
            # file_path = os.path.join(base_dir, file.replace('/', os.sep))
            file_path = file  # os.path.join(base_dir, file)
            absolute_path = "H:/dernSol/" + base_dir + '/' + file  # os.path.abspath(file_path)
            print('Lin 13 copy_specific_files.py - file_path =', file_path, ' --', base_dir)
            print('Lin 14 copy_specific_files.py - file_path =', file_path, ' --', file)
            print('Lin 15 copy_specific_files.py - absolute_path =', absolute_path)
            if os.path.exists(file):
                print('Lin 17 copy_specific_files.py - File exists:', file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    print('Lin 20 copy_specific_files.py - content =', content)

                relative_path = os.path.relpath(file_path, base_dir)
                print('Lin 23 copy_specific_files.py - relative_path:', relative_path)
                output.write(f"\n\n{'#' * 10} {file} {'#' * 10}\n\n")
                output.write(content)
            else:
                print('Lin 27 copy_specific_files.py - File does not exist:', file_path)

    print(f"Selected files copied to {output_file}")


base_directory = 'dernSol'
output_file_path = 'copy_specific_files_1_codes.txt'
specific_files = [
    r"H:\dernSol\chat\middleware.py",
    r"H:\dernSol\dernSol\settings.py",
    r"H:\dernSol\accounts\models.py",
    r"H:\dernSol\chat\models.py",
    r"H:\dernSol\chat\urls.py",
    r"H:\dernSol\chat\views.py",
]

copy_specific_files_to_single_file(base_directory, output_file_path, specific_files)
