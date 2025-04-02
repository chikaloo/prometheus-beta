def z_algorithm(text, pattern):
    """
    Implement the Z algorithm for string matching.
    
    The Z algorithm finds all occurrences of a pattern within a text efficiently.
    
    Args:
        text (str): The full text to search in
        pattern (str): The pattern to search for
    
    Returns:
        list: Indices where the pattern starts in the text
    
    Raises:
        TypeError: If inputs are not strings
        ValueError: If inputs are empty strings
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Construct the Z array
    def compute_z_array(s):
        n = len(s)
        z = [0] * n
        left, right = 0, 0
        
        for k in range(1, n):
            # If k is outside the current Z-box, compute z[k] naively
            if k > right:
                left = right = k
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[k] = right - left
                right -= 1
            else:
                # k is inside the Z-box
                k1 = k - left
                
                # If the remaining length is within the Z-box
                if z[k1] < right - k + 1:
                    z[k] = z[k1]
                else:
                    # Extend beyond the current Z-box
                    left = k
                    while right < n and s[right - left] == s[right]:
                        right += 1
                    z[k] = right - left
                    right -= 1
        
        return z
    
    # Combine pattern and text with a separator
    combined = pattern + '$' + text
    z_array = compute_z_array(combined)
    
    # Find match indices 
    match_indices = []
    for i in range(len(pattern) + 1, len(combined)):
        if z_array[i] >= len(pattern):
            match_indices.append(i - len(pattern) - 1)
    
    return match_indices