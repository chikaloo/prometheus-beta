def find_most_frequent_char(input_string):
    """
    Find the most frequently occurring character in a given string.

    Args:
        input_string (str): The input string to analyze.

    Returns:
        str: The most frequently occurring character. 
             Prioritizes non-whitespace characters.
             Returns the first character if all frequencies are equal.
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
    
    # Count character frequencies with custom tiebreaker
    def custom_key(char):
        """Custom sorting key that prioritizes non-whitespace characters."""
        return (
            # Frequency (descending)
            -input_string.count(char),  
            # Prefer non-whitespace
            0 if not char.isspace() else 1,
            # Stable order 
            input_string.index(char)
        )
    
    # Return the character with the most favorable key
    return max(set(input_string), key=custom_key)