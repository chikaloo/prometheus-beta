import os
import pytest
import tempfile
import pathlib

from src.largest_file import find_largest_file

def test_find_largest_file_basic():
    """Test finding the largest file in a directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple files with different sizes
        files = [
            ('small.txt', '100 bytes'),
            ('medium.txt', '1000 bytes'),
            ('large.txt', '10000 bytes')
        ]
        
        for filename, content in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content * (len(content.split()[0]))
        
        # Find the largest file
        largest_file = find_largest_file(temp_dir)
        
        # Check if the correct file was identified
        assert os.path.basename(largest_file) == 'large.txt'

def test_empty_directory():
    """Test behavior with an empty directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Empty directory should return None
        assert find_largest_file(temp_dir) is None

def test_directory_with_zero_byte_files():
    """Test directory with only zero-byte files"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create zero-byte files
        open(os.path.join(temp_dir, 'empty1.txt'), 'w').close()
        open(os.path.join(temp_dir, 'empty2.txt'), 'w').close()
        
        # Should return one of the zero-byte files
        largest_file = find_largest_file(temp_dir)
        assert largest_file is not None
        assert largest_file.endswith(('empty1.txt', 'empty2.txt'))

def test_nonexistent_directory():
    """Test handling of nonexistent directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        nonexistent_dir = os.path.join(temp_dir, 'nonexistent')
        
        with pytest.raises(FileNotFoundError):
            find_largest_file(nonexistent_dir)

def test_not_a_directory():
    """Test handling of a file path instead of a directory"""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file with the directory name
        file_path = os.path.join(temp_dir, 'not_a_dir.txt')
        with open(file_path, 'w') as f:
            f.write('Some content')
        
        with pytest.raises(NotADirectoryError):
            find_largest_file(file_path)

def test_large_file_absolute_path():
    """Test that the function returns an absolute path"""
    with tempfile.TemporaryDirectory() as temp_dir:
        files = [
            ('small.txt', '100 bytes'),
            ('large.txt', '10000 bytes')
        ]
        
        for filename, content in files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content * (len(content.split()[0]))
        
        # Find the largest file
        largest_file = find_largest_file(temp_dir)
        
        # Verify it's an absolute path
        assert os.path.isabs(largest_file)
        assert os.path.exists(largest_file)