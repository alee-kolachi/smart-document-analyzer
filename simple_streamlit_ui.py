import streamlit as st
import requests

st.title("Smart Document Analyzer")

uploaded_file = st.file_uploader("Upload a document image", type=["jpg", "png", "webp", "pdf", "jpeg"])
if uploaded_file is not None:
    with open(f"/tmp/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())


    response = requests.post("http://127.0.0.1:8000/process_document", files={"file": open(f"/tmp/{uploaded_file.name}", "rb")})
    st.json(response.json())