def sum_to_n(n: int) -> int:
    """
    Calculate the sum of all numbers from 1 to n in constant time using the arithmetic series formula.
    
    This function uses the formula n * (n + 1) / 2 to compute the sum in O(1) time complexity.
    
    Args:
        n (int): A non-negative integer representing the upper limit of the sum.
    
    Returns:
        int: The sum of all integers from 1 to n.
    
    Raises:
        ValueError: If n is negative.
    
    Examples:
        >>> sum_to_n(5)
        15
        >>> sum_to_n(0)
        0
    """
    # Check for negative input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Use arithmetic series formula: n * (n + 1) / 2
    return n * (n + 1) // 2  # Use integer division to avoid floating point