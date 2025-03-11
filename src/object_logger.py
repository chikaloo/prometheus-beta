import json
import pprint
import textwrap
import inspect

def log_object(obj, indent=2, max_width=80, use_json=False):
    """
    Log an object in a readable format.

    Args:
        obj: The object to be logged
        indent (int, optional): Number of spaces for indentation. Defaults to 2.
        max_width (int, optional): Maximum width for formatted output. Defaults to 80.
        use_json (bool, optional): Use JSON formatting instead of pprint. Defaults to False.

    Returns:
        str: A readable string representation of the object

    Raises:
        TypeError: If the object cannot be serialized
    """
    def is_serializable(obj):
        """Check if an object is JSON serializable"""
        try:
            json.dumps(obj)
            return True
        except (TypeError, OverflowError):
            return False

    def custom_formatter(obj, indent=2):
        """Custom formatter for non-standard objects"""
        # First, check if object has a dict representation
        if hasattr(obj, '__dict__'):
            return f"Error logging object: Unable to serialize {type(obj)}"
        
        # Fallback to string representation
        return str(obj)

    try:
        # Use JSON for serialization if requested
        if use_json:
            return json.dumps(obj, indent=indent)
        
        # Check if directly serializable
        if is_serializable(obj):
            # Use pprint for formatting with custom indentation
            formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
            return formatter.pformat(obj)
        
        # Handle non-serializable objects
        return custom_formatter(obj)
    
    except Exception as e:
        # Final catch-all for any unexpected errors
        return f"Error logging object: {str(e)}"