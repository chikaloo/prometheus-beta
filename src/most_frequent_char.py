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
    char_order = {}
    char_counts = {}
    for i, char in enumerate(input_string):
        char_counts[char] = char_counts.get(char, 0) + 1
        if char not in char_order:
            char_order[char] = i
    
    # Find max frequency
    max_freq = max(char_counts.values())
    
    # Find the first character that appears with max frequency
    candidates = [char for char, count in char_counts.items() if count == max_freq]
    
    # Prioritize non-whitespace characters
    non_space = [char for char in candidates if not char.isspace()]
    
    # Return first non-space character if exists, else first candidate
    return non_space[0] if non_space else min(candidates, key=char_order.get)