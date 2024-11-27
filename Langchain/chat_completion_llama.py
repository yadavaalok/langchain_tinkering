import json

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import vertexai.preview
from google.auth import default, transport
import google.auth
import google.auth.transport.requests
from google.oauth2 import service_account


# credentials, _ = default()
# auth_request = transport.requests.Request()
# credentials.refresh(auth_request)

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']

# Replace 'NAME_OF_FILE' with your service account JSON file name that you downloaded
SERVICE_ACCOUNT_FILE = 'document.json'

# Load credentials from the service account file with the specified SCOPES
cred = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Create an authentication request
auth_req = google.auth.transport.requests.Request()

# Refresh the credentials
cred.refresh(auth_req)

# Obtain the bearer token
bearer_token = cred.token

vertexai.init(project="mpaas-generativeai-dev-358327", location="us-central1")

llm = ChatOpenAI(
    model="meta/llama3-405b-instruct-maas",
    base_url="",
    api_key=bearer_token,
    stream=False
)

# template = "You are an AI assistant that helps people find information"
#
# prompt = PromptTemplate(input_variables=["messages"], template=template)
#
# chain = llm | prompt
#
# response = chain.invoke({"messages": "Hello"})

template = """You are an AI assistant that helps people find information.
User asks a question: {messages}, so you need to provide information on that.
"""

prompt = PromptTemplate(input_variables=["messages"], template=template)

text_to_translate = "Hi, what's your name?"  # @param {type:"string"}
target_language = "Italian"  # @param {type:"string"}\
question = "What is ollama?"

chain = prompt | llm

messages = [
    {
        "role": "system",
        "content": """You are an AI assistant. Your goal is to answer questions using the pieces of context. If you don't know the answer, say that you don't know.""",
    },
    {"role": "user", "content": "what is mxuv?"}
]

messages = [{'content': 'You are an AI assistant that helps people find information. User asks a question: {messages}, so you need to provide information on that.features of mxuv700', 'role': 'user'}]

messages = [{'role': 'assistant', 'content': 'You are an AI assistant that helps people find information. User asks a question: {messages}, so you need to provide information on that.'}, {'role': 'user', 'content': 'features of mxuv700'}]

response = chain.invoke({"messages": messages})

print(response.content)

