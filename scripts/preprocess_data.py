# # scripts/preprocess_data.py

# import os
# import json
# import re
# import docx
# import pdfplumber
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')

# # Function to extract text from PDF
# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"
#     return text.strip()

# # Function to extract text from DOCX
# def extract_text_from_docx(docx_path):
#     doc = docx.Document(docx_path)
#     text = "\n".join([para.text for para in doc.paragraphs])
#     return text.strip()

# # Function to clean and preprocess text
# def clean_text(text):
#     text = text.lower()
#     text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
#     text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
#     stop_words = set(stopwords.words('english'))
#     words = text.split()
#     filtered_words = [word for word in words if word not in stop_words]
#     return " ".join(filtered_words)

# # Process all resumes
# def process_resumes(input_folder, output_file):
#     processed_data = []
    
#     for filename in os.listdir(input_folder):
#         file_path = os.path.join(input_folder, filename)
#         if filename.endswith('.pdf'):
#             text = extract_text_from_pdf(file_path)
#         elif filename.endswith('.docx'):
#             text = extract_text_from_docx(file_path)
#         else:
#             continue
        
#         cleaned_text = clean_text(text)
#         processed_data.append({"filename": filename, "text": cleaned_text})

#     # Save processed data to JSON
#     with open(output_file, 'w', encoding='utf-8') as f:
#         json.dump(processed_data, f, indent=4)
    
#     print(f"✅ Processed {len(processed_data)} resumes and saved to {output_file}")

# # Run the script
# if __name__ == "__main__":
#     input_folder = "../data/sample_resumes"
#     output_file = "../data/processed_data.json"
#     process_resumes(input_folder, output_file)
# File: scripts/preprocess_data.py

import json
import spacy
import csv

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Cleans and tokenizes text."""
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])

# Load raw dataset
processed_data = []
with open("../data/kaggle_dataset.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row
    
    for row in reader:
        if len(row) >= 3:  # Ensure correct number of columns
            job_title = row[0].strip()
            required_skills = row[1].strip()
            experience_required = row[2].strip()

            # Create a meaningful job description
            job_desc = f"{job_title} - Skills: {required_skills}, Experience: {experience_required} years"

            processed_data.append({
                "text": preprocess_text(job_desc),
                "job_description": preprocess_text(job_desc)
            })
        else:
            print(f"⚠️ Skipping malformed row: {row}")

# Save processed data
with open("../data/processed_data.json", "w", encoding="utf-8") as f:
    json.dump(processed_data, f, indent=4)

print("✅ Data Preprocessing Completed - Saved as 'processed_data.json'")
