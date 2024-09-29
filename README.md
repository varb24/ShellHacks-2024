# ShellHacks-2024

# Inclusive Aid

Inclusive Aid is a Streamlit-based application that provides resources and assistance to individuals in need. It aims to create an inclusive approach to offering aid, regardless of background or location.

## Features
- Interactive questions to gather user information and provide tailored results.
- AI-powered follow-up questions to refine the user’s needs.
- Dynamic insights based on user input.
- Links to external resources such as OpenAI API, Streamlit Docs, and LangGraph Documentation.

## Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

## Usage
To run the application, use the following command:
```bash
streamlit run nav.py
```

### Navigation
- **Main Page**: Introduction to the platform and a button to start the questions.
- **Questions Page**: Asks initial demographic and location-related questions.
- **AI Questions Page**: Provides further questions based on AI-generated responses.
- **Results Page**: Displays insights based on the answers provided.

## File Structure
```
.
├── pages/
│   ├── main_page.py        # Main landing page
│   ├── questions.py        # Page for demographic and location questions
│   ├── ai_questions.py     # Page for AI-generated follow-up questions
│   ├── results.py          # Page showing tailored insights
├── openAI_client.py        # OpenAI client for generating AI responses
├── lang_prompt.py          # Example using Langchain for language models
└── requirements.txt        # List of required dependencies
```

## External Resources
- [OpenAI API](https://beta.openai.com/docs/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LangGraph Documentation](https://docs.langchain.com/)


