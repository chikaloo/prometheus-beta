import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_basic():
    """Test basic run-length encoding scenarios."""
    assert run_length_encode('AABBBCCCC') == '2A3B4C'
    assert run_length_encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB') == '12W1B12W3B24W1B'

def test_run_length_encode_single_char():
    """Test encoding with a single character."""
    assert run_length_encode('A') == '1A'
    assert run_length_encode('Z') == '1Z'

def test_run_length_encode_list_input():
    """Test encoding with list input."""
    assert run_length_encode(['A', 'A', 'B', 'B', 'B']) == '2A3B'
    assert run_length_encode([1, 1, 1, 2, 2]) == '3A2B'

def test_run_length_encode_error_handling():
    """Test error handling for encoding."""
    with pytest.raises(TypeError):
        run_length_encode(12345)

def test_run_length_decode_basic():
    """Test basic run-length decoding scenarios."""
    assert run_length_decode('2A3B4C') == 'AABBBCCCC'
    assert run_length_decode('12W1B12W3B24W1B') == 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB'

def test_run_length_decode_single_char():
    """Test decoding with a single character."""
    assert run_length_decode('1A') == 'A'
    assert run_length_decode('1Z') == 'Z'

def test_run_length_decode_error_handling():
    """Test error handling for decoding."""
    with pytest.raises(TypeError):
        run_length_decode(12345)
    
    with pytest.raises(ValueError):
        run_length_decode('A')  # No count before character
    
    with pytest.raises(ValueError):
        run_length_decode('1')  # Incomplete encoding

def test_encode_decode_roundtrip():
    """Test that encoding followed by decoding returns the original input."""
    test_cases = [
        'AABBBCCCC',
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB',
        'A',
        '12345',
        'abcdefg'
    ]
    
    for test_input in test_cases:
        encoded = run_length_encode(test_input)
        decoded = run_length_decode(encoded)
        assert decoded == test_input

def test_empty_input_handling():
    """Test handling of empty inputs."""
    assert run_length_encode('') == ''
    assert run_length_decode('') == ''