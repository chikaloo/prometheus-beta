import concurrent.futures
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Uses a thread pool to sort numbers based on their values.
    
    Args:
        arr (List[int]): Input list of non-negative integers to be sorted.
    
    Returns:
        List[int]: Sorted list of input numbers.
    
    Raises:
        ValueError: If the input contains negative numbers.
    """
    # Validate input - no negative numbers allowed
    if any(num < 0 for num in arr):
        raise ValueError("Sleep sort only works with non-negative integers")
    
    # If input is empty, return empty list
    if not arr:
        return []
    
    # Sort mechanism with thread pool
    max_val = max(arr) if arr else 0
    result = []
    
    # Use thread-safe synchronized list
    from threading import Lock
    result_lock = Lock()
    
    def place_number(num):
        # Sleep proportionally to the number's value
        time.sleep(0.001 * num / (max_val + 1))
        
        with result_lock:
            result.append(num)
    
    # Use thread pool to manage concurrent execution
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(arr)) as executor:
        # Submit all threads
        futures = [executor.submit(place_number, num) for num in arr]
        
        # Wait for all threads to complete
        concurrent.futures.wait(futures)
    
    return sorted(result)