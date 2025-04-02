import pytest
import logging
import json

from src.json_logger import log_json

class MockLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, level, message):
        self.logs.append((level, message))

def test_log_json_without_message():
    logger = MockLogger()
    test_obj = {"key": "value", "nested": {"sub_key": 42}}
    
    log_json(logger, logging.INFO, test_obj)
    
    assert len(logger.logs) == 1
    level, message = logger.logs[0]
    
    assert level == logging.INFO
    # Verify JSON is properly indented
    assert json.dumps(test_obj, indent=2) in message

def test_log_json_with_message():
    logger = MockLogger()
    test_obj = {"key": "value"}
    message = "Test logging context"
    
    log_json(logger, logging.DEBUG, test_obj, message)
    
    assert len(logger.logs) == 1
    level, full_message = logger.logs[0]
    
    assert level == logging.DEBUG
    assert message in full_message
    assert json.dumps(test_obj, indent=2) in full_message

def test_invalid_logger_type():
    with pytest.raises(TypeError, match="First argument must be a valid logging.Logger instance"):
        log_json("not a logger", logging.INFO, {"key": "value"})

def test_invalid_json_obj_type():
    logger = MockLogger()
    with pytest.raises(TypeError, match="JSON object must be a dictionary"):
        log_json(logger, logging.INFO, "not a dict")

def test_non_serializable_json():
    logger = MockLogger()
    # Create an object that can't be JSON serialized
    non_serializable = {"key": set()}
    
    with pytest.raises(ValueError, match="Unable to serialize JSON object"):
        log_json(logger, logging.INFO, non_serializable)