import pytest
import logging
from src.object_logger import log_object_details

def test_log_object_details(caplog):
    """
    Test logging of a standard dictionary.
    """
    caplog.set_level(logging.INFO)
    test_dict = {"name": "John", "age": 30, "city": "New York"}
    
    log_object_details(test_dict)
    
    assert len(caplog.records) == 4  # 1 info header + 3 key-value pairs
    assert "Object Details:" in caplog.text
    assert "Key: name, Value: John" in caplog.text
    assert "Key: age, Value: 30" in caplog.text
    assert "Key: city, Value: New York" in caplog.text

def test_empty_dictionary(caplog):
    """
    Test behavior with an empty dictionary.
    """
    caplog.set_level(logging.WARNING)
    
    log_object_details({})
    
    assert len(caplog.records) == 1
    assert "Empty dictionary provided" in caplog.text

def test_invalid_input():
    """
    Test error handling for non-dictionary inputs.
    """
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details("not a dictionary")
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(123)
    
    with pytest.raises(TypeError, match="Input must be a dictionary"):
        log_object_details(None)