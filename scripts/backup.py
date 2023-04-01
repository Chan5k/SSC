import os
import shutil

def backup_file(file_path):
    """
    Creates a backup of a file by copying it to a new file with a '.bak' extension.

    Args:
    file_path (str): The path of the file to backup.
    """
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a file")
        return

    # Create a backup file by copying the original file
    backup_file_path = file_path + ".bak"
    shutil.copy2(file_path, backup_file_path)
    print(f"{file_path} backed up to {backup_file_path}")
