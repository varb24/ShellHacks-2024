import streamlit as st
import re
from how_to_use import response2


st.title("AI questions")
st.header("Here are some more questions to narrow your search")

if 'response2' not in st.session_state:
    # Store the response from how_to_use
    st.session_state.response2 = response2

response2_content=st.session_state.response2['content']

# Using regex to find all questions in the response text
questions = re.findall(r'\*\*(.*?)\*\*',response2_content)



# Assign questions to variables
if len(questions) >= 3:
    question1 = questions[0]
    question2 = questions[1]
    question3 = questions[2]

    # Print each question to verify
    print(f"Question 1: {question1}")
    print(f"Question 2: {question2}")
    print(f"Question 3: {question3}")
else:
    print("Error: Could not extract exactly three questions from the text.")

newresponse1 = st.text_area(label=question1)
newresponse2 = st.text_area(label=question2)
newresponse3 = st.text_area(label=question3)

if st.button("Next"):
    if newresponse1 and newresponse2 and newresponse3:
        st.switch_page("results.py")
   
    else:
        st.warning("Please answer all questions before submitting.")
    