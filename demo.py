# import libraries
import logging

from src.config.config import config
from src.utils import initialize_personal_directory, initialize_developer_directory
from src.config.logging_config import get_logger

logger = get_logger(__name__)


if __name__ == "__main__":
    initialize_developer_directory()
