import logging
import pytest
from src.multi_value_logger import log_multiple_values

class MockLogger:
    def __init__(self):
        self.debug_messages = []
        self.info_messages = []
        self.warning_messages = []
        self.error_messages = []
        self.critical_messages = []

    def debug(self, msg):
        self.debug_messages.append(msg)

    def info(self, msg):
        self.info_messages.append(msg)

    def warning(self, msg):
        self.warning_messages.append(msg)

    def error(self, msg):
        self.error_messages.append(msg)

    def critical(self, msg):
        self.critical_messages.append(msg)

def test_log_multiple_values_basic():
    """Test logging multiple values with default separator"""
    mock_logger = MockLogger()
    log_multiple_values('info', 'Hello', 42, 3.14, logger=mock_logger)
    assert mock_logger.info_messages == ['Hello | 42 | 3.14']

def test_log_multiple_values_custom_separator():
    """Test logging with a custom separator"""
    mock_logger = MockLogger()
    log_multiple_values('warning', 'Test', 'Case', separator='---', logger=mock_logger)
    assert mock_logger.warning_messages == ['Test---Case']

def test_log_multiple_values_different_levels():
    """Test logging at different levels"""
    mock_logger = MockLogger()
    
    log_multiple_values('debug', 'Debug', 'Message', logger=mock_logger)
    log_multiple_values('info', 'Info', 'Message', logger=mock_logger)
    log_multiple_values('warning', 'Warning', 'Message', logger=mock_logger)
    log_multiple_values('error', 'Error', 'Message', logger=mock_logger)
    log_multiple_values('critical', 'Critical', 'Message', logger=mock_logger)
    
    assert mock_logger.debug_messages == ['Debug | Message']
    assert mock_logger.info_messages == ['Info | Message']
    assert mock_logger.warning_messages == ['Warning | Message']
    assert mock_logger.error_messages == ['Error | Message']
    assert mock_logger.critical_messages == ['Critical | Message']

def test_log_multiple_values_invalid_level():
    """Test invalid logging level raises ValueError"""
    with pytest.raises(ValueError, match="Invalid logging level"):
        log_multiple_values('invalid_level', 'Test')

def test_log_multiple_values_invalid_logger():
    """Test invalid logger raises TypeError"""
    with pytest.raises(TypeError, match="Invalid logger object"):
        log_multiple_values('info', 'Test', logger="not a logger")

def test_log_multiple_values_no_values():
    """Test logging with no values"""
    mock_logger = MockLogger()
    log_multiple_values('info', logger=mock_logger)
    assert mock_logger.info_messages == ['']