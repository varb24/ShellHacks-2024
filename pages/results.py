import streamlit as st

# Title and header
st.title("Results")
st.header("Here are your results")

# Introduction section (filler text)
st.markdown("""
    Based on the information provided, we have generated insights tailored to your needs.
    The following results are dynamically generated and will be populated with relevant data.
""")

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
if st.button("Home"):
    st.switch_page("pages/main_page.py")

# Footer note
st.markdown("---")
st.markdown("Results are generated dynamically based on your responses. The content above is subject to change.")
