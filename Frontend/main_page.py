import streamlit as st

st.title("Inclusive Aid")
st.header("Providing help for all who need")

st.markdown("Please click the button below to begin")

if st.button("Begin"):
    st.switch_page("questions.py")
