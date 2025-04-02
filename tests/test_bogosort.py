import pytest
import random
from src.bogosort import bogosort

def test_bogosort_empty_list():
    """Test sorting an empty list"""
    assert bogosort([]) == []

def test_bogosort_single_element():
    """Test sorting a list with a single element"""
    assert bogosort([5]) == [5]

def test_bogosort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert bogosort(arr) == arr

def test_bogosort_unsorted_integers():
    """Test sorting a list of unsorted integers"""
    arr = [5, 2, 9, 1, 7]
    sorted_arr = sorted(arr)
    assert bogosort(arr) == sorted_arr

def test_bogosort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_arr = sorted(arr)
    assert bogosort(arr) == sorted_arr

def test_bogosort_negative_numbers():
    """Test sorting a list with negative numbers"""
    arr = [-5, 2, -10, 0, 7]
    sorted_arr = sorted(arr)
    assert bogosort(arr) == sorted_arr

def test_bogosort_float_numbers():
    """Test sorting a list with floating point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58]
    sorted_arr = sorted(arr)
    assert bogosort(arr) == sorted_arr

def test_bogosort_invalid_input():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        bogosort("not a list")
    with pytest.raises(TypeError):
        bogosort(123)

def test_bogosort_preserves_original_list():
    """Test that the original list is not modified"""
    arr = [5, 2, 1, 4, 3]
    original = arr.copy()
    bogosort(arr)
    assert arr == original