import pytest
from src.perfect_number import is_perfect_number

def test_known_perfect_numbers():
    """Test known perfect numbers"""
    # First few known perfect numbers
    perfect_numbers = [6, 28, 496, 8128]
    for num in perfect_numbers:
        assert is_perfect_number(num) == True, f"{num} should be a perfect number"

def test_non_perfect_numbers():
    """Test numbers that are not perfect numbers"""
    non_perfect_numbers = [1, 12, 15, 100, 200]
    for num in non_perfect_numbers:
        assert is_perfect_number(num) == False, f"{num} should not be a perfect number"

def test_edge_cases():
    """Test edge cases"""
    # Test zero and negative numbers
    assert is_perfect_number(0) == False
    assert is_perfect_number(-6) == False

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test non-integer inputs
    with pytest.raises(ValueError):
        is_perfect_number(6.5)
    
    with pytest.raises(ValueError):
        is_perfect_number("6")
    
    with pytest.raises(ValueError):
        is_perfect_number([6])