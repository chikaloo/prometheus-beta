import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, Node

def test_cartesian_tree_sort_basic():
    """Test basic sorting functionality."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list."""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a single-element list."""
    arr = [42]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_sorted_list():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 3, 1, 5, 3, 1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-3, 1, -5, 0, 4, -2]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_invalid_input_type():
    """Test handling of invalid input type."""
    with pytest.raises(TypeError):
        cartesian_tree_sort("not a list")

def test_build_cartesian_tree_structure():
    """Test the structure of a built Cartesian tree."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    tree_root = build_cartesian_tree(arr)
    
    # Validate root is maximum element
    assert tree_root.value == max(arr)
    
    # Additional structure validation could be added here
    # This would involve tracing the tree structure against Cartesian tree properties

def test_build_cartesian_tree_empty():
    """Test building a Cartesian tree from an empty list."""
    assert build_cartesian_tree([]) is None

def test_in_order_traversal_correctness():
    """Verify that in-order traversal produces a sorted sequence."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_result = cartesian_tree_sort(arr)
    assert sorted_result == sorted(arr)