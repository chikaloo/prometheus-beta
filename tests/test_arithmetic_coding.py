"""
Test suite for Arithmetic Coding implementation
"""

import pytest
import math
from src.arithmetic_coding import (
    arithmetic_encode, 
    arithmetic_decode, 
    _calculate_prob_distribution,
    _validate_prob_distribution
)


def test_prob_distribution_calculation():
    """Test probability distribution calculation"""
    data = "hello"
    prob_dist = _calculate_prob_distribution(data)
    
    assert len(prob_dist) == 4  # 4 unique characters
    assert all(0 <= prob < 1 for prob in prob_dist.values())
    assert math.isclose(sum(prob_dist.values()), 1.0)


def test_prob_distribution_validation():
    """Test probability distribution validation"""
    valid_dist = {'a': 0.5, 'b': 0.5}
    invalid_dist1 = {'a': 0.3, 'b': 0.3}  # Doesn't sum to 1
    invalid_dist2 = {'a': 1.5, 'b': -0.5}  # Probabilities out of range
    
    assert _validate_prob_distribution(valid_dist) is True
    assert _validate_prob_distribution(invalid_dist1) is False
    assert _validate_prob_distribution(invalid_dist2) is False


def test_basic_arithmetic_coding():
    """Test basic arithmetic encoding and decoding"""
    data = "hello"
    
    # Encode without custom probability distribution
    encoded = arithmetic_encode(data)
    
    # Decode using the same length and automatically calculated distribution
    decoded = arithmetic_decode(encoded, len(data), 
                                _calculate_prob_distribution(data))
    
    assert decoded == data


def test_custom_prob_distribution():
    """Test arithmetic coding with custom probability distribution"""
    data = "hello"
    custom_prob_dist = {
        'h': 0.2,
        'e': 0.2,
        'l': 0.3,
        'o': 0.3
    }
    
    # Encode with custom distribution
    encoded = arithmetic_encode(data, custom_prob_dist)
    
    # Decode with the same custom distribution
    decoded = arithmetic_decode(encoded, len(data), custom_prob_dist)
    
    assert decoded == data


def test_edge_cases():
    """Test edge cases and error handling"""
    # Empty input
    with pytest.raises(ValueError):
        arithmetic_encode("")
    
    # Invalid probability distribution
    invalid_dist = {'a': 0.5, 'b': 0.6}  # Sums to > 1
    with pytest.raises(ValueError):
        arithmetic_encode("test", invalid_dist)
    
    # Decoding with zero or negative length
    with pytest.raises(ValueError):
        arithmetic_decode(0.5, 0, {'a': 1.0})
    with pytest.raises(ValueError):
        arithmetic_decode(0.5, -1, {'a': 1.0})


def test_different_data_types():
    """Test arithmetic coding with different data types and patterns"""
    test_cases = [
        "aaaa",  # Uniform character
        "abcde",  # Varied characters
        "11223344",  # Numeric
        "!@#$%^",  # Special characters
    ]
    
    for data in test_cases:
        encoded = arithmetic_encode(data)
        decoded = arithmetic_decode(encoded, len(data), 
                                    _calculate_prob_distribution(data))
        assert decoded == data