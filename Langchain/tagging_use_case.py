from langchain_openai import AzureChatOpenAI
from langchain.chains import create_tagging_chain
schema = {
    "properties": {
        "sentiment": {"type": "string"},
        "aggressiveness": {"type": "integer"},
        "language": {"type": "string"},
    }
}

llm = AzureChatOpenAI(
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="",
        azure_deployment='',
    )

chain = create_tagging_chain(schema, llm)

test_string = "Hey there!! We are going to celerate john's birthday. Suggest some celebration idea."

res = chain.invoke(test_string)
print(res)
