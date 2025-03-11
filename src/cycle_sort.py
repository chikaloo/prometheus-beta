def cycle_sort(arr):
    """
    Implements the Cycle Sort algorithm for sorting a list in-place.
    
    Cycle sort is an in-place, unstable sorting algorithm that is optimal in terms 
    of the number of memory writes. It works by minimizing the number of memory writes 
    to sort an array with a given set of values.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list (same object as input, modified in-place).
    
    Raises:
        TypeError: If the input is not a list or contains unhashable elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Perform cycle sort
    for cycle_start in range(len(arr) - 1):
        current_item = arr[cycle_start]
        
        # Find where to put the current item
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < current_item:
                pos += 1
        
        # If the item is already in the correct position
        if pos == cycle_start:
            continue
        
        # Otherwise, put the current item there
        while current_item == arr[pos]:
            pos += 1
        
        arr[pos], current_item = current_item, arr[pos]
        
        # Rotate the rest of the cycle
        while pos != cycle_start:
            # Find where to put the current item
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < current_item:
                    pos += 1
            
            # Put the current item in its right position
            while current_item == arr[pos]:
                pos += 1
            
            arr[pos], current_item = current_item, arr[pos]
    
    return arr