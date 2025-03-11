def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word in a given string.

    Args:
        text (str): The input string to capitalize.

    Returns:
        str: A new string with the first letter of each word capitalized.

    Raises:
        AttributeError: If input is not a string.

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
        >>> capitalize_words("python programming language")
        'Python Programming Language'
        >>> capitalize_words("")
        ''
        >>> capitalize_words("  spaced  words  ")
        '  Spaced  Words  '
    """
    # Validate input is a string
    if not isinstance(text, str):
        raise AttributeError("Input must be a string")
    
    # Handle empty string case
    if not text:
        return text
    
    # Split into words, capitalize each word, then join back
    return ' '.join(word.capitalize() for word in text.split(' '))