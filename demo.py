# import libraries
from openai import OpenAI

from src.react_agent import Agent
from src.config.config import config
from src.utils import extract_tool, initialize_developer_directory
from src.config.logging_config import get_logger
from src.prompts import chain_of_though_system_message
from src.tools import get_working_directory, create_directory, move_files

logger = get_logger(__name__)

tool_registry = {
    "get_working_directory": get_working_directory,
    "create_directory": create_directory,
    "move_files": move_files
}

if __name__ == "__main__":
    client = OpenAI(api_key=config.openai_api_key.get_secret_value())
    agent = Agent(system_message=chain_of_though_system_message, openai_client=client)
    response = agent("Please organize code directory and make it more clear")
    print("="*40, "AI Message", "="*40)
    print(response)

    while response.endswith("PAUSE"):
        tool_call = extract_tool(response)

        if tool_call["tool"] not in tool_registry:
            logger.error(f"Tool {tool_call['tool']} not found in tool registry.")
            break

        tool_function = tool_registry[tool_call["tool"]]

        if tool_call["args"]:
            tool_result = tool_function(tool_call["args"])
        else:
            tool_result = tool_function()

        print("="*40, "Tool Result", "="*40)
        print(tool_result, "\n")

        response = agent(f"Observation: {tool_result}")
        print("="*40, "AI Message", "="*40)
        print(response)