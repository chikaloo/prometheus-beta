import json
import pprint

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
        else:
            # Use pprint for more flexible formatting
            formatter = pprint.PrettyPrinter(indent=indent, width=max_width)
            return formatter.pformat(obj)
    except TypeError as e:
        # Handle objects that can't be directly serialized
        return f"Error logging object: {str(e)}"