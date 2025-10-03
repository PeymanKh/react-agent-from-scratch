"""
Project Utilities and Helper Functions

This module implements functions to initialize variations of messy directories for testing.

Author: Peyman Kh
Last Edited: 03-10-2025
"""
# Import libraries
import os
import shutil
import logging
from pathlib import Path


logger = logging.getLogger(__name__)

def initialize_personal_directory():
    """
    Initialize a personal test directory for Agent to manipulate.
    It first removes the working directory if it exists and then creates a messy directory.

    Returns:
        dict: A dictionary containing the directory structure.
    """
    working_directory = "working_directory"
    try:
        # Remove the working directory if it exists
        if os.path.exists(working_directory):
            shutil.rmtree(working_directory)

        # Create the working directory
        os.mkdir(working_directory)

        # Add files to the directory
        Path(f"{working_directory}/invoice_2024.pdf").touch()
        Path(f"{working_directory}/vacation_photo.jpg").touch()
        Path(f"{working_directory}/project_proposal.docx").touch()
        Path(f"{working_directory}/setup.exe").touch()
        Path(f"{working_directory}/budget_spreadsheet.xlsx").touch()
        Path(f"{working_directory}/family_video.mp4").touch()
        Path(f"{working_directory}/tax_return_2023.pdf").touch()
        Path(f"{working_directory}/recipes.pdf").touch()
        Path(f"{working_directory}/screenshot_12345.png").touch()
        Path(f"{working_directory}/thesis_final_FINAL_v2.docx").touch()
        Path(f"{working_directory}/presentation.pptx").touch()
        Path(f"{working_directory}/random_notes.txt").touch()
        Path(f"{working_directory}/contract_signed.pdf").touch()
        Path(f"{working_directory}/game_installer.zip").touch()
        Path(f"{working_directory}/backup_code.py").touch()

        logger.info("Personal directory created successfully")

    except Exception as e:
        logger.error(f"Failed to initialize working directory: {e}")


def initialize_developer_directory():
    """
    Initialize a developer test directory for Agent to manipulate.
    It first removes the working directory if it exists and then creates a messy directory.

    Returns:
        dict: A dictionary containing the directory structure.
    """
    working_directory = "working_directory"
    try:
        # Remove the working directory if it exists
        if os.path.exists(working_directory):
            shutil.rmtree(working_directory)

        # Create the working directory
        os.mkdir(working_directory)

        # Add files to the directory
        Path(f"{working_directory}/main.py").touch()
        Path(f"{working_directory}/test.py").touch()
        Path(f"{working_directory}/requirements.txt").touch()
        Path(f"{working_directory}/README.md").touch()
        Path(f"{working_directory}/config.json").touch()
        Path(f"{working_directory}/data_analysis.ipynb").touch()
        Path(f"{working_directory}/old_version.py").touch()
        Path(f"{working_directory}/todo.txt").touch()
        Path(f"{working_directory}/architecture_diagram.png").touch()
        Path(f"{working_directory}/api_documentation.pdf").touch()
        Path(f"{working_directory}/database_schema.sql").touch()
        Path(f"{working_directory}/test_results.csv").touch()
        Path(f"{working_directory}/logo.svg").touch()
        Path(f"{working_directory}/screenshot_bug.png").touch()
        Path(f"{working_directory}/credentials.env").touch()

        logger.info("Developer directory created successfully")

    except Exception as e:
        logger.error(f"Failed to initialize working directory: {e}")
