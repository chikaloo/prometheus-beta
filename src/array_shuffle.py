import random
from typing import List, TypeVar

T = TypeVar('T')

def shuffle_array(arr: List[T]) -> List[T]:
    """
    Shuffle the elements of an input array randomly.
    
    Args:
        arr (List[T]): The input array to be shuffled.
    
    Returns:
        List[T]: A new list with elements randomly shuffled.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input list is None.
    """
    # Check for invalid inputs
    if arr is None:
        raise ValueError("Input array cannot be None")
    
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the list to avoid modifying the original
    shuffled = arr.copy()
    
    # Use Fisher-Yates (Knuth) shuffle algorithm
    for i in range(len(shuffled) - 1, 0, -1):
        # Generate a random index from 0 to i
        j = random.randint(0, i)
        
        # Swap elements
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    
    return shuffled