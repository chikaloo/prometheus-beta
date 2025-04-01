import pytest
from src.find_minimum import find_minimum

def test_find_minimum_basic():
    """Test finding minimum in a basic list of numbers."""
    assert find_minimum([5, 2, 8, 1, 9]) == 1

def test_find_minimum_negative_numbers():
    """Test finding minimum with negative numbers."""
    assert find_minimum([-5, -2, -8, -1, -9]) == -9

def test_find_minimum_mixed_numbers():
    """Test finding minimum in a list with mixed positive and negative numbers."""
    assert find_minimum([-5, 2, 0, 8, -1]) == -5

def test_find_minimum_single_element():
    """Test finding minimum in a single-element list."""
    assert find_minimum([42]) == 42

def test_find_minimum_float_numbers():
    """Test finding minimum in a list with float numbers."""
    assert find_minimum([5.5, 2.3, 8.1, 1.2, 9.7]) == 1.2

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty list"):
        find_minimum([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")

def test_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "three", 4])

def test_duplicate_minimum():
    """Test finding minimum when there are duplicate minimum values."""
    assert find_minimum([5, 1, 8, 1, 9]) == 1