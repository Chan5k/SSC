import os

def remove_useless_files():
    # Define a list of file extensions to remove
    extensions = [
        ".log", ".gz", ".old", ".bak", ".swp", ".tmp", ".temp",
        ".cache", ".thumbnails", ".Trash"
    ]

    # Define a list of directories to search for files to remove
    directories = [
        "/var/log", "/var/cache", "/var/tmp", "/tmp", "/home/*/.cache",
        "/home/*/.thumbnails", "/home/*/.local/share/Trash"
    ]

    # Search for and delete files with the specified extensions in the specified directories
    num_files_deleted = 0
    for directory in directories:
        cmd = f"sudo find {directory} -type f -iname {' -o -iname '.join(extensions)} -delete"
        result = os.system(cmd)
        if result == 0:
            num_files_deleted += 1

    # Print a message indicating whether files were deleted or not
    if num_files_deleted > 0:
        print(f"{num_files_deleted} files have been deleted successfully.")
    else:
        print("No files were found to delete.")

if __name__ == "__main__":
    remove_useless_files()
