def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character. 
             If multiple characters have the same highest frequency, 
             returns the first non-whitespace character (if possible).
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
    
    # Find most frequent characters with max frequency
    most_frequent = [char for char, count in char_counts.items() if count == max_freq]
    
    # Prioritize non-whitespace characters
    non_whitespace = [char for char in most_frequent if not char.isspace()]
    
    # Return first non-whitespace char if available, else first char in most_frequent
    return non_whitespace[0] if non_whitespace else most_frequent[0]