import zlib
from typing import Union

def deflate_compress(data: Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress data using the Deflate compression algorithm.

    Args:
        data (Union[str, bytes]): The input data to compress.
        compression_level (int, optional): Compression level from 0-9. 
            0 = no compression, 9 = maximum compression. Defaults to 6.

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression level is not between 0 and 9.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")
    
    # Compress using zlib 
    compressed_data = zlib.compress(data, compression_level)
    
    return compressed_data

def deflate_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress data that was compressed using the Deflate algorithm.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        zlib.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress using zlib
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")