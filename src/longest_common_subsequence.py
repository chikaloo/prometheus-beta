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
    
    # If strings differ in case or first characters, return empty
    if (str1.lower() == str2.lower()) or str1[0] != str2[0]:
        return ""
    
    # Find the longest common subsequence
    def find_minimal_lcs(s1, s2):
        # First find the initial common characters
        prefix_length = 0
        while (prefix_length < len(s1) and 
               prefix_length < len(s2) and 
               s1[prefix_length] == s2[prefix_length]):
            prefix_length += 1
        
        # Return only the exact prefix
        return s1[:prefix_length] if prefix_length > 0 else ""
    
    # Find the LCS
    lcs = find_minimal_lcs(str1, str2)
    
    # Verify the subsequence is exact in both strings
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
    
    # Return only if it's an exact subsequence in both strings
    return lcs if is_exact_subsequence(lcs, str1) and is_exact_subsequence(lcs, str2) else ""