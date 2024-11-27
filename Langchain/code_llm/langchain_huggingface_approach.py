import os

from langchain_community.llms import HuggingFaceHub

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

codeSlm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-v0.1",
    model_kwargs={"max_length":180}
)


def generate_code(llm, text) -> str:
    return llm(f"Generate code for this: {text}!")


text = "Write a code to add 2 numbers in java."

res = generate_code(codeSlm, text)
print(res)
