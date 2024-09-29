import streamlit as st
import time
from pages.helpers.results_prompt import create_recommendations

question_answers = {}
st.title("AI questions")
st.header("Here are some more questions to narrow your search")
# Check if AI_questions exist in session state
if 'AI_questions' in st.session_state:
    AI_questions = st.session_state['AI_questions']['questions']

    # Display the AI questions
    for i, question in enumerate(AI_questions, 1):
        print(f'writing question {question}')
        answer = st.text_area(f"{question}")
        question_answers[question] = answer
    # merge both previous answers and extra answers
    st.session_state['final_answers'] = st.session_state['profile'] | question_answers
    print(st.session_state['final_answers'])

if st.button("Next"):
    st.session_state['final_recs'] = create_recommendations(st.session_state["final_answers"])
    st.switch_page("pages/results.py")
