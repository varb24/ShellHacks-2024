# ShellHacks-2024

# Inclusive Aid

Inclusive Aid is a Streamlit-based application that provides resources and assistance to individuals in need. It aims to create an inclusive approach to offering aid, regardless of background or location.

## Features
- Interactive questions to gather user information and provide tailored results.
- Translate the main page and questions for users that does not know english (Work in Progress)
- AI image generation for the results (Work in Progress)
- AI-powered follow-up questions to refine the user’s needs.
- Dynamic insights based on user input.
- Links to external resources such as OpenAI API, Streamlit Docs, and LangGraph Documentation.

## Installation
To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Usage
To run the application, use the following command:
```
streamlit run nav.py
```

### Navigation
- **Main Page**: Introduction to the platform and a button to start the questions.
- **Questions Page**: Asks initial demographic and location-related questions.
- **AI Questions Page**: Provides further questions based on AI-generated responses.
- **Results Page**: Displays insights based on the answers provided.

## File Structure
## File Structure

```
.
├── locales
│   ├── en
│   ├── es
│   ├── main_page.pot                           # Translation template for main page in different languages
│   └── questions.pot                           # Translation template for question-related content
├── pages
│   ├── ...                                     # Cache of compiled Python files
│   ├── helpers
│   │   ├── ...                                 # Cache of compiled Python files for helpers
│   │   ├── __init__.py                         # Initializes the 'helpers' package
│   │   ├── lang_prompt.py                      # Helper functions for handling language prompts
│   │   ├── results_prompt.py                   # Helper functions for managing results prompts
│   │   └── __init__.py                         # Initializes the 'helpers' sub-package
│   ├── __init__.py                             # Initializes the 'pages' package
│   ├── ai_questions.py                         # Handles AI-related questions logic
│   ├── main_page.py                            # Main page functionality and logic
│   ├── questions.py                            # General question-related logic
│   └── results.py                              # Logic for managing and displaying results
├── .env                                        # Environment variables for the project
├── .gitignore                                  # Specifies files and directories to be ignored by Git
├── all_countries.json                          # Data file containing information about countries
├── general_prompts.py                          # General prompts logic used across the application
├── how_to_use.py                               # Instructions or logic for user guidance
├── lang_prompt.py                              # Manages language-specific prompts (possibly reused by multiple components)
├── nav.py                                      # Handles navigation logic within the application
├── openAI_client.py                            # Manages interaction with OpenAI's API
├── README.md                                   # Project overview and documentation
└── requirements.txt                            # List of required Python packages and dependencies


## External Resources
- [OpenAI API](https://beta.openai.com/docs/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LangGraph Documentation](https://docs.langchain.com/)


