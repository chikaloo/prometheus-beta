def heapify(arr, n, i):
    """
    Maintain heap property for a subtree rooted at index i.
    
    Args:
        arr (list): The list to be heapified
        n (int): Size of the heap
        i (int): Index of the root of the subtree
    """
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    """
    Perform heap sort on the input list.
    
    Args:
        arr (list): The list to be sorted
    
    Returns:
        list: Sorted list in ascending order
    
    Raises:
        TypeError: If input is not a list
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    # If list is empty or has only one element, return as is
    if len(arr) <= 1:
        return arr.copy()

    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # Build max heap
    # Start from last non-leaf node and move upwards
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        sorted_arr[0], sorted_arr[i] = sorted_arr[i], sorted_arr[0]
        # Heapify the reduced heap
        heapify(sorted_arr, i, 0)

    return sorted_arr