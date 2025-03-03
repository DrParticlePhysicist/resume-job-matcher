import streamlit as st
import requests

def display_match_results(api_url, resume_text):
    """Handles job description input and displays match results."""
    job_desc = st.text_area("Paste Job Description", "", height=200)
    
    if st.button("Match Resume") and job_desc:
        payload = {"resume_text": resume_text, "job_descriptions": [job_desc]}
        match_response = requests.post(f"{api_url}/match", json=payload)
        
        if match_response.status_code == 200:
            score = match_response.json().get("matches", [0])[0]
            st.write(f"### Match Score: {score:.2f}")
        else:
            st.error("Error processing match request")
