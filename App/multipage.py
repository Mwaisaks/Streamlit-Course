import streamlit as st

st.title("Sidebar Navigation Example")

pages = ["Home", "Dashboard", "Settings"]
choice = st.sidebar.radio("Go to", pages)

if choice == "Home":
    st.header("Home Page")
    st.write("Welcome!")
elif choice == "Dashboard":
    st.header("Dashboard Page")
    st.write("Metrucs and charts go here.")
elif choice == "Settings":
    st.header("SettingsPage")
    st.write("User Preferences here.")