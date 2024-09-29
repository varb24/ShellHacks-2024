import streamlit as st
import time
import json
from pages.helpers.lang_prompt import create_questions

with open('./all_countries.json', 'r') as f:
    all_countries = json.load(f)

st.header("Let us ask you a few questions")

# Gender selection outside of the form to enable real-time updates
gender_options = ["Male", "Female", "Other"]
gender = st.selectbox("What is your gender?", gender_options)

# Conditionally display the other gender input based on real-time selection
if gender == "Other":
    other_gender = st.text_input("Please specify your gender")
else:
    other_gender = None  # Set to None if not applicable

# Create a form using st.form, which allows users to submit multiple inputs at once
with st.form("defined_questions", clear_on_submit=True):

    # Slider input for age
    age = st.slider("How old are you?", min_value=16)

    # Slider input for Dependents
    dependents = st.slider("How many people are dependent of you?", max_value=20)

    # Dropdown for ethnicity options
    ethnicity = st.selectbox("What ethnicity do you identify as?", ["Black", "White", "Hispanic/Latino", "Native American", "Pacific Islander", "Asian American"])

    # HTML to style the question text
    where_loc = '<p style="font-size:14px;">Where are you located?</p>'
    st.markdown(where_loc, unsafe_allow_html=True)

    # location details (city, state/province, country)
    city = st.text_input("City")
    state_or_province = st.text_input("State/Province")
    country = st.selectbox("Country", all_countries)

    # Combine the location inputs
    location = f"{city}, {state_or_province}, {country}"

    # Text input for employer details
    employer = st.text_input("Who is your current employer? (If not employed, please write 'Not Employed')")

    # Text input for income
    income = st.text_input("How much money do you make yearly? (If unknown, provide an estimate)")

    # Dropdown input for selecting if the user is pursuing higher education
    education = st.selectbox("Are you pursuing Higher Education?", ["Yes", "No"])

    # Form submission button, when pressed it triggers the form to submit the inputs
    if st.form_submit_button("Next"):
        # Display a warning message while loading (simulated with sleep)

        profile_input = {
            "profile_input": {
                "age": age,
                "occupation": employer,
                "education": education,
                "income": income,
                "location": location,
                "dependents": dependents,
                "ethnicity": ethnicity
            }
        }
        #st.warning("Loading Answers and Generating Further Questions")
        with st.spinner("Loading data from OpenAI..."):
            AI_questions = create_questions(profile_input)
        st.session_state['profile'] = profile_input
        st.session_state['AI_questions'] = AI_questions
        # Code to show that 
        #st.markdown(f"This is what you inputted: {gender}, {age}, {location}, {employer}, {income}, {education}")
        st.warning("Loading Answers and Generating Further Questions")
        # Simulate a loading delay

        st.switch_page("pages/ai_questions.py")