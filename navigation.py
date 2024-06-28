import streamlit as st
from pages import home
from pages import register
from pages import dashboard
from pages import form
from pages import contact
from pages import chat_bot_forlocation
from pages import pages



# Create a sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
st.write(f"You selected: {selection}")  # Display selected page for clarity (optional)
page()  # Call the app function from the selected module
