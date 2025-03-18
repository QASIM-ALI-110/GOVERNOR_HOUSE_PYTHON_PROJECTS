import streamlit as st

def length_converter(value, from_unit, to_unit):
    conversion_factors = {
        'meter': 1, 'kilometer': 0.001, 'centimeter': 100, 'millimeter': 1000,
        'mile': 0.000621371, 'yard': 1.09361, 'foot': 3.28084, 'inch': 39.3701
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def weight_converter(value, from_unit, to_unit):
    conversion_factors = {
        'kilogram': 1, 'gram': 1000, 'milligram': 1000000,
        'pound': 2.20462, 'ounce': 35.274
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value - 273.15) * 9/5 + 32
    return value

def time_converter(value, from_unit, to_unit):
    conversion_factors = {
        'second': 1, 'minute': 1/60, 'hour': 1/3600,
        'day': 1/86400, 'week': 1/604800
    }
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

st.title("Unit Converter")

category = st.selectbox("Select category", ["Length", "Weight", "Temperature", "Time"])
value = st.number_input("Enter value", min_value=0.0, format="%.6f")

if category == "Length":
    from_unit = st.selectbox("From Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    to_unit = st.selectbox("To Unit", ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"])
    result = length_converter(value, from_unit, to_unit)

elif category == "Weight":
    from_unit = st.selectbox("From Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    to_unit = st.selectbox("To Unit", ["kilogram", "gram", "milligram", "pound", "ounce"])
    result = weight_converter(value, from_unit, to_unit)

elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = temperature_converter(value, from_unit, to_unit)

elif category == "Time":
    from_unit = st.selectbox("From Unit", ["second", "minute", "hour", "day", "week"])
    to_unit = st.selectbox("To Unit", ["second", "minute", "hour", "day", "week"])
    result = time_converter(value, from_unit, to_unit)

st.write(f"### Converted Value: {result:.6f} {to_unit}")