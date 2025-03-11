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
    # Special handling for non-serializable objects
    def safe_serialize(obj):
        """Try to convert object to a serializable format"""
        try:
            # If it has a __dict__ attribute, convert to dictionary
            if hasattr(obj, '__dict__'):
                raise TypeError("Custom object serialization needed")
            return obj
        except Exception:
            return f"Error logging object: Unable to serialize {type(obj)}"

    try:
        # Use JSON for serialization if requested
        if use_json:
            return json.dumps(obj, indent=indent)
        
        # Check if object can be serialized
        try:
            # Use pprint for formatting
            formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
            result = formatter.pformat(obj)
            
            # If max_width is less than standard, attempt to wrap
            if max_width < 80:
                # Split the result and wrap each line
                wrapped_lines = []
                for line in result.split('\n'):
                    if len(line) > max_width:
                        wrapped_lines.extend(textwrap.wrap(line, width=max_width))
                    else:
                        wrapped_lines.append(line)
                return '\n'.join(wrapped_lines)
            
            return result
        except Exception:
            # Fallback for custom/non-serializable objects
            return f"Error logging object: Unable to serialize {type(obj)}"
    except Exception as e:
        # Final catch-all
        return f"Error logging object: {str(e)}"