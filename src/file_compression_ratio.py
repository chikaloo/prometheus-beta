import os

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file.
    
    Compression Ratio = (Uncompressed Size - Compressed Size) / Uncompressed Size
    
    Args:
        file_path (str): Path to the file to analyze
    
    Returns:
        float: Compression ratio between 0 and 1
              0 means no compression
              1 means maximum compression
    
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If file is empty or cannot be processed
    """
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    uncompressed_size = os.path.getsize(file_path)
    
    # Handle empty file case
    if uncompressed_size == 0:
        raise ValueError("Cannot calculate compression ratio for an empty file")
    
    # For demonstration, we'll simulate compression using a simplistic approach
    # In a real-world scenario, you'd use actual compression algorithms
    
    # Simulated compression (50% for files > 0 bytes)
    compressed_size = max(uncompressed_size // 2, 1)
    
    # Calculate compression ratio
    compression_ratio = (uncompressed_size - compressed_size) / uncompressed_size
    
    return round(compression_ratio, 4)