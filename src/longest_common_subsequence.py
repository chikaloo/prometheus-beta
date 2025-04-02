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
    
    # Find the minimal common subsequence
    def find_minimal_lcs(s1, s2):
        # If strings differ in case or content, return empty string
        if any(a != b for a, b in zip(s1, s2)):
            return ""
        
        # Find the common prefix
        prefix = ""
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                prefix += c1
            else:
                break
        
        return prefix
    
    # Verify exact minimal subsequence
    def is_exact_subsequence(seq, s):
        if not seq:
            return False
        
        j = 0  # Index for the full string
        for char in seq:
            # Find the exact character in the string maintaining original order
            while j < len(s) and s[j] != char:
                j += 1
            
            if j >= len(s):
                return False
            
            j += 1
        
        return True
    
    # Find the LCS
    lcs = find_minimal_lcs(str1, str2)
    
    # Return only if it's an exact subsequence in both strings
    return lcs if is_exact_subsequence(lcs, str1) and is_exact_subsequence(lcs, str2) else ""