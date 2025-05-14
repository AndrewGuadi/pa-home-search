import os

# Files to exclude (exact filenames)
EXCLUDED_FILES = {
    '.env',
    'requirements.txt',
    'readme.MD',
    'README.md',
    '.gitignore',
    'LICENSE'
}

# Directory names to exclude (these names will be skipped anywhere in the path)
EXCLUDED_DIRS = {
    'myEnv',        # Virtual environment directory
    '__pycache__',  # Python cache files
    '.pytest_cache',
    '.git' # Pytest cache, if present
}

# Specific directory paths to exclude relative to the base directory
SPECIFIC_EXCLUDED_DIRS = {
    os.path.join('app', 'instance')
}

OUTPUT_FILE = 'all_code.txt'

def should_exclude_file(filepath):
    """Return True if the file should be excluded based on its name."""
    filename = os.path.basename(filepath)
    return filename in EXCLUDED_FILES

def should_exclude_dir(dirpath):
    """Return True if the directory should be excluded based on its name or specific paths."""
    # Check if directory name is in the generic exclusion list
    if os.path.basename(dirpath) in EXCLUDED_DIRS:
        return True

    # Check if the directory matches any specific path exclusion (e.g., app/instance)
    for specific_dir in SPECIFIC_EXCLUDED_DIRS:
        # Normalize the paths to handle differences across operating systems
        if os.path.normpath(dirpath).endswith(os.path.normpath(specific_dir)):
            return True

    return False

def main():
    base_dir = os.getcwd()  # run the script from the project root
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(base_dir):
            # Filter out excluded directories in-place so they aren't recursed into
            dirs[:] = [d for d in dirs if not should_exclude_dir(os.path.join(root, d))]
            
            for file in files:
                file_path = os.path.join(root, file)
                # Skip the output file to avoid including it
                if os.path.abspath(file_path) == os.path.abspath(OUTPUT_FILE):
                    continue
                if should_exclude_file(file_path):
                    continue
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    # If there is an error reading a file, log the error in the output
                    content = f"ERROR reading file: {e}"
                
                # Write a header and the file's content to the output file
                out_file.write("=" * 80 + "\n")
                out_file.write(f"FILE: {file_path}\n")
                out_file.write("=" * 80 + "\n\n")
                out_file.write(content)
                out_file.write("\n\n")
    print(f"All code has been written to {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
