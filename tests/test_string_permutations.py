import pytest
from src.string_permutations import generate_unique_permutations

def test_generate_unique_permutations_basic():
    """Test basic string permutation generation"""
    result = generate_unique_permutations('abc')
    assert set(result) == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
    assert len(result) == 6

def test_generate_unique_permutations_empty_string():
    """Test permutation generation for empty string"""
    result = generate_unique_permutations('')
    assert result == ['']

def test_generate_unique_permutations_single_char():
    """Test permutation generation for single character"""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_generate_unique_permutations_with_duplicates():
    """Test permutation generation with duplicate characters"""
    result = generate_unique_permutations('abb')
    assert set(result) == {'abb', 'bab', 'bba'}
    assert len(result) == 3

def test_generate_unique_permutations_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(None)

def test_generate_unique_permutations_order():
    """Test that the output is sorted"""
    result = generate_unique_permutations('cab')
    assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def test_generate_unique_permutations_long_string():
    """Test permutation generation for longer strings"""
    result = generate_unique_permutations('abcd')
    assert len(result) == 24  # 4! = 24 unique permutations