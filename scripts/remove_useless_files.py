import os


def remove_useless_files():
    # List of file extensions to remove
    file_exts = [".log", ".tmp", ".bak", ".swp"]

    # List of directories to search
    dirs_to_search = ["/var/log", "/tmp"]

    # Loop through the directories and remove files with the specified extensions
    for dir_path in dirs_to_search:
        for dir_name, _, files in os.walk(dir_path):
            for file_name in files:
                _, ext = os.path.splitext(file_name)
                if ext in file_exts:
                    file_path = os.path.join(dir_name, file_name)
                    print(f"Removing file: {file_path}")
                    os.remove(file_path)
