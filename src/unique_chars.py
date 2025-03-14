def count_unique_characters(input_string):
    """
    Count the number of unique characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        int: The number of unique characters in the input string.
    
    Notes:
        - The function is case-sensitive ('a' and 'A' are considered different)
        - Whitespace characters are counted if present
        - Returns 0 for empty strings
    
    Examples:
        >>> count_unique_characters('hello')
        4
        >>> count_unique_characters('aAaA')
        2
        >>> count_unique_characters('')
        0
        >>> count_unique_characters('  ')
        1
    """
    # Handle empty string case
    if input_string is None:
        return 0
    
    # Use a set to count unique characters, preserving case sensitivity
    return len(set(input_string))