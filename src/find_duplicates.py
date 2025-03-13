from typing import List


def find_duplicates(numbers: List[int]) -> List[int]:
    """
    Find and return a list of duplicate integers in the input list.

    Args:
        numbers (List[int]): A list of integers to search for duplicates.

    Returns:
        List[int]: A list of integers that appear more than once in the input list.
                   Duplicates are returned only once, in the order of their first occurrence.

    Examples:
        >>> find_duplicates([1, 2, 3, 4, 2, 5, 6, 3, 7])
        [2, 3]
        >>> find_duplicates([1, 1, 1, 1])
        [1]
        >>> find_duplicates([])
        []
    """
    # Track number occurrences and first occurrence index
    count = {}
    seen_positions = {}

    # First pass: count occurrences and track first position
    for idx, num in enumerate(numbers):
        count[num] = count.get(num, 0) + 1
        if num not in seen_positions:
            seen_positions[num] = idx

    # Find duplicates while preserving first occurrence order
    duplicates = [num for num, freq in count.items() if freq > 1]
    duplicates.sort(key=lambda x: seen_positions[x])

    return duplicates