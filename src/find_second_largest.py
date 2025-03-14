def find_second_largest(arr):
    """
    Find the second largest element in an unsorted array of integers.

    Args:
        arr (list): A list of integers.

    Returns:
        int: The second largest element in the array.

    Raises:
        ValueError: If the input array has fewer than 2 unique elements.
    """
    # Check if input is valid
    if not arr or len(arr) < 2:
        raise ValueError("Input array must contain at least 2 unique elements")
    
    # Remove duplicates and convert to a set for unique values
    unique_nums = list(set(arr))
    
    # Check if there are at least 2 unique elements
    if len(unique_nums) < 2:
        raise ValueError("Input array must contain at least 2 unique elements")
    
    # Sort the unique numbers in descending order
    unique_nums.sort(reverse=True)
    
    # Return the second element (second largest)
    return unique_nums[1]