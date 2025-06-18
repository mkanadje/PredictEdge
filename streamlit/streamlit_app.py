import streamlit as st
import requests

st.title("Predict Edge App")

uploaded_file = st.file_uploader("Upload a CSV file for analysis", type=["csv"])

if uploaded_file is not None:
    st.write(f"Selected File: {uploaded_file.name}")
    if st.button("Upload"):
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post("http://backend:8000/ingest/upload", files=files)
        if response.status_code == 200:
            st.success(f"File uploaded successfully!")
        else:
            st.error(f"Failed to upload file: {response.textr}")
