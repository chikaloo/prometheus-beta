import pytest
from src.heap_sort import heap_sort, heapify

def test_heap_sort_empty_list():
    """Test sorting an empty list"""
    assert heap_sort([]) == []

def test_heap_sort_single_element():
    """Test sorting a list with a single element"""
    assert heap_sort([5]) == [5]

def test_heap_sort_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert heap_sort(input_list) == [1, 2, 3, 4, 5]

def test_heap_sort_reverse_sorted_list():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert heap_sort(input_list) == [1, 2, 3, 4, 5]

def test_heap_sort_unsorted_list():
    """Test sorting an unsorted list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert heap_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_heap_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 4, 4]
    assert heap_sort(input_list) == [1, 1, 3, 3, 3, 4, 4]

def test_heap_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-1, -5, 10, 0, -3, 4]
    assert heap_sort(input_list) == [-5, -3, -1, 0, 4, 10]

def test_heap_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        heap_sort("not a list")
        heap_sort(123)
        heap_sort(None)

def test_heap_sort_does_not_modify_original():
    """Test that the original list is not modified"""
    original = [5, 2, 8, 12, 1, 3]
    heap_sort(original)
    assert original == [5, 2, 8, 12, 1, 3]

def test_heapify_basic():
    """Test basic heapify functionality"""
    arr = [4, 10, 3, 5, 1]
    heapify(arr, len(arr), 0)
    # Heapify should arrange in max heap order
    assert arr[0] == max(arr)