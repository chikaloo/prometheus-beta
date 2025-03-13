def fibonacci_log_time(n):
    """
    Calculate the n-th Fibonacci number with O(log n) time complexity using matrix exponentiation.
    
    Args:
        n (int): The index of the Fibonacci number to calculate (non-negative integer)
    
    Returns:
        int: The n-th Fibonacci number
    
    Raises:
        ValueError: If n is negative
        TypeError: If n is not an integer
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    # Type checking
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle edge cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for first few Fibonacci numbers
    if n <= 1:
        return n
    
    def multiply_matrix(a, b):
        """Multiply 2x2 matrices."""
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]
        ]
    
    def matrix_power(matrix, power):
        """Calculate matrix to the power of n using exponentiation by squaring."""
        # Base case for matrix power
        if power == 0:
            return [[1, 0], [0, 1]]  # Identity matrix
        
        if power == 1:
            return matrix
        
        # Recursive matrix power calculation
        half_power = matrix_power(matrix, power // 2)
        result = multiply_matrix(half_power, half_power)
        
        # If power is odd, multiply by original matrix
        if power % 2 == 1:
            result = multiply_matrix(result, matrix)
        
        return result
    
    # Matrix representing Fibonacci recurrence relation
    base_matrix = [[1, 1], [1, 0]]
    
    # Calculate matrix power
    result_matrix = matrix_power(base_matrix, n - 1)
    
    # The first element of the resulting matrix is the n-th Fibonacci number
    return result_matrix[0][0]