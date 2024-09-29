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
    .subheader {
        font-size: 30px;
        color: #1F618D;
        text-align: center;
        margin-top: 10px;
    }
    .description {
        font-size: 1.25rem;
        font-weight: 400;
        text-align: center;
        margin-bottom: 30px;
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

# Title and header
st.markdown('<div class="title">Results</div>', unsafe_allow_html = True)
st.markdown('<div class="subheader">Here Are Your Results!</div>', unsafe_allow_html = True)
st.divider()

# Introduction section (filler text)
st.markdown('<div class="description"> Based on the information provided, we have generated insights tailored to your needs. The following results are dynamically generated and will be populated with relevant data.</div>', unsafe_allow_html = True)

# Create 3 columns for a card-like layout
col1, col2, col3 = st.columns(3)

# First card: Placeholder for OpenAI API Result 1
with col1:
    st.subheader("Insight 1")
    st.markdown("Here will be the first personalized insight based on your input. Stay tuned for further updates.")
    st.markdown("**Example Insight**: You are eligible for the following financial benefits...")

# Second card: Placeholder for OpenAI API Result 2
with col2:
    st.subheader("Insight 2")
    st.markdown("This is a placeholder for the second insight. It will contain relevant recommendations.")
    st.markdown("**Example Insight**: Based on your location, we found resources for food assistance nearby...")

# Third card: Placeholder for OpenAI API Result 3
with col3:
    st.subheader("Insight 3")
    st.markdown("Here will be the third insight with helpful advice and guidance.")
    st.markdown("**Example Insight**: We recommend reaching out to local community centers for additional support...")

# Button to go back to the home page
st.divider()
if st.button("Home", use_container_width = True):
    st.switch_page("pages/main_page.py")

# Footer note
st.markdown("Results are generated dynamically based on your responses. The content above is subject to change.")
st.markdown('<div class="footer">"Empowering communities, one person at a time."</div>', unsafe_allow_html=True)
