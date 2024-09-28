"""
import streamlit as st

st.title("Inclusive Aid")
st.header("Providing help for all who need")

st.markdown("Please click the button below to begin")

if st.button("Begin"):
    st.switch_page("questions.py")
"""
import streamlit as st

# Apply some custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        color: #2E86C1;
        font-weight: bold;
        text-align: center;
        margin-top: 50px;
    }
    .header {
        font-size: 30px;
        color: #1F618D;
        text-align: center;
        margin-bottom: 50px;
    }
    .description {
        font-size: 20px;
        text-align: center;
        margin-bottom: 30px;
        color: #555;
    }
    .footer {
        font-size: 15px;
        color: #888;
        text-align: center;
        margin-top: 100px;
        font-style: italic;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title and Header with custom styling
st.markdown('<div class="title">Inclusive Aid</div>', unsafe_allow_html=True)
st.markdown('<div class="header">Providing help for all who need</div>', unsafe_allow_html=True)

# Introduction or description section
st.markdown('<div class="description">We believe in an inclusive approach to offering aid to everyone in need, regardless of background or location. Please click the button below to begin your journey with us.</div>', unsafe_allow_html=True)

# Centering the button using a div with flexbox
st.markdown('<div class="button-container">', unsafe_allow_html=True)
if st.button("Begin"):
    st.switch_page("pages/questions.py")
st.markdown('</div>', unsafe_allow_html=True)

# Footer section
st.markdown('<div class="footer">"Empowering communities, one person at a time."</div>', unsafe_allow_html=True)


