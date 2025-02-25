from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini and get response
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])


def get_gemini_respose(question):
    response = chat.send_message(question, stream=True)
    return response


# initialise session our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Autism chatbot")
# initialise session state for chat history if it doesn"t exist
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and input:
    # response=get_gemini_response(input)
    response = get_gemini_respose(input)
    # Add user query and response to chat history
    st.session_state["chat_history"].append(("You", input))
    st.subheader("the response is ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("bot", chunk.text))
st.subheader("the chat history is")

for role, text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")


def app():
    st.title("autsim chatbot Page")
    st.write("This is the chatbot")
