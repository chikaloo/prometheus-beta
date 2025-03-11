import os
import tarfile
import pytest
import shutil
import tempfile

from src.tar_archiver import create_tar_archive


@pytest.fixture
def temp_directory():
    """Create a temporary directory with some test files."""
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some test files
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'file2.txt'), 'w') as f:
            f.write('Test content 2')
        
        yield temp_dir
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


def test_create_tar_archive_default(temp_directory):
    """Test creating a tar.gz archive with default settings."""
    archive_path = create_tar_archive(temp_directory)
    
    # Check archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        assert len(tar.getmembers()) > 0
        names = tar.getnames()
        assert os.path.basename(temp_directory) in names


def test_create_tar_archive_custom_path(temp_directory):
    """Test creating archive with a custom output path."""
    custom_path = os.path.join(os.path.dirname(temp_directory), 'custom_archive.tar.bz2')
    archive_path = create_tar_archive(temp_directory, output_path=custom_path, compression='bz2')
    
    assert os.path.exists(archive_path)
    assert archive_path == custom_path
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:bz2') as tar:
        assert len(tar.getmembers()) > 0


def test_create_tar_archive_no_compression(temp_directory):
    """Test creating an uncompressed tar archive."""
    archive_path = create_tar_archive(temp_directory, compression=None)
    
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:') as tar:
        assert len(tar.getmembers()) > 0


def test_create_tar_archive_invalid_directory():
    """Test handling of non-existent or non-directory paths."""
    with pytest.raises(ValueError, match="Directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')
    
    with pytest.raises(ValueError, match="Path is not a directory"):
        create_tar_archive(__file__)  # Use this test file as an example of a non-directory path


def test_create_tar_archive_invalid_compression(temp_directory):
    """Test handling of invalid compression type."""
    with pytest.raises(ValueError, match="Invalid compression type"):
        create_tar_archive(temp_directory, compression='invalid')