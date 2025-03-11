import pytest
from src.quick_sort import quick_sort

def test_quick_sort_basic():
    """Test basic sorting of positive integers."""
    assert quick_sort([3, 6, 1, 8, 2, 4]) == [1, 2, 3, 4, 6, 8]

def test_quick_sort_negative_numbers():
    """Test sorting with negative numbers."""
    assert quick_sort([-3, -6, -1, -8, -2, -4]) == [-8, -6, -4, -3, -2, -1]

def test_quick_sort_mixed_numbers():
    """Test sorting with mixed positive and negative numbers."""
    assert quick_sort([-3, 6, 1, -8, 2, 4]) == [-8, -3, 1, 2, 4, 6]

def test_quick_sort_duplicate_numbers():
    """Test sorting with duplicate numbers."""
    assert quick_sort([3, 3, 1, 1, 2, 2]) == [1, 1, 2, 2, 3, 3]

def test_quick_sort_already_sorted():
    """Test sorting an already sorted list."""
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_quick_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_quick_sort_empty_list():
    """Test sorting an empty list."""
    assert quick_sort([]) == []

def test_quick_sort_single_element():
    """Test sorting a list with a single element."""
    assert quick_sort([42]) == [42]

def test_quick_sort_error_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        quick_sort("not a list")

def test_quick_sort_preserves_original():
    """Test that the original list is not modified."""
    original = [3, 1, 4, 1, 5, 9]
    sorted_list = quick_sort(original)
    assert original != sorted_list
    assert original == [3, 1, 4, 1, 5, 9]