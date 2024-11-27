from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import AzureChatOpenAI
from langchain.memory import ChatMessageHistory

contextualize_q_system_prompt1 = """Given a chat history and the latest user question \
which might reference context in the chat history, formulate a standalone question \
which can be understood without the chat history. Do NOT answer the question, \
just reformulate it if needed and otherwise return it as is."""

contextualize_q_system_prompt = """Given a chat history and the latest user question which might reference context in the chat history.
Your primary task is to first ask for details regarding model like MX, AX, etc, transmisson type like Auto & Manual, fuel and drive
Do not elaborate on them just capture them.
And if put None if any detail is not provided.
And always answer in below format
Model: or Transmission: or Fuel: or Drive:,
"""

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", contextualize_q_system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

llm = AzureChatOpenAI(
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="",
        azure_deployment='chat',
    )

contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()

history = ChatMessageHistory()
history.add_user_message("Hi, I have some questions.")
history.add_ai_message("Sure, but before that I want to know some details")
# history.add_user_message("What details you want?")
# history.add_ai_message("Details are related to vehicle model, fuel type, drive type , transmission type")

flag = True

while flag:
    human_input = input("You: ")
    if human_input == "/stop":
        flag=False
        continue
    res = contextualize_q_chain.invoke(
        {
            # "chat_history": [
            #     HumanMessage(content="What does LLM stand for?"),
            #     AIMessage(content="Large language model"),
            # ],
            "chat_history": history.messages,
            "question": f"{human_input}",
        }
    )
    history.add_user_message(human_input)
    history.add_ai_message(res)
    print(res)
