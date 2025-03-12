"""
Arithmetic Coding Implementation for Data Compression

This module provides functions for arithmetic coding, a data compression technique
that encodes the entire input by representing it as a fraction between 0 and 1.
"""

import math
from typing import Dict, Union, List


def arithmetic_encode(data: str, prob_dist: Dict[str, float] = None) -> float:
    """
    Perform arithmetic encoding on the input string.
    
    Args:
        data (str): The input string to be encoded
        prob_dist (Dict[str, float], optional): Probability distribution of characters.
            If not provided, it will be calculated from the input data.
    
    Returns:
        float: The encoded value representing the compressed data
    
    Raises:
        ValueError: If input is empty or probabilities don't sum to 1
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # If no probability distribution is provided, calculate it
    if prob_dist is None:
        prob_dist = _calculate_prob_distribution(data)
    
    # Validate probability distribution
    if not _validate_prob_distribution(prob_dist):
        raise ValueError("Probability distribution must sum to 1 and all values must be between 0 and 1")
    
    # Initialize encoding range
    low, high = 0.0, 1.0
    
    # Sort characters by their probabilities for efficient encoding
    sorted_chars = sorted(prob_dist.keys(), key=lambda x: prob_dist[x])
    
    # Encode each character
    for char in data:
        # Calculate the range
        range_width = high - low
        
        # Update range based on character probability
        high = low + range_width * _cumulative_prob(char, prob_dist, sorted_chars)
        low = low + range_width * _cumulative_prob_start(char, prob_dist, sorted_chars)
    
    # Return the midpoint of the final range
    return (low + high) / 2


def arithmetic_decode(encoded_value: float, length: int, 
                      prob_dist: Dict[str, float]) -> str:
    """
    Decode an arithmetic encoded value back to its original string.
    
    Args:
        encoded_value (float): The encoded value to decode
        length (int): Length of the original string
        prob_dist (Dict[str, float]): Probability distribution of characters
    
    Returns:
        str: The decoded string
    
    Raises:
        ValueError: If inputs are invalid
    """
    # Validate inputs
    if length <= 0:
        raise ValueError("Length must be positive")
    
    if not _validate_prob_distribution(prob_dist):
        raise ValueError("Probability distribution must sum to 1 and all values must be between 0 and 1")
    
    # Sort characters by their probabilities for efficient decoding
    sorted_chars = sorted(prob_dist.keys(), key=lambda x: prob_dist[x])
    
    # Initialize decoding
    decoded = []
    low, high = 0.0, 1.0
    
    # Decode each character
    for _ in range(length):
        range_width = high - low
        
        # Find the character corresponding to the current encoded value
        for char in sorted_chars:
            char_high = low + range_width * _cumulative_prob(char, prob_dist, sorted_chars)
            char_low = low + range_width * _cumulative_prob_start(char, prob_dist, sorted_chars)
            
            if char_low <= encoded_value < char_high:
                decoded.append(char)
                
                # Update range
                high = char_high
                low = char_low
                break
    
    return ''.join(decoded)


def _calculate_prob_distribution(data: str) -> Dict[str, float]:
    """
    Calculate character probabilities from input data.
    
    Args:
        data (str): Input string
    
    Returns:
        Dict[str, float]: Probability distribution of characters
    """
    # Count character frequencies
    char_counts = {}
    for char in data:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Calculate probabilities
    total_chars = len(data)
    return {char: count/total_chars for char, count in char_counts.items()}


def _validate_prob_distribution(prob_dist: Dict[str, float]) -> bool:
    """
    Validate that probabilities sum to 1 and are between 0 and 1.
    
    Args:
        prob_dist (Dict[str, float]): Probability distribution
    
    Returns:
        bool: True if probabilities are valid, False otherwise
    """
    # Check total sum
    if not math.isclose(sum(prob_dist.values()), 1.0, abs_tol=1e-9):
        return False
    
    # Check each probability is between 0 and 1
    return all(0 <= prob <= 1 for prob in prob_dist.values())


def _cumulative_prob_start(char: str, prob_dist: Dict[str, float], 
                            sorted_chars: List[str]) -> float:
    """
    Calculate the starting cumulative probability for a character.
    
    Args:
        char (str): Target character
        prob_dist (Dict[str, float]): Probability distribution
        sorted_chars (List[str]): Sorted list of characters
    
    Returns:
        float: Starting cumulative probability
    """
    return sum(prob_dist[c] for c in sorted_chars 
               if sorted_chars.index(c) < sorted_chars.index(char))


def _cumulative_prob(char: str, prob_dist: Dict[str, float], 
                     sorted_chars: List[str]) -> float:
    """
    Calculate the cumulative probability for a character.
    
    Args:
        char (str): Target character
        prob_dist (Dict[str, float]): Probability distribution
        sorted_chars (List[str]): Sorted list of characters
    
    Returns:
        float: Cumulative probability
    """
    return sum(prob_dist[c] for c in sorted_chars 
               if sorted_chars.index(c) <= sorted_chars.index(char))