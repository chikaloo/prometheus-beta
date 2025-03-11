import pytest
import time
from src.sleep_sort import sleep_sort


def test_sleep_sort_basic():
    """Test basic sorting functionality."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, f"Expected {expected}, but got {result}"


def test_sleep_sort_empty_list():
    """Test sorting an empty list."""
    assert sleep_sort([]) == [], "Empty list should return empty list"


def test_sleep_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert sleep_sort(input_list) == input_list, "Single element list should remain unchanged"


def test_sleep_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    result = sleep_sort(input_list)
    assert result == input_list, "Already sorted list should remain in the same order"


def test_sleep_sort_negative_numbers():
    """Test that negative numbers raise a ValueError."""
    with pytest.raises(ValueError, match="Sleep sort only works with non-negative integers"):
        sleep_sort([-1, 2, -3, 4])


def test_sleep_sort_zero_values():
    """Test sorting a list with zero values."""
    input_list = [0, 3, 0, 1, 0]
    expected = sorted(input_list)
    result = sleep_sort(input_list)
    assert result == expected, "List with zero values should be sorted correctly"


def test_sleep_sort_performance():
    """Verify that sleep sort completes in a reasonable time."""
    input_list = [1, 2, 3, 4, 5]
    start_time = time.time()
    sleep_sort(input_list)
    end_time = time.time()
    
    # The entire sort should complete in less than 1 second
    assert end_time - start_time < 1.0, "Sleep sort took too long to complete"