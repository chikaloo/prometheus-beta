import pytest
import json
from src.object_logger import log_object

def test_log_object_dict():
    """Test logging a simple dictionary"""
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    result = log_object(test_dict)
    assert "John" in result
    assert "30" in result
    assert "New York" in result

def test_log_object_list():
    """Test logging a list of mixed types"""
    test_list = [1, "string", {"key": "value"}, [1, 2, 3]]
    result = log_object(test_list)
    assert "1" in result
    assert "string" in result
    assert "key" in result
    assert "[1, 2, 3]" in result

def test_log_object_json():
    """Test JSON formatting"""
    test_dict = {"name": "Alice", "scores": [85, 90, 95]}
    result = log_object(test_dict, use_json=True)
    # Verify it's valid JSON
    parsed = json.loads(result)
    assert parsed == test_dict

def test_log_object_custom_indent():
    """Test custom indentation"""
    test_dict = {"a": 1, "b": 2}
    result = log_object(test_dict, indent=4)
    # Check that the indentation is 4 spaces
    lines = result.split('\n')
    assert any(line.startswith('    "a"') for line in lines)

def test_log_object_complex_nested():
    """Test logging a complex nested structure"""
    test_complex = {
        "users": [
            {"name": "John", "details": {"age": 30, "city": "New York"}},
            {"name": "Jane", "details": {"age": 25, "city": "San Francisco"}}
        ]
    }
    result = log_object(test_complex)
    assert "John" in result
    assert "New York" in result
    assert "Jane" in result
    assert "San Francisco" in result

def test_log_object_non_serializable():
    """Test handling of non-serializable objects"""
    class NonSerializable:
        def __init__(self):
            self.x = 1

    obj = NonSerializable()
    result = log_object(obj)
    assert "Error logging object" in result

def test_log_object_max_width():
    """Test max width functionality"""
    long_string = "This is a very long string that should be wrapped"
    test_dict = {"description": long_string}
    result = log_object(test_dict, max_width=20)
    # Verify that the result respects max width
    assert len(max(result.split('\n'), key=len)) <= 20