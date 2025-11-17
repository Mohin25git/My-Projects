# Streamlit Continuous Calculator Web App

import streamlit as st  # Importing Streamlit library for creating web apps easily

# Page Setup
# Sets up the page title, icon, and layout before the app runs.
# 'layout=centered' keeps everything neatly aligned in the center of the page.
st.set_page_config(page_title="AI Calculator", page_icon="🧮", layout="centered")

# Header Section
# Using Markdown (with HTML styling) to create a colorful, centered header.
# This makes the UI look professional and more engaging.
st.markdown("<h1 style='text-align: center; color: #3f51b5;'>🧮 Calculator Web App</h1>", unsafe_allow_html=True)
st.write("Perform quick arithmetic operations right from your browser — clean and simple!")

# A horizontal line to separate the header from the input section visually
st.markdown("---")

# Input Section
# The app uses two side-by-side input boxes (columns) for entering numbers.
# st.number_input() allows users to type or use arrows to input numbers (including decimals).
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number:", format="%.6f")  # %.6f → shows up to 6 decimal places

with col2:
    num2 = st.number_input("Enter next number:", format="%.6f")

# The dropdown menu (selectbox) lets users choose which arithmetic operation to perform.
# Each label represents a symbol for the operation.
operation = st.selectbox(
    "Choose an operation:",
    ("+", "-", "*", "/", "** (Power)", "// (Floor Division)")
)

# Perform Calculation
# Initialize a variable 'result' to store the final output of the calculation.
# When the user clicks the 'Calculate' button, the selected operation is performed.
result = None

if st.button("Calculate"):
    # Each condition checks which operation the user selected.
    if operation == "+":
        # ➕ Addition
        result = num1 + num2

    elif operation == "-":
        # ➖ Subtraction
        result = num1 - num2

    elif operation == "*":
        # ✖️ Multiplication
        result = num1 * num2

    elif operation.startswith("/"):
        # ➗ Division
        # Includes safety check for division by zero.
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Error! Division by zero.")  # Displays red error message box

    elif operation.startswith("**"):
        # Power
        result = num1 ** num2

    elif operation.startswith("//"):
        # Floor Division
        if num2 != 0:
            result = num1 // num2
        else:
            st.error("❌ Error! Division by zero.")

    else:
        # Invalid input handling
        # This is triggered if the user somehow selects an unrecognized operation.
        st.warning("Invalid operation selected!")

# Result Display
# If a valid result is obtained, it’s displayed inside a green success box.
# Streamlit automatically updates the result without refreshing the page.
if result is not None:
    st.success(f"✅ Result: {result}")

# Footer
# A decorative footer message displayed at the bottom of the app.
# It uses HTML for styling and centers the text with a subtle gray color.
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with Streamlit by Mohin Man Shakya</p>",
    unsafe_allow_html=True
)
