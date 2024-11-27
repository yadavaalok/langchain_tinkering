import os
from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import ChatHuggingFace
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
)

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceHub(
    # repo_id="microsoft/Phi-3-mini-4k-instruct",
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
)

system_prompt = """
You are an AI specialized in code generation, code completion, and related tasks.
Your role is to provide the requested code without any additional explanations or commentary.
Strictly just give the code, no explanation or comments.

This is the user question : {}
"""

# system_prompt = """
# <|system|>
#
# You are an AI specialized in code generation, code completion, and related tasks.
# Your role is to provide the requested code without any additional explanations or commentary.
# Strictly just give the code, no explanation or comments.
# <|end|>
# <|user|>
# Write a python code to read an excel and print it's column.
# <|end|>
# <|assistant|>
# """


# messages = [
#     SystemMessage(content=system_prompt),
#     HumanMessage(
#         content="Write a python code to read an excel and print it's column."
#     ),
# ]

chat_model = ChatHuggingFace(llm=llm)

ai_msg = chat_model.invoke(system_prompt.format("Write a python code to read an excel and print it's column."))

print(ai_msg.content)
