import os
import pytest
from src.write_to_file import write_string_to_file

def test_write_string_to_file_success(tmp_path):
    """Test successful file writing."""
    # Create a temporary file path
    test_file = tmp_path / "test_file.txt"
    test_content = "Hello, World!"
    
    # Write to the file
    write_string_to_file(str(test_file), test_content)
    
    # Verify file contents
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == test_content

def test_write_string_to_file_empty_content(tmp_path):
    """Test writing an empty string."""
    test_file = tmp_path / "empty_file.txt"
    write_string_to_file(str(test_file), "")
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == ""

def test_write_string_to_file_invalid_file_path_type():
    """Test raising TypeError for invalid file path type."""
    with pytest.raises(TypeError, match="file_path must be a string"):
        write_string_to_file(123, "content")

def test_write_string_to_file_invalid_content_type():
    """Test raising TypeError for invalid content type."""
    with pytest.raises(TypeError, match="content must be a string"):
        write_string_to_file("test.txt", 123)

def test_write_string_to_file_empty_file_path():
    """Test raising ValueError for empty file path."""
    with pytest.raises(ValueError, match="file_path cannot be an empty string"):
        write_string_to_file("   ", "content")

def test_write_string_to_file_overwrite(tmp_path):
    """Test overwriting existing file."""
    test_file = tmp_path / "overwrite_file.txt"
    
    # First write
    write_string_to_file(str(test_file), "First content")
    
    # Overwrite
    write_string_to_file(str(test_file), "Updated content")
    
    # Verify new content
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == "Updated content"

def test_write_string_to_file_unicode(tmp_path):
    """Test writing unicode characters."""
    test_file = tmp_path / "unicode_file.txt"
    unicode_content = "Hello, 世界! ✨"
    
    write_string_to_file(str(test_file), unicode_content)
    
    with open(test_file, 'r', encoding='utf-8') as file:
        assert file.read() == unicode_content