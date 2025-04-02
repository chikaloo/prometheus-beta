import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test LCS with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("test", "") == ""
    assert longest_common_subsequence("", "test") == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test when there's no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HELLO", "WORLD") == ""

def test_partial_matches():
    """Test partial matches"""
    assert longest_common_subsequence("abcde", "ace") == "ace"

def test_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "test")
    with pytest.raises(TypeError):
        longest_common_subsequence("test", [1,2,3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "test")

def test_unicode_handling():
    """Test Unicode character handling"""
    # Exact unicode matching and minimal common subsequence
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こん"
    # Exact unicode matching with different lengths
    assert longest_common_subsequence("こんにちは世界", "こんにちは") == "こんにちは"
    # No common unicode sequence
    assert longest_common_subsequence("こんにちは", "さようなら") == ""

def test_repeated_subsequence():
    """Test repeated subsequence"""
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"