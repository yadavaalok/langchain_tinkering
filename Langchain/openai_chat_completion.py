import os
from langchain.llms import AzureOpenAI

client = AzureOpenAI(
  azure_endpoint = "",
  api_key="",
  api_version="2024-02-15-preview"
)

message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."}]

completion = client.chat.completions.create(
  model="gpt-35-turbo-1106",
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion.choices[0].message.content)