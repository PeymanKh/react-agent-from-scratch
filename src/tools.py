"""
Agent Tools

This module implements three tools needed by the agent to manipulate the filesystem.

Here is the list of available tools:
1. get_working_directory(): Returns a dictionary mapping directory paths to their contents.
2. create_directory(directory_path_list: list[str]): Creates provided directories.
3. move_files(file_map: dict[str, str]): Moves the files from one directory to another.

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
    working_directory = "working_directory"
    result = {}

    try:
        for root, dirs, files in os.walk(working_directory):
            # Get the relative path of the current directory
            rel_path = os.path.relpath(root, working_directory)
            # Create a key for the dictionary with the relative path as the key
            key = "root" if rel_path == "." else f"root/{rel_path.replace(os.sep, '/')}"
            # Add the directories and files to the dictionary
            result[key] = dirs + files

        # Log the result and return the working directory
        logger.info("Working directory retrieved successfully")
        return result

    except Exception as e:
        logger.error(f"Failed to get working directory: {e}")
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

        # Log the result and return the working directory after changes
        logger.info(f"{len(directory_path_list)} directories created successfully")
        return get_working_directory()

    except Exception as e:
        logger.error(f"Failed to create directory: {e}")
        return {"msg": "Failed to create directories"}


def move_files(file_map: dict[str, str]) -> dict:
    """
    Get a dictionary of file paths as keys and destination paths as values and moves the files.

    Args:
        file_map: A dictionary of file paths as keys and destination paths as values.

    Returns:
        dict: A dictionary of directories and their content after changes.
    """
    file_counter = 0

    try:
        for file_path, destination_path in file_map.items():
            if "root" in file_path:
                # Replace "root" with "working_directory"
                file_path = file_path.replace("root", "working_directory")
            if "root" in destination_path:
                # Replace "root" with "working_directory"
                destination_path = destination_path.replace("root", "working_directory")

            # Move the file and increase the counter
            shutil.move(file_path, destination_path)
            file_counter += 1

        # Log the result and return the working directory after changes
        logger.info(f"{file_counter} Files moved successfully")
        return get_working_directory()

    except Exception as e:
        logger.error(f"Failed to move files: {e}")
        return {"msg": "Failed to move files"}

