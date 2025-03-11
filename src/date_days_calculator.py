from datetime import datetime, date

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime or date): First date 
        date2 (str or datetime or date): Second date

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        TypeError: If input is not a valid date type
        ValueError: If input cannot be parsed as a date
    """
    # Convert inputs to date objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.strptime(date1, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}. Use YYYY-MM-DD")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.strptime(date2, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}. Use YYYY-MM-DD")
    
    # Ensure inputs are date or datetime objects
    if not (isinstance(date1, (date, datetime)) and isinstance(date2, (date, datetime))):
        raise TypeError("Inputs must be date, datetime, or valid date strings")
    
    # Convert to date objects if they are datetime
    if isinstance(date1, datetime):
        date1 = date1.date()
    if isinstance(date2, datetime):
        date2 = date2.date()
    
    # Calculate and return absolute number of days
    return abs((date2 - date1).days)