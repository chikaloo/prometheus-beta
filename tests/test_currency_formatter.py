import pytest
import logging
from src.currency_formatter import log_currency_number

def test_log_currency_number_default_symbol(caplog):
    """Test logging with default $ symbol"""
    caplog.set_level(logging.INFO)
    result = log_currency_number(1234.56)
    assert result == '$1,234.56'
    assert '$1,234.56' in caplog.text

def test_log_currency_number_custom_symbol(caplog):
    """Test logging with custom currency symbol"""
    caplog.set_level(logging.INFO)
    result = log_currency_number(1234.56, '£')
    assert result == '£1,234.56'
    assert '£1,234.56' in caplog.text

def test_log_currency_number_integer(caplog):
    """Test logging an integer number"""
    caplog.set_level(logging.INFO)
    result = log_currency_number(1234)
    assert result == '$1,234.00'
    assert '$1,234.00' in caplog.text

def test_log_currency_number_zero(caplog):
    """Test logging zero"""
    caplog.set_level(logging.INFO)
    result = log_currency_number(0)
    assert result == '$0.00'
    assert '$0.00' in caplog.text

def test_log_currency_number_invalid_type():
    """Test raising TypeError for invalid input type"""
    with pytest.raises(TypeError, match="Number must be an int or float"):
        log_currency_number("123")

def test_log_currency_number_negative():
    """Test raising ValueError for negative number"""
    with pytest.raises(ValueError, match="Number must be non-negative"):
        log_currency_number(-100)

def test_log_currency_number_empty_symbol():
    """Test raising ValueError for empty currency symbol"""
    with pytest.raises(ValueError, match="Currency symbol cannot be empty"):
        log_currency_number(100, '')