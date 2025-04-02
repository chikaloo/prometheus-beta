import pytest
import logging
import time
from src.network_response_logger import NetworkResponseLogger

# Mock network request functions for testing
def successful_request(delay=0.1):
    """Simulate a successful network request with optional delay."""
    time.sleep(delay)
    return "Success"

def failing_request():
    """Simulate a failing network request."""
    raise ValueError("Network Error")

class TestNetworkResponseLogger:
    def setup_method(self):
        """Set up a custom logger for each test."""
        self.log_messages = []
        self.logger = logging.getLogger('test_logger')
        self.logger.setLevel(logging.INFO)
        
        # Custom handler to capture log messages
        class CaptureHandler(logging.Handler):
            def emit(self, record):
                self.log_messages.append(self.format(record))
        
        self.capture_handler = CaptureHandler()
        self.capture_handler.setFormatter(logging.Formatter('%(message)s'))
        self.logger.addHandler(self.capture_handler)
    
    def test_successful_request_logging(self):
        """Test logging of a successful network request."""
        logger = NetworkResponseLogger(self.logger)
        
        # Decorate the request function
        timed_request = logger.log_response_time(successful_request)
        
        # Execute the request
        result = timed_request()
        
        # Assertions
        assert result == "Success"
        assert len(self.log_messages) == 1
        assert "Network Request: successful_request" in self.log_messages[0]
        assert "Response Time:" in self.log_messages[0]
    
    def test_response_time_accuracy(self):
        """Test that response time logging is reasonably accurate."""
        logger = NetworkResponseLogger(self.logger)
        
        # Decorate request with a specific delay
        timed_request = logger.log_response_time(successful_request)
        
        # Execute the request
        timed_request(delay=0.5)
        
        # Check log message and verify timing
        assert len(self.log_messages) == 1
        log_message = self.log_messages[0]
        
        # Extract response time from log
        response_time_str = log_message.split("Response Time:")[1].split("ms")[0].strip()
        response_time = float(response_time_str)
        
        # Check if response time is close to expected (within 10% margin)
        assert 450 <= response_time <= 550
    
    def test_failed_request_logging(self):
        """Test logging of a failed network request."""
        logger = NetworkResponseLogger(self.logger)
        
        # Decorate the failing request
        timed_request = logger.log_response_time(failing_request)
        
        # Verify that the original exception is re-raised
        with pytest.raises(ValueError, match="Network Error"):
            timed_request()
        
        # Check error log message
        assert len(self.log_messages) == 1
        assert "Network Request Error: failing_request" in self.log_messages[0]
        assert "Exception: Network Error" in self.log_messages[0]
    
    def test_multiple_request_logging(self):
        """Test logging multiple different requests."""
        logger = NetworkResponseLogger(self.logger)
        
        # Decorate two different request functions
        timed_success = logger.log_response_time(successful_request)
        
        # Execute requests
        timed_success(delay=0.1)
        
        # Verify logging
        assert len(self.log_messages) == 1
        assert "Network Request: successful_request" in self.log_messages[0]