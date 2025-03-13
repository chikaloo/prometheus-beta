def is_anagram(str1: str, str2: str) -> bool:
    """
    Determine if two strings are valid anagrams of each other.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. This implementation is case-sensitive
    and assumes only lowercase letters.
    
    Args:
        str1 (str): The first input string (lowercase letters only)
        str2 (str): The second input string (lowercase letters only)
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    
    Raises:
        ValueError: If input strings contain non-lowercase letters
    """
    # Validate input: check if strings contain only lowercase letters
    if not (str1.islower() and str2.islower()):
        raise ValueError("Input strings must contain only lowercase letters")
    
    # Quick length check
    if len(str1) != len(str2):
        return False
    
    # Use character frequency counting
    char_count = {}
    
    # Count characters in first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for second string
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True