import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_longest_increasing_subsequence_normal_case():
    """Test with a typical increasing subsequence."""
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4

def test_longest_increasing_subsequence_already_sorted():
    """Test with an already sorted list."""
    assert longest_increasing_subsequence([1, 2, 3, 4, 5]) == 5

def test_longest_increasing_subsequence_reverse_sorted():
    """Test with a reverse sorted list."""
    assert longest_increasing_subsequence([5, 4, 3, 2, 1]) == 1

def test_longest_increasing_subsequence_duplicate_elements():
    """Test with duplicate elements."""
    assert longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_longest_increasing_subsequence_empty_list():
    """Test with an empty list."""
    assert longest_increasing_subsequence([]) == 0

def test_longest_increasing_subsequence_single_element():
    """Test with a single element."""
    assert longest_increasing_subsequence([42]) == 1

def test_longest_increasing_subsequence_duplicate_max_length():
    """Test with multiple subsequences of max length."""
    assert longest_increasing_subsequence([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

def test_longest_increasing_subsequence_all_same_elements():
    """Test with all elements being the same."""
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7]) == 1