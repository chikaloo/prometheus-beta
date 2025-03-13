import pytest
from src.matrix_addition import add_matrices

def test_basic_matrix_addition():
    """Test basic matrix addition"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_single_element_matrices():
    """Test addition of single-element matrices"""
    matrix1 = [[1]]
    matrix2 = [[2]]
    expected = [[3]]
    assert add_matrices(matrix1, matrix2) == expected

def test_different_row_length_error():
    """Test error when matrices have different row lengths"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6, 7], [8, 9, 10]]
    with pytest.raises(ValueError, match="All rows must have the same number of columns"):
        add_matrices(matrix1, matrix2)

def test_different_row_count_error():
    """Test error when matrices have different row counts"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of rows"):
        add_matrices(matrix1, matrix2)

def test_none_input_error():
    """Test error when input is None"""
    with pytest.raises(ValueError, match="Matrices cannot be None"):
        add_matrices(None, [[1, 2]])
    with pytest.raises(ValueError, match="Matrices cannot be None"):
        add_matrices([[1, 2]], None)

def test_empty_matrix_error():
    """Test error when input is an empty matrix"""
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([], [[1, 2]])
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices([[1, 2]], [])