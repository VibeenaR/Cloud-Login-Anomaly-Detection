import streamlit as st
import pandas as pd

st.title("Login Anomaly Detection System")

data = pd.read_csv("top_alerts.csv")

st.write("Top Alerts")
st.dataframe(data)

user = st.text_input("Enter User ID")

if user:
    filtered = data[data["User ID"].astype(str) == user]
    st.write(filtered)