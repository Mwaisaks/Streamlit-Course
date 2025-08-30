import streamlit as st
import pandas as pd
import numpy as np

st.title("Built in Charts")

data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

st.subheader('Line Chart')
st.line_chart(data)

st.subheader('Area Chart')
st.area_chart(data)

st.subheader('Bar Chart')
st.bar_chart(data)

# ------ Creating visualizations with Plotly ------
import plotly.express as px

st.subheader("Plotly Demo")
fig = px.scatter(data, x='A', y='B', color='C', title='Plotly Scatter')
st.plotly_chart(fig)

# ------ Creating visualizations with Altair ------
import altair as alt

st.subheader("Altair Example")
chart = alt.Chart(data).mark_line().encode(
    x='A',
    y='B',
    color='C'
)
st.altair_chart(chart, use_container_width=True)

# ------ Adding interactivity and themes to charts ------
# Example: Theme toggle with a checkbox
st.subheader("Interactive Theme Example")
dark_mode = st.checkbox("Enable Dark Theme")

fig = px.line(data, x=data.index, y='A', title="Interactive Line Chart")
if dark_mode:
    fig.update_layout(template="plotly_dark")

st.plotly_chart(fig)

# ------ Creating visualizations with Seaborn and Matplotlib ------
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader("Seaborn Example")
fig, ax = plt.subplots()
sns.histplot(data['A'], kde= True, ax=ax)
st.pyplot(fig)


