import streamlit as st

pg = st.navigation([st.Page("main_page.py"), st.Page("questions.py"), st.Page("ai_questions.py"), st.Page("results.py")], position="hidden")
st.set_page_config(page_title="Inclusive Aid", page_icon="::man-woman-girl-boy:")

pg.run()