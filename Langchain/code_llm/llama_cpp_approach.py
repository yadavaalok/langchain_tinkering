from langchain_community.llms import HuggingFaceHub
import os
from getpass import getpass

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-v0.1",
    model_kwargs={"temperature": 0.5, "max_length": 64,"max_new_tokens":512},
)

query = "Write a python program to add 2 numbers."

prompt = f"""
 <|system|>
You are an AI assistant that follows instruction extremely well.
Please be truthful and give direct answers
</s>
 <|user|>
 {query}
 </s>
 <|assistant|>
"""

response = llm.predict(prompt)
print(response)