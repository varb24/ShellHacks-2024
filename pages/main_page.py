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
        margin-top: 30px;
    }
    .header {
        font-size: 30px;
        color: #1F618D;
        text-align: center;
        margin-bottom: 50px;
    }
    .subheader {
        font-size: 30px;
        color: #1F618D;
        text-align: center;
        margin-top: 10px;
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
    </style>
    """, unsafe_allow_html=True
)

# Title and Header with custom styling
st.markdown('<div class="title">Inclusive Aid</div>', unsafe_allow_html = True)
st.markdown('<div class="header">Providing help for all who need</div>', unsafe_allow_html = True)

# Introduction or description section
st.markdown('<div class="description">We believe in an inclusive approach to offering aid to everyone in need, regardless of background or location. Please click the button below to begin your journey with us.</div>', unsafe_allow_html=True)

# Centering the button using a div with flexbox
if st.button("Begin", use_container_width = True):
    st.switch_page("pages/questions.py")

with st.container(border= True):
    st.markdown('<div class="title">Helpful Resources</div>', unsafe_allow_html=True)

    # Instructional header
    st.markdown('<div class="subheader">Explore these resources for further assistance:</div>', unsafe_allow_html = True)
    st.divider()

    # Create columns for the cards
    #col1 = st.container()
    col2, col3, col4 = st.columns(3)

    # First card: Vanguard Investor
    
    #with col1:
    #    st.markdown('<div class="h3">Vanguard Investor</div>', unsafe_allow_html = True)
    #    st.subheader("Vanguard Investor")
    #    st.markdown("Access investment resources to plan for your financial future.")
    #    st.link_button("Visit Vanguard Investor", "https://investor.vanguard.com/corporate-portal")

    # Second card: USA.GOV
    with col2:
        st.subheader("USA.GOV")
        st.markdown("Get information on benefits and services provided by the U.S. Government.")
        st.link_button("Visit USA.GOV", "https://www.usa.gov/benefits")
        

    # Third card: Treasury Assisstance
    with col3:
        st.subheader("Treasury Assistance")
        st.markdown("Explore policies and assistance for American families and workers.")
        st.link_button("Visit Treasury Assistance", "https://home.treasury.gov/policy-issues/coronavirus/assistance-for-American-families-and-workers")

    # Fourth card: FindHelp
    with col4:
        st.subheader("FindHelp.org")
        st.markdown("Find local resources and help for food, housing, medical care, and more.")
        st.link_button("Visit FindHelp.org", "https://www.findhelp.org")

# Footer section
st.markdown('<div class="footer">"Empowering communities, one person at a time."</div>', unsafe_allow_html=True)