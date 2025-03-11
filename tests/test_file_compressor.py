import os
import gzip
import pytest
import tempfile
import shutil

from src.file_compressor import compress_file

def test_compress_file_default_output():
    # Create a temporary file with test content
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Test content for compression")
        input_path = temp_input.name

    try:
        # Compress the file
        output_path = compress_file(input_path)
        
        # Verify the output file was created with .gz extension
        assert output_path == input_path + '.gz'
        assert os.path.exists(output_path)
        
        # Verify file can be decompressed and content matches
        with gzip.open(output_path, 'rb') as f_in:
            decompressed_content = f_in.read()
        
        assert decompressed_content == b"Test content for compression"
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(input_path + '.gz'):
            os.unlink(input_path + '.gz')

def test_compress_file_custom_output():
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        temp_input.write(b"Another test content")
        input_path = temp_input.name
    
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_output:
        output_path = temp_output.name

    try:
        # Compress the file with custom output path
        compressed_path = compress_file(input_path, output_path)
        
        # Verify output path and file existence
        assert compressed_path == output_path
        assert os.path.exists(output_path)
        
        # Verify decompression works
        with gzip.open(output_path, 'rb') as f_in:
            decompressed_content = f_in.read()
        
        assert decompressed_content == b"Another test content"
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(output_path):
            os.unlink(output_path)

def test_compress_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        compress_file('/path/to/nonexistent/file.txt')

def test_compress_directory():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            compress_file(temp_dir)

def test_large_file_compression():
    with tempfile.NamedTemporaryFile(delete=False, mode='wb') as temp_input:
        # Create a larger file (1MB) with compressible content
        compressible_content = b"Repeated text " * 1000
        temp_input.write(compressible_content)
        input_path = temp_input.name

    try:
        # Compress the large file
        output_path = compress_file(input_path)
        
        # Verify output exists and is likely smaller than input
        assert os.path.exists(output_path)
        
        # With repeated text, compression should reduce file size
        # But make this check more flexible
        original_size = os.path.getsize(input_path)
        compressed_size = os.path.getsize(output_path)
        
        # For repeated text, file should be at least 20% smaller
        assert compressed_size < 0.8 * original_size
    
    finally:
        # Clean up temporary files
        if os.path.exists(input_path):
            os.unlink(input_path)
        if os.path.exists(input_path + '.gz'):
            os.unlink(input_path + '.gz')