"""
merge_docs.py - Merge a set of docx files in a folder into a single document.

pip install docxcompose
"""

import sys
import os
from docxcompose.composer import Composer
from docx import Document

def main():
    """Program entry point."""
    # There should be one argument, the folder to print
    if len(sys.argv) != 3:
        print("Usage: merge_docs.py <folder> <output_file>")
        sys.exit(1)

    # Get the folder from the command line
    folder = sys.argv[1]

    # Get the output file from the command line
    output_file = sys.argv[2]

    print(f"Folder: {folder}")

    # Get a list of all the files in the folder, excluding directories
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    # Sort the files alphabetically
    files.sort()

    # Get the firt file to use as the base document
    base_file_path = os.path.join(folder, files.pop(0))
    print(f"Base doc: {base_file_path}")
    base_doc = Document(base_file_path)
    composer = Composer(base_doc)

    # Print all the files in the folder
    for file in files:
        file_path = os.path.join(folder, file)
        print(f"Merging:  {file_path}")

        # Add a page break before merging
        base_doc.add_page_break()

        # Append the file
        composer.append(Document(file_path))

    # Save the merged document
    composer.save(output_file)
    print(f"Output file: {output_file}")

# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
