import os
import pytest
import tempfile

from src.file_size import get_file_size


def test_get_file_size_normal_file():
    """Test getting size of a normal file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, World!")
        temp_file.close()
        
        try:
            size = get_file_size(temp_file.name)
            assert size == 13, f"Expected file size of 13, got {size}"
        finally:
            os.unlink(temp_file.name)


def test_get_file_size_empty_file():
    """Test getting size of an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            size = get_file_size(temp_file.name)
            assert size == 0, f"Expected file size of 0, got {size}"
        finally:
            os.unlink(temp_file.name)


def test_get_file_size_nonexistent_file():
    """Test getting size of a nonexistent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        get_file_size("/path/to/nonexistent/file.txt")


def test_get_file_size_directory():
    """Test getting size of a directory raises IsADirectoryError."""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(IsADirectoryError):
            get_file_size(temp_dir)