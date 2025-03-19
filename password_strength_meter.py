import streamlit as st
from zxcvbn import zxcvbn

# Streamlit App Title
st.title("Password Strength Meter")

# User Input for Password
password = st.text_input("Enter your password:")

# Checking password strength
if password:
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']

    # Displaying Strength
    if score == 0:
        strength = "Very Weak"
        color = "red"
    elif score == 1:
        strength = "Weak"
        color = "orange"
    elif score == 2:
        strength = "Fair"
        color = "yellow"
    elif score == 3:
        strength = "Strong"
        color = "lightgreen"
    else:
        strength = "Very Strong"
        color = "green"

    # Display Strength and Feedback
    st.markdown(f"<h3 style='color:{color};'>{strength}</h3>", unsafe_allow_html=True)
    st.write("Feedback:", feedback.get('suggestions', ['No suggestions available.']))

# To run the app use the following command:
# streamlit run app.py
