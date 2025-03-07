import logging
import os
from datetime import datetime

def setup_logger(name, log_filename):
    """
    Creates and configures a logger with both console and file handlers.

    Args:
        name (str): Logger name.
        log_filename (str): Log file name.

    Returns:
        logging.Logger: Configured logger instance.
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"{log_filename}_{datetime.now().strftime('%Y-%m-%d')}.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if not logger.handlers:
        # Console Handler (DEBUG and above)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # File Handler (ERROR and above)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.ERROR)

        # Log Format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Attach Handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger