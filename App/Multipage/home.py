import streamlit as st

st.title("Welcome to my Multipage App")
st.write("Use the sidebar to navigate between pages.")

def show_header(title):
    st.markdown(f"## {title}")

def show_metric(label, value):
    st.metric(label=label, value=value)

show_header("Dashboard")
show_metric("Revenue", "$10,000")
show_metric("Users", "1,250")

st.set_page_config(
    page_title="My Custom App",
    page_icon="📚",
    layout="wide", 
    initial_sidebar_state="expanded"
)

st.title("Custom Branding Example")
st.write("This app has a custom page title, icon and wide layout.")