from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.llms import AzureOpenAI
from langchain.chat_models import AzureChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_core.messages import SystemMessage
from langchain_core.prompts import MessagesPlaceholder
from langchain_experimental.plan_and_execute.agent_executor import PlanAndExecute
from langchain_experimental.plan_and_execute.executors.agent_executor import (
    load_agent_executor,
)
from langchain_experimental.plan_and_execute.planners.chat_planner import (
    load_chat_planner,
)

from langchain import SerpAPIWrapper, LLMMathChain, WikipediaAPIWrapper
from langchain.agents.tools import Tool

llm = AzureOpenAI(openai_api_key="", api_version="",
                  azure_endpoint="", deployment_name="gpt-35-914",
                  model_name="gpt-35-turbo", max_tokens=1000)

llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)

# search = SerpAPIWrapper()
# wikipedia = WikipediaAPIWrapper()

tools = [
        Tool(name="Current Search",
             func=search.run,
             description="Useful when you need to check that all the user details are collected."
        )
]
memory_key = "history"

system_message = SystemMessage(
        content=(
            "You need to collect user's name and location"
            "First collect this data then only starts conversation"
            "If user doesn't provide the data then again ask for it until all data are collected"
        )
)

memory = ConversationBufferMemory(memory_key=memory_key, return_messages=True)

prompt = OpenAIFunctionsAgent.create_prompt(
        system_message=system_message,
        extra_prompt_messages=[MessagesPlaceholder(variable_name=memory_key)]
    )

model = AzureChatOpenAI(
    azure_endpoint="",
    openai_api_key="",
    openai_api_version="",
    azure_deployment='chat',
)

agent = OpenAIFunctionsAgent(llm=llm, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)
