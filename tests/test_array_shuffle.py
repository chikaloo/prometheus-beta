import pytest
import random
from src.array_shuffle import shuffle_array

def test_shuffle_array_basic():
    """Test basic shuffling of a list of integers."""
    original = [1, 2, 3, 4, 5]
    shuffled = shuffle_array(original)
    
    # Check that shuffled list has same elements
    assert set(shuffled) == set(original)
    
    # Check that the order is not always the same 
    # (statistically unlikely to return original order multiple times)
    attempts = 0
    different_order = False
    while attempts < 10:
        new_shuffle = shuffle_array(original)
        if new_shuffle != original:
            different_order = True
            break
        attempts += 1
    
    assert different_order, "Shuffle did not change the order of elements"

def test_shuffle_array_empty():
    """Test shuffling an empty list."""
    empty_list = []
    shuffled = shuffle_array(empty_list)
    assert shuffled == []

def test_shuffle_array_single_element():
    """Test shuffling a list with a single element."""
    single_element_list = [42]
    shuffled = shuffle_array(single_element_list)
    assert shuffled == [42]

def test_shuffle_array_mixed_types():
    """Test shuffling a list with mixed types."""
    mixed_list = [1, 'a', True, 3.14]
    shuffled = shuffle_array(mixed_list)
    
    # Check that shuffled list has same elements
    assert set(shuffled) == set(mixed_list)

def test_shuffle_array_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test None input
    with pytest.raises(ValueError, match="Input array cannot be None"):
        shuffle_array(None)
    
    # Test non-list input
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        shuffle_array(123)

def test_shuffle_array_randomness():
    """Test the statistical randomness of the shuffle."""
    original = list(range(10))
    shuffle_results = [tuple(shuffle_array(original)) for _ in range(100)]
    
    # Check that we get different permutations
    assert len(set(shuffle_results)) > 1, "Shuffle is not providing sufficient randomness"