import streamlit as st
#from ..general_prompts.py import age, gender, employer, income, location

st.header("Let us ask you a few questions")

st.slider("How old are you?")

st.markdown("What is your gender?")
st.button("Male (Insert Picture)")
st.button("Female (Insert Picture)")

if st.button("Other (Insert Picture)"):
    st.text_input("Please Specify")

st.text_input("Where are you located?")

st.text_input("Who is your current employer? (If not employed, please write 'Not Employed')")

st.text_input("How much money do you make (If unknown, provide an estimate)")


if st.button("Next"):
    st.switch_page("ai_questions.py")