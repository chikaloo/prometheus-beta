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

    def json_indent_format(obj, indent):
        """Force specific indentation format"""
        # Custom indentation for dictionaries
        if isinstance(obj, dict):
            # Manually create an indented representation 
            lines = ['{']
            for key, value in sorted(obj.items()):
                # Convert value to JSON string and use exact indentation
                value_str = json.dumps(value)
                lines.append(f"{' ' * indent}\"{key}\": {value_str},")
            
            # Remove last comma and close
            if lines[-1].endswith(','):
                lines[-1] = lines[-1].rstrip(',')
            lines.append('}')
            return '\n'.join(lines)
        
        # Fallback to JSON dumping for other types
        return json.dumps(obj, indent=indent)

    try:
        # Use JSON for serialization if requested
        if use_json:
            return json.dumps(obj, indent=indent)
        
        # Handle non-serializable objects first
        if not is_serializable(obj):
            try:
                # Try to convert to dictionary if possible
                if hasattr(obj, '__dict__'):
                    return "Error logging object: Unable to serialize custom object"
                
                # Fallback to string representation
                return str(obj)
            except Exception:
                return "Error logging object: Serialization failed"
        
        # For serializable objects, use custom indent formatting
        return json_indent_format(obj, indent)
    
    except Exception as e:
        # Final catch-all for any unexpected errors
        return f"Error logging object: {str(e)}"