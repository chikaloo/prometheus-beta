import pytest
from src.merge_sorted_arrays import merge_sorted_arrays, _is_sorted

def test_merge_sorted_arrays_basic():
    """Test merging two sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_with_duplicates():
    """Test merging sorted arrays with duplicate values"""
    arr1 = [1, 2, 3, 3]
    arr2 = [2, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 3, 3, 4, 5]

def test_merge_sorted_arrays_empty_input():
    """Test merging with empty arrays"""
    arr1 = []
    arr2 = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]
    
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_both_empty():
    """Test merging two empty arrays"""
    assert merge_sorted_arrays([], []) == []

def test_merge_sorted_arrays_type_error():
    """Test type checking"""
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_merge_sorted_arrays_unsorted_error():
    """Test sorted order checking"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])

def test_is_sorted():
    """Test _is_sorted helper function"""
    assert _is_sorted([]) == True
    assert _is_sorted([1]) == True
    assert _is_sorted([1, 1, 2, 3]) == True
    assert _is_sorted([1, 2, 3, 4]) == True
    assert _is_sorted([4, 3, 2, 1]) == False