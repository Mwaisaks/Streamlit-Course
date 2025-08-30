import streamlit as st

# ------ Grouping widgets into forms ------
st.title("Forms Demo")

with st.form("contact form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("submit")

if submitted:
    st.success(f"Thanks {name}, we will contact you as soon as possible.")

st.subheader("Forms Demo with Logic")

with st.form("Calc_form"):
    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number", step=2)
    calculate = st.form_submit_button("Calculate Sum")

if calculate:
    st.write(f"Result: {num1 + num2}")

# ------ Creating step-by-step workflows ------
st.title("Step-by_step Workflow")

# Initialize state
if "step" not in st.session_state:
    st.session_state.step=1
if "name" not in st.session_state:
    st.session_state.name=""
if "choice" not in st.session_state:
    st.session_state.choice=""

# Step transition functions
def next_step():
    st.session_state.step+= 1

def restart():
    st.session_state.step=1
    st.session_state.name=""
    st.session_state.choice=""

if st.session_state.step == 1:
    st.write("Step 1: Enter your name")
    st.text_input("Name", value=st.session_state.name, key="name")
    st.button("Next", on_click=next_step)

elif st.session_state.step == 2:
    st.write(f"Hello {st.session_state.name} Step 2: Choose your preference")
    st.radio("Choose a restaurant", ['Chipotle', 'Moes'], key="choice")
    st.button("Next", on_click=next_step)

elif st.session_state.step == 3:
    st.write(f"You selected {st.session_state.choice}")
    st.button("Restart", on_click=restart)