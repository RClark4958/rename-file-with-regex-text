import os
import re

def get_string_from_nfo(folder_path):
    """
    Retrieve the desired string from the .nfo file in the given folder.

    Args:
        folder_path (str): Path to the folder to be checked for an .nfo file.

    Returns:
        str or None: Desired string that starts with '0100' or None if not found.
    """
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # If the current file is an .nfo file, process it
        if filename.endswith('.nfo'):
            # Open the .nfo file, ignoring any unrecognized characters during decoding
            with open(os.path.join(folder_path, filename), 'r', errors='ignore') as file:
                content = file.read()
                # Use regex to find a string starting with '0100' and not followed by whitespaces
                match = re.search(r'0100[^\s]*', content)
                if match:
                    return match.group(0)  # Return the found string
    return None  # Return None if no matching string is found

def main():
    # Prompt the user to input the directory's path
    base_directory = input("Enter the path of the directory: ")

    # Loop through all items (files/folders) in the given directory
    for folder_name in os.listdir(base_directory):
        folder_path = os.path.join(base_directory, folder_name)
        
        # Check if the current item is a directory/folder
        if os.path.isdir(folder_path):
            # Retrieve the desired string from the .nfo file in this folder
            desired_string = get_string_from_nfo(folder_path)
            
            # If a desired string was found
            if desired_string:
                # List all .xci or .nsp files in the current folder
                files_to_rename = [file for file in os.listdir(folder_path) if file.endswith('.xci') or file.endswith('.nsp')]
                
                # Rename each of these files with the desired string
                for file in files_to_rename:
                    new_filename = desired_string + os.path.splitext(file)[1]
                    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_filename))
                    # Assuming only one .xci or .nsp file needs to be renamed per directory
                    break

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()

