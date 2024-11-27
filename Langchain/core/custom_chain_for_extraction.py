import json

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

_PYDANTIC_FORMAT_INSTRUCTIONS = """The output should be formatted as a JSON instance that conforms to the JSON schema below.

As an example, for the schema {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}
the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schema. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Here is the output schema:
```
{schema}
```"""  # noqa: E501

def get_format_instructions(pydantic_object) -> str:
    try:
        # Copy schema to avoid altering original Pydantic schema.
        schema = {k: v for k, v in pydantic_object.schema().items()}

        # Remove extraneous fields.
        reduced_schema = schema
        if "title" in reduced_schema:
            del reduced_schema["title"]
        if "type" in reduced_schema:
            del reduced_schema["type"]
        # Ensure json in context is well-formed with double quotes.
        schema_str = json.dumps(reduced_schema)

        return _PYDANTIC_FORMAT_INSTRUCTIONS.format(schema=schema_str)
    except Exception as e:
        print(e)

def pydantic_model_extractor(pydantic_model):
    # Set up a parser
    parser = PydanticOutputParser(pydantic_object=pydantic_model)

    # Model
    model = AzureChatOpenAI(
        azure_endpoint="",
        openai_api_key="",
        openai_api_version="",
        azure_deployment='chat',
    )

    # Prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer the user query. Wrap the output in `json` tags\n{format_instructions}",
            ),
            ("human", "{query}"),
        ]
    ).partial(format_instructions=get_format_instructions(pydantic_model))

    #chain
    chain = prompt | model | parser
    return chain
