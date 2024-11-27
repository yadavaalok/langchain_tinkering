from langchain.agents import initialize_agent, AgentType
from langchain_core.language_models import BaseLanguageModel
from langchain_core.tools import BaseTool
from langchain_core.prompts import BasePromptTemplate
from langchain.agents.self_ask_with_search.base import create_self_ask_with_search_agent, AgentExecutor
from langchain_openai import AzureOpenAI

from core.custom_tool import UserDetailsTool
from langchain_core.tools import Tool

# Define the language model to be used by the agent
# language_model = BaseLanguageModel()  # Replace with the desired language model


# Define the tools available to the agent
tools = [Tool(
        name="User Details",
        func=UserDetailsTool.run,
        description="useful for when you want to get user details"
    )]  # Replace with the actual tool instance

llm = AzureOpenAI(openai_api_key="", api_version="",
                  azure_endpoint="", deployment_name="gpt-35-914",
                  model_name="gpt-35-turbo", max_tokens=1000)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# agent.invoke("Hi I am Alok")

# Define the prompt template for the agent
# prompt_template = BasePromptTemplate()

# Create the "Self-ask with search" agent using the tools, language model, and prompt template
# agent = create_self_ask_with_search_agent(language_model, tools, prompt_template)

# Create an instance of the AgentExecutor to run the agent
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Invoke the agent to start the conversation and collect user details
agent_executor.invoke({"input": "Hi, I am Alok"})  # Replace "start" with the desired input prompt