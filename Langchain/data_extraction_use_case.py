# To help construct our Chat Messages
from langchain.schema import HumanMessage
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

# To parse outputs and get structured data back
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_openai import AzureChatOpenAI

chat_model = AzureChatOpenAI(
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="",
        azure_deployment='chat',
    )

instructions = """
You will be given a sentence with fruit names, extract those fruit names and assign an emoji to them
Return the fruit name and emojis in a python dictionary
"""

fruit_names = """
Apple, Pear, this is an kiwi
"""


# Make your prompt which combines the instructions w/ the fruit names
prompt = (instructions + fruit_names)

# Call the LLM
output = chat_model([HumanMessage(content=prompt)])

output_dict = eval(output.content)

# print (output_dict)
# print (type(output_dict))


# The schema I want out
response_schemas = [
    ResponseSchema(name="artist", description="The name of the musical artist"),
    ResponseSchema(name="song", description="The name of the song that the artist plays")
]

# The parser that will look for the LLM output in my schema and return it back to me
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)

# The format instructions that LangChain makes. Let's look at them
format_instructions = output_parser.get_format_instructions()


prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("Given a command from the user, extract the artist and song names and if not provided all the then ask for remaining. \n \
                                                    {format_instructions}\n{user_prompt}")
    ],
    input_variables=["user_prompt"],
    partial_variables={"format_instructions": format_instructions}
)
flag=True

while flag:
    user_input = input("You: ")

    if user_input == "/stop":
        flag=False
        continue
    fruit_query = prompt.format_prompt(user_prompt=user_input)

    fruit_output = chat_model(fruit_query.to_messages())
    output = output_parser.parse(fruit_output.content)

    print (output)
    print (type(output))