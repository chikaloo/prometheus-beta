import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test valid anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("", "") == True  # Empty strings

def test_invalid_anagrams():
    """Test invalid anagram scenarios"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "typhon") == True
    assert is_anagram("cat", "act") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("debit card", "bad credit") == False  # Full string, with spaces

def test_different_lengths():
    """Test anagram validation for strings of different lengths"""
    assert is_anagram("short", "shorter") == False
    assert is_anagram("a", "b") == False

def test_input_validation():
    """Test input validation for non-lowercase inputs"""
    with pytest.raises(ValueError):
        is_anagram("Hello", "hello")
    
    with pytest.raises(ValueError):
        is_anagram("hello", "Hello")
    
    with pytest.raises(ValueError):
        is_anagram("Hello", "World")

def test_repeated_characters():
    """Test anagram validation with repeated characters"""
    assert is_anagram("aab", "aba") == True
    assert is_anagram("aab", "baa") == True
    assert is_anagram("aab", "aaa") == False