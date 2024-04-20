import hashlib
import os

# ChatGPT Prompt:
# Write a Python script which takes one argument (using argparse): a path to either a file or a directory.
# If it's a file, then it should read that file, calculate the md5 hash as base16 lowercase,
# and then rename that file to: <first 6 md5 characters>_<old filename>. 
# If it's a folder, then it should perform that operation recursively on all files in the folder.
# Prompt the user to press enter for each rename.

def get_md5_hash(file_path):
    """Calculate the md5 hash of a file and return the first 6 characters."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buffer = file.read(8192)
        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(8192)
    return hasher.hexdigest()[:6]

def rename_file(file_path):
    """Rename a file to include the first 6 characters of its md5 hash."""
    dir_name, file_name = os.path.split(file_path)
    hash_prefix = get_md5_hash(file_path)
    new_file_name = f"{hash_prefix}_{file_name}"
    new_file_path = os.path.join(dir_name, new_file_name)

    if file_name.startswith(hash_prefix + '_'):
        print(f"Skipping '{file_path}' (already renamed)")
        return
    
    inp = input(f"Press Enter to rename the file '{file_path}' to '{hash_prefix}_{file_name[:10]}...', or Ctrl+C to cancel, or 's' to skip >> ")

    if 's' in inp.lower():
        print(f"Skipping '{file_path}'")
        return
    os.rename(file_path, new_file_path)
    print(f"Renamed '{file_path}' to '{new_file_path}'")

def process_path(path):
    """Process a path, recursively renaming files if it's a directory."""
    if os.path.isfile(path):
        rename_file(path)
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if not os.path.isfile(file_path):
                    print(f"Skipping non-file: {file_path}")
                    continue
                rename_file(file_path)