"""
ReAct Agent

This module implements the Agent class that initializes the agent with a system message and an OpenAI client.
Any instance of this class can be called with a user message to pass the message history to OpenAI and
return the response.

Author: Peyman Kh
Last Edited: 03-10-2025
"""
# Import libraries
from openai import OpenAI


class Agent:
    """A class representing a ReAct agent that can engage in conversations using OpenAI API."""
    def __init__(self, system_message: str, openai_client: OpenAI) -> None:
        """
        Initializes the agent with a system message and an OpenAI client.

        Args:
            system_message: The system message to pass to the agent.
            openai_client: The OpenAI client to use for the agent.
        """
        self.client = openai_client
        self.system_message = system_message
        self.messages = []
        if self.system_message:
            self.messages.append({"role": "system", "content": self.system_message})


    def invoke(self) -> str:
        """
        Invoke the LLM by sending the messages history to OpenAI and returning the response.

        Returns:
            str: The response from the LLM.
        """
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=self.messages
        )

        return completion.choices[0].message.content


    def __call__(self, user_message: str) -> str:
        """
        This function makes the Agent instance callable.

        Args:
            user_message(str): The user message to pass to the agent.

        Returns:
            str: The response from the LLM.
        """
        # Add the user message to the messages history
        self.messages.append({"role": "user", "content": user_message})

        result = self.invoke()

        # Add the LLM response to the messages history
        self.messages.append({"role": "assistant", "content": result})

        return result