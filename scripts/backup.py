import os
import shutil

def backup_files():
    """
    Creates a backup of files in a directory by copying them to a new file with a '.bak' extension.

    Args:
    source_dir (str): The path of the source directory to backup.
    dest_dir (str): The path of the destination directory to store the backup files.
    """
    source_dir = input("Enter the path of the source directory to backup: ")
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a directory")
        return

    dest_dir = input("Enter the path of the destination directory to store the backup files: ")
    if not os.path.isdir(dest_dir):
        print(f"Error: {dest_dir} is not a directory")
        return

    # Create a backup file by copying the original file
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            backup_file_path = os.path.join(dest_dir, file + ".bak")
            shutil.copy2(file_path, backup_file_path)
            print(f"{file_path} backed up to {backup_file_path}")
