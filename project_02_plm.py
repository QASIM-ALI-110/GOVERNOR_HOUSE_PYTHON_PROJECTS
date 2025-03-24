import streamlit as st

st.title("Personal Library Manager")

# Session state to store books
if "books" not in st.session_state:
    st.session_state.books = []

# Input field to add books
new_book = st.text_input("Enter book name:")

if st.button("Add Book"):
    if new_book:
        st.session_state.books.append(new_book)
        st.success(f'"{new_book}" added to library!')
    else:
        st.warning("Please enter a book name.")

# Show book list
if st.session_state.books:
    st.subheader("Your Books:")
    for book in st.session_state.books:
        st.write(f"- {book}")

    # Remove book
    remove_book = st.selectbox("Select a book to remove:", ["None"] + st.session_state.books)
    if st.button("Remove Book"):
        if remove_book != "None":
            st.session_state.books.remove(remove_book)
            st.success(f'"{remove_book}" removed from library!')
else:
    st.write("No books in your library yet.")