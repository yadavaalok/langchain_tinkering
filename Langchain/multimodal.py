import PIL.Image
from vertexai.preview.generative_models import GenerativeModel
import vertexai.preview

image = PIL.Image.open("sample.png")
vertexai.init(project="mpaas-generativeai-dev-358327", location="us-central1")
vision_model = GenerativeModel('gemini-1.0-pro-001')
response = vision_model.generate_content(["how to create conditional access policy?", image])
print(response.text)
