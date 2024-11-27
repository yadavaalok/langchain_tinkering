from langchain_core.tools import Tool
from langchain.tools import BaseTool
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from typing import Optional, Type


# Function to collect user details
def collect_user_details(query):
    # Prompt the user for their name, location, and age
    name = input("Please enter your name: ")
    location = input("Please enter your location: ")
    age = input("Please enter your age: ")

    return "Thank you for providing your details. Let's start the conversation."


# Define the tool for collecting user details
class UserDetailsTool(BaseTool):
    name = "Starting Answers"
    description = "Tool for collecting user details"

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return collect_user_details(query)

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")


# Create an instance of the UserDetailsTool
user_details_tool = UserDetailsTool()