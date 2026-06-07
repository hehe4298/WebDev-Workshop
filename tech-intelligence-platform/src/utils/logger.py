import logging
import os

def setup_logger():
    """Sets up and returns a configured logger."""
    # Ensure logs directory exists
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, "app.log")

    logger = logging.getLogger("TechIntelligencePlatform")
    logger.setLevel(logging.INFO)

    # Avoid adding handlers multiple times if logger is already setup
    if not logger.handlers:
        # Create handlers
        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(log_format)
        console_handler.setFormatter(log_format)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()
