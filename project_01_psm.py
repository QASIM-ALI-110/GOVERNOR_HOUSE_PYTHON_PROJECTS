import streamlit as st

def check_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Medium"
    else:
        return "Strong"

st.title("Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_strength(password)
    st.write(f"Password Strength: **{strength}**")