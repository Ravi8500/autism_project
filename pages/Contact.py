# import streamlit as st  

# st.title(":mailbox: :blue[Get In Touch With Us!]")


# contact_form = """
# <form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
#      <input type="hidden" name="_captcha" value="false">
#      <input type="text" name="name" placeholder="Your name" required>
#      <input type="email" name="email" placeholder="Your email" required>
#      <textarea name="message" placeholder="Your message here"></textarea>
#      <button type="submit">Send</button>
# </form>
# """

# st.markdown(contact_form, unsafe_allow_html=True)

# # Use Local CSS File
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style.css")
# st.warning("Go to Q&A chatbot!")

# def app():
#     st.title("Contact Page")
#     st.write("This is the contact page. You can reach us at contact@example.com.")


import streamlit as st  
import os

st.title(":mailbox: :blue[Get In Touch With Us!]")

contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")
st.warning("Go to Q&A chatbot!")

def app():
    st.title("Contact Page")
    st.write("This is the contact page. You can reach us at contact@example.com.")
