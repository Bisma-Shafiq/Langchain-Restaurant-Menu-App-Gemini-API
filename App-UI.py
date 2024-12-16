import streamlit as st
import langchain_helper

# Set page configuration
st.set_page_config(page_title="GenAi-Menu-Generator")

# Page title
st.title("Restaurant Menu GenAI")

# Sidebar cuisine selection
cuisine = st.sidebar.selectbox(
    'Pick a cuisine',
    ('Indian', 'Pakistani', 'Arabian', 'Italian', 'Mexican')
)

# Generate menu when cuisine is selected
if cuisine:
    try:
        # Generate restaurant concept
        response = langchain_helper.generate_items(cuisine)

        # Display restaurant name
        st.header(response['restaurant_name'])

        # Display menu items
        st.subheader("Menu Items")
        menu_items = response['menu_items'].split(",")  # Corrected response key
        for item in menu_items:
            st.write("• " + item.strip())
    except Exception as e:
        st.error(f"Error generating menu: {str(e)}")
