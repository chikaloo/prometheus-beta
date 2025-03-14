def find_matrix_coordinates(matrix, target):
    """
    Find the coordinates of a target value in a 2D matrix.
    
    Args:
        matrix (List[List[int]]): A 2D matrix to search through
        target (int): The value to find in the matrix
    
    Returns:
        tuple: A tuple of (row, col) coordinates if found, or None if not found
    
    Raises:
        TypeError: If input is not a valid 2D matrix
        ValueError: If matrix is empty or contains non-numeric elements
    
    Time Complexity: O(m*n), where m is rows and n is columns
    Space Complexity: O(1)
    
    Examples:
        >>> find_matrix_coordinates([[1,2,3],[4,5,6],[7,8,9]], 5)
        (1, 1)
        >>> find_matrix_coordinates([[1,2,3],[4,5,6],[7,8,9]], 10)
        None
    """
    # Validate input matrix
    if not matrix or not isinstance(matrix, list):
        raise TypeError("Input must be a non-empty 2D list")
    
    # Check if matrix is 2D and rectangular
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a 2D list")
    
    # Check if matrix is empty
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise ValueError("Matrix cannot be empty")
    
    # Ensure consistent row lengths
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise ValueError("All rows must have the same length")
    
    # Search through the matrix
    for row_idx, row in enumerate(matrix):
        for col_idx, value in enumerate(row):
            # Validate numeric values
            if not isinstance(value, (int, float)):
                raise ValueError("Matrix must contain only numeric values")
            
            # Check if current value matches target
            if value == target:
                return (row_idx, col_idx)
    
    # Target not found
    return None