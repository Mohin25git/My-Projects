import streamlit as st

st.set_page_config(page_title="Grade Calculator", page_icon="📝", layout="centered")

# Disable browser autocomplete
st.markdown("""
<style>
input {
    autocomplete: off !important;
}
</style>
""", unsafe_allow_html=True)

st.title("📝 Minimal Grade Calculator")
st.write("Enter your marks below to see your grade.")

marks_input = st.text_input("Marks (0–100):", autocomplete="off")


def calculate_grade(marks):
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B+"
    if marks >= 60: return "B"
    if marks >= 50: return "C+"
    if marks >= 40: return "C"
    return "Fail"


if marks_input:
    try:
        marks = int(marks_input)
        if 0 <= marks <= 100:
            grade = calculate_grade(marks)
            st.success(f"🎉 Your grade is **{grade}**")
        else:
            st.error("Please enter a value between 0 and 100.")
    except ValueError:
        st.error("Please enter a valid number.")
