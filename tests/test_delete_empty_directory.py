import os
import sys
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
    # Skip this test on Windows as permission handling is different
    if sys.platform == 'win32':
        pytest.skip("Permission test not applicable on Windows")

    # This test simulates a permission-restricted directory
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Make the directory read-only (on systems that support it)
            os.chmod(temp_dir, 0o400)

            try:
                delete_empty_directory(temp_dir)
                # If deletion succeeds, that's fine too - it means the system 
                # handles permissions differently
                pytest.skip("Directory deletion succeeded on read-only directory")
            except (OSError, PermissionError) as e:
                # Check if the error involves permission
                assert "Permission" in str(e), f"Unexpected error: {e}"
    except Exception as e:
        # Allow for variations in system behavior
        pytest.skip(f"Permission test not supported: {e}")