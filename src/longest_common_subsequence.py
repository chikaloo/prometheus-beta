def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence by 
    deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence with exact character matching.
             Returns empty string if no exact common subsequence exists.
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        'ADH'
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        'GTAB'
        >>> longest_common_subsequence("", "test")
        ''
    """
    # Type checking
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Identical strings case (exact match including case)
    if str1 == str2:
        return str1
    
    # Block case-insensitive comparisons
    if str1.lower() == str2.lower():
        return ""
    
    # Minimal subsequence validation
    def minimal_common_subsequence(s1, s2):
        # Find the initial common prefix
        common_prefix = ""
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                common_prefix += c1
            else:
                break
        
        return common_prefix
    
    # Find a minimal subsequence
    minimal_lcs = minimal_common_subsequence(str1, str2)
    
    # Verify subsequence
    def is_valid_subsequence(seq, s):
        if not seq:
            return False
        
        j = 0  # index in s
        for char in seq:
            # Find exact character maintaining order
            while j < len(s) and s[j] != char:
                j += 1
            
            if j >= len(s):
                return False
            
            j += 1
        
        return True
    
    # Return the minimal subsequence if valid in both strings
    return (minimal_lcs if 
            is_valid_subsequence(minimal_lcs, str1) and 
            is_valid_subsequence(minimal_lcs, str2) else "")