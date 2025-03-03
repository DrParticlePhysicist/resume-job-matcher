# Resume-Job Matcher

A web application that matches resumes to job descriptions using advanced Natural Language Processing (NLP) techniques.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The Resume-Job Matcher leverages NLP to analyze and compare the content of resumes against job descriptions, providing a similarity score to indicate how well a resume matches a given job description.

## Features
- **Resume Parsing**: Extracts text from PDF, DOCX, and TXT formats.
- **Job Description Analysis**: Processes multiple job descriptions for comparison.
- **Similarity Scoring**: Computes cosine similarity between resume and job descriptions.
- **User-Friendly Interface**: Allows users to upload resumes and view matching scores.

## Architecture
The application is divided into two main components:

- **Backend**: Built with FastAPI, it handles the processing and analysis of resumes and job descriptions.
- **Frontend**: Developed using Streamlit, it provides an interactive user interface for uploading resumes and viewing results.

## Prerequisites
- **Python 3.8+**: Ensure Python is installed on your system. You can download it from the official Python website.

## Installation
Follow the steps below to set up the project on your local machine.

### 🛠 Backend Setup
#### 📌 Navigate to the Backend Directory:
```bash
cd backend
```
#### 🛠 Create a Virtual Environment:
```bash
python -m venv env
```
#### 🔄 Activate the Virtual Environment:
- **Windows**:
  ```bash
  .\env\Scriptsctivate
  ```
- **macOS/Linux**:
  ```bash
  source env/bin/activate
  ```
#### 📦 Install Dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
#### 📖 Download NLTK Data:
```bash
python -m nltk.downloader punkt stopwords
```
#### 📖 Download spaCy Model:
```bash
python -m spacy download en_core_web_sm
```

---

### 🛠 Frontend Setup
#### 📌 Navigate to the Frontend Directory:
```bash
cd frontend
```
#### 🛠 Create a Virtual Environment:
```bash
python -m venv env
```
#### 🔄 Activate the Virtual Environment:
- **Windows**:
  ```bash
  .\env\Scriptsctivate
  ```
- **macOS/Linux**:
  ```bash
  source env/bin/activate
  ```
#### 📦 Install Dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Running the Application
Follow these steps to start both the **backend** and **frontend** components.

### 🚀 Start the Backend Server
#### 📌 Navigate to the Backend Directory:
```bash
cd backend
```
#### 🔄 Activate the Virtual Environment:
```bash
source env/bin/activate
```
#### ▶️ Run the FastAPI Server:
```bash
uvicorn main:app --reload
```
**🔗 The backend API will be accessible at:**  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🚀 Start the Frontend Application
#### 📌 Navigate to the Frontend Directory:
```bash
cd frontend
```
#### 🔄 Activate the Virtual Environment:
```bash
source env/bin/activate
```
#### ▶️ Run the Streamlit Application:
```bash
streamlit run app.py
```
**🔗 The frontend will be accessible at:**  
[http://localhost:8501](http://localhost:8501)

---

## 🎯 Usage
1. **Access the Frontend**  
   Open your web browser and navigate to:  
   [http://localhost:8501](http://localhost:8501)
2. **Upload a Resume**  
   Click the **Upload** button and select a resume file (**PDF, DOCX, or TXT**).
3. **Paste Job Description**  
   Copy and paste the **job description** into the provided text area.
4. **Match Resume with Job**  
   Click the **"Match Resume with Job"** button to compute the similarity score.
5. **View Results**  
   The application will display the **similarity score**, indicating how well the resume matches the job description.

---
