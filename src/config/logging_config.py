# Import libraries
import logging
from src.config.config import config

def get_logger(name: str) -> logging.Logger:
    """
    Get a configured logger instance for any module.

    Args:
        name: Usually __name__ from the calling module

    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)

    # Only configure if not already configured
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(config.log_format)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(getattr(logging, config.log_level.value))

    return logger
