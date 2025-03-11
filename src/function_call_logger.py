from functools import wraps
from typing import Callable, Any

class FunctionCallTracker:
    """
    A class to track the number of times functions are called.
    
    This class provides a decorator that can be used to log function calls
    and retrieve call counts for tracked functions.
    """
    
    def __init__(self):
        """
        Initialize the function call tracker.
        """
        self._call_counts = {}
    
    def track(self, func: Callable) -> Callable:
        """
        Decorator to track the number of times a function is called.
        
        Args:
            func (Callable): The function to be tracked.
        
        Returns:
            Callable: A wrapper function that logs function calls.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Increment the call count for this function
            func_name = func.__name__
            self._call_counts[func_name] = self._call_counts.get(func_name, 0) + 1
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper
    
    def get_call_count(self, func_name: str) -> int:
        """
        Get the number of times a function has been called.
        
        Args:
            func_name (str): The name of the function to check.
        
        Returns:
            int: The number of times the function has been called.
            Returns 0 if the function has not been tracked.
        """
        return self._call_counts.get(func_name, 0)
    
    def reset_call_count(self, func_name: str = None) -> None:
        """
        Reset the call count for a specific function or all functions.
        
        Args:
            func_name (str, optional): The name of the function to reset. 
                                       If None, resets all function call counts.
        """
        if func_name is None:
            self._call_counts.clear()
        elif func_name in self._call_counts:
            del self._call_counts[func_name]

# Global instance of FunctionCallTracker for convenience
function_call_tracker = FunctionCallTracker()