# import streamlit as st
# import requests
# import os

# API_URL = "http://localhost:8000"

# # Load custom CSS
# def load_css():
#     css_path = os.path.join(os.path.dirname(__file__), "styles", "theme.css")
#     if os.path.exists(css_path):
#         with open(css_path, "r") as f:
#             st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# # Apply CSS
# load_css()

# # Title
# st.title("🚀 Resume-Job Matcher 🌌")

# # Upload Resume
# uploaded_file = st.file_uploader("📂 Upload your Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

# if uploaded_file:
#     st.write(f"📂 File Name: {uploaded_file.name}")
#     st.write(f"📝 File Type: {uploaded_file.type}")  # Debugging output

#     # Ensure file type is set correctly
#     if not uploaded_file.type:
#         if uploaded_file.name.endswith(".txt"):
#             uploaded_file.type = "text/plain"
#         elif uploaded_file.name.endswith(".pdf"):
#             uploaded_file.type = "application/pdf"
#         elif uploaded_file.name.endswith(".doc") or uploaded_file.name.endswith(".docx"):
#             uploaded_file.type = "application/msword"

#     files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

#     with st.spinner("🔍 Extracting text from resume..."):
#         response = requests.post(f"{API_URL}/upload", files=files)

#     if response.status_code == 200:
#         resume_text = response.json().get("resume_text", "")
#         st.text_area("📜 Extracted Resume Text", resume_text, height=200)
        
#         # Job Description Input
#         job_desc = st.text_area("📌 Paste Job Description", "", height=200)

#         if st.button("✨ Match Resume with Job"):
#             if job_desc:
#                 payload = {"resume_text": resume_text, "job_descriptions": [job_desc]}

#                 with st.spinner("🤖 Matching resume..."):
#                     match_response = requests.post(f"{API_URL}/match", json=payload)

#                 if match_response.status_code == 200:
#                     matches = match_response.json().get("matches", [])
#                     if matches:
#                         best_match, score = matches[0]
#                         st.success(f"🚀 **Best Match:** {best_match} 🎯 (Score: {score:.2f})")
#                     else:
#                         st.warning("⚠️ No suitable matches found.")
#                 else:
#                     st.error("⚠️ Error processing match request.")
#             else:
#                 st.warning("⚠️ Please provide a job description.")
#     else:
#         st.error(f"⚠️ Failed to extract resume text: {response.json()}")


import streamlit as st
import requests
import os
from components.upload_jd import upload_job_descriptions  # Importing new JD upload component

API_URL = "http://localhost:8000"

# Load custom CSS
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "styles", "theme.css")
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply CSS
load_css()

# Title
st.title("🚀 Resume-Job Matcher 🌌")

# Upload Resume
uploaded_file = st.file_uploader("📂 Upload your Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:

    # Ensure file type is set correctly
    if not uploaded_file.type:
        if uploaded_file.name.endswith(".txt"):
            uploaded_file.type = "text/plain"
        elif uploaded_file.name.endswith(".pdf"):
            uploaded_file.type = "application/pdf"
        elif uploaded_file.name.endswith(".doc") or uploaded_file.name.endswith(".docx"):
            uploaded_file.type = "application/msword"

    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

    with st.spinner("🔍 Extracting text from resume..."):
        response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        resume_text = response.json().get("resume_text", "")
        st.text_area("📜 Extracted Resume Text", resume_text, height=200)
        
        # Job Description Upload
        job_descriptions = upload_job_descriptions()

        if st.button("✨ Match Resume with Jobs"):
            if job_descriptions:
                payload = {"resume_text": resume_text, "job_descriptions": job_descriptions}

                with st.spinner("🤖 Matching resume..."):
                    match_response = requests.post(f"{API_URL}/match", json=payload)

                if match_response.status_code == 200:
                    matches = match_response.json().get("matches", [])
                    if matches:
                        best_match, score = matches[0]
                        st.success(f"🚀 **Best Match:** {best_match} 🎯 (Score: {score:.2f})")
                    else:
                        st.warning("⚠️ No suitable matches found.")
                else:
                    st.error("⚠️ Error processing match request.")
            else:
                st.warning("⚠️ Please upload at least one job description.")
    else:
        st.error(f"⚠️ Failed to extract resume text: {response.json()}")
