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
    def is_serializable(obj):
        """Check if an object is JSON serializable"""
        try:
            json.dumps(obj)
            return True
        except (TypeError, OverflowError):
            return False

    def custom_pprint(obj, indent=2, max_width=80):
        """Custom pretty printing with forced indentation"""
        try:
            # Use json for serialization with forced indentation
            formatted = json.dumps(obj, indent=indent, sort_keys=True)
            
            # If max_width is specified, attempt to wrap
            if max_width < 80:
                wrapped_lines = []
                for line in formatted.split('\n'):
                    if len(line) > max_width:
                        wrapped_lines.extend(textwrap.wrap(line, width=max_width))
                    else:
                        wrapped_lines.append(line)
                return '\n'.join(wrapped_lines)
            
            return formatted
        except Exception:
            # Fallback to pprint if json serialization fails
            formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
            return formatter.pformat(obj)

    try:
        # Use JSON for serialization if requested
        if use_json:
            return json.dumps(obj, indent=indent)
        
        # Check if directly serializable
        if is_serializable(obj):
            return custom_pprint(obj, indent, max_width)
        
        # Handle non-serializable objects
        try:
            # If it has a __dict__, attempt to serialize its contents
            return custom_pprint(vars(obj), indent, max_width)
        except Exception:
            return f"Error logging object: Unable to serialize {type(obj)}"
    
    except Exception as e:
        # Final catch-all for any unexpected errors
        return f"Error logging object: {str(e)}"