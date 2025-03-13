import pytest
from src.remove_unique_elements import remove_unique_elements

def test_remove_unique_elements():
    # Test basic case with duplicates
    assert sorted(remove_unique_elements([1, 2, 2, 3, 3, 4])) == [2, 3]
    
    # Test case with multiple duplicates
    assert sorted(remove_unique_elements([1, 1, 1, 2, 2, 3])) == [1, 2]
    
    # Test case with no duplicates
    assert remove_unique_elements([1, 2, 3, 4, 5]) == []
    
    # Test empty list
    assert remove_unique_elements([]) == []
    
    # Test list with repeated elements of same value
    assert remove_unique_elements([5, 5, 5, 5]) == [5]
    
    # Test mixed types (though function is type-hinted for integers)
    assert sorted(remove_unique_elements([1, 1, 'a', 'a', 2, 3])) == [1, 'a']

def test_input_preservation():
    # Ensure original list is not modified
    original = [1, 2, 2, 3, 3, 4]
    result = remove_unique_elements(original)
    assert original == [1, 2, 2, 3, 3, 4]
    assert result != original