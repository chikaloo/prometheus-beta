import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares"""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for square in perfect_squares:
        assert is_perfect_square(square) is True, f"{square} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares"""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 12, 15, 17, 20]
    for number in non_perfect_squares:
        assert is_perfect_square(number) is False, f"{number} should not be a perfect square"

def test_floating_point_squares():
    """Test floating point perfect squares"""
    assert is_perfect_square(4.0) is True
    assert is_perfect_square(16.0) is True
    assert is_perfect_square(25.0) is True

def test_floating_point_non_squares():
    """Test floating point non-perfect squares"""
    assert is_perfect_square(5.5) is False
    assert is_perfect_square(3.14) is False

def test_large_perfect_squares():
    """Test large perfect squares"""
    large_squares = [10000, 1000000, 123454321]
    for square in large_squares:
        assert is_perfect_square(square) is True

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Test negative numbers
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    
    # Test non-numeric types
    with pytest.raises(TypeError, match="Input must be an integer or float"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be an integer or float"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be an integer or float"):
        is_perfect_square(None)