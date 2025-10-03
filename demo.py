# import libraries
import logging

from src.config.config import config
from src.tools import move_files, get_working_directory
from src.config.logging_config import get_logger

logger = get_logger(__name__)


if __name__ == "__main__":
    print(get_working_directory())
    print(move_files({"root/api_documentation.pdf": "root/gaming/"}))
