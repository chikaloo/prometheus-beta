import pytest
from src.z_algorithm import z_algorithm

def test_basic_string_matching():
    """Test basic string matching scenarios"""
    # Simple match
    assert z_algorithm("hello world", "o w") == [4]
    
    # Multiple matches
    assert z_algorithm("banana banana", "ana") == [1, 3, 8, 10]
    
    # No matches
    assert z_algorithm("hello world", "xyz") == []

def test_full_text_match():
    """Test when pattern matches the entire text"""
    assert z_algorithm("python", "python") == [0]

def test_overlapping_matches():
    """Test scenarios with overlapping matches"""
    assert z_algorithm("aaaaa", "aa") == [0, 1, 2, 3]

def test_edge_cases():
    """Test various edge cases"""
    # Single character match
    assert z_algorithm("hello", "l") == [2, 3]
    
    # Match at start
    assert z_algorithm("hello world", "hello") == [0]
    
    # Match at end
    assert z_algorithm("hello world", "world") == [6]

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Non-string inputs
    with pytest.raises(TypeError):
        z_algorithm(123, "pattern")
    
    with pytest.raises(TypeError):
        z_algorithm("text", 456)
    
    # Empty inputs
    with pytest.raises(ValueError):
        z_algorithm("", "pattern")
    
    with pytest.raises(ValueError):
        z_algorithm("text", "")
    
    with pytest.raises(ValueError):
        z_algorithm("", "")