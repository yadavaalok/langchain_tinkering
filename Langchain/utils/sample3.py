from typing import List, Optional, Dict
import re

from langchain.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from models.model import Details


def extract_details(text: str) -> Dict[str, str]:
    details = {}
    pattern = r"Model: (?P<model_name>\w+)\nTransmission: (?P<transmission_type>\w+)\nFuel: (?P<fuel_type>\w+)\nDrive: (?P<drive_type>\w+)"
    match = re.search(pattern, text)
    if match:
        details = match.groupdict()
    return details


def collect_data(human_input):
    # Set up a parser
    parser = PydanticOutputParser(pydantic_object=Details)

    model = AzureChatOpenAI(
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="",
        azure_deployment='chat',
    )
    # Prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            # (
            #     "system",
            #     "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
            # )
            (
                "system",
                "From the query extract the detail regarding model like MX, AX, etc, transmisson type like Auto & Manual, fuel and drive"
                "Do not elaborate on them just capture them."
                "And if put None if any detail is not provided."
                "And always answer in below format"
                "Model: or Transmission: or Fuel: or Drive:",
            ),
            ("human", "{query}"),
        ]
    )

    prefix = "This is user query check for details regarding model, transmission, fuel and drive details:  "

    # query = (prefix + "Manual AX7 Petrol AWD")

    query = (prefix + human_input)

    print(prompt.format_prompt(query=query).to_string())

    chain = prompt | model
    try:
        res = chain.invoke({"query": query})
        print(res.content)
        return extract_details(res.content)
    except Exception as e:
        print(e)
