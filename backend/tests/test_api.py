from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Resume Matcher API is running"}

def test_match_resume():
    payload = {
        "resume_text": "Experienced software engineer skilled in Python and ML.",
        "job_descriptions": [
            "Looking for a Python developer with machine learning experience.",
            "Seeking a Java developer for backend services."
        ]
    }
    response = client.post("/match", json=payload)
    assert response.status_code == 200
    assert "matches" in response.json()
    assert isinstance(response.json()["matches"], list)

def test_upload_resume_invalid_format():
    files = {"file": ("test.txt", "This is a sample text file", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200  # Should be accepted since TXT is supported

def test_upload_resume_unsupported_format():
    files = {"file": ("image.png", b"fake_image_data", "image/png")}
    response = client.post("/upload", files=files)
    assert response.status_code == 400
    assert response.json()["detail"] == "Unsupported file type"
