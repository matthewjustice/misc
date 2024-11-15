"""
print_folder.py - On Windows, print all the files in a folder.
"""

import sys
import os
import ctypes
import time

def main():
    """Program entry point."""
    # There should be one argument, the folder to print
    if len(sys.argv) != 2:
        print("Usage: print_folder.py <folder>")
        sys.exit(1)

    # Get the folder from the command line
    folder = sys.argv[1]

    print(f"Folder: {folder}")

    # Get a list of all the files in the folder, excluding directories
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # Sort the files alphabetically
    files.sort()

    # Print all the files in the folder
    for file in files:
        file_path = os.path.join(folder, file)
        print(f"Printing {file}...")

        # Use ShellExecute to print the file
        ctypes.windll.shell32.ShellExecuteW(None, "print", file_path, None, None, 0)

        # Delay for a moment to avoid overloading the printer,
        # and to ensure that files are printed in order
        time.sleep(5)

# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
