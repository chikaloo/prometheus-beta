import pytest
from src.inverse_case import convert_to_inverse_case

def test_convert_to_inverse_case_basic():
    """Test basic string conversion to inverse case."""
    assert convert_to_inverse_case("Hello World") == "hELLO wORLD"

def test_convert_to_inverse_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_inverse_case("") == ""

def test_convert_to_inverse_case_mixed_case():
    """Test conversion of a mixed case string."""
    assert convert_to_inverse_case("PyThOn Is AwEsOmE") == "pYtHoN iS aWeSoMe"

def test_convert_to_inverse_case_numbers_and_symbols():
    """Test conversion with numbers and symbols."""
    assert convert_to_inverse_case("Hello123!@#") == "hELLO123!@#"

def test_convert_to_inverse_case_non_string_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_inverse_case([])