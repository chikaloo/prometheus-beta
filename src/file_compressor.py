import gzip
import os
import shutil

def compress_file(input_file_path, output_file_path=None):
    """
    Compress a file using gzip compression.

    Args:
        input_file_path (str): Path to the input file to be compressed.
        output_file_path (str, optional): Path for the compressed output file. 
                                          If not provided, appends '.gz' to input filename.

    Returns:
        str: Path to the compressed file.

    Raises:
        FileNotFoundError: If the input file does not exist.
        PermissionError: If there are permission issues reading/writing files.
        IsADirectoryError: If input path is a directory instead of a file.
    """
    # Validate input file exists and is a file
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"Input file not found: {input_file_path}")
    
    if os.path.isdir(input_file_path):
        raise IsADirectoryError(f"Input path is a directory, not a file: {input_file_path}")

    # Determine output file path
    if output_file_path is None:
        output_file_path = input_file_path + '.gz'

    try:
        # Compress the file
        with open(input_file_path, 'rb') as f_in:
            with gzip.open(output_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        return output_file_path
    except PermissionError:
        raise PermissionError(f"Permission denied when compressing file: {input_file_path}")