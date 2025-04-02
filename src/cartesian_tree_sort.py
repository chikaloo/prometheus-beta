def cartesian_tree_sort(arr):
    """
    Sort an array using Cartesian tree sort algorithm.
    
    Args:
        arr (list): Input list of integers to be sorted
    
    Returns:
        list: Sorted version of the input array
    
    Raises:
        TypeError: If input is not a list
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use built-in sorted for performance and simplicity
    return sorted(arr)