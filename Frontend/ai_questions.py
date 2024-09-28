import streamlit as st

st.title("AI questions")
st.header("Here are some more questions to narrow your search")

if st.button("Next"):
    st.switch_page("results.py")