from general_prompts import prompt
from general_prompts import prompt2 
from general_prompts import prompt3
from openAI_client import client

response1 = client.generate_completion(prompt)
print(response1['content'])

response2 = client.generate_completion(prompt2)
print(response2['content'])

response3 = client.generate_completion(prompt3)
print(response3['content'])
