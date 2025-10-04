"""
Demo Script for ReAct Agent

This script demonstrates how to use the ReAct agent to organize a messy directory.
Run this script to see the agent in action with a pre-configured test directory.

Usage:
    python demo.py
"""
import argparse
from openai import OpenAI

from src.react_agent import Agent
from src.config.config import config
from src.utils import extract_tool
from src.config.logging_config import get_logger
from src.prompts import chain_of_thought_system_message
from src.tools import get_working_directory, create_directory, move_files

logger = get_logger(__name__)

# Tool registry mapping tool names to their functions
tool_registry = {
    "get_working_directory": get_working_directory,
    "create_directory": create_directory,
    "move_files": move_files
}


def run_agent_loop(agent: Agent, user_message: str) -> None:
    """
    Run the agent loop: send message, extract tool calls, execute tools, repeat.

    Args:
        agent: The ReAct agent instance.
        user_message: The initial user message to the agent.
    """
    response = agent(user_message)
    print("=" * 40, "AI Message", "=" * 40)
    print(response)
    print()

    # Continue loop while agent requests tool execution
    while response.endswith("PAUSE"):
        tool_call = extract_tool(response)

        if tool_call["tool"] not in tool_registry:
            logger.error(f"Tool {tool_call['tool']} not found in tool registry.")
            break

        tool_function = tool_registry[tool_call["tool"]]

        # Execute tool with or without arguments
        if tool_call["args"]:
            tool_result = tool_function(tool_call["args"])
        else:
            tool_result = tool_function()

        print("=" * 40, "Tool Result", "=" * 40)
        print(tool_result)
        print()

        # Send tool result back to the agent
        response = agent(f"Observation: {tool_result}")
        print("=" * 40, "AI Message", "=" * 40)
        print(response)
        print()


def main():
    """Main function to run the demo."""
    user_message = "Please organize my directory and make it more clear and professional."

    # Initialize OpenAI client and agent
    client = OpenAI(api_key=config.openai_api_key.get_secret_value())
    agent = Agent(
        system_message=chain_of_thought_system_message,
        openai_client=client
    )

    # Run the agent
    print(f"User Message: {user_message}\n")
    run_agent_loop(agent, user_message)

    print("\nDemo completed! Check the /working_directory folder to see the organized files: cd working_directory && ls")


if __name__ == "__main__":
    main()