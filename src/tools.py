"""
Agent Tools

This module implements all tools needed by the ReAct Agent to read and manipulate directories and files.

Author: Peyman Kh
Last Edited: 03-10-2025
"""
# Import libraries
import os
import shutil
import logging

logger = logging.getLogger(__name__)


def get_working_directory() -> dict:
    """
    Return a dictionary mapping each directory path to its contained files and folders at the root.

    Returns:
        dict: A dictionary of directories and their contents.
    """
    import os

    working_directory = "working_directory"
    result = {}

    try:
        for root, dirs, files in os.walk(working_directory):
            rel_path = os.path.relpath(root, working_directory)
            key = "root" if rel_path == "." else f"root/{rel_path.replace(os.sep, '/')}"
            result[key] = dirs + files

        return result
    except Exception as e:
        logging.error(f"Failed to get working directory: {e}")
        return {"msg": "Failed to get working directory"}


def create_directory(directory_path_list: list[str]) -> dict:
    """
    Get a list of directory paths and creates them.

    Args:
        directory_path_list: A list of directory paths.

    Returns:
        dict: A dictionary of directories and their content after changes.
    """
    try:
        # Create directories
        for directory_path in directory_path_list:
            if "root" in directory_path:
                # Replace "root" with "working_directory"
                directory_path = directory_path.replace("root", "working_directory")

                # Create the directory if it doesn't exist
                os.makedirs(directory_path, exist_ok=True)

        return get_working_directory()

    except Exception as e:
        logging.error(f"Failed to create directory: {e}")
        return {"msg": "Failed to create directories"}


def move_files(file_map: dict[str, str]) -> dict:
    """
    Get a dictionary of a file path as keys and destination path as values and moves the files.

    Args:
        file_map: A dictionary of file paths as keys and destination paths as values.

    Returns:
        dict: A dictionary of directories and their content after changes.
    """
    try:
        for file_path, destination_path in file_map.items():
            if "root" in file_path:
                # Replace "root" with "working_directory"
                file_path = file_path.replace("root", "working_directory")
            if "root" in destination_path:
                # Replace "root" with "working_directory"
                destination_path = destination_path.replace("root", "working_directory")
            shutil.move(file_path, destination_path)

        logger.info("Files moved successfully.")
        return get_working_directory()

    except Exception as e:
        logger.error(f"Failed to move files: {e}")
        return {"msg": "Failed to move files"}

