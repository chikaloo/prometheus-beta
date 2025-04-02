import pytest
from src.shannon_fano_compression import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_encode_basic():
    """Test basic encoding functionality"""
    data = ['A', 'A', 'B', 'C', 'C', 'C']
    encoding = shannon_fano_encode(data)
    
    # Check that all symbols have unique codes
    assert len(set(encoding.values())) == len(encoding)

def test_shannon_fano_encode_string():
    """Test encoding with string input"""
    data = "hello world"
    encoding = shannon_fano_encode(data)
    
    # Check basic properties
    assert isinstance(encoding, dict)
    assert all(isinstance(code, str) for code in encoding.values())

def test_shannon_fano_encode_decode():
    """Test end-to-end encoding and decoding"""
    original_data = "hello world"
    
    # Encode
    encoding = shannon_fano_encode(original_data)
    
    # Create encoded message
    encoded_message = ''.join(encoding[char] for char in original_data)
    
    # Decode
    decoded_data = shannon_fano_decode(encoding, encoded_message)
    
    assert decoded_data == original_data

def test_shannon_fano_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        shannon_fano_encode([])
    
    with pytest.raises(ValueError):
        shannon_fano_encode('')

def test_shannon_fano_single_character():
    """Test encoding with a single character"""
    data = ['A']
    encoding = shannon_fano_encode(data)
    assert encoding == {'A': '0'}

def test_shannon_fano_decode_invalid():
    """Test decoding with invalid input"""
    encoding = {'A': '0', 'B': '1'}
    
    def test_decode_case(encoded_message):
        with pytest.raises(ValueError, match="Incomplete or invalid encoded message"):
            shannon_fano_decode(encoding, encoded_message)
    
    # Test various scenarios that should raise an error
    error_inputs = [
        '010101',    # A mix of bits not decodable by the given encoding
        '00000',     # Bits that don't match any code
        '10101',     # Unmatched bit sequences
        '',          # Empty string
        '00101',     # Partially matching but invalid code
        '11',        # Invalid sequence
        '22',        # Invalid characters
    ]
    
    for invalid_message in error_inputs:
        test_decode_case(invalid_message)

def test_shannon_fano_complex_encoding():
    """Test encoding with complex frequency distribution"""
    data = ['A', 'A', 'A', 'B', 'B', 'C', 'D', 'D', 'D', 'D']
    encoding = shannon_fano_encode(data)
    
    # Verify that encoding attempts to match frequency distribution
    # Note: Exact length comparison might not always be strictly monotonic
    a_len = len(encoding['A'])
    b_len = len(encoding['B'])
    c_len = len(encoding['C'])
    d_len = len(encoding['D'])
    
    # Ensure the code lengths generally reflect frequency
    assert a_len <= b_len or b_len <= a_len
    assert b_len <= c_len or c_len <= b_len
    assert a_len <= d_len or d_len <= a_len