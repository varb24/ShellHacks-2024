from openAI_client import client

response = client.generate_completion("This is how you create a file, use the import above for the client")

print(response)