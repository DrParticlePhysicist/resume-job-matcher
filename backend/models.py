from pydantic import BaseModel
from typing import List

class ResumeMatchRequest(BaseModel):
    resume_text: str
    job_descriptions: List[str]

class MatchResponse(BaseModel):
    matches: List[float]
