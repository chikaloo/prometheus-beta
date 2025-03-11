import pytest
from src.merge_sorted_arrays import merge_sorted_arrays, is_sorted

def test_merge_sorted_arrays_basic():
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 6]

def test_merge_sorted_arrays_different_lengths():
    arr1 = [1, 3, 5, 7, 9]
    arr2 = [2, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3, 4, 5, 7, 9]

def test_merge_sorted_arrays_empty_arrays():
    arr1 = []
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == []

def test_merge_sorted_arrays_one_empty():
    arr1 = [1, 2, 3]
    arr2 = []
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 3]

def test_merge_sorted_arrays_with_duplicates():
    arr1 = [1, 2, 2, 3]
    arr2 = [2, 3, 4]
    assert merge_sorted_arrays(arr1, arr2) == [1, 2, 2, 2, 3, 3, 4]

def test_merge_sorted_arrays_type_error():
    with pytest.raises(TypeError):
        merge_sorted_arrays("not a list", [1, 2, 3])
    with pytest.raises(TypeError):
        merge_sorted_arrays([1, 2, 3], "not a list")

def test_merge_sorted_arrays_unsorted_error():
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])

def test_is_sorted():
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 2, 3]) == True
    assert is_sorted([1, 1, 2]) == True
    assert is_sorted([3, 2, 1]) == False