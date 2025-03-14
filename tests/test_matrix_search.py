import pytest
from src.matrix_search import find_matrix_coordinates

def test_basic_matrix_search():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 5) == (1, 1)
    assert find_matrix_coordinates(matrix, 1) == (0, 0)
    assert find_matrix_coordinates(matrix, 9) == (2, 2)

def test_target_not_found():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert find_matrix_coordinates(matrix, 10) is None

def test_single_element_matrix():
    matrix = [[42]]
    assert find_matrix_coordinates(matrix, 42) == (0, 0)
    assert find_matrix_coordinates(matrix, 43) is None

def test_invalid_matrix_input():
    with pytest.raises(TypeError, match="Input must be a non-empty 2D list"):
        find_matrix_coordinates(None, 5)
    
    with pytest.raises(TypeError, match="Matrix must be a 2D list"):
        find_matrix_coordinates([1, 2, 3], 5)

def test_empty_matrix():
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        find_matrix_coordinates([], 5)
    
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        find_matrix_coordinates([[], [], []], 5)

def test_inconsistent_matrix():
    with pytest.raises(ValueError, match="All rows must have the same length"):
        find_matrix_coordinates([[1, 2], [3, 4, 5]], 5)

def test_non_numeric_matrix():
    with pytest.raises(ValueError, match="Matrix must contain only numeric values"):
        find_matrix_coordinates([[1, 2], ['a', 'b']], 'a')

def test_float_support():
    matrix = [
        [1.1, 2.2],
        [3.3, 4.4]
    ]
    assert find_matrix_coordinates(matrix, 3.3) == (1, 0)
    assert find_matrix_coordinates(matrix, 4.4) == (1, 1)