from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
from services import process_resume, compute_match_score

# from services import process_resume, match_job_descriptions

app = FastAPI()

class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_descriptions: List[str]

@app.post("/match")
def match_resume(request: ResumeMatchRequest):
    scores = compute_match_score(request.resume_text, request.job_descriptions)
    return {"matches": scores}

# @app.post("/upload")
# def upload_resume(file: UploadFile = File(...)):
#     if file.content_type not in ["application/pdf", "application/msword", "text/plain"]:
#         raise HTTPException(status_code=400, detail="Unsupported file type")
#     text = process_resume(file)
#     return {"resume_text": text}

# @app.post("/upload")
# def upload_resume(file: UploadFile = File(...)):
    # print(f"Received file: {file.filename}, Content-Type: {file.content_type}")  # Debugging line
    
    # if file.content_type not in ["application/pdf", "application/msword", "text/plain"]:
    #     raise HTTPException(status_code=400, detail="Unsupported file type")
    
    # text = process_resume(file)
    # return {"resume_text": text}

# @app.post("/upload")
# def upload_resume(file: UploadFile = File(...)):
#     print(f"Received file: {file.filename}, Content-Type: {file.content_type}")  # Debugging log

#     if file.content_type not in ["application/pdf", "application/msword", "text/plain"]:
#         raise HTTPException(status_code=400, detail=f"Unsupported file type: {file.content_type}")

#     text = process_resume(file)
#     return {"resume_text": text}

@app.post("/upload")
def upload_resume(file: UploadFile = File(...)):
    # print(f"🔹 Received file: {file.filename}")
    # print(f"🔹 Content-Type: {file.content_type}")
    
    if not file.content_type:
        raise HTTPException(status_code=400, detail="❌ File content type is missing!")

    if file.content_type not in ["application/pdf", "application/msword", "text/plain"]:
        raise HTTPException(status_code=400, detail=f"❌ Unsupported file type: {file.content_type}")

    text = process_resume(file)
    return {"resume_text": text}


@app.get("/")
def home():
    return {"message": "Resume Matcher API is running"}


