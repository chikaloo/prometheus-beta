def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. This implementation:
    - is case-sensitive
    - assumes only lowercase letters
    - requires full character match for entire input strings
    
    Args:
        str1 (str): The first input string (lowercase letters only)
        str2 (str): The second input string (lowercase letters only)
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        ValueError: If input strings contain non-lowercase letters
    """
    # Remove whitespace from both strings
    str1_clean = str1.replace(" ", "")
    str2_clean = str2.replace(" ", "")
    
    # Special case for empty strings
    if not str1_clean and not str2_clean:
        return True
    
    # Validate input: check if strings contain only lowercase letters
    if not (str1_clean.islower() and str2_clean.islower()):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Check if original inputs match (when removing spaces)
    if str1 == str2:
        return True
    
    # Quick length check
    if len(str1_clean) != len(str2_clean):
        return False
    
    # Use character frequency counting
    char_count = {}
    
    # Count characters in first string
    for char in str1_clean:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for second string
    for char in str2_clean:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True