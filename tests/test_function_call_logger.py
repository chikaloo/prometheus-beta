import pytest
from src.function_call_logger import FunctionCallTracker, function_call_tracker

class TestFunctionCallTracker:
    def setup_method(self):
        """Reset call counts before each test."""
        function_call_tracker.reset_call_count()
    
    def test_basic_function_tracking(self):
        """Test basic function call tracking."""
        @function_call_tracker.track
        def sample_function():
            return "Hello"
        
        # Call the function multiple times
        sample_function()
        sample_function()
        sample_function()
        
        # Check the call count
        assert function_call_tracker.get_call_count("sample_function") == 3
    
    def test_function_with_args(self):
        """Test tracking a function with arguments."""
        @function_call_tracker.track
        def add_numbers(a, b):
            return a + b
        
        add_numbers(1, 2)
        add_numbers(3, 4)
        
        assert function_call_tracker.get_call_count("add_numbers") == 2
    
    def test_multiple_tracked_functions(self):
        """Test tracking multiple different functions."""
        @function_call_tracker.track
        def func1():
            pass
        
        @function_call_tracker.track
        def func2():
            pass
        
        func1()
        func1()
        func2()
        
        assert function_call_tracker.get_call_count("func1") == 2
        assert function_call_tracker.get_call_count("func2") == 1
    
    def test_get_call_count_untracked_function(self):
        """Test getting call count for an untracked function."""
        assert function_call_tracker.get_call_count("nonexistent_function") == 0
    
    def test_reset_specific_function(self):
        """Test resetting call count for a specific function."""
        @function_call_tracker.track
        def func_to_reset():
            pass
        
        func_to_reset()
        func_to_reset()
        
        assert function_call_tracker.get_call_count("func_to_reset") == 2
        
        function_call_tracker.reset_call_count("func_to_reset")
        
        assert function_call_tracker.get_call_count("func_to_reset") == 0
    
    def test_reset_all_functions(self):
        """Test resetting call counts for all functions."""
        @function_call_tracker.track
        def func1():
            pass
        
        @function_call_tracker.track
        def func2():
            pass
        
        func1()
        func2()
        
        function_call_tracker.reset_call_count()
        
        assert function_call_tracker.get_call_count("func1") == 0
        assert function_call_tracker.get_call_count("func2") == 0
    
    def test_function_return_value(self):
        """Test that tracked function returns original return value."""
        @function_call_tracker.track
        def return_five():
            return 5
        
        result = return_five()
        
        assert result == 5
        assert function_call_tracker.get_call_count("return_five") == 1