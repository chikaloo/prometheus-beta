import pytest
from src.find_missing_numbers import find_missing_numbers

def test_basic_missing_numbers():
    """Test finding missing numbers in a typical scenario."""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_large_range_missing_numbers():
    """Test finding missing numbers in a larger range."""
    assert find_missing_numbers([1, 10]) == [2, 3, 4, 5, 6, 7, 8, 9]

def test_no_missing_numbers():
    """Test when there are no missing numbers in the range."""
    assert find_missing_numbers([5, 6, 7, 8, 9, 10]) == []

def test_single_element_array():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == []

def test_duplicates_in_array():
    """Test an array with duplicate elements."""
    assert find_missing_numbers([1, 1, 3, 3, 5]) == [2, 4]

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError."""
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_missing_numbers([])

def test_none_input_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Input cannot be None"):
        find_missing_numbers(None)

def test_non_integer_raises_error():
    """Test that non-integer input raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_missing_numbers([1, 2, 'three', 4])

def test_unsorted_input():
    """Test that the function works with unsorted input."""
    assert find_missing_numbers([5, 1, 3]) == [2, 4]