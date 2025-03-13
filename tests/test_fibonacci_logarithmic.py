import pytest
from src.fibonacci_logarithmic import fibonacci_log_time

def test_fibonacci_edge_cases():
    """Test edge cases of the Fibonacci function."""
    # Check first few Fibonacci numbers
    assert fibonacci_log_time(0) == 0
    assert fibonacci_log_time(1) == 1
    assert fibonacci_log_time(2) == 1
    assert fibonacci_log_time(3) == 2
    assert fibonacci_log_time(4) == 3
    assert fibonacci_log_time(5) == 5

def test_fibonacci_larger_numbers():
    """Test Fibonacci numbers for larger indices."""
    # Known Fibonacci numbers
    assert fibonacci_log_time(10) == 55
    assert fibonacci_log_time(20) == 6765
    assert fibonacci_log_time(30) == 832040

def test_fibonacci_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-1)
    
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_log_time(-100)

def test_fibonacci_type_handling():
    """Test type handling for the function."""
    with pytest.raises(TypeError):
        fibonacci_log_time(3.14)
    
    with pytest.raises(TypeError):
        fibonacci_log_time("5")
    
    with pytest.raises(TypeError):
        fibonacci_log_time(None)