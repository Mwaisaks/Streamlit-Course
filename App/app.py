import streamlit as st
import pandas as pd
import json

st.title("Session State Demo")

if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button('Increment'):
    st.session_state.counter += 1

st.write('Counter value: ',st.session_state.counter)

#######

if 'name' not in st.session_state:
    st.session_state.name = "Guest"

name_input = st.text_input("Enter your name ", st.session_state.name)

if name_input != st.session_state.name:
    st.session_state.name = name_input

st.write("Hello", st.session_state.name)

######

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.success("You are now logged in!")
else:
    st.write("Welcome back!")
    if st.button("Log out"):
        st.session_state.logged_in = False

st.title("FIle Upload and Preview")

uploaded_file = st.file_uploader("Upload a CSV, Excel or JSON file", type=["csv", "xlsx", "json"])

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
        st.write("CSV Preview:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".XLSX"):
        df = pd.read_excel(uploaded_file)
        st.write("Excel Preview:")
        st.dataframe(df.head())
    elif uploaded_file.name.endswith(".JSON"):
        data = json.load(uploaded_file)
        st.write("JSON Preview")
        st.json(data)

# ------ Validating uploaded files and showing previews ------
if uploaded_file:
    file_size = uploaded_file.size / 1024
    st.write(f"File name: {uploaded_file.name}, SIze: {file_size:.2f} KB")
    if file_size > 500:
        st.warning("File is large! Preview may be limited.")

# ------ Caching data and resources for performance ------
@st.cache_data
def load_large_csv(file):
    return pd.read_csv(file)

st.header("Upload a large csv for caching demo")
large_csv = st.file_uploader("Upload CSV for caching", type=["csv"], key="large")

if large_csv:
    df_large = load_large_csv(large_csv)
    st.write("Cached CSV Loaded:")
    st.dataframe(df_large.head())


