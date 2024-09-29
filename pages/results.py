import streamlit as st
from pages.helpers.create_image import generate_image 
from openAI_client import client

# Fill the three recs we will use
rec1 = st.session_state['final_recs']['recommendations'][0]
rec2 = st.session_state['final_recs']['recommendations'][1]
rec3 = st.session_state['final_recs']['recommendations'][2]

# Putting recs in a list to package them later
rec_list = [rec1, rec2, rec3]

# Debugging: Print the structure of rec_list to see what it looks like
st.write("Rec list structure:", rec_list)

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
st.markdown('<div class="title">Results</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Here Are Your Results!</div>', unsafe_allow_html=True)
st.divider()

# Introduction section (filler text)
st.markdown(
    '<div class="description"> Based on the information provided, we have generated insights tailored to your needs. The following results are dynamically generated and will be populated with relevant data.</div>', 
    unsafe_allow_html=True
)

# Create 3 columns for a card-like layout
col1, col2, col3 = st.columns(3)

results_columns = zip([col1, col2, col3], rec_list)

# Loop through columns and recommendations
for col, rec in results_columns:
    with col:
        main_key = list(rec.keys())[0]  # Get the first key, which is the service name
        details = rec[main_key]  # Access the details dictionary for that service
        #image_url = generate_image(details.get('description', 'Generate placeholder'))
        image_url = client.generate_completion(f'Search the given url for a picture which represents the company or webpage. Return ONLY the image url. Given Url: {details.get("link", "No link")}')
        print(f'image url ---- {image_url}')
        # Add check to ensure `details` is a dictionary
        if isinstance(details, dict):
            st.subheader(main_key)  # Service name
            st.image(image_url, width=224)
            st.markdown(f"[Link to service]({details.get('link', 'No link available')})")  # Display the link as markdown
            st.markdown(f"**Description**: {details.get('description', 'No description available')}")  # Display the description
            st.markdown(f"**Rationale**: {details.get('rationale', 'No rationale available')}")  # Display the rationale
        else:
            st.write(f"Error: Expected dictionary for {main_key}, but got {type(details)}")

# Button to go back to the home page
st.divider()
if st.button("Home", use_container_width=True):
    st.switch_page("pages/main_page.py")

# Footer note
st.markdown("Results are generated dynamically based on your responses. The content above is subject to change.")
st.markdown('<div class="footer">"Empowering communities, one person at a time."</div>', unsafe_allow_html=True)
