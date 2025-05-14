import streamlit as st
from streamlit_option_menu import option_menu

# Set up session state if not already initialized
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Option menu for navigation
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu", 
        options=["Home", "Page 1", "Page 2"], 
        default_index=0
    )

    # Update the session state based on selected option
    st.session_state.page = selected

# Define content for Home page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    name = st.text_input("Enter your name")
    if st.button("Submit"):
        st.session_state.name = name
        st.success(f"Hello {st.session_state.name}!")

# Define content for Page 1
def page_1():
    st.title("Page 1")
    st.write("This is Page 1 with a slider.")
    slider_value = st.slider("Select a number", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")

# Define content for Page 2
def page_2():
    st.title("Page 2")
    st.write("This is Page 2 with a checkbox and button.")
    checkbox_value = st.checkbox("Check me")
    if checkbox_value:
        st.write("Checkbox is checked!")
    if st.button("Click me"):
        st.session_state.click_count = st.session_state.get('click_count', 0) + 1
        st.write(f"Button clicked {st.session_state.click_count} times!")

# Load the corresponding page content based on session state
if st.session_state.page == "Home":
    home_page()
elif st.session_state.page == "Page 1":
    page_1()
elif st.session_state.page == "Page 2":
    page_2()
