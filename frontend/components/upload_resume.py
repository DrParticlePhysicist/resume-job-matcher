# import streamlit as st
# import requests

# def upload_resume(api_url):
#     uploaded_file = st.file_uploader("Upload your resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
#     if uploaded_file is not None:
#         files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
#         response = requests.post(f"{api_url}/upload", files=files)
        
#         if response.status_code == 200:
#             return response.json().get("text", "")
#         else:
#             st.error("Failed to extract resume text")
#             return None
import requests

def upload_resume(file):
    url = "http://localhost:8000/upload"

    files = {"file": (file.name, file, "text/plain")}  # Ensure MIME type is set
    response = requests.post(url, files=files)

    print(f"🔹 Status: {response.status_code}")
    print(f"🔹 Response: {response.json()}")  # Log response
    return response.json()
