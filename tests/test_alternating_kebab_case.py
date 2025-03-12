import pytest
from src.alternating_kebab_case import to_alternating_kebab_case

def test_basic_conversion():
    """Test basic string conversion to alternating kebab case."""
    assert to_alternating_kebab_case("Hello World") == 'hello-WORLD'
    assert to_alternating_kebab_case("python is awesome") == 'python-IS-awesome'

def test_empty_string():
    """Test conversion of empty string."""
    assert to_alternating_kebab_case("") == ''

def test_single_word():
    """Test conversion of a single word."""
    assert to_alternating_kebab_case("hello") == 'hello'

def test_multiple_consecutive_spaces():
    """Test conversion with multiple consecutive spaces."""
    assert to_alternating_kebab_case("hello   world  python") == 'hello-WORLD-python'

def test_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_kebab_case(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_kebab_case(None)

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert to_alternating_kebab_case("HeLLo WoRLd") == 'hello-WORLD'