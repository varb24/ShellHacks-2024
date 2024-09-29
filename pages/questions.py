import streamlit as st
import json
from nav import lang_setup
_ = lang_setup()
from pages.helpers.lang_prompt import create_questions

with open('./all_countries.json', 'r') as f:
    all_countries = json.load(f)

st.header(_("Let us ask you a few questions"))

# Gender selection outside of the form to enable real-time updates
gender_options = [_("Male"), _("Female"), _("Other")]
gender = st.selectbox(_("What is your gender?"), gender_options)

# Conditionally display the other gender input based on real-time selection
if gender == "Other":
    other_gender = st.text_input(_("Please specify your gender"))
else:
    other_gender = None  # Set to None if not applicable

# Create a form using st.form, which allows users to submit multiple inputs at once
with st.form("defined_questions", clear_on_submit=True):

    # Slider input for age
    age = st.slider(_("How old are you?"), min_value=16)

    # Slider input for Dependents
    dependents = st.slider(_("How many people are dependent of you?"), max_value=20)

    # Dropdown for ethnicity options
    ethnicity = st.selectbox(_("What ethnicity do you identify as?"), [_("Black"), _("White"), _("Hispanic/Latino"), _("Native American"), _("Pacific Islander"), _("Asian American")])

    # HTML to style the question text
    where_loc = '<p style="font-size:14px;">{}</p>'.format(_("Where are you located?"))
    st.markdown(where_loc, unsafe_allow_html=True)

    # location details (street address, city, state/province, country)
    st_address = st.text_input(_("Street Address"))
    city = st.text_input(_("City"))
    state_or_province = st.text_input(_("State/Province"))

    # Translate each country name in the list using gettext
    translated_countries = [_(country) for country in all_countries]

    # Display the translated list of countries in a select box
    country = st.selectbox(_("Country"), translated_countries)

    # Combine the location inputs
    location = f"{st_address}, {city}, {state_or_province}, {country}"

    # Text input for employer details
    employer = st.text_input(_("Who is your current employer? (If not employed, please write 'Not Employed')"))

    # Text input for income
    income = st.text_input(_("How much money do you make yearly? (If unknown, provide an estimate)"))

    # Dropdown input for selecting if the user is pursuing higher education
    education = st.selectbox(_("Are you pursuing Higher Education?"), [_("Yes"), _("No")])

    # Form submission button, when pressed it triggers the form to submit the inputs
    if st.form_submit_button(_("Next")):
        # Display a warning message while loading (simulated with sleep)
        st.warning("Loading Answers and Generating Further Questions")
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

        AI_questions = create_questions(profile_input)
        st.session_state['profile'] = profile_input
        st.session_state['AI_questions'] = AI_questions
        # Code to show that 
        #st.markdown(f"This is what you inputted: {gender}, {age}, {location}, {employer}, {income}, {education}")

        # Simulate a loading delay

        st.switch_page("pages/ai_questions.py")