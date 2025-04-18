import streamlit as st   #Importing the streamlit library for creating the web app  
import random            #Importing the random library for generating random characters
import string            #Importing the string library for using string characters     

# Function to generate a password based on the user preferences
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters   #Include all letters (a-z, A-Z,)

    if use_digits:
        characters += string.digits #Add numbers (0-9) if selected

        if use_special:
            characters += string.punctuation #Add special characters (!, @, #, $, %, ^, &, *) if selected
#Generate a random password of the specified length using the characters defined above
    return ''.join(random.choice(characters) for _ in range(length))     

# Streamlit UI setup
st.title("Simple Password Generator 🗝️🔐❤️") # Display the app title on the web page

# User input: password length (slider to select length between 6 and 32 characters)
length = st.slider("Select Password Length", min_value=6 , max_value=32, value=12)

# Checkbox options for including numbers and special characters in the password
use_digits = st.checkbox("Include Digits")   # Checkbox for numbers (0-9)

use_special = st.checkbox("Use Special")   # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)   # Call the password generation function
    st.write(f"Generated Password: `{password}`")    # Display the generated password

st.write("------------------------------------------------------------")
st.write("Build with ♥️ by [Amna Ali](https://github.com/AmnaAli1234)")