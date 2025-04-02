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
    
    # For case-sensitive check
    def is_same_case(a, b):
        return a.isupper() == b.isupper()
    
    # Find the longest common subsequence
    def find_lcs(s1, s2):
        m, n = len(s1), len(s2)
        
        # Create a matrix to store LCS lengths
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the LCS length matrix
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1] and is_same_case(s1[i-1], s2[j-1]):
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
            if s1[i-1] == s2[j-1] and is_same_case(s1[i-1], s2[j-1]):
                lcs.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        # Reverse to get correct order
        return ''.join(reversed(lcs))
    
    # Find the LCS
    lcs = find_lcs(str1, str2)
    
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