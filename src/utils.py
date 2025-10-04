"""
Project Utilities and Helper Functions

This module implements utilities and helper functions for the project.

Functions:
1. initialize_personal_directory(): Initializes a personal test directory for Agent to manipulate.
2. initialize_developer_directory(): Initializes a developer test directory for Agent to manipulate.
3. extract_tool(llm_response: str) -> dict: Parses the LLM response and returns the tool name and arguments.

Author: Peyman Kh
Last Edited: 03-10-2025
"""
# Import libraries
import re
import os
import ast
import shutil
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def initialize_personal_directory():
    """
    Initialize a personal test directory for Agent to manipulate.
    It first removes the working directory if it exists and then creates a messy directory.
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


def extract_tool(llm_response: str) -> dict:
    """
    This function parses the LLM response and returns the tool name and arguments.

    Args:
        llm_response (str): The LLM response string.

    Returns:
        dict: A dictionary containing the tool name and arguments.
    """
    # Regex pattern to extract tool name and arguments
    pattern = r'Tool:\s*(\w+)\((.*?)\)'

    # Search for the pattern in the response
    match = re.search(pattern, llm_response, re.DOTALL)

    # Return None if no match is found
    if not match:
        logger.info("No tool found in the response")
        return {"tool": None, "args": None}

    tool_name = match.group(1).strip()
    tool_args = match.group(2).strip()

    # Handle empty arguments (no args case)
    if not tool_args:
        logger.info(f"Tool found in the response: {tool_name}()")
        return {"tool": tool_name, "args": None}

    try:
        parsed_args = ast.literal_eval(tool_args)
        logger.info(f"Tool found in the response: {tool_name}({parsed_args})")
        return {"tool": tool_name, "args": parsed_args}
    except (ValueError, SyntaxError) as e:
        logger.error(f"Could not parse arguments: {e}")
        return {"tool": tool_name, "args": None}