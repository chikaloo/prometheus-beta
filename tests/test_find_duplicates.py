import pytest
from src.find_duplicates import find_duplicates


def test_find_duplicates_basic():
    """Test basic functionality of find_duplicates."""
    assert find_duplicates([1, 2, 3, 4, 2, 5, 6, 3, 7]) == [2, 3]


def test_find_duplicates_multiple_duplicates():
    """Test finding multiple duplicates."""
    assert find_duplicates([1, 1, 1, 1]) == [1]


def test_find_duplicates_no_duplicates():
    """Test when no duplicates are present."""
    assert find_duplicates([1, 2, 3, 4, 5]) == []


def test_find_duplicates_empty_list():
    """Test with an empty list."""
    assert find_duplicates([]) == []


def test_find_duplicates_order_preservation():
    """Test that duplicates are returned in order of first occurrence."""
    assert find_duplicates([3, 1, 2, 3, 1, 4, 2, 5]) == [3, 1, 2]


def test_find_duplicates_negative_numbers():
    """Test with negative numbers."""
    assert find_duplicates([-1, -2, 3, -1, 4, -2, 5]) == [-1, -2]


def test_find_duplicates_large_numbers():
    """Test with large numbers."""
    assert find_duplicates([1000000, 1, 1000000, 2, 1]) == [1000000, 1]