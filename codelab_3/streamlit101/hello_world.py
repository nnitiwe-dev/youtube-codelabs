# app.py

import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Hello World App", layout="centered")

# Display the title
st.title("Hello, Streamlit World! 🌎")

# Add a header and some text
st.header("Welcome to your first Streamlit app!")
st.write("This is a simple example to get you started with Streamlit.")

# Display an interactive button
if st.button("Click Me!"):
    st.success("Button clicked! 🎉")

# Input box for user interaction
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, **{name}**! 👋")

# Display a slider
age = st.slider("Select your age:", 1, 100)
st.write(f"You're {age} years old!")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
