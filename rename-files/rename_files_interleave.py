"""
rename_files_interleave for Python 3
Renames a set of files in a folder based on their filename.
Currently copies to a new folder rather than rename.
Example:
file_0001.txt > file_0001.txt
file_0002.txt > file_0016.txt
file_0003.txt > file_0002.txt
file_0004.txt > file_0015.txt
file_0005.txt > file_0003.txt
file_0006.txt > file_0014.txt
file_0007.txt > file_0004.txt
file_0008.txt > file_0013.txt
file_0009.txt > file_0005.txt
file_0010.txt > file_0012.txt
file_0011.txt > file_0006.txt
file_0012.txt > file_0011.txt
file_0013.txt > file_0007.txt
file_0014.txt > file_0010.txt
file_0015.txt > file_0008.txt
file_0016.txt > file_0009.txt
"""
import sys
import os
import glob
import shutil


def main():
    """Program entry point"""

    # Check command line argument length
    if len(sys.argv) < 3:
        print('Syntax: rename_files_interleave.py INPUT_FOLDER_NAME OUTPUT_FOLDER_NAME')
        return

    # Get command line args
    input_folder_name = sys.argv[1]
    output_folder_name = sys.argv[2]
    print(f'Input folder = {input_folder_name}')
    print(f'Output folder = {output_folder_name}')

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder_name):
        os.makedirs(output_folder_name)

    # Get the list of files to process
    files_to_process = sorted(glob.glob(os.path.join(input_folder_name, '*')))

    # How many files do we have?
    file_count = len(files_to_process)
    print(f'Count of files = {file_count}')

    # Loop though the files, copying to the new file name as we go.
    count = 1
    for old_file_name in files_to_process:
        # Determine the new file number based on whether the current file is even or odd.
        if count % 2 == 0:
            # Even files
            new_file_number = int(file_count - (count / 2) + 1)
        else:
            # Odd files
            new_file_number = int((count + 1) / 2)

        # Get the file name, everything before the nnnn number
        file_parts = os.path.splitext(old_file_name)
        file_name_base = os.path.basename(file_parts[0])
        file_name_base_no_number = file_name_base[0:-4]

        # Get the file extension
        file_name_ext = file_parts[1]

        # Generate the new file name
        new_file_name = f'{file_name_base_no_number}{new_file_number:04d}{file_name_ext}'
        new_file_with_path = os.path.join(output_folder_name, new_file_name)

        print(f'{old_file_name} -> {new_file_with_path}')

        # Copy the old file to the new file
        shutil.copyfile(old_file_name, new_file_with_path)

        # increment our counter
        count += 1


# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
