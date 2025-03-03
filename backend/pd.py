import requests

file_path = "../data/sample_resumes/john_doe.txt"
url = "http://localhost:8000/upload"

with open(file_path, "rb") as f:
    files = {"file": (file_path, f, "text/plain")}
    response = requests.post(url, files=files)

print(response.json())  # Check API response
