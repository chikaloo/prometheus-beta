import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_basic_space_replacement():
    """Test basic space replacement"""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_multiple_spaces():
    """Test multiple and leading/trailing spaces"""
    assert replace_spaces_with_underscores("  multiple   spaces  ") == "__multiple___spaces__"

def test_empty_string():
    """Test empty string input"""
    assert replace_spaces_with_underscores("") == ""

def test_no_spaces():
    """Test string with no spaces"""
    assert replace_spaces_with_underscores("nospaces") == "nospaces"

def test_error_handling():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
        replace_spaces_with_underscores(None)