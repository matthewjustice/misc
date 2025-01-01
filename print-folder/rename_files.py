"""
rename_files.py

"""

import sys
import os

def main():
    """Program entry point."""
    # Get the folder from the command line
    folder = sys.argv[1]

    print(f"Folder: {folder}")

    # Get a list of all the files in the folder, excluding directories
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # Print all the files in the folder
    for file in files:
        file_path = os.path.join(folder, file)
        print(f"Working on:  {file_path}")

        # Check if the file name begins with a single digit
        if file[0].isdigit() and not file[1].isdigit():
            # Rename the file
            new_file_path = os.path.join(folder, f"0{file}")
            os.rename(file_path, new_file_path)
            print(f"Renamed:  {new_file_path}")

    # Loop again over the new files names
    # Get a list of all the files in the folder, excluding directories
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # Print all the files in the folder
    for file in files:
        file_path = os.path.join(folder, file)
        print(f"Working on:  {file_path}")

        # Look for any single digit numbers in the file name, surrounded by spaces
        new_file_path = file_path
        for i in range(1, 10):
            # Check if the file name contains a single digit
            if f" {i} " in new_file_path:
                # Rename the file
                new_file_path = os.path.join(folder, new_file_path.replace(f" {i} ", f" 0{i} "))
        os.rename(file_path, new_file_path)
        print(f"Renamed:  {new_file_path}")


# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
