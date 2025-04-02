import pytest
from src.shannon_fano_compression import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_encode_basic():
    """Test basic encoding functionality"""
    data = ['A', 'A', 'B', 'C', 'C', 'C']
    encoding = shannon_fano_encode(data)
    
    # Check that all symbols have unique codes
    assert len(set(encoding.values())) == len(encoding)
    
    # Verify that most frequent symbol has a shorter code
    assert len(encoding['C']) <= len(encoding['B'])
    assert len(encoding['B']) <= len(encoding['A'])

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
    
    with pytest.raises(ValueError):
        shannon_fano_decode(encoding, '01010')  # Incomplete decoding

def test_shannon_fano_complex_encoding():
    """Test encoding with complex frequency distribution"""
    data = ['A', 'A', 'A', 'B', 'B', 'C', 'D', 'D', 'D', 'D']
    encoding = shannon_fano_encode(data)
    
    # Verify code lengths reflect frequency
    assert len(encoding['A']) <= len(encoding['B'])
    assert len(encoding['B']) <= len(encoding['C'])
    assert len(encoding['A']) <= len(encoding['D'])