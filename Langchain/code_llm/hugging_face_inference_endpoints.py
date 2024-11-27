import os
from huggingface_hub import InferenceClient
import json

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"


repo_id = "HuggingFaceH4/zephyr-7b-beta"

llm_client = InferenceClient(
    model=repo_id,
    timeout=120
)

def call_llm(inference_client: InferenceClient, prompt: str):
    response = inference_client.post(
        json={
            "inputs": prompt,
            "task": "text-generation"
        },
    )
    return json.loads(response.decode())[0]["generated_text"]

response = call_llm(llm_client, "Write a java code to check if string is palindrome or not.")
print(response)
