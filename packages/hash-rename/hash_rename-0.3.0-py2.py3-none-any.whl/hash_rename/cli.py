import argparse
import os

from .core import process_path

def main():
    parser = argparse.ArgumentParser(description="Process a file or directory to rename files based on md5 hashes.")
    parser.add_argument("path", type=str, help="Path to the file or directory to process.")
    # TODO: add a "--no-prompt" (aka "-y") flag to skip the prompt
    # TODO: add a hash_length arg
    # TODO: add a hash_func arg (to select md5, etc.)
    # TODO: add a no-recursion flag

    args = parser.parse_args()

    # Check if the path exists
    if not os.path.exists(args.path):
        print(f"The path {args.path} does not exist.")
        return

    process_path(args.path)

if __name__ == "__main__":
    main()
