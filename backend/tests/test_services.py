from backend.services import process_resume_text, match_resume_with_jobs

def test_clean_text():
    assert process_resume_text("Hello, World!") == "hello world"
    assert process_resume_text("Python & ML!!!") == "python ml"

def test_match_resume_logic():
    resume_text = "Experienced software engineer skilled in Python and ML."
    job_descriptions = [
        "Looking for a Python developer with machine learning experience.",
        "Seeking a Java developer for backend services."
    ]
    scores = match_resume_with_jobs(resume_text, job_descriptions)
    assert len(scores) == len(job_descriptions)
    assert all(isinstance(score, float) for score in scores)
