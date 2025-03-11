import pytest
from src.second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a normal array"""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 2, 8, 1, 9]) == 8

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values"""
    assert find_second_largest([1, 1, 2, 2, 3, 3]) == 2
    assert find_second_largest([5, 5, 5, 2, 2]) == 2

def test_find_second_largest_edge_cases():
    """Test edge cases"""
    assert find_second_largest([1, 1]) is None
    assert find_second_largest([5]) is None
    assert find_second_largest([]) is None

def test_find_second_largest_negative_numbers():
    """Test with negative numbers"""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, 0, 5]) == 0

def test_find_second_largest_mixed_types():
    """Test with mixed numeric types"""
    assert find_second_largest([1, 2.5, 3, 4.7, 5]) == 4.7
    assert find_second_largest([1.1, 1.2, 1.3]) is None

def test_find_second_largest_error_cases():
    """Test error handling"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_second_largest("not a list")
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_second_largest([1, 2, "three"])
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_second_largest([1, 2, None])