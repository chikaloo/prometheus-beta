import os
import pathlib

def find_largest_file(directory):
    """
    Find the largest file in a given directory.

    Args:
        directory (str): Path to the directory to search.

    Returns:
        str: Absolute path to the largest file in the directory.
        None: If the directory is empty or contains no files.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        NotADirectoryError: If the specified path is not a directory.
    """
    # Convert to absolute path and validate directory
    dir_path = pathlib.Path(directory).resolve()

    # Check if directory exists
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory not found: {dir_path}")

    # Check if it's a directory
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Specified path is not a directory: {dir_path}")

    # Find files in the directory
    files = [f for f in dir_path.iterdir() if f.is_file()]

    # Return None if no files
    if not files:
        return None

    # Find the largest file by size
    largest_file = max(files, key=lambda f: f.stat().st_size)

    return str(largest_file.resolve())