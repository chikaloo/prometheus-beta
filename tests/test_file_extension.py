import pytest
import os
from src.file_extension import get_file_extension

def test_basic_file_extension():
    """Test getting extension from a simple filename"""
    assert get_file_extension('document.txt') == 'txt'
    assert get_file_extension('image.jpg') == 'jpg'

def test_file_extension_with_path():
    """Test getting extension from a full file path"""
    assert get_file_extension('/home/user/document.pdf') == 'pdf'
    assert get_file_extension('C:\\Users\\Name\\file.docx') == 'docx'

def test_multiple_dots():
    """Test files with multiple dots"""
    assert get_file_extension('archive.tar.gz') == 'gz'
    assert get_file_extension('script.test.py') == 'py'

def test_no_extension():
    """Test files without an extension"""
    assert get_file_extension('README') == ''
    assert get_file_extension('file_without_ext') == ''

def test_dot_only_filename():
    """Test files that start with a dot"""
    assert get_file_extension('.gitignore') == ''
    assert get_file_extension('.bashrc') == ''

def test_case_sensitivity():
    """Test that extensions are returned in lowercase"""
    assert get_file_extension('DOCUMENT.PDF') == 'pdf'
    assert get_file_extension('Image.PNG') == 'png'

def test_error_handling():
    """Test error cases"""
    with pytest.raises(TypeError):
        get_file_extension(None)
    
    with pytest.raises(TypeError):
        get_file_extension(123)
    
    with pytest.raises(ValueError):
        get_file_extension('')