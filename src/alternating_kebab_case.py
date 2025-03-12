def to_alternating_kebab_case(s: str) -> str:
    """
    Convert a string to alternating kebab case.
    
    Args:
        s (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating kebab case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> to_alternating_kebab_case("Hello World")
        'hello-WORLD'
        >>> to_alternating_kebab_case("python is awesome")
        'python-IS-awesome'
        >>> to_alternating_kebab_case("")
        ''
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not s:
        return ""
    
    # Split the string into words
    words = s.split()
    
    # Alternate the case of words
    alternating_words = [
        word.lower() if idx % 2 == 0 else word.upper() 
        for idx, word in enumerate(words)
    ]
    
    # Join with kebab case
    return '-'.join(alternating_words)