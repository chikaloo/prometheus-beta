def quick_sort(arr):
    """
    Implement the Quick Sort algorithm to sort a list in ascending order.
    
    Quick Sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer strategy.
    It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays, 
    according to whether they are less than or greater than the pivot.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a copy to avoid modifying the original list
    arr = arr.copy()
    
    def _quick_sort(low, high):
        """
        Recursive helper function to perform quick sort on a subarray.
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        """
        if low < high:
            # Partition the array and get the pivot index
            pivot_index = _partition(low, high)
            
            # Recursively sort the sub-arrays
            _quick_sort(low, pivot_index - 1)
            _quick_sort(pivot_index + 1, high)
    
    def _partition(low, high):
        """
        Partition the subarray and return the pivot index.
        
        Uses the last element as the pivot and places it in its correct position.
        
        Args:
            low (int): Starting index of the subarray
            high (int): Ending index of the subarray
        
        Returns:
            int: The index of the pivot element after partitioning
        """
        # Choose the rightmost element as pivot
        pivot = arr[high]
        
        # Index of smaller element
        i = low - 1
        
        # Traverse through all elements
        # Compare each element with pivot
        for j in range(low, high):
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                # Increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        # Place pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        return i + 1
    
    # Start the quick sort process
    _quick_sort(0, len(arr) - 1)
    
    return arr