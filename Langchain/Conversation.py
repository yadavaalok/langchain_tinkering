from langchain.chains import ConversationChain
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_openai import AzureOpenAI
from utils.sample3 import collect_data


llm = AzureOpenAI(openai_api_key="", api_version="",
                  azure_endpoint="", deployment_name="gpt-35-914",
                  model_name="gpt-35-turbo", max_tokens=1000)


conversation = ConversationChain(llm=llm, verbose=False)

data = {}
flag = True
history = ChatMessageHistory()
while flag:
    human_input = input("You: ")
    history.add_user_message(human_input)
    print(collect_data(human_input))
    ai_response = conversation.predict(input=human_input)
    history.add_ai_message(ai_response)

    if human_input == "/stop":
        ai_response = "It's nice to meet you!! See you next time :)"
        flag = False
    print(f"AI: {ai_response}")

# print("Whole Conversation: \n", history.messages)
print(data)