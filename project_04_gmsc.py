import streamlit as st

# App ka title
st.title("Office Department Manager")

# Departments ka list
departments = ["HR", "IT", "Finance", "Marketing", "Production"]

# Employee ka naam input
employee_name = st.text_input("Enter Employee Name:")

# Department choose karne ka option
department = st.selectbox("Select Department:", departments)

# Task input
task = st.text_area("Assign Task:")

# Submit button
if st.button("Assign Task"):
    if employee_name and task:
        st.success(f"Task assigned to {employee_name} in {department} department.")
    else:
        st.warning("Please enter employee name and task before assigning.")

# Footer message
st.write("**Manage office departments efficiently!**")