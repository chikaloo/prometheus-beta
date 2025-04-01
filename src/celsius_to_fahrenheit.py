def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius degrees.

    Returns:
        float: Equivalent temperature in Fahrenheit degrees.

    Raises:
        TypeError: If input is not a number.
    """
    # Check if input is a number
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number (integer or float)")
    
    # Standard Celsius to Fahrenheit conversion formula
    fahrenheit = (celsius * 9/5) + 32
    
    return fahrenheit