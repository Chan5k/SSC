import os
import shutil

def backup_files(source_dir, dest_dir):
    """
    Creates a backup of a file by copying it to a new file with a '.bak' extension.

    Args:
    file_path (str): The path of the file to backup.
    """
    if not os.path.isdir(source_dir):
        print(f"Error: {source_dir} is not a directory")
        return

    # Create a backup file by copying the original file
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            backup_file_path = os.path.join(dest_dir, file + ".bak")
            shutil.copy2(file_path, backup_file_path)
            print(f"{file_path} backed up to {backup_file_path}")
