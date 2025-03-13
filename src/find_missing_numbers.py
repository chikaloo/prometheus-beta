def find_missing_numbers(arr):
    """
    Find all missing numbers between the smallest and largest numbers in a sorted array.
    
    Args:
        arr (list): A sorted list of integers in ascending order.
    
    Returns:
        list: A list of missing numbers between the smallest and largest numbers.
    
    Raises:
        ValueError: If the input array is empty or None.
        TypeError: If the input is not a list or contains non-integer elements.
    
    Examples:
        >>> find_missing_numbers([1, 3, 5])
        [2, 4]
        >>> find_missing_numbers([1, 10])
        [2, 3, 4, 5, 6, 7, 8, 9]
        >>> find_missing_numbers([5, 5, 5])
        []
    """
    # Validate input
    if arr is None:
        raise ValueError("Input cannot be None")
    
    if not arr:
        raise ValueError("Input array cannot be empty")
    
    # Check all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Sort and remove duplicates to handle unsorted or duplicate inputs
    arr = sorted(set(arr))
    
    # If there's only one unique number, return empty list
    if len(arr) == 1:
        return []
    
    # Find missing numbers between smallest and largest
    start, end = arr[0], arr[-1]
    missing_numbers = [
        num for num in range(start + 1, end) 
        if num not in arr
    ]
    
    return missing_numbers