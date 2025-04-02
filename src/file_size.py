import os


def get_file_size(file_path):
    """
    Get the size of a given file in bytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: Size of the file in bytes.

    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path is a directory.
        PermissionError: If there's no permission to access the file.
    """
    try:
        # Check if the path exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Check if it's a file (not a directory)
        if os.path.isdir(file_path):
            raise IsADirectoryError(f"Path is a directory, not a file: {file_path}")
        
        # Get and return file size
        return os.path.getsize(file_path)
    
    except PermissionError:
        raise PermissionError(f"Permission denied when accessing file: {file_path}")