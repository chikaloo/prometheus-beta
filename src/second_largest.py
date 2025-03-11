def find_second_largest(arr):
    """
    Find the second largest number in the given array.

    Args:
        arr (list): A list of numbers.

    Returns:
        int or float or None: The second largest number in the array, or None if 
        the array has fewer than 2 unique numbers.

    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-numeric elements
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("All elements must be numeric")
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(arr), reverse=True)
    
    # Return second largest if possible
    return unique_sorted[1] if len(unique_sorted) >= 2 else None