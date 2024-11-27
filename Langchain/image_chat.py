import httpx
from anthropic import AnthropicBedrock

import base64
from PIL import Image
import io

def image_to_base64(image_path):
    # Open the image file
    with open(image_path, "rb") as image_file:
        # Read the image file and encode it to base64
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string



def image_chat(image):
    img_url = "https://mazldmapsa.blob.core.windows.net/langchainestsb/images/TSB_2021_BOD_PPC_03050/1_1.png?sp=r&st=2024-09-12T18:51:30Z&se=2024-09-13T02:51:30Z&spr=https&sv=2022-11-02&sr=b&sig=P0%2BmHPWR9EZHuxDvO2Ub3ZfsZAjFkSzPfJuknzxqqGI%3D"
    image1_data = base64.b64encode(httpx.get(img_url).content).decode("utf-8")
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image1_data,
                    },
                },
                {
                    "type": "text",
                    "text": "This is the answer : 'Engine oil capacity for honda is 6 litre.' , you need to check whether the image is related to this answer. If yes then just return 1 else return 0. Do not return any explanation."
                }
            ],
        }
    ]

    client = AnthropicBedrock(
            aws_access_key="",
            aws_secret_key="",
        )
    response = client.messages.create(
        model="anthropic.claude-3-sonnet-20240229-v1:0",
        max_tokens=1024,
        messages=messages,
        stream=False
    )
    print(response.content[0].text)
path = "/home/alok/Documents/AI_Project_Doc/Langchain/sample.png"
image_string = image_to_base64(path)
image_chat(image_string)
