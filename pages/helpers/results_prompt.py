from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
import json
from typing import List, Dict
import time

# Model setup
model = ChatOpenAI(model="gpt-4o")

class RecommendationItem(BaseModel):
    link: str = Field(description="URL link associated with the recommendation")
    description: str = Field(description="Description of the recommendation")
    rationale: str = Field(description="Why this recommendation is helpful for the user")

class Recommendations(BaseModel):
    recommendations: List[Dict[str, RecommendationItem]] = Field(
        description="List of recommendations with name, link, description, and rationale"
    )

parser = JsonOutputParser(pydantic_object=Recommendations)

system_template = """
You are an agent who is trying to help a person find financial assistance, your role is that of a social worker.
You are allowed to use the internet to generate more localized results.
Take the information given by the user and create recommendations which will help the user's financial or social situation. 
Example: {{
    'recommendations': [
        {{'name_of_the_service': {{'link': 'http://example.com', 'description': 'A great resource.', 'rationale':'it has proven useful for many users of the same age'}}}},
        {{'name_of_the_service': {{'link': 'http://anotherexample.com', 'description': 'Another great resource.', 'rationale':'This is like example, but better'}}}}
    ]
}}
name_of_the_service should be the key using the name of the service being recommended.
If a recommendation does not have a 'link', add instructions on how to access the resource.
Return the results as a valid JSON object with 'recommendations' as the head key.
"""

filter_template = """
You are a social worker given a list of financial and social recommendations.
Evaluate each recommendation with the following criteria: 
1. How likely is it to help a user's financial situation?
2. How likely is it to help a user's social situation?
3. How accessible is it? Are there barriers the user might face in accessing this resource?

Example: {{
    'recommendations': [
        {{'name_of_the_service': {{'link': 'http://example.com', 'description': 'A great resource.', 'rationale':'it has proven useful for many users of the same age'}}}},
        {{'name_of_the_service': {{'link': 'http://anotherexample.com', 'description': 'Another great resource.', 'rationale':'This is like example, but better'}}}}
    ]
}}
name_of_the_service should be the key using the name of the service being recommended.
Do not alter any of the information on the list, except for the rationale.
Return the results as a valid JSON object with 'recommendations' as the head key.
"""

# Set up prompts
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{profile_input}")]
)

filter_prompt_template = ChatPromptTemplate.from_messages(
    [("system", filter_template), ("user", "{recommendations}")]
)

# Chain setup for generating recommendations
chain_generate = prompt_template | model | parser

# Chain setup for filtering top 3 recommendations
chain_filter = filter_prompt_template | model | parser

# Retry configuration
RETRY_LIMIT = 3
RETRY_DELAY = 2  # Seconds to wait between retries

# Run the chain and handle errors with retries
def create_recommendations(profile_input):
    for attempt in range(RETRY_LIMIT):
        try:
            #First pass with recs
            print(f"Attempt {attempt + 1}: Generating recommendations...")
            result = chain_generate.invoke(profile_input)
            print("Generated Recommendations:", result)

            # Ensure that recommendations exist in the result
            if "recommendations" not in result:
                raise ValueError("No recommendations found in the generated result")
            
            # Second pass to select the best recs
            filter_result = chain_filter.invoke({"recommendations": result["recommendations"]})
            print("Filtered Recommendations:", filter_result)
            
            if "recommendations" not in result:
                raise ValueError("No recommendations found in the generated result")
            
            return filter_result

        except json.JSONDecodeError as e:
            print(f"Attempt {attempt + 1}: JSON decoding error: {e}")
        except ValueError as e:
            print(f"Attempt {attempt + 1}: Error: {e}")
        except Exception as e:
            print(f"Attempt {attempt + 1}: Unexpected error: {e}")

        # Retry delay
        time.sleep(RETRY_DELAY)

    print("Failed to generate and filter recommendations after several attempts.")
    return None

# Example profile input
profile_input = {
    "profile_input": {
        "name": "John Doe", 
        "age": 25,
        "occupation": "Student",
        "education": "High School",
        "income": "Low",
        "location": "New York, NY",
        "dependents": 0,
        "ethnicity": "Hispanic"
    }
}

# Call the function
# create_recommendations(profile_input)
