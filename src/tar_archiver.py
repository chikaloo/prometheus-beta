import os
import tarfile
from typing import Union, Optional


def create_tar_archive(directory_path: str, 
                       output_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a specified directory.

    Args:
        directory_path (str): Path to the directory to be archived
        output_path (Optional[str], optional): Path where the tar archive will be saved. 
            If None, archive will be saved in the same directory as the source. 
            Defaults to None.
        compression (str, optional): Compression type. 
            Options: 'gz' (gzip), 'bz2' (bzip2), 'xz', or None for no compression. 
            Defaults to 'gz'.

    Returns:
        str: Full path to the created tar archive

    Raises:
        ValueError: If directory does not exist or is not a directory
        ValueError: If invalid compression type is specified
    """
    # Validate directory exists and is a directory
    directory_path = os.path.abspath(directory_path)
    if not os.path.exists(directory_path):
        raise ValueError(f"Directory does not exist: {directory_path}")
    if not os.path.isdir(directory_path):
        raise ValueError(f"Path is not a directory: {directory_path}")

    # Validate compression type
    valid_compression_modes = {
        'gz': 'w:gz', 
        'bz2': 'w:bz2', 
        'xz': 'w:xz', 
        None: 'w'
    }
    if compression not in valid_compression_modes:
        raise ValueError(f"Invalid compression type: {compression}. "
                         f"Must be one of {list(valid_compression_modes.keys())}")

    # Determine output path
    if output_path is None:
        output_path = os.path.join(directory_path, 
                                   f"{os.path.basename(directory_path)}.tar.{compression or 'tar'}")
    else:
        output_path = os.path.abspath(output_path)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Create tar archive
    with tarfile.open(output_path, valid_compression_modes[compression]) as tar:
        tar.add(directory_path, arcname=os.path.basename(directory_path))

    return output_path