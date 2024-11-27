from langchain.prompts import PromptTemplate
from langchain_contrib.prompts import ChoicePromptTemplate
from langchain_openai import AzureChatOpenAI, AzureOpenAI
from langchain.chains import LLMChain

template = ChoicePromptTemplate.from_template(
    "This {product} is available in {choices}. Which color should I pick?",
)
print(template.format(product="dress", choices=["red", "green", "blue"]))
exit()


# Define the Choice Prompt Template for collecting user details
user_details_prompt_template = ChoicePromptTemplate.from_template(
    "Please select your {detail_type} from the following {choices}"
)

# Define the options for each user detail category
model_name_options = ["MX", "AX3", "AX5", "AX7", "AX7L"]
transmission_type_options = ["Auto", "Manual"]
fuel_type_options = ["Petrol", "Diesel"]
drive_type_options = ["AWD", "FWD"]

# Format the Choice Prompt Template for each user detail category
model_name_prompt = user_details_prompt_template.format(detail_type="model_name", choices=model_name_options)
transmission_type_prompt = user_details_prompt_template.format(detail_type="transmission_type", choices=transmission_type_options)
fuel_type_prompt = user_details_prompt_template.format(detail_type="fuel_type", choices=fuel_type_options)
drive_type_prompt = user_details_prompt_template.format(detail_type="drive_type", choices=drive_type_options)

llm = AzureOpenAI(openai_api_key="", api_version="",
                  azure_endpoint="", deployment_name="gpt-35-914",
                  model_name="gpt-35-turbo", max_tokens=1000)

chain = LLMChain(llm=llm, prompt=model_name_prompt)

chain.invoke("Hi")
