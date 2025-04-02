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
    
    # Find the longest common subsequence with strict matching
    def find_strict_lcs(s1, s2):
        m, n = len(s1), len(s2)
        
        # Create a matrix to store LCS lengths
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the LCS length matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # If no common subsequence found, return empty string
        if dp[m][n] == 0:
            return ""
        
        # Reconstruct the LCS
        lcs = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        # Reverse to get correct order
        return ''.join(reversed(lcs))
    
    # Find the longest common subsequence
    lcs = find_strict_lcs(str1, str2)
    
    # Verify that the LCS is a valid subsequence in both strings
    def is_valid_subsequence(sequence, full_string):
        if not sequence:
            return True
        
        j = 0  # Index for full_string
        for char in sequence:
            # Find the next matching character
            while j < len(full_string) and full_string[j] != char:
                j += 1
            
            # If we can't find the character, it's not a valid subsequence
            if j >= len(full_string):
                return False
            
            # Move to next character
            j += 1
        
        return True
    
    # Return the LCS only if it's a valid subsequence in both strings
    return lcs if is_valid_subsequence(lcs, str1) and is_valid_subsequence(lcs, str2) else ""