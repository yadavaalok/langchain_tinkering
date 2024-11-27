from langchain.chat_models import init_chat_model

user_config = {
    "openai_api_key": "",
    "api_version": "2024-02-01",
    "azure_endpoint" : "",
    "deployment_name" : "gpt-4o-global-standard",
    "model" : "gpt-4o",
    "model_provider": "openai",
    "max_tokens" : 500,
    "temperature" : 0.0,
}


# Returns a langchain_openai.ChatOpenAI instance.
gpt_4o = init_chat_model(**user_config)
# Returns a langchain_anthropic.ChatAnthropic instance.
claude_opus = init_chat_model(
    "claude-3-opus-20240229", model_provider="anthropic", temperature=0
)
# Returns a langchain_google_vertexai.ChatVertexAI instance.
gemini_15 = init_chat_model(
    "gemini-1.5-pro", model_provider="google_vertexai", temperature=0
)

# Since all model integrations implement the ChatModel interface, you can use them in the same way.
print("GPT-4o: " + gpt_4o.invoke("what's your name").content + "\n")
# print("Claude Opus: " + claude_opus.invoke("what's your name").content + "\n")
# print("Gemini 1.5: " + gemini_15.invoke("what's your name").content + "\n")