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
    try:
        if use_json:
            # Use JSON for serialization with custom formatting
            return json.dumps(obj, indent=indent)
        
        # Special handling for non-serializable objects
        if not hasattr(obj, '__dict__') and not isinstance(obj, (dict, list, tuple, set)):
            try:
                # First try to convert to dict if it's an object with __dict__
                obj_dict = vars(obj)
                formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
                return formatter.pformat(obj_dict)
            except (TypeError, ValueError):
                return f"Error logging object: Unable to serialize object of type {type(obj)}"
        
        # Use pprint for more flexible formatting
        formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
        formatted = formatter.pformat(obj)

        # Wrap long lines if they exceed max_width
        if max_width < 80:
            wrapped_lines = []
            for line in formatted.split('\n'):
                # If line is longer than max_width, wrap it
                if len(line) > max_width:
                    wrapped_lines.extend(textwrap.wrap(line, width=max_width))
                else:
                    wrapped_lines.append(line)
            return '\n'.join(wrapped_lines)
        
        return formatted
    except Exception as e:
        # Catch-all for any serialization errors
        return f"Error logging object: {str(e)}"