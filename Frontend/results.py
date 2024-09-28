import streamlit as st

st.title("results")
st.header("Here are your results")

if st.button("Home"):
    st.switch_page("main_page.py")