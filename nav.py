import streamlit as st

pg = st.navigation([st.Page("pages/main_page.py"), st.Page("pages/questions.py"), st.Page("pages/ai_questions.py"), st.Page("pages/results.py")], position="hidden")
st.set_page_config(page_title="Inclusive Aid", page_icon="::man-woman-girl-boy:", layout="centered")

pg.run()