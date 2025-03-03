# components/upload_jd.py
import streamlit as st
from io import StringIO

def upload_job_descriptions():
    """Component to upload multiple Job Descriptions."""
    st.subheader("Upload Job Descriptions")
    uploaded_files = st.file_uploader("Upload one or more job descriptions", type=["txt"], accept_multiple_files=True)
    
    job_descriptions = []
    if uploaded_files:
        for uploaded_file in uploaded_files:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            job_text = stringio.read()
            job_descriptions.append(job_text)
    
    return job_descriptions
