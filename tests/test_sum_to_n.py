import pytest
from src.sum_to_n import sum_to_n

def test_sum_to_n_positive_numbers():
    """Test sum for various positive numbers."""
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
    assert sum_to_n(5) == 15
    assert sum_to_n(10) == 55
    assert sum_to_n(100) == 5050

def test_sum_to_n_large_number():
    """Test sum for a large number to check performance and accuracy."""
    large_n = 10**6
    expected = large_n * (large_n + 1) // 2
    assert sum_to_n(large_n) == expected

def test_sum_to_n_negative_input():
    """Test that a negative input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        sum_to_n(-1)
        sum_to_n(-100)

def test_sum_to_n_type_checking():
    """Ensure the function only accepts integers."""
    with pytest.raises(TypeError):
        sum_to_n(3.14)
    with pytest.raises(TypeError):
        sum_to_n("5")