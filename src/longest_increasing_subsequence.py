def longest_increasing_subsequence(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    A subsequence is a sequence that can be derived from another sequence by 
    deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        nums (list): A list of numbers to find the longest increasing subsequence in.
    
    Returns:
        int: Length of the longest increasing subsequence.
    
    Examples:
        >>> longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
        4
        >>> longest_increasing_subsequence([0, 1, 0, 3, 2, 3])
        4
        >>> longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
        1
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    # Handle edge cases
    if not nums:
        return 0
    
    # Length of the dynamic programming array
    n = len(nums)
    
    # Initialize dp array where each element is at least a subsequence of length 1
    dp = [1] * n
    
    # Compute longest increasing subsequence length
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length found
    return max(dp)