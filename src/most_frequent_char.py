def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             returns the first one encountered from left to right.
             Returns None for an empty string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check for invalid input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not input_string:
        return None
    
    # Count character frequencies
    char_counts = {}
    for char in input_string:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Find the first character with max frequency from left to right
    max_freq = max(char_counts.values())
    
    # Special handling for whitespace-heavy inputs
    non_space_chars = [char for char in input_string if not char.isspace()]
    
    # If there are non-space characters with max frequency, return the first one
    if non_space_chars:
        for char in input_string:
            if char_counts[char] == max_freq and char in non_space_chars:
                return char
    
    # Fallback to first character with max frequency
    for char in input_string:
        if char_counts[char] == max_freq:
            return char