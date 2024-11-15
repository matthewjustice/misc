"""
print_folder.py - On Windows, print all the files in a folder.
"""

import sys
import os
import ctypes

def main():
    """Program entry point."""
    # There should be one argument, the folder to print
    if len(sys.argv) != 2:
        print("Usage: print_folder.py <folder>")
        sys.exit(1)

    # Get the folder from the command line
    folder = sys.argv[1]

    print(f"Folder: {folder}")

    # Print all the files in the folder
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            print(file)
            # Use ShellExecute to print the file
            ctypes.windll.shell32.ShellExecuteW(None, "print", file_path, None, None, 0)

# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
