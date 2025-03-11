import os
import pytest
import tempfile
import shutil

from src.directory_exists import check_directory_exists


def test_existing_directory():
    """Test that an existing directory returns True."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert check_directory_exists(temp_dir) is True


def test_non_existing_directory():
    """Test that a non-existing directory returns False."""
    # Use a path that is very unlikely to exist
    non_existent_path = "/tmp/extremely_unlikely_directory_12345"
    assert check_directory_exists(non_existent_path) is False


def test_file_instead_of_directory():
    """Test that a file path returns False."""
    with tempfile.NamedTemporaryFile() as temp_file:
        assert check_directory_exists(temp_file.name) is False


def test_invalid_input_types():
    """Test error handling for invalid input types."""
    # Test non-string inputs
    with pytest.raises(TypeError):
        check_directory_exists(123)
    
    with pytest.raises(TypeError):
        check_directory_exists(None)
    
    with pytest.raises(TypeError):
        check_directory_exists(["not", "a", "string"])


def test_empty_string():
    """Test error handling for empty string input."""
    with pytest.raises(ValueError):
        check_directory_exists("")


def test_path_normalization():
    """Test that path normalization works correctly."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Test various path representations
        assert check_directory_exists(temp_dir) is True
        assert check_directory_exists(temp_dir + "/") is True
        assert check_directory_exists(os.path.join(temp_dir, "..")) is True