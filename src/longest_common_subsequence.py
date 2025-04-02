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
    
    # If case-insensitive match, return empty
    if str1.lower() == str2.lower():
        return ""
    
    # Find the longest common subsequence
    def find_lcs(s1, s2):
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
    
    # Verify subsequence validity
    def is_valid_subsequence(lcs, s1, s2):
        # Check if LCS can be found in the same order in both strings
        def check_sequence(seq, s):
            j = 0  # index in s
            for char in seq:
                # Find next occurrence of char
                while j < len(s) and s[j] != char:
                    j += 1
                if j >= len(s):
                    return False
                j += 1
            return True
        
        return (check_sequence(lcs, s1) and 
                check_sequence(lcs, s2))
    
    # Find the LCS
    lcs = find_lcs(str1, str2)
    
    # Return only if it satisfies subsequence conditions
    return lcs if is_valid_subsequence(lcs, str1, str2) else ""