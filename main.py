import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")

selection_x = st.selectbox("Select the data for the X-axis", df.columns)
selection_y = st.selectbox("Select the data for the Y-axis", df.columns)

st.header(f"{str(selection_x).capitalize()} and {str(selection_y).capitalize()}")

data_x = df[selection_x]
data_y = df[selection_y]

figure = px.scatter(x=data_x, y=data_y, labels={"x": str(selection_x).capitalize(), "y": str(selection_y).capitalize()})
st.plotly_chart(figure)
