from langchain import ConversationChain
from langchain.memory import ChatMessageHistory, ConversationBufferMemory

from langchain.chains import create_tagging_chain_pydantic, create_tagging_chain
# from core.create_tagging_chain_pydantic import create_tagging_chain_pydantic
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

from langchain_openai import AzureChatOpenAI, AzureOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field

# from models.model import PersonalDetails
from core.custom_chain_for_extraction import pydantic_model_extractor


class PersonalDetails(BaseModel):
    first_name: str = Field(
        ...,
        description="This is the first name of the user.",
    )
    last_name: str = Field(
        ...,
        description="This is the last name or surname of the user.",
    )
    full_name: str = Field(
        ...,
        description="Is the full name of the user ",
    )
    city: str = Field(
        ...,
        description="The name of the city where someone lives",
    )
    email: str = Field(
        ...,
        description="an email address that the person associates as theirs",
    )
    language: str = Field(
        ..., enum=["spanish", "english", "french", "german", "italian"]
    )


llm = AzureOpenAI(openai_api_key="", api_version="",
                  azure_endpoint="", deployment_name="gpt-35-914",
                  model_name="gpt-35-turbo", max_tokens=1000)


model = AzureChatOpenAI(
    azure_endpoint="",
    openai_api_key="",
    openai_api_version="",
    azure_deployment='chat',
)

user_123_personal_details = PersonalDetails(first_name="", last_name="", full_name="", city="", email="", language="")


def ask_for_info(ask_for=["name", "age", "location"]):
    # prompt template 1
    first_prompt = ChatPromptTemplate.from_template(
        "Below are some things to ask the user in a coversational way. You should only ask one question at a time Strictly \
        don't ask as a list! Don't greet the user! Don't say Hi.Explain you need to get some info. If the ask_for list is empty then thank them and ask how you can help them \n\n \
        ### ask_for list: {ask_for}"
    )
    second_prompt = ChatPromptTemplate.from_template(
        "There is a list of things you need to ask to the user in a conversational way."
        "Take one element from list and ask about it to the user and if user responds then pick up the next element and do this until all the elements are done. But please don't ask about all elements of list at once."
        "Please Don't greet the user! Don't say Hi/Hello and any other greeting. Explain you need to get some info."
        "If the below list is empty then thank them and ask how you can help them?"
        "This is the list: {ask_for}."
    )
    # info_gathering_chain
    info_gathering_chain = LLMChain(llm=llm, prompt=second_prompt)
    ai_chat = info_gathering_chain.invoke({"ask_for": ask_for})
    return ai_chat["text"]


def add_non_empty_details(current_details: PersonalDetails, new_details: PersonalDetails):
    non_empty_details = {k: v for k, v in new_details.dict().items() if v not in [None, ""]}
    updated_details = current_details.copy(update=non_empty_details)
    return updated_details


def check_what_is_empty(user_personal_details):
    ask_for = []
    # Check if fields are empty
    for field, value in user_personal_details.dict().items():
        if value in [None, "", 0]:  # You can add other 'empty' conditions as per your requirements
            ask_for.append(f'{field}')
    return ask_for


def filter_response(text_input, user_details):
    # schema = {"title": "PersonalDetails",
    #           "type": "object",
    #           "properties": {
    #               "first_name": {"title": "First Name", "description": "This is the first name of the user.", "type": "string"},
    #               "last_name": {"title": "Last Name", "description": "This is the last name or surname of the user.", "type": "string"},
    #               "full_name": {"title": "Full Name", "description": "Is the full name of the user", "type": "string"},
    #               "city": {"title": "City", "description": "The name of the city where someone lives", "type": "string"},
    #               "email": {"title": "Email", "description": "an email address that the person associates as theirs", "type": "string"},
    #               "language": {
    #                   "title": "Language",
    #                   "enum": ["spanish", "english", "french", "german", "italian"],
    #                   "type": "string"}
    #           },
    #           "required": ["first_name", "last_name", "full_name", "city", "email", "language"]
    #           }
    try:
        chain = create_tagging_chain_pydantic(PersonalDetails, model)
        # chain = pydantic_model_extractor(pydantic_model=PersonalDetails)
        res = chain.invoke({"query": text_input})
        user_details = add_non_empty_details(user_details, res)
        ask_for = check_what_is_empty(user_details)
    except Exception as e:
        ask_for = check_what_is_empty(user_details)
    return user_details, ask_for


print("WELCOME TO YOUR AI CHATBOT!!")

flag = True
history = ChatMessageHistory()
conversation = ConversationChain(llm=llm, verbose=False)
while flag:
    human_input = input("You: ")
    history.add_user_message(human_input)

    user_details, ask_for = filter_response(human_input, user_123_personal_details)

    if ask_for:
        ai_response = ask_for_info(ask_for)
    else:
        ai_response = conversation.predict(input=human_input)
    history.add_ai_message(ai_response)

    if human_input == "/stop":
        ai_response = "It's nice to meet you!! See you next time :)"
        flag = False
    print(f"AI: {ai_response}")

print("Whole Conversation: \n", history.messages)
print("User Details:\n", user_details)
