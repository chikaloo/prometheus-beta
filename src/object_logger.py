import json
import pprint
import textwrap

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
    def safe_serialize(obj):
        """Safely serialize an object"""
        try:
            # Attempt to convert to dictionary
            if hasattr(obj, '__dict__'):
                return vars(obj)
            return obj
        except Exception:
            return str(obj)

    try:
        if use_json:
            # Use JSON for serialization with custom formatting
            return json.dumps(obj, indent=indent)
        
        # Special handling for non-serializable objects
        try:
            # Try to serialize the object
            serializable_obj = safe_serialize(obj)
            
            # Use pprint for formatting
            formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
            return formatter.pformat(serializable_obj)
        except Exception as e:
            # Fallback error message
            return f"Error logging object: Unable to serialize {type(obj)}"
    except Exception as e:
        # Catch-all for any remaining serialization errors
        return f"Error logging object: {str(e)}"