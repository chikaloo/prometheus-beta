import threading
import time
from typing import List


def sleep_sort(arr: List[int]) -> List[int]:
    """
    Implement the sleep sort algorithm.
    
    Sleep sort works by creating a separate thread for each number, 
    where each thread sleeps for a duration proportional to the number's value,
    and then adds the number to the result list.
    
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
    
    # Normalize values to a time range
    max_val = max(arr) if arr else 0
    
    # Shared result list and synchronization mechanism
    result = []
    result_lock = threading.Lock()
    
    # Synchronization event to coordinate threads
    start_event = threading.Event()
    
    # Function to be run by each thread
    def sort_thread(num):
        # Wait for start signal
        start_event.wait()
        
        # Sleep proportional to (normalized) number's value
        time.sleep(0.001 * num / (max_val + 1))
        
        # Safely append to shared result list
        with result_lock:
            result.append(num)
    
    # Create threads
    threads = [threading.Thread(target=sort_thread, args=(num,)) for num in arr]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Signal all threads to start simultaneously
    start_event.set()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return result