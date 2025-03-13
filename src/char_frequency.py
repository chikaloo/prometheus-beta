def get_char_frequency(input_string):
    """
    Calculate the frequency of characters in a given string.
    
    Args:
        input_string (str): The input string to analyze.
    
    Returns:
        dict: A dictionary with characters as keys and their frequencies as values.
    
    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Create a frequency dictionary
    frequency = {}
    
    # Count character frequencies
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    
    return frequency