import pytest
from src.palindrome_checker import is_palindrome

def test_is_palindrome_basic():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_is_palindrome_case_insensitive():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("Abba") == True

def test_is_palindrome_edge_cases():
    # Empty string is considered a palindrome
    assert is_palindrome("") == True
    
    # Single character is a palindrome
    assert is_palindrome("a") == True
    
    # Only alphanumeric characters matter
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b1c") == False

def test_is_palindrome_special_characters():
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("a!b@c#") == True
    assert is_palindrome("ab!c") == False

def test_is_palindrome_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False