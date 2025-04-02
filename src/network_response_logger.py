import time
import logging
from typing import Callable, Any, Optional

class NetworkResponseLogger:
    """
    A utility class for logging network request response times.
    
    This class provides methods to measure and log the response times 
    of network requests with configurable logging levels and formats.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the NetworkResponseLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If not provided, a default logger will be created.
        """
        self.logger = logger or logging.getLogger(__name__)
    
    def log_response_time(self, func: Callable[..., Any], *args, **kwargs) -> Any:
        """
        Decorator method to log the response time of a network request.
        
        Args:
            func (Callable): The network request function to be timed
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
        
        Returns:
            The result of the original function
        
        Raises:
            Exception: Reraises any exceptions from the original function
        """
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                response_time_ms = (end_time - start_time) * 1000
                
                # Log the response time with function name and duration
                self.logger.info(
                    f"Network Request: {func.__name__} "
                    f"Response Time: {response_time_ms:.2f} ms"
                )
                
                return result
            except Exception as e:
                # Log any exceptions that occur during the request
                self.logger.error(
                    f"Network Request Error: {func.__name__} "
                    f"Exception: {str(e)}"
                )
                raise
        
        return wrapper