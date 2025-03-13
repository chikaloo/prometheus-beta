def remove_unique_elements(my_list):
    """
    Remove unique (non-duplicate) elements from a list.
    
    Args:
        my_list (list): A list to process.
    
    Returns:
        list: A new list containing only elements that appear more than once.
    
    Examples:
        >>> remove_unique_elements([1, 2, 2, 3, 3, 4])
        [2, 3]
        >>> remove_unique_elements([1, 1, 1, 2, 2, 3])
        [1, 2]
        >>> remove_unique_elements([1, 2, 3, 4, 5])
        []
    """
    # Use list comprehension with count() to keep only elements that appear more than once
    return [x for x in set(my_list) if my_list.count(x) > 1]