from GeneralPrompts import prompt
from openAI_client import client

response = client.generate_completion(prompt)
print(response['content'])