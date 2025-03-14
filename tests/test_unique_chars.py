import pytest
from src.unique_chars import count_unique_characters

def test_basic_unique_characters():
    """Test basic functionality of unique character counting."""
    assert count_unique_characters('hello') == 4
    assert count_unique_characters('world') == 5

def test_case_sensitivity():
    """Verify that the function is case-sensitive."""
    assert count_unique_characters('aAaA') == 2
    assert count_unique_characters('AbA') == 2

def test_empty_and_whitespace_strings():
    """Test handling of empty and whitespace strings."""
    assert count_unique_characters('') == 0
    assert count_unique_characters('  ') == 1
    assert count_unique_characters('\t\n') == 2

def test_repeated_characters():
    """Test strings with repeated characters."""
    assert count_unique_characters('aabbcc') == 3
    assert count_unique_characters('111222333') == 3

def test_special_characters():
    """Test strings with special characters."""
    assert count_unique_characters('!@#$%') == 5
    assert count_unique_characters('!!@@##') == 3

def test_mixed_character_types():
    """Test strings with mixed character types."""
    assert count_unique_characters('a1B!') == 4
    assert count_unique_characters('Hello, World!') == 10

def test_none_input():
    """Test handling of None input."""
    assert count_unique_characters(None) == 0