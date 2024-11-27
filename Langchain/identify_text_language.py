from anthropic import AnthropicBedrock

def identify_language(text):

    prompt = f"""
    You are a multilingual expert who can identify and convert the text into the identified language.

    This is the text : {text}

    This is the list of language from which you need to identify ['English', 'Hindi', 'Tamil', 'Telugu', 'Kannada', 'Malayalam', 'Punjabi', 'Gujarati', 'Marathi']

    Detect the language of the given sentence and rewrite it correctly in the same language. Make sure the sentence remains natural
    
    The response should be in json format. Below is the sample format:
        
        "original_text": '',
        "language": '',
        "translated_text": ''
        

    Instructions:
        - Do not mention anything other than the instructed response.
        - Do not include any other text or explanation.
        - Strictly do not include any other thing in the response.
        - Also keep it concise and well formatted.
    """

    client = AnthropicBedrock(
        aws_access_key="",
        aws_secret_key="",
        aws_region="us-east-1",
    )

    response = client.messages.create(
        model="anthropic.claude-3-sonnet-20240229-v1:0",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
    # return response.content[0].text.strip()

identify_language("engine oil kasa change karaycha?")
