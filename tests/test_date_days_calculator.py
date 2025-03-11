import pytest
from datetime import datetime, date, timedelta
from src.date_days_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_string_input():
    """Test calculation with string inputs in YYYY-MM-DD format"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-10") == 9
    assert calculate_days_between_dates("2023-01-10", "2023-01-01") == 9

def test_calculate_days_between_dates_date_input():
    """Test calculation with date object inputs"""
    date1 = date(2023, 1, 1)
    date2 = date(2023, 1, 10)
    assert calculate_days_between_dates(date1, date2) == 9
    assert calculate_days_between_dates(date2, date1) == 9

def test_calculate_days_between_dates_datetime_input():
    """Test calculation with datetime object inputs"""
    datetime1 = datetime(2023, 1, 1, 12, 0)
    datetime2 = datetime(2023, 1, 10, 14, 30)
    assert calculate_days_between_dates(datetime1, datetime2) == 9
    assert calculate_days_between_dates(datetime2, datetime1) == 9

def test_calculate_days_between_dates_same_date():
    """Test calculation when dates are the same"""
    assert calculate_days_between_dates("2023-01-01", "2023-01-01") == 0

def test_calculate_days_between_dates_across_years():
    """Test calculation across different years"""
    assert calculate_days_between_dates("2022-12-31", "2023-01-02") == 2

def test_calculate_days_between_dates_invalid_string_format():
    """Test error handling for invalid date string formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("01-01-2023", "2023-01-10")
    
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates("2023-01-01", "10-01-2023")

def test_calculate_days_between_dates_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Inputs must be date, datetime, or valid date strings"):
        calculate_days_between_dates(123, "2023-01-10")
    
    with pytest.raises(TypeError, match="Inputs must be date, datetime, or valid date strings"):
        calculate_days_between_dates("2023-01-01", [1, 2, 3])