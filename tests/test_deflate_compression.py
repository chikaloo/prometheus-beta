import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_deflate_compress_string():
    """Test compressing a string"""
    test_string = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(test_string)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_deflate_compress_bytes():
    """Test compressing bytes"""
    test_bytes = b"Binary data to compress"
    compressed = deflate_compress(test_bytes)
    assert isinstance(compressed, bytes)
    assert len(compressed) > 0

def test_deflate_decompress():
    """Test decompressing compressed data"""
    test_string = "Hello, world! This is a test of Deflate compression."
    compressed = deflate_compress(test_string)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == test_string

def test_compression_levels():
    """Test different compression levels"""
    test_data = "Repeated data to test compression levels" * 100
    
    # Test each compression level
    compressed_sizes = [len(deflate_compress(test_data, level)) for level in range(10)]
    
    # Verify monotonically decreasing compressed data sizes 
    for i in range(1, len(compressed_sizes)):
        assert compressed_sizes[i] <= compressed_sizes[i-1]

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        deflate_compress(123)
    
    with pytest.raises(TypeError):
        deflate_decompress("not bytes")

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        deflate_compress("test", -1)
    
    with pytest.raises(ValueError):
        deflate_compress("test", 10)

def test_empty_input():
    """Test compression and decompression of empty input"""
    empty_string = ""
    empty_bytes = b""
    
    compressed_str = deflate_compress(empty_string)
    compressed_bytes = deflate_compress(empty_bytes)
    
    assert deflate_decompress(compressed_str) == empty_string.encode('utf-8')
    assert deflate_decompress(compressed_bytes) == empty_bytes

def test_large_input():
    """Test compression of large input"""
    large_data = "Large test data " * 10000
    compressed = deflate_compress(large_data)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == large_data

def test_invalid_compressed_data():
    """Test handling of invalid compressed data"""
    with pytest.raises(zlib.error):
        deflate_decompress(b"Invalid compressed data")