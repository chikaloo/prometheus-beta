from typing import List, Union
import math

def calculate_variance(numbers: List[Union[int, float]]) -> float:
    """
    Calculate the variance of a list of numbers.
    
    Variance is a measure of variability calculated as the average of squared 
    deviations from the mean.
    
    Args:
        numbers (List[Union[int, float]]): A list of numbers to calculate variance for.
    
    Returns:
        float: The variance of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric elements.
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Validate input is numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Convert to float to ensure precision
    numbers = [float(x) for x in numbers]
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate squared deviations
    squared_deviations = [(x - mean) ** 2 for x in numbers]
    
    # Calculate variance (average of squared deviations)
    variance = sum(squared_deviations) / len(numbers)
    
    return variance