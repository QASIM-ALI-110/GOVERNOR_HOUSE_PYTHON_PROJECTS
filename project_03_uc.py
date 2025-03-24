import streamlit as st

st.title("Simple Unit Converter")

# Conversion function
def convert(value, unit):
    if unit == "Kilometers to Miles":
        return value * 0.621371
    elif unit == "Miles to Kilometers":
        return value / 0.621371
    elif unit == "Celsius to Fahrenheit":
        return (value * 9/5) + 32
    elif unit == "Fahrenheit to Celsius":
        return (value - 32) * 5/9
    else:
        return None

# Input value
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

# Unit selection
unit = st.selectbox("Select conversion:", [
    "Kilometers to Miles", 
    "Miles to Kilometers", 
    "Celsius to Fahrenheit", 
    "Fahrenheit to Celsius"
])

# Convert button
if st.button("Convert"):
    result = convert(value, unit)
    st.write(f"Converted Value: **{result:.2f}**")