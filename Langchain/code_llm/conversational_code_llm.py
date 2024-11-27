from langchain.chains.conversation.base import ConversationChain
from langchain_community.chat_message_histories import ChatMessageHistory
import os
from langchain_community.llms import HuggingFaceHub


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

codeSlm = HuggingFaceHub(
    # repo_id="mistralai/Mistral-7B-v0.1",
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    model_kwargs={"max_length":180}
)

conversation = ConversationChain(llm=codeSlm, verbose=False)

data = {}
flag = True
history = ChatMessageHistory()
while flag:
    human_input = input("You: ")
    history.add_user_message(human_input)
    ai_response = conversation.predict(input=human_input)
    history.add_ai_message(ai_response)

    if human_input == "/stop":
        ai_response = "It's nice to meet you!! See you next time :)"
        flag = False
    print(f"AI: {ai_response}")

# print("Whole Conversation: \n", history.messages)
print(data)
