import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_unsorted():
    """Test finding second largest in an unsorted array"""
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_sorted():
    """Test finding second largest in a sorted array"""
    assert find_second_largest([1, 2, 5, 8, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate elements"""
    assert find_second_largest([5, 5, 2, 8, 1, 9, 9]) == 8

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers"""
    assert find_second_largest([-5, -2, -8, -1, -9]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers"""
    assert find_second_largest([-5, 2, 8, -1, 9]) == 8

def test_find_second_largest_raises_on_single_element():
    """Test that ValueError is raised for single-element array"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([5])

def test_find_second_largest_raises_on_empty_array():
    """Test that ValueError is raised for empty array"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([])

def test_find_second_largest_raises_on_all_same_elements():
    """Test that ValueError is raised when all elements are the same"""
    with pytest.raises(ValueError, match="Input array must contain at least 2 unique elements"):
        find_second_largest([5, 5, 5, 5])