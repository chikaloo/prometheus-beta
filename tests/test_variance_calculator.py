import pytest
import math
from src.variance_calculator import calculate_variance

def test_variance_normal_list():
    """Test variance calculation for a normal list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected_variance = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_variance_single_element():
    """Test variance for a single-element list."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_variance_with_floating_points():
    """Test variance calculation with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_variance = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_variance_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_variance_non_numeric_list():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, '3', 4, 5])

def test_variance_mixed_numeric_types():
    """Test variance calculation with mixed numeric types (int and float)."""
    numbers = [1, 2.5, 3, 4.5, 5]
    expected_variance = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_variance_negative_numbers():
    """Test variance calculation with negative numbers."""
    numbers = [-1, -2, -3, -4, -5]
    expected_variance = 2.0  # Calculated manually
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_variance_zero_values():
    """Test variance calculation with zero values."""
    numbers = [0, 0, 0, 0, 0]
    assert calculate_variance(numbers) == 0.0