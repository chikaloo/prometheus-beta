import logging

def log_multiple_values(level, *values, logger=None, separator=' | '):
    """
    Log multiple values in a single statement with flexible configuration.

    Args:
        level (str): Logging level ('debug', 'info', 'warning', 'error', 'critical')
        *values: Variable number of values to log
        logger (logging.Logger, optional): Custom logger. Uses root logger if not provided.
        separator (str, optional): Separator between logged values. Defaults to ' | '.

    Raises:
        ValueError: If an invalid logging level is provided
        TypeError: If logger is not a valid logger
    """
    # Use root logger if no logger is specified
    if logger is None:
        logger = logging.getLogger()

    # Validate logger type
    if not hasattr(logger, 'debug') or not hasattr(logger, 'info') or \
       not hasattr(logger, 'warning') or not hasattr(logger, 'error') or \
       not hasattr(logger, 'critical'):
        raise TypeError("Invalid logger object")

    # Convert all values to strings and join
    log_message = separator.join(str(value) for value in values)

    # Map logging levels to corresponding logger methods
    log_methods = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }

    # Validate and execute logging
    if level.lower() not in log_methods:
        raise ValueError(f"Invalid logging level: {level}. Must be one of: debug, info, warning, error, critical")

    # Call the appropriate logging method
    log_methods[level.lower()](log_message)