import pytest
from src.most_frequent_char import find_most_frequent_char

def test_most_frequent_char_normal_case():
    """Test finding most frequent character in a typical string."""
    assert find_most_frequent_char("aabbccde") == 'a'

def test_most_frequent_char_multiple_max_frequency():
    """Test case where multiple chars have same max frequency."""
    assert find_most_frequent_char("abccc") == 'c'

def test_most_frequent_char_empty_string():
    """Test empty string returns None."""
    assert find_most_frequent_char("") is None

def test_most_frequent_char_single_char():
    """Test string with a single character."""
    assert find_most_frequent_char("x") == 'x'

def test_most_frequent_char_whitespace():
    """Test string with whitespace characters."""
    assert find_most_frequent_char("a b a b a") == 'a'

def test_most_frequent_char_invalid_input():
    """Test handling of non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(123)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)