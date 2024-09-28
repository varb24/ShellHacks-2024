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

st.title("Helpful Resources")

# Instructional header
st.header("Explore these resources for further assistance:")

# Create columns for the cards (2 cards per row)
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# First card: USA.GOV
with col1:
    st.subheader("USA.GOV")
    st.markdown("Get information on benefits and services provided by the U.S. Government.")
    if st.button("Visit USA.GOV"):
        st.markdown("[Click here to visit USA.GOV Benefits](https://www.usa.gov/benefits)")

# Second card: Treasury Assistance
with col2:
    st.subheader("Treasury Assistance")
    st.markdown("Explore policies and assistance for American families and workers.")
    if st.button("Visit Treasury Assistance"):
        st.markdown("[Click here to visit Treasury Assistance](https://home.treasury.gov/policy-issues/coronavirus/assistance-for-American-families-and-workers)")

# Third card: FindHelp
with col3:
    st.subheader("FindHelp.org")
    st.markdown("Find local resources and help for food, housing, medical care, and more.")
    if st.button("Visit FindHelp.org"):
        st.markdown("[Click here to visit FindHelp.org](https://www.findhelp.org)")

# Fourth card: Vanguard Investor
with col4:
    st.subheader("Vanguard Investor")
    st.markdown("Access investment resources to plan for your financial future.")
    if st.button("Visit Vanguard Investor"):
        st.markdown("[Click here to visit Vanguard Investor](https://investor.vanguard.com/corporate-portal)")