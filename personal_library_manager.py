import streamlit as st
import pandas as pd

# Set Streamlit page config
st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="centered")

# Sample library data
if 'library' not in st.session_state:
    st.session_state.library = []

# Title
st.title("Personal Library Manager 📚")

# Sidebar for navigation
st.sidebar.title("Library Management")
option = st.sidebar.selectbox("Choose an action", ("View Library", "Add Book"))

# Function to display library
def display_library():
    if len(st.session_state.library) > 0:
        library_df = pd.DataFrame(st.session_state.library)
        st.dataframe(library_df)
    else:
        st.write("Your library is empty!")

# Add Book Form
def add_book_form():
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.text_input("Year of Publication")
        genre = st.text_input("Genre")
        submit_button = st.form_submit_button("Add Book")
        
        if submit_button:
            if title and author and year and genre:
                new_book = {
                    "Title": title,
                    "Author": author,
                    "Year": year,
                    "Genre": genre
                }
                st.session_state.library.append(new_book)
                st.success(f"Book '{title}' added to your library!")
            else:
                st.error("Please fill in all fields!")

# Display content based on selected option
if option == "View Library":
    display_library()
elif option == "Add Book":
    add_book_form()

