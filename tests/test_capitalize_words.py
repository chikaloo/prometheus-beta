import pytest
from src.capitalize_words import capitalize_words

def test_standard_capitalization():
    """Test basic word capitalization."""
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python programming language") == "Python Programming Language"

def test_empty_string():
    """Test handling of empty string."""
    assert capitalize_words("") == ""

def test_already_capitalized():
    """Test string where words are already capitalized."""
    assert capitalize_words("Hello World") == "Hello World"

def test_mixed_case():
    """Test mixed case input."""
    assert capitalize_words("hElLo wOrLd") == "Hello World"

def test_multiple_spaces():
    """Test input with multiple or leading/trailing spaces."""
    assert capitalize_words("  spaced  words  ") == "  Spaced  Words  "

def test_single_word():
    """Test capitalization of a single word."""
    assert capitalize_words("python") == "Python"

def test_unicode_characters():
    """Test capitalization with unicode characters."""
    assert capitalize_words("árvíztűrő tükör") == "Árvíztűrő Tükör"

def test_input_types():
    """Test that function raises TypeError for non-string input."""
    with pytest.raises(AttributeError):
        capitalize_words(123)
    with pytest.raises(AttributeError):
        capitalize_words(None)