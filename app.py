import streamlit as st

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
fruits = st.selectbox("Pick a fruit:", ["Apple", "Banana`", "Orange"])
st.write("Your favourite fruit is:", fruits)

colors = st.multiselect("Pick some colors:", ["Red", "Green", "Blue", "Yellow"])
st.write("You chose:", colors)

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