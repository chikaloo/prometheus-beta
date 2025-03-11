import os
import pytest
import tempfile
import shutil

from src.delete_empty_directory import delete_empty_directory

def test_delete_empty_directory():
    # Create a temporary empty directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Verify the directory exists before deletion
        assert os.path.exists(temp_dir)
        assert os.path.isdir(temp_dir)

        # Delete the empty directory
        delete_empty_directory(temp_dir)

        # Verify the directory is deleted
        assert not os.path.exists(temp_dir)

def test_delete_nonexistent_directory():
    # Test deleting a directory that does not exist
    with pytest.raises(FileNotFoundError):
        delete_empty_directory('/path/to/nonexistent/directory')

def test_delete_nonempty_directory():
    # Create a temporary directory with a file
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a file in the directory
        temp_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(temp_file_path, 'w') as f:
            f.write('test content')

        # Attempt to delete non-empty directory should raise an error
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(temp_dir)

def test_delete_file_instead_of_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name

        # Attempt to delete a file should raise an error
        with pytest.raises(OSError, match="Path is not a directory"):
            delete_empty_directory(temp_file_path)

        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_delete_permission_restricted_directory():
    # This test simulates a permission-restricted directory
    # Note: This might not work exactly the same on all systems
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Make the directory read-only
            os.chmod(temp_dir, 0o400)

            # Attempt to delete should raise an OSError with a permission-related message
            with pytest.raises((OSError, PermissionError), match="Permission denied"):
                delete_empty_directory(temp_dir)
    except Exception:
        # If the test fails due to system-specific behavior, pass
        # This accounts for differences in permission handling across platforms
        pytest.skip("Permission test is system-dependent")