from collections import Counter
from typing import Dict, List, Union

def shannon_fano_encode(data: Union[str, List[str]]) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Shannon-Fano coding is a method of generating a prefix code for data compression 
    where symbols are assigned variable-length codes based on their frequency.
    
    Args:
        data (str or List[str]): Input data to be encoded
    
    Returns:
        Dict[str, str]: A dictionary mapping original symbols to their encoded representation
    
    Raises:
        ValueError: If input data is empty or invalid
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to list if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Count frequency of each symbol
    freq_counter = Counter(data)
    
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(freq_counter.items(), key=lambda x: x[1], reverse=True)
    
    # Generate Shannon-Fano codes
    def generate_codes(symbols):
        if len(symbols) <= 1:
            return {symbols[0][0]: '0'} if symbols else {}
        
        # Find the split point that most evenly divides total frequency
        total_freq = sum(freq for _, freq in symbols)
        current_freq = 0
        best_split = 0
        min_diff = float('inf')
        
        for i in range(len(symbols)):
            current_freq += symbols[i][1]
            remaining_freq = total_freq - current_freq
            
            diff = abs(current_freq - remaining_freq)
            if diff < min_diff:
                min_diff = diff
                best_split = i + 1
        
        # Recursively generate codes for each group
        left_codes = generate_codes(symbols[:best_split])
        right_codes = generate_codes(symbols[best_split:])
        
        # Prefix codes
        for symbol in left_codes:
            left_codes[symbol] = '0' + left_codes[symbol]
        
        for symbol in right_codes:
            right_codes[symbol] = '1' + right_codes[symbol]
        
        return {**left_codes, **right_codes}
    
    # Generate and return the codes
    return generate_codes(sorted_symbols)

def shannon_fano_decode(encoded_data: Dict[str, str], encoded_message: str) -> str:
    """
    Decode a message that was encoded using Shannon-Fano coding.
    
    Args:
        encoded_data (Dict[str, str]): Dictionary of symbol to code mappings
        encoded_message (str): The encoded binary message
    
    Returns:
        str: The decoded original message
    
    Raises:
        ValueError: If decoding is not possible
    """
    # Validate input
    if not encoded_message or not encoded_data:
        raise ValueError("Incomplete or invalid encoded message")
    
    # Validate encoding contains only 0s and 1s
    if not all(bit in '01' for bit in encoded_message):
        raise ValueError("Incomplete or invalid encoded message")
    
    # Create reverse mapping for decoding
    reverse_mapping = {code: symbol for symbol, code in encoded_data.items()}
    codes = list(reverse_mapping.keys())
    
    # Validate codes are unique and prevent prefix overlap
    for i, code1 in enumerate(codes):
        for code2 in codes[i+1:]:
            if code1.startswith(code2) or code2.startswith(code1):
                raise ValueError("Incomplete or invalid encoded message")
    
    decoded_message = []
    current_code = ''
    
    for bit in encoded_message:
        current_code += bit
        
        # If current code is a complete code, add to decoded message
        if current_code in reverse_mapping:
            decoded_message.append(reverse_mapping[current_code])
            current_code = ''
        # If no code starts with current prefix, raise error
        elif not any(code.startswith(current_code) for code in codes):
            raise ValueError("Incomplete or invalid encoded message")
        
        # Prevent overrunning the available codes
        if len(current_code) > max(len(code) for code in codes):
            raise ValueError("Incomplete or invalid encoded message")
    
    # Check if entire message was decoded
    if current_code:
        raise ValueError("Incomplete or invalid encoded message")
    
    if not decoded_message:
        raise ValueError("Incomplete or invalid encoded message")
    
    return ''.join(decoded_message)