import streamlit as st

st.title("🌍 Unit Convertor App")
st.markdown("### Convert Length, Weight And Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time.")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometer to miles":
            return value * 0.621371
        elif unit == "Miles to Kilometer":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Seconds to minutes":
            return value / 60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Hours to days":
            return value / 24
        elif unit == "Days to hours":
            return value * 24

# Selecting Unit Based on Category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometer to miles", "Miles to Kilometer"])
elif category == "Weight":
    unit = st.selectbox("⚖ Select Conversion", ["Kilograms to pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("🕓 Select Conversion", ["Seconds to minutes", "Minutes to seconds", "Hours to days", "Days to hours"])

# Input Value for Conversion
value = st.number_input("Enter a value to convert")

# Convert Button and Output
if st.button("Convert"):
    result = convert_units(category, value, unit)
    if result is not None:
        st.success(f"The result is {result:.2f}")
    else:
        st.error("Invalid input! Please try again.")


                