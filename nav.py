import streamlit as st
import gettext

# Define the locale directory where translation files will be stored
locales_dir = 'locales'

pg = st.navigation([st.Page("pages/main_page.py"), st.Page("pages/questions.py"), st.Page("pages/ai_questions.py"), st.Page("pages/results.py")], position="hidden")

def lang_setup():
    # Set the language based on user selection
    language_mapping = {
        'English': 'en',
        'Español': 'es'
    }

    select_lang = st.selectbox("Please Select Your Language", ["English", "Español"])

    # Set the language based on user selection
    lang_code = language_mapping[select_lang]
    lang = gettext.translation('main_page', localedir='locales', languages=[lang_code])
    lang.install()
    _ = lang.gettext
    return _

pg.run()