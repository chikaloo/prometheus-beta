import os
import pytest
import tempfile
from src.file_compression_ratio import calculate_compression_ratio

def test_calculate_compression_ratio_normal_file():
    # Create a temporary file with known content
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'This is a test file for compression ratio')
        temp_file_path = temp_file.name
    
    try:
        ratio = calculate_compression_ratio(temp_file_path)
        assert 0 <= ratio <= 1, "Compression ratio should be between 0 and 1"
        assert ratio > 0, "Compression ratio should be greater than 0 for non-empty file"
    finally:
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_empty_file():
    # Create an empty temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        with pytest.raises(ValueError, match="Cannot calculate compression ratio for an empty file"):
            calculate_compression_ratio(temp_file_path)
    finally:
        os.unlink(temp_file_path)

def test_calculate_compression_ratio_nonexistent_file():
    with pytest.raises(FileNotFoundError, match="File not found"):
        calculate_compression_ratio('/path/to/nonexistent/file.txt')

def test_calculate_compression_ratio_large_file():
    # Create a larger temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'0' * 1024 * 1024)  # 1 MB of zeros
        temp_file_path = temp_file.name
    
    try:
        ratio = calculate_compression_ratio(temp_file_path)
        assert 0 <= ratio <= 1, "Compression ratio should be between 0 and 1"
    finally:
        os.unlink(temp_file_path)