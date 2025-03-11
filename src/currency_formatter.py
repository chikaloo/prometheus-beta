import logging
from typing import Union

def log_currency_number(number: Union[int, float], currency_symbol: str = '$') -> str:
    """
    Format and log a number with a specified currency symbol.

    Args:
        number (int or float): The number to be formatted and logged.
        currency_symbol (str, optional): Currency symbol to use. Defaults to '$'.

    Returns:
        str: Formatted currency string.

    Raises:
        ValueError: If the number is negative or the currency symbol is invalid.
    """
    # Validate inputs
    if not isinstance(number, (int, float)):
        raise TypeError("Number must be an int or float")
    
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    if not currency_symbol or len(currency_symbol.strip()) == 0:
        raise ValueError("Currency symbol cannot be empty")

    # Format the number with two decimal places
    formatted_number = f"{currency_symbol}{number:,.2f}"

    # Log the formatted number
    logging.info(formatted_number)

    return formatted_number