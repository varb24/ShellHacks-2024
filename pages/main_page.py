import streamlit as st
from nav import lang_setup

st.set_page_config(page_title="Inclusive Aid", page_icon="::man-woman-girl-boy:", layout="centered")

_ = lang_setup()

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
intro_html = '<div class="title">{}</div>'.format(_("Welcome to Inclusive Aid"))
mission_html = '<div class="header">{}</div>'.format(_("Our mission is to provide help to everyone, regardless of background."))
st.markdown(intro_html, unsafe_allow_html=True)
st.markdown(mission_html, unsafe_allow_html=True)

# Introduction or description section
desc_html = '<div class="description">{}</div>'.format(_("We believe in an inclusive approach to offering aid to everyone in need, regardless of background or location. Please click the button below to begin your journey with us."))
st.markdown(desc_html, unsafe_allow_html=True)

# Centering the button using a div with flexbox
if st.button(_("Begin"), use_container_width = True):
    st.switch_page("pages/questions.py")

with st.container(border= True):
    help_html = '<div class="title">{}</div>'.format(_("Helpful Resources"))
    st.markdown(help_html, unsafe_allow_html=True)

    # Instructional header
    help_instruc_html = '<div class="subheader">{}</div>'.format(_("Explore these resources for further assistance: "))
    st.markdown(help_instruc_html, unsafe_allow_html = True)
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
        st.markdown(_("Get information on benefits and services provided by the U.S. Government."))
        st.link_button(_("Visit USA.GOV"), "https://www.usa.gov/benefits")
        

    # Third card: Treasury Assisstance
    with col3:
        st.subheader(_("Treasury Assistance"))
        st.markdown(_("Explore policies and assistance for American families and workers."))
        st.link_button(_("Visit Treasury Assistance"), "https://home.treasury.gov/policy-issues/coronavirus/assistance-for-American-families-and-workers")

    # Fourth card: FindHelp
    with col4:
        st.subheader("FindHelp.org")
        st.markdown(_("Find local resources and help for food, housing, medical care, and more."))
        st.link_button(_("Visit FindHelp.org"), "https://www.findhelp.org")

# Footer section
foot_html = '<div class="footer">{}</div>'.format(_("Empowering communities, one person at a time."))
st.markdown(foot_html, unsafe_allow_html=True)