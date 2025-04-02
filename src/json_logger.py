import json
import logging

def log_json(logger, level, json_obj, message=None):
    """
    Log a JSON object with proper formatting and optional additional message.

    Args:
        logger (logging.Logger): The logger to use for logging.
        level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
        json_obj (dict): The JSON object to log.
        message (str, optional): Additional context message to prepend to the JSON log.

    Raises:
        TypeError: If json_obj is not a dictionary or logger is not a valid logger.
        ValueError: If json_obj cannot be serialized to JSON.

    Returns:
        None
    """
    # Validate inputs
    if not isinstance(logger, logging.Logger):
        raise TypeError("First argument must be a valid logging.Logger instance")
    
    if not isinstance(json_obj, dict):
        raise TypeError("JSON object must be a dictionary")
    
    try:
        # Serialize JSON with indentation for readability
        formatted_json = json.dumps(json_obj, indent=2)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Unable to serialize JSON object: {e}")
    
    # Prepare log message
    log_message = formatted_json if message is None else f"{message}\n{formatted_json}"
    
    # Log the message at the specified level
    logger.log(level, log_message)