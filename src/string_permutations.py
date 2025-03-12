def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all unique permutations of a given string.
    
    Args:
        s (str): Input string to generate permutations for
    
    Returns:
        list[str]: A list of unique permutations of the input string
    
    Raises:
        TypeError: If input is not a string
    
    Examples:
        >>> generate_unique_permutations('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> generate_unique_permutations('')
        ['']
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Special case for empty or single character string
    if len(s) <= 1:
        return [s]
    
    # Convert to list for easier manipulation
    chars = list(s)
    
    # Use set to store unique permutations
    unique_perms = set()
    
    def backtrack(start: int):
        """
        Recursive backtracking to generate unique permutations
        
        Args:
            start (int): Starting index for permutation generation
        """
        # Base case: if we've reached the end of the list, add the permutation
        if start == len(chars) - 1:
            unique_perms.add(''.join(chars))
            return
        
        # Try swapping current element with each subsequent element
        for i in range(start, len(chars)):
            # Swap characters
            chars[start], chars[i] = chars[i], chars[start]
            
            # Recursively generate permutations for the rest of the string
            backtrack(start + 1)
            
            # Backtrack (undo the swap)
            chars[start], chars[i] = chars[i], chars[start]
    
    # Start the backtracking process
    backtrack(0)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_perms))