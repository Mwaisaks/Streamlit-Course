import streamlit as st
import pandas as pd

st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.markdown('**Markdown** _is_ supported! [Visit Streamlit](https://streamlit.io)')
st.text('This is plain text')
st.write("`st.write()` can handle *mixed content*, like **bold**, _italic_, and numbers:", 123)


st.markdown(' ### Code Block Example')
st.code("""
# Python Example
def greet(name):
    return f"Hello, {name}!"
print(greet("Streamlit"))
        """, language="python")

st.markdown("#### Inline LaTeX: $a^2 + b^2 = c^2$")
st.latex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")

# -----Showing feedback messages------
st.success('This is a success message!')
st.warning('Be careful! This is a warning.')
st.error('Ooops! Somwthing went wrong.')
st.info('This is some information.')

# Adding a helpful tip:
st.markdown('> **Tip** Use feedback messages to guide the user.')

# buttons, radio buttons, and checkboxes 
if st.button("Click me!"):
    st.write("Button clicked!")

choice = st.radio("Choose an option:", ["Donjo Maber","Taya", "Tai Chi"])
st.write("You selected:", choice)

agree = st.checkbox("I agree")
if agree:
    st.write("Thanks for agreeing!")

# ------ Selectors: selectbox, multiselect ------
fruits = st.selectbox("Pick a fruit:", ["Apple", "Banana", "Orange"])
st.write("Your favourite fruit is:", fruits)

colors = st.multiselect("Pick some colors:", ["Red", "Green", "Blue", "Yellow"])
st.write("You chose:", colors)

# ------ User inputs: slider, number input, text input, text area ------
age = st.slider("Select your age:", 0, 100, 25)
st.write("Age:", age)

number = st.number_input("Enter a number:", min_value=0, max_value=100, value=10)
st.write("Number:", number)

name = st.text_input("Enter your name:")
st.write("Hello,", name)

bio = st.text_area("Write a short bio:")
st.write("Your bio:", bio)

# ------ Date and time pickers ------
date = st.date_input("Pick a date")
st.write("Selected date:", date)

time = st.time_input("Pick a time")
st.write("Selected time:", time)

# ------ File uploader for reading external files ------
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File content", content, height=200)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

st.write("### Using st.write() for Dataframe")
st.write(df)

st.table(df) # Static table
st.dataframe(df)

# ------ Displaying JSON and dictionaries ------
person = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Streamlit", "Data Science"]
}

st.json(person)
st.write("Dictionary displayed with st.write():", person)

# ------ Using editable tables with data editor ------
editable_df = st.data_editor(df, num_rows="dynamic")
st.write("Uodated DataFrame:")
st.write(editable_df)



"""
st.header('Hello world!')

st.title('Re-execution Demo')

# Get input
name = st.text_input('Enter your name ')

if name:
    st.write(f'Hello, {name}')
else:
    st.write('Please type your name above.')

print('Script Executed')

"""