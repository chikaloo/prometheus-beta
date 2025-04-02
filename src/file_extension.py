import os

def get_file_extension(file_path):
    """
    Extract the file extension from a given file path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The file extension (without the dot) in lowercase.
             Returns an empty string if no extension is found.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is an empty string.
    """
    # Validate input
    if not isinstance(file_path, str):
        raise TypeError("Input must be a string")
    
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    # Extract the extension using os.path.splitext
    # This handles various edge cases like multiple dots, different path formats
    extension = os.path.splitext(file_path)[1].lstrip('.')
    
    return extension.lower()