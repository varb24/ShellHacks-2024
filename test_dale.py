import os
from dotenv import load_dotenv
from openai import OpenAI
import openai

def generate_image(in_prompt):

load_dotenv()

openai.api_key = os.getenv('OPENAI_KEY')

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt=in_prompt,
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

return image_url
