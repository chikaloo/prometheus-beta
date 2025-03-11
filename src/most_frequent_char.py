def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             returns the first non-whitespace character from left to right.
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
    
    # Find the max frequency
    max_freq = max(char_counts.values())
    
    # Find the first non-whitespace character with max frequency from left to right
    non_space_chars = [char for char in input_string if not char.isspace()]
    
    for char in input_string:
        if char_counts[char] == max_freq:
            # If possible, return a non-whitespace character with max frequency
            if non_space_chars and char in non_space_chars:
                return char
    
    # Fallback to first character with max frequency if no non-space chars found
    for char in input_string:
        if char_counts[char] == max_freq:
            return char