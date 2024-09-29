import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

openai_api_key = os.getenv('OPENAI_KEY')

class OpenAIClient:
    def __init__(self, api_key: str):
        # Initialize the OpenAI client with the provided API key
        self.client = OpenAI(api_key=api_key)
        
    def generate_completion(self, prompt: str, model="gpt-4o"):
        try:
            # Send the request to the chat completion API
            response = self.client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model=model
            )
            # Return the content of the response and the request ID
            #print(response)
            return {
                "content": response.choices[0].message.content.strip(),
            }
        except Exception as e:
            return {"error": str(e)}

# Usage
client = OpenAIClient(openai_api_key)

# response = client.generate_completion("Once upon a time,")
# print(response)


