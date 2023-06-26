import os
import re

# The directory where your subdirectories are located.
# You can replace this with your desired directory.
main_dir_path = r"D:"

# Pattern for the title ID in the .nfo file
pattern = re.compile(r'(0100[^\s]*)')

# Iterate over each subdirectory in the main directory
for dir_name in os.listdir(main_dir_path):
    dir_path = os.path.join(main_dir_path, dir_name)
    if os.path.isdir(dir_path):
        # This variable will hold the Title ID once it's found
        title_id = None

        # Iterate over every file in the subdirectory
        for filename in os.listdir(dir_path):
            # If the file is a .nfo file
            if filename.endswith('.nfo'):
                with open(os.path.join(dir_path, filename), 'r') as f:
                    # Read the contents of the file
                    contents = f.read()
                    # Search for the Title ID
                    match = pattern.search(contents)
                    # If found, store it in the title_id variable
                    if match:
                        title_id = match.group(1)
                        break

        # If the Title ID was found
        if title_id:
            # Iterate over every file in the directory again
            for filename in os.listdir(dir_path):
                # If the file is a .xci or .nsp file
                if filename.endswith('.xci') or filename.endswith('.nsp'):
                    # Split the filename into name and extension
                    name, ext = os.path.splitext(filename)
                    # Create a new filename using the Title ID and the extension
                    new_filename = f'{title_id}{ext}'
                    # Check if the new file name already exists
                    if not os.path.exists(os.path.join(dir_path, new_filename)):
                        # Rename the file
                        os.rename(os.path.join(dir_path, filename),
                                  os.path.join(dir_path, new_filename))
