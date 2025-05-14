import streamlit as st

# Title
st.title("Hello Streamlit!")

# Input field
name = st.text_input("What's your name?")

# Display name if provided
if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please enter your name.")