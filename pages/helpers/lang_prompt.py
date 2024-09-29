from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
import json

# Model setup
model = ChatOpenAI(model="gpt-4o")

# Pydantic model for questions
class Questions(BaseModel):
    questions: list = Field(description="List of questions")

parser = JsonOutputParser(pydantic_object=Questions)

# Define system template to enforce well-formed JSON output
system_template = """
You are an agent who is trying to help a person find financial assistance, your role is that of a social worker.
Take the information given by the user and create questions that will assist you in finding resources for this person.
Respond only with a valid JSON object using double quotes. Example: {{"questions": ["What is your name?", "How many siblings do you have?"]}}
"""

# Define filter template to pick top 3 questions
filter_template = """
You are given a list of questions. Pick the best three questions that will help you gather the most important information to assist the person.
Return the three questions in a valid JSON object. Example: {{"questions": ["What is your most pressing financial need?", "What is your occupation?", "How many dependents do you have?"]}}
"""

# Profile input setup
# profile_input = {
#     "profile_input": {
#         "name": "Ian De Leon", 
#         "age": 2,
#         "occupation": "Vagabond",
#         "education": "BA in Computer Science",
#         "income": "Poor",
#         "location": "Miami, FL",
#         "dependents": "Two",
#         "ethnicity": "Hispanic"
#     }
# }

# Prompt template setup for initial question generation
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{profile_input}")]
)

# Prompt template setup for filtering top 3 questions
filter_prompt_template = ChatPromptTemplate.from_messages(
    [("system", filter_template), ("user", "{questions}")]
)

# Chain setup for generating questions
chain_generate = prompt_template | model | parser

# Chain setup for filtering top 3 questions
chain_filter = filter_prompt_template | model | parser

# Run the chain and handle invalid JSON
def create_questions(profile_input):
    try:
        # Step 1: Generate questions based on the profile input
        result = chain_generate.invoke(profile_input)
        print("Generated Questions:", result)

        # Step 2: Filter the top 3 questions
        filter_result = chain_filter.invoke({"questions": result["questions"]})
        print("Top 3 Questions:", filter_result)

        return filter_result

    except json.JSONDecodeError as e:
        print(f"JSON decoding error: {e}")
        result = chain_generate.invoke(profile_input)
        return create_questions(result)
    except Exception as e:
        print(f"Error: {e}")
        result = chain_generate.invoke(profile_input)
        return create_questions(result)

# Call the function
#create_questions(profile_input)
