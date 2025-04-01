import pytest
from src.celsius_to_fahrenheit import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_positive():
    """Test conversion of positive Celsius temperatures."""
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(37) == 98.6

def test_celsius_to_fahrenheit_negative():
    """Test conversion of negative Celsius temperatures."""
    assert celsius_to_fahrenheit(-40) == -40.0
    assert celsius_to_fahrenheit(-273.15) == -459.67

def test_celsius_to_fahrenheit_float():
    """Test conversion with float values."""
    assert round(celsius_to_fahrenheit(25.5), 2) == 77.9

def test_celsius_to_fahrenheit_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([10])