import logging

def log_object_details(obj):
    """
    Log the keys and values of an object.

    Args:
        obj (dict): The object (dictionary) to log.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    # Validate input is a dictionary
    if not isinstance(obj, dict):
        raise TypeError("Input must be a dictionary")

    # Check if dictionary is empty
    if not obj:
        logging.warning("Empty dictionary provided")
        return

    # Log each key-value pair
    logging.info("Object Details:")
    for key, value in obj.items():
        logging.info(f"Key: {key}, Value: {value}")