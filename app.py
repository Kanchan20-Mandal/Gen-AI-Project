# Load the packages
import streamlit as st
from groq import Groq

# Provide a title for streamlit website
st.set_page_config(page_title="GEN AI PROJECT")

# Load the API key
api_key=st.secrets["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"]

# Initialize the Groq client
client=Groq(api_key=api_key)

# Function to generate the model responses based on user inputs
def get_response(text,model_name="llama-3.3-70b-versatile"):
    stream=client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"You are a helpful assistant"
            },
            {
                "role":"user",
                "content":text
            }
        ],
        model=model_name,
        stream=True
    )

    for chunk in stream:
        response=chunk.choices[0].delta.content
        if response is not None:
            yield response 
# Add the title to streamlit website
st.title("Gen AI Project using llama-3.3-70b-versatile")
st.subheader("By Kanchan Mandal")

# Provide a text box area for users to provide their inputs
user_ip=st.text_area("Ask your question here")

# Create submit button
submit=st.button("Generate Response",type="primary")

if submit:
    st.subheader("Model Response:")
    st.write_stream(get_response(user_ip))